class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Ім'я {self.name} Вік {self.age}"


class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number

    def info(self):
        base_info = super().info()
        return f"{base_info} Посвідчення водія {self.license_number}"


person = Person("Олег", 28)
driver = Driver("Максім", 35, "ВХ2342АС")

print(person.info())
print(driver.info())
