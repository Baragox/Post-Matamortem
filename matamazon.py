# TODO add all imports needed here

ZERO = 0 #avoiding "magic" numbers (whatever that means...)

class InvalidIdException(Exception):
    
    def ___init__(self, invalid_id):
        self.invalid_id = invalid_id
        super().__init__(f"InvalidIdException: {invalid_id}") #accesing parent class implementation
                                                                #(the built-in class "Exception") with super()


def _is_valid_non_negative_int(value):
    # only for non-negative integer (excluding bool, which is an int subclass)
    return isinstance(value, int) and not isinstance(value, bool) and value >= ZERO


class InvalidPriceException(Exception):
    #when price is not valid non-negative number
    def __init__(self, invalid_price):
        self.invalid_price = invalid_price
        super().__init__(f"InvalidPriceException: {invalid_price}")

def _is_valid_non_negative_real(value):
    #allowing int/float, not allowing bool
    return (isinstance(value, (int, float))
        and not isinstance(value,bool)
        and value >= ZERO)

    

class Customer:
    """
    Represents a customer in the Matamazon system.
    """

    def __init__(self, id, name, city, address):
        if not _is_valid_non_negative_int(id):
            raise InvalidIdException(id)


        self.id = id
        self.name = name
        self.city = city
        self.address = address

    def __str__(self):
        return (
            f"Customer(id={self.id}, name='{self.name}', "
            f"city='{self.city}',a ddress = '{self.adress}')"
        )
    
    def __repr__(self): #__repr__ represents as string, regardless of type
        return str(self)


class Supplier:
    """
    Represents a supplier in the Matamazon system.
    """

    def __init__(self, id, name, city, address):
        if not _is_valid_non_negative_int(id):
            raise InvalidIdException(id)
        
        self.id = id
        self.name = name
        self.city = city
        self.address = address


    def __str__(self):
        return (
            f"Supplier(id={self.id}, name='{self.name}', "
            f"city='{self.city}', adress='{self.adress}')"
        )
    
    def __repr__(self):
        return str(self)


class Product:
    """
    Represents a product sold on the Matamazon website.
    """

    def __init__(self,id, name, price, supplier_id, quantity):
        if not _is_valid_non_negative_int(id):
            raise InvalidIdException(id)
        if not _is_valid_non_negative_int(supplier_id):
            raise InvalidIdException(supplier_id)
        if not _is_valid_non_negative_int(quantity):
            raise InvalidIdException(quantity)
        if not _is_valid_non_negative_real(price):
            raise InvalidPriceException(price)
        
        self.id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id
        self.quantity = quantity

def __str__(self):
    return (
        f"Product({self.id}, name='{self.name}', price={self.price}, "
        f"supplier_id={self.supplier_id}, quantity={self.quantity}"
    )

def __repr__(self):
    return str(self)

class Order:
    """
    Represents a placed order.
    """

    def __init__(self, id, customer_id, product_id, quantity, total_price):
        if not _is_valid_non_negative_int(id):
            raise InvalidIdException(id)
        if not _is_valid_non_negative_int(customer_id):
            raise InvalidIdException(customer_id)
        if not _is_valid_non_negative_int(product_id):
            raise InvalidIdException(product_id)
        if not _is_valid_non_negative_int(quantity):
            raise InvalidIdException(quantity)
        if not _is_valid_non_negative_real(total_price):
            raise InvalidPriceException(total_price)
    
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self):
        return (
            f"Order(id={self.id}, customer_id={self.customer_id}, "
            f"product_id={self.product_id}, quantity={self.quantity}, "
            f"total_price={self.total_price})"
    )
    
    def __repr__(self):
        return str(self)


