class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, job_title, salary):
        self.first = first
        self.last = last
        self.job_title = job_title
        self.salary = salary
        self.email = first + '.' + last + '@coding-temple.com'

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return f"Congrats, {self.full_name()}. You've recieved a raise of {self.raise_amount} making you new salary {self.salary}."

class Sales(Employee):
    def __init__(self, first, last, job_title, salary, phone_number):
        super().__init__(first, last, job_title, salary)
        self.phone_number = phone_number
        
    def send_email(self):
        return f"Dear Customer, Thank you for your interest in our product. Please let me know if you have any queations. My email is {self.email} or my phone number is # {self.phone_number}. Thanks, {self.full_name()}"

class Developement(Employee):
    def __init__(self, first, last, job_title, salary):
        super().__init__(first, last, job_title, salary)
        self.code = f'{self.full_name()} is writing code'



emp_1 = Sales('Mike', "O'Neil", 'Top G', 50000, '(208)573-6901')
emp_2 = Sales('Hannah', 'Stern', 'Beta G', 75000, '(123)456-7890')
emp_3 = Developement('John', 'Doe', 'Alpha G', 100000)

print(emp_1.apply_raise())
print(emp_1.send_email())
print(emp_2.send_email())

print(emp_3.code)
print(emp_3.apply_raise())