class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"


class Driver(Person):
    def __init__(self, name, age, license_number):
        # Викликаємо конструктор батьківського класу
        super().__init__(name, age)
        self.license_number = license_number

    def info(self):
        # Розширюємо метод батьківського класу
        base_info = super().info()
        return f"{base_info}, Посвідчення водія: {self.license_number}"


# Перевірка роботи
person = Person("Олег", 28)
driver = Driver("Максим", 35, "AB987654")

print(person.info())
print(driver.info())