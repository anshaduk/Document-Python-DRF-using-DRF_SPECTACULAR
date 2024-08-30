LIST_DOCS = """
    
    Retrieve a list of products from the database with optional filtering by category
    and limit by quantity.

    **Query Parameters:**
    - `category` (string, optional): Filters products by a case-insensitive match
      of the category name.
    - `qty` (integer, optional): Limits the number of products returned to the specified
      quantity.

    **Returns:**
    - A JSON response containing a list of products, filtered and limited according
      to the provided query parameters.

    """
CREATE_DOCS = """
    Create a new product in the database.

    This method handles POST requests to add a new product entry to the database.
    It expects data in the request body that includes the product's name, description,
    price, and category. The data is validated, and if valid, a new product instance 
    is created and saved.

    **Request Body:**
    - `name` (string, required): The name of the product. Must be unique and less than 255 characters.
    - `description` (string, required): A detailed description of the product.
    - `price` (decimal, required): The price of the product. Must be a positive number with up to 10 digits and 2 decimal places.
    - `category` (string, required): The category of the product. Must be one of the predefined categories 
      (e.g., 'electronics', 'clothings', 'books', 'toys', 'others').

    """

RETRIEVE_DOCS  = """
    Retrieve a specific product by its ID.

    This method handles GET requests to retrieve the details of a specific 
    product based on its primary key (ID). It returns the product's data 
    if found, including fields such as name, description, price, and category.

    **URL Parameter:**
    - `pk` (integer, required): The primary key of the product to be retrieved.
    """

UPDATE_DOCS = """

        Update an existing product in the database.

        This method handles PUT requests to update the details of a specific product.
        It requires the product's ID as a URL parameter and the updated data in the 
        request body. The method validates the input data and updates the product if 
        it passes validation.

        **URL Parameter:**
        - `pk` (integer, required): The primary key of the product to be updated.

        **Request Body:**
        - `name` (string, required): The new name of the product. Must be unique and less than 255 characters.
        - `description` (string, required): The updated description of the product.
        - `price` (decimal, required): The updated price of the product. Must be a positive number with up to 10 digits and 2 decimal places.
        - `category` (string, required): The updated category of the product. Must be one of the predefined categories 
          (e.g., 'electronics', 'clothings', 'books', 'toys', 'others').
    """

PARTIAL_UPDATE_DOCS = """
        Partially update an existing product in the database.

        This method handles PATCH requests to update specific fields of a product.
        It requires the product's ID as a URL parameter and the fields to be updated 
        in the request body. Only the provided fields will be updated, and others 
        will remain unchanged.

        **URL Parameter:**
        - `pk` (integer, required): The primary key of the product to be updated.

        **Request Body:**
        - Fields can include any of the product attributes:
            - `name` (string, optional): The new name of the product.
            - `description` (string, optional): The updated description of the product.
            - `price` (decimal, optional): The updated price of the product.
            - `category` (string, optional): The updated category of the product.
    """

DELETE_DOCS = """
        Delete a specific product from the database.

        This method handles DELETE requests to remove a product identified by its 
        primary key (ID). If the product is found, it will be deleted from the database; 
        otherwise, a 404 error will be returned.

        **URL Parameter:**
        - `pk` (integer, required): The primary key of the product to be deleted.
    """