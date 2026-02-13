
import json

ZERO = 0 #avoiding "magic" numbers (whatever that means...)
ONE = 1

SUCCESS_ORDER_MSG = "The order has been accepted in the system"
NO_PRODUCT_MSG = "The product does not exist in the system"
NOT_ENOUGH_STOCK_MSG = "The quantity requested for this product is greater than the quantity in stock"

class InvalidIdException(Exception):
    
    def __init__(self, invalid_id):
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
            f"city='{self.city}', address='{self.address}')"
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
            f"city='{self.city}', address='{self.address}')"
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
        f"Product(id={self.id}, name='{self.name}', price={self.price}, "
        f"supplier_id={self.supplier_id}, quantity={self.quantity})"
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
    """

    def __init__(self):
        """
        Initialize an empty Matamazon system.
        """
       
        self.customers = {} # id -> Customer 
        self.suppliers = {} # id -> Supplier 
        self.products = {} # id -> Product 
        self.orders = {} # id -> Order 
        self._next_order_id = ONE 


    def register_entity(self, entity, is_customer):
        """
        Register a Customer or Supplier in the system.
        """
        if not hasattr(entity, "id") or not _is_valid_non_negative_int(entity.id):
            raise InvalidIdException(getattr(entity, "id",  None))  #using getattr to get the obj.name


        if entity.id in self.customers or entity.id in self.suppliers:
            raise InvalidIdException(entity.id)
        #registration shares the same ID space as customers and suppliers


        if is_customer:
            self.customers[entity.id] = entity
        else:
            self.suppliers[entity.id] = entity


    def add_or_update_product(self, product):
        """
        Add a new product or update an existing product.
        """
      
        if product.supplier_id not in self.suppliers:
            raise InvalidIdException(product.supplier_id)
    
        if product.id not in self.products:
            self.products[product.id] = product
            return
    
        existing = self.products[product.id]
        if existing.supplier_id != product.supplier_id:
            raise InvalidIdException(product.supplier_id) #its invalid to update with a different supplier_id


        existing.name = product.name
        existing.price = product.price
        existing.quantity = product.quantity


    def place_order(self, customer_id, product_id, quantity=ONE):
        """
        Place an order for a product by a customer.
        """


        #to validate the IDs && quantity types

        if not _is_valid_non_negative_int(customer_id):
            raise InvalidIdException(customer_id)
        if not _is_valid_non_negative_int(product_id):
            raise InvalidIdException(product_id)
        if not _is_valid_non_negative_int(quantity):
            raise InvalidIdException(quantity)
        

        if customer_id not in self.customers:
            raise InvalidIdException(customer_id)
        

        product = self.products.get(product_id)
        if product is None:
            return NO_PRODUCT_MSG
            
        if quantity > product.quantity:
            return NOT_ENOUGH_STOCK_MSG
        
        product.quantity -= quantity
        total_price = product.price * quantity
        order = Order(self._next_order_id, customer_id, product_id, quantity, total_price)

        self.orders[order.id] = order
        self._next_order_id += ONE
        
        return SUCCESS_ORDER_MSG






    def remove_object(self, _id, class_type):
        """
        Remove an object from the system by ID and type.
        """
        
        if not _is_valid_non_negative_int(_id):
            raise InvalidIdException(_id)
        
        if class_type == "Order":
            order = self.orders.get(_id)
            if order is None:
                raise InvalidIdException(_id)
            

            product = self.products.get(order.product_id)
            if product is None:
                raise InvalidIdException(order.product_id)
                #shouldn't happen if we prevent deleting products with existing orders, but just incase

            product.quantity += order.quantity
            qty = order.quantity
            del self.orders[_id]
            return qty
        

        if class_type == "Customer":
            if _id not in self.customers:
                raise InvalidIdException(_id)
            if any(o.customer_id == _id for o in self.orders.values()):
                raise InvalidIdException(_id)
            del self.customers[_id]
            return None
        
        if class_type == "Product":
            if _id not in self.products:
                raise InvalidIdException(_id)
            if any(o.product_id == _id for o in self.orders.values()):
                raise InvalidIdException(_id)
            del self.products[_id]
            return None
        

        if class_type == "Supplier":
            if _id not in self.suppliers:
                raise InvalidIdException(_id)
            

            if any(p.supplier_id == _id for p in self.products.values()):
                raise InvalidIdException(_id) #a product's supplier must already exist in the system
            
            for o in self.orders.values(): # a supplier has dependant order if there're
                p = self.products.get(o.product_id) #any order's for a product wof that supplier
                if p is not None and p.supplier_id == _id:
                    raise InvalidIdException(_id)
            del self.suppliers[_id]
            return None
        



        raise InvalidIdException(_id)
    

    

    def search_products(self, query, max_price=None):
        """
        Search products by query in the product name, and optionally filter by max_price.
        """

        if max_price is not None and not _is_valid_non_negative_real(max_price):
            raise InvalidPriceException(max_price)
        

        q = str(query).lower()


        matches = []

        for p in self.products.values():
            if p.quantity == ZERO:
                continue
            if q in p.name.lower():
                if max_price is None or p.price <= max_price:
                    matches.append(p)

        return sorted(matches, key=lambda p: p.price) #sorting by comparing the key values
                                                        #of each element

    def export_system_to_file(self, path):
        """
        Export system state (customers, suppliers, products) to a text file.
        """
        
        #without orders
        # will use the standard utf-8 to encode (f0r names/adresses)


        with open(path, "w", encoding = "utf-8") as f: #opens for writing
            for c in self.customers.values():
                f.write(str(c)+ "\n")
            for s in self.suppliers.values():
                f.write(str(s) + "\n")
            for p in self.products.values():
                f.write(str(p) + "\n")


        


    def export_orders(self, out_file):
        """
        Export orders in JSON format grouped by origin city.
        """

        grouped = {}

        for o in self.orders.values():
            p = self.products.get(o.product_id)
            if p is None:
                continue
            sup = self.suppliers.get(p.supplier_id)
            if sup is None:
                continue
            

            city = sup.city
            grouped.setdefault(city, []).append(str(o)) #if its not a already a key
                                                        # then create a grouped[city] = [] and return it to the new lsit
                                                        #then also add the order string to the last with append().

        json.dump(grouped, out_file)




def load_system_from_file(path):
    """
    Load a MatamazonSystem from an input file.
    """

    system = MatamazonSystem()

    customers = []
    suppliers = []
    products = []

    allowed_names = {
        "Customer": Customer,
        "Supplier": Supplier,
        "Product": Product,
    }



    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if line =="":
                continue

            try:
                obj = eval(line, allowed_names)
            except (SyntaxError,NameError,TypeError,ValueError):
                continue #ignore it if its in an unvalid format
                # also, any InvalidIdException/InvalidPriceException will not be caught


            if isinstance(obj, Customer):
                customers.append(obj)
            elif isinstance(obj, Supplier):
                suppliers.append(obj)
            elif isinstance(obj, Product):
                products.append(obj)
            else:
                continue
    
    for c in customers:
        system.register_entity(c,True)
    for s in suppliers:
        system.register_entity(s,False)
    for p in products:
        system.add_or_update_product(p)


    return system