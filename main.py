# 11. EmployeeSalary
class EmployeeSalary:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase(self, percent):
        self.salary += self.salary * percent / 100

    def show_salary(self):
        print(f"Yangi oylik: {int(self.salary)}$")


es = EmployeeSalary("Ali", 1000)
es.increase(20)
es.show_salary()


# 12. GameCharacter
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, damage):
        self.health -= damage
        print(f"{self.name} zarar oldi: {self.health} HP qoldi")

    def heal(self, amount):
        self.health += amount
        print(f"Tiklandi: {self.health} HP")


gc = GameCharacter("Ali", 100)
gc.attack(30)
gc.heal(20)
