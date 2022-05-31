# your User class goes here
class Users():
    def __init__(self, first, last, phone) -> None:
        self.first = first
        self.last = last
        self.phone = phone

    def __str__(self) -> str:
        return f"""
        user:       {self.name}
        email:      {self.email}
        license:    {self.drivers_license}
        """

    @property
    def email(self) -> str:
        return f"{self.first}.{self.last} + @email.com"
         

user_1 = Users('John', 'john.doe@email.com', 'J123-4567')
user_2 = Users('Jane', 'jane.doe@email.com', 'J789-1011')

print(user_1)
print(user_2)