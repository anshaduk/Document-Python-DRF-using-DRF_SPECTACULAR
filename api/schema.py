from drf_spectacular.utils import extend_schema,OpenApiParameter,extend_schema_view
from drf_spectacular.types import OpenApiTypes

from . serializers import ProductSerializer
from . docstring import *

product_list_docs = extend_schema(
    responses=ProductSerializer(many=True),
    summary = "List all the products",
    description = LIST_DOCS,
    parameters=[
        OpenApiParameter(
            name = "category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="The category of products to retrieve."
        ),
        OpenApiParameter(
            name='qty',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="The quantity of products to retrieve"
    
        ),
    ]

)

product_viewset_docs = extend_schema_view(
    list = product_list_docs,
    retrieve = extend_schema(
        summary = "Retrieve the product",
        description = RETRIEVE_DOCS
    ),
    create = extend_schema(
        summary = "Create a new product",
        description = CREATE_DOCS
    ),
    update = extend_schema(
        summary = "Update existing product",
        description = UPDATE_DOCS
    ),
    partial_update = extend_schema(
        summary = "Partially update the product",
        description = PARTIAL_UPDATE_DOCS
    ),
    destroy = extend_schema(
        summary = "Delete the product",
        description = DELETE_DOCS
    )

)