from . seed import DUMMY_PRODUCT
from rest_framework.response import Response
from rest_framework import status
from . models import Product
from rest_framework.decorators import api_view
from . serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from . schema import product_list_docs,product_viewset_docs
from rest_framework.exceptions import AuthenticationFailed,ValidationError

# Create your views here.
@product_viewset_docs
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # @product_list_docs
    def list(self, request):
        '''
        This method helps to retrieve products in database.
        '''
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")

        if category:
            if request.user.is_authenticated:
                self.queryset = self.queryset.filter(category__icontains=category)
            else:
                raise AuthenticationFailed("Unautherized request.")
        if qty:
            if int(qty)>0:
                self.queryset = self.queryset[:int(qty)]
            else:
                raise ValidationError("Quantity cannot be 0 or less than.")

        serializer = ProductSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):
        '''
        This method helps to add new product into database.
        '''
    

@api_view(['GET','POST',])
def import_dummy_data(request):
    try:
        for entry in DUMMY_PRODUCT:
            Product.objects.create(
                name = entry["name"],
                description = entry["description"],
                price = entry["price"],
                category = entry["category"]
            )
        response = {"message":"Data Imported Successfully."}
        return Response(response,status=status.HTTP_201_CREATED)

    except Exception as e:
        error_response = {"message":f"An error occured - {e}"}
        return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def num_product(request):
    """
    Retrieve the total number of products in the database.

    This view function processes GET requests and returns a JSON response with
    the total count of `Product` instances currently stored in the database.
    It is designed to provide a quick summary of the number of products available
    for administrative or analytical purposes.

    **Behavior:**
    - The function queries the database to count the number of `Product` entries
      and returns this count in a JSON object.

    **Example Response:**
    ```json
    {
        "count": 120
    }
    ```

    **HTTP Status Codes:**
    - 200 OK: Indicates that the request was successful, and the product count
      is included in the response.

    **Permissions:**
    - This endpoint does not require any special permissions or authentication.
      It is accessible to any client making a GET request.

    **URL Endpoint:**
    - `/num-product/` (adjust according to your URL routing configuration)

    **Request Method:**
    - GET

    **Response:**
    - A JSON object with a single key "count" which holds the integer value of
      the total number of products.

    **Request Example:**
    ```
    GET /num-product/
    ```

    **Response Example:**
    ```json
    {
        "count": 120
    }
    ```

    **Notes:**
    - Ensure that the `Product` model is correctly defined and migrated in your
      database to get accurate counts.
    - The endpoint provides a simple metric which can be useful for dashboard
      displays, administrative views, or monitoring purposes.

    Returns:
        Response: A Response object containing a JSON payload with the total count
                  of products in the database.
    """
    data = {"count":Product.objects.count()}
    return Response(data)
