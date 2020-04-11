class Property:
    def __init__(self, square_feet='', beds='',
            baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print("Property Details \n ============")
        print("square footage:{}".format(self.square_feet))
        print("Beds:{} ".format(self.beds))
        print("Bathrooms:{}".format(self.baths))

    def prompt_init():
        return dict(square_feet = input("no of sq feet"),
                beds = input("no of beds"),
                baths = input("how many bathroom ?"))

    prompt_init = staticmethod(prompt_init)
# We see something new in the prompt_init method. This method is made into a
# static method immediately after it is initially created. Static methods are associated
# only with a class (much like class variables), rather than a specific object instance.
# Hence, they have no self argument. Because of this, the super keyword won't work
# (there is no parent object, only a parent class), so we simply call the static method
# on the parent class directly. 

def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_valconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super.__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("Apartment Details")
        print("laundry %s" % self.laundry)
        print("has balcony %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("Laundry options",
                Apartment.valid_laundries)
        balcony = get_valid_input("Balcony Options",
                Apartment.valid_valconies)
        
        parent_init.update({
            "laundry":laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fence = ("yes", "no")

    def __init__(self, garage='', num_stories='',
            fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()   
        print("House Details")
        print("No of stories:{}".format(self.num_stories))
        print("Garage options:{}".format(self.garage))
        print("fence options:{}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Fence Options",
                House.valid_fence)
        garage = get_valid_input("Garage Options",
                House.valid_garage)
        num_stories = input("no of stories")

        parent_init.update({
            "garage":garage,
            "fenced":fenced,
            "num_stories":num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("Purchase")
        print("Price:{}".format(self.price))
        print("Taxes:{}".format(self.taxes))

    def prompt_init():
        return dict(
            price = input("selling price"),
            taxes = input("Estimated tax")
        )
    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self, furnished='', rent='',
            utilities='',**kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("Rental")
        print("Furnished:{}".format(self.furnished))
        print("Rent:{}".format(self.rent))
        print("Utilities:{}".format(self.utilities))

    def prompt_init():
        return dict(
            furnished = input("is it furnished?"),
            rent = input("rent per year"),
            utilities = input("are there much utilities?")
        )

    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map={
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rent"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }
    
    def add_property(self):
        property_type = get_valid_input("Type of property",
                ("house","apartment")).lower()
        payment_type = get_valid_input("Payment Type",
                ("rental", "purchase")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)
        ]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))