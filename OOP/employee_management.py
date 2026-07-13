
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    @abstractmethod
    def caculate_salary(self):
        pass
    def __str__(self):
        return f"{self.name}: {self.caculate_salary()}"
    
class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus_precent):
        super().__init__(name, base_salary)
        self.bonus_precent = bonus_precent
    def caculate_salary(self):
        salary = self.base_salary + (self.base_salary * self.bonus_precent / 100)
        return salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked, hours_rate):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate
    def caculate_salary(self):
        salary = (self.hours_worked * self.hours_rate)
        return salary

class Manager(FullTimeEmployee):
    def __init__(self, name, base_salary, bonus_precent, team_size):
        super().__init__(name, base_salary, bonus_precent)
        self.team_size = team_size
    def caculate_salary(self):
        return (super().caculate_salary() + self.team_size * 500000)

class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    @property
    def total_payroll(self):
        total = 0
        for pay in self.employees:
            total += pay.caculate_salary()
        return total
    def get_salary(self,employee):
        return employee.caculate_salary()
    def highest_paid(self):
        return max(self.employees, key= self.get_salary)
    def __len__(self):
        return len(self.employees)

company = Company()
company.add_employee(FullTimeEmployee("Hau", 15000000, 10))
company.add_employee(PartTimeEmployee("Minh", 0, 80, 50000))
company.add_employee(Manager("ABC", 20000000, 15, 5))
for emp in company.employees:
    print(emp)
print(f"Tổng : {company.total_payroll:.2f}")
print(f"Nhân viên lương cao nhất: {company.highest_paid().name}")
print(f"Số lượng nhân viên: {len(company)}")
