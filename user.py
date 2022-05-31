# your User class goes here
from audioop import add


class Users():
    def __init__(self, first, last, phone, address) -> None:
        self.first = first
        self.last = last
        self.phone = phone
        self.address = address

    def __str__(self) -> str:
        return f"""
        user:       {self.fullname}
        email:      {self.email}
        phone:      {self.phone}
        address:    {self.address}
        """

    @property   # Property tag allows method to be called like an attribute
    def email(self) -> str:
        return f"{self.first.lower()}.{self.last.lower()}" + "@email.com"

    @property   # Property tag allows method to be called like an attribute
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    @fullname.setter    # Setter allows class to automatically update attributes as properties change
    def fullname(self, name) -> str:
        first, last = name.split(' ')
        self.first = first
        self.last = last
         
# Instantiate users 1 and 2
user_1 = Users('John', 'Doe', '123-456-7890', '123 Main St')
user_2 = Users('Jane', 'Doe', '098-765-4321', '456 Grand Blvd')

# Display their properties
print(f"User 1: {user_1}")
print(f"User 2: {user_2}")

# Change their names
user_1.fullname = 'Michael Heinzinger'
user_2.fullname = 'Erika Fernandez'

# Other attributes update as well
print(f"User 1: {user_1}")
print(f"User 2: {user_2}")