class MatamazonSystem:
    """
    Main system class that stores and manages customers, suppliers, products and orders.

    The system must support:
        - Registering customers/suppliers (with unique IDs across both types).
        - Adding/updating products (must validate supplier existence).
        - Placing orders (validate product existence and stock).
        - Removing objects by ID and type (with dependency constraints).
        - Searching products by name/query and optional max price.
        - Exporting system state to a text file (customers/suppliers/products only).
        - Exporting orders to JSON grouped by supplier origin city.

    Notes:
        - The specification does not require specific internal fields. Any data structures are allowed,
          as long as the behaviors match the spec.
        - A parameterless constructor is required.
    """

    def __init__(self):
        """
        Initialize an empty Matamazon system.

        Requirements:
            - Must be parameterless.
            - Internal collections may be chosen freely (dict/list, etc.).
        """
        # TODO implement this method if needed
        pass

    def register_entity(self, entity, is_customer):
        """
        Register a Customer or Supplier in the system.

        Args:
            entity: A Customer or Supplier object.
            is_customer (bool): True if entity is Customer, False if entity is Supplier.

        Raises:
            InvalidIdException:
                - If the entity ID is invalid.
                - If the entity ID already exists in the system (note: IDs must be unique across
                  customers AND suppliers).
        """
        # TODO implement this method as instructed
        pass

    def add_or_update_product(self, product):
        """
        Add a new product or update an existing product.

        Behavior:
            - If product does not exist in system: add it.
            - If product exists:
                - It must belong to the same supplier as the existing one (same supplier_id),
                  otherwise raise InvalidIdException.
                - Update the stored product's fields according to the new product.

        Args:
            product: A Product object.

        Raises:
            InvalidIdException:
                - If the supplier_id does not exist in the system.
                - If attempting to update a product but supplier_id differs from the existing product.
        """
        # TODO implement this method as instructed
        pass

    def place_order(self, customer_id, product_id, quantity=1):
        """
        Place an order for a product by a customer.

        Args:
            customer_id (int): Customer ID.
            product_id (int): Product ID.
            quantity (int, optional): Quantity to order. Defaults to 1.

        Returns:
            str: Status message according to specification:
                - "The order has been accepted in the system"
                - "The product does not exist in the system"
                - "The quantity requested for this product is greater than the quantity in stock"

        Behavior:
            - If product does not exist: return the relevant message.
            - If quantity requested > stock: return the relevant message.
            - Otherwise:
                - Decrease product stock by quantity.
                - Create a new Order with an auto-incremented system ID (starting at 1).
                - Store the order in the system.
                - Return success message.

        Notes:
            - The specification assumes quantity is an integer.
        """
        # TODO implement this method as instructed
        pass

    def remove_object(self, _id, class_type):
        """
        Remove an object from the system by ID and type.

        Args:
            _id (int): Object ID to remove.
            class_type (str): One of: "Customer", "Supplier", "Product", "Order"
                              (exact casing/spelling per assignment).

        Returns:
            int | None:
                - If removing an Order: return the ordered quantity of that order (to restore stock).
                - Otherwise: no return value required.

        Raises:
            InvalidIdException:
                - If _id is not a valid non-negative integer.
                - If attempting to remove a Customer/Supplier/Product that still has dependent orders
                  in the system (i.e., orders that were not removed).
                - Additional InvalidIdException conditions as required by specification.
        """
        # TODO implement this method as instructed
        pass

    def search_products(self, query, max_price=None):
        """
        Search products by query in the product name, and optionally filter by max_price.

        Args:
            query (str): Product name or part of product name.
            max_price (float, optional): If provided, only return products with price <= max_price.

        Returns:
            list[Product]:
                - Products that match the query and have quantity != 0,
                - Sorted by ascending price.
                - If no matching products exist, return an empty list.
        """
        # TODO implement this method as instructed
        pass

    def export_system_to_file(self, path):
        """
        Export system state (customers, suppliers, products) to a text file.

        Args:
            path (str): Output file path.

        Behavior:
            - Write each object on its own line, using the object's print/str representation.
            - Orders must NOT be included.
            - No constraint on the ordering of objects in the output.

        Raises:
            OSError (or any file-open exception): Must be propagated to the caller.
        """
        # TODO implement this method as instructed
        pass

    def export_orders(self, out_file):
        """
        Export orders in JSON format grouped by origin city.

        Args:
            out_file (file-like)

        Behavior (per specification):
            - Produce a JSON object where:
                - Keys: origin city (supplier city) for each order.
                - Values: list of strings representing orders (format as specified in section 4.1.4).
            - Order lists can be in any order.
            - No requirement on key ordering.

        Raises:
            Any exception during writing: Must be propagated to the caller.

        Notes:
            - The order origin city is the supplier city of the ordered product.
        """
        # TODO implement this method as instructed
        pass


def load_system_from_file(path):
    """
    Load a MatamazonSystem from an input file.

    Args:
        path (str): Path to a text file containing customers, suppliers and products.

    Returns:
        MatamazonSystem: Initialized system with the data found in the file.

    Behavior:
        - The file lines contain objects in the format produced by export_system_to_file (section 4.2).
        - Lines may appear in any order (e.g., product lines can appear before supplier lines).
        - Illegal lines may be ignored.
        - If an exception occurs during the creation of any required object due to invalid data,
          the function should stop and propagate the exception (as specified).

    Notes:
        - The assignment hints that eval() may be used.
    """
    # TODO implement this function as instructed
    pass

# TODO all the main part here