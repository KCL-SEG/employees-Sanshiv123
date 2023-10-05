"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, workType="", pay=0, commissionType="", commission=0, no_of_hours=0, no_of_contract=0, description = "" ):
        self.name = name
        self.workType = workType
        self.commissionType = commissionType
        self.commission = commission
        self.pay = pay
        self.no_of_hours = no_of_hours
        self.no_of_contract = no_of_contract
        self.get_description = description
    
    def get_pay(self):
        total_pay = self.pay
        if(self.workType == "salary_contract"):
            if(self.commissionType == "bonus"):
                total_pay +=  self.commission
                self.get_description = f'works on a monthly salary of {self.pay} and receives a bonus commission of {self.commission}'
            elif(self.commissionType == "contract"):
                total_pay += self.commission * self.no_of_contract
                self.get_description = f'works on a monthly salary of {self.pay} and receives a commission for {self.no_of_contract} contract(s) at {self.commission}/contract'
            else:
                self.get_description = f'works on a monthly salary of {total_pay}'
        elif(self.workType == "hourly_contract"):
            total_pay *= self.no_of_hours
            if(self.commissionType == "bonus"):
                total_pay +=  self.commission
                self.get_description = f'works on a contract of {self.no_of_hours} hours at {self.pay}/hour and receives a bonus commission of {self.commission}'
            elif(self.commissionType == "contract"):
                total_pay += self.commission * self.no_of_contract
                self.get_description = f'works on a contract of {self.no_of_hours} hours at {self.pay}/hour and receives a commission for {self.no_of_contract} contract(s) at {self.commission}/contract'
            else:
                self.get_description = f'works on a contract of {self.no_of_hours} hours at {self.pay}/hour'
        return total_pay

    def __str__(self):
        return f'{self.name} {self.get_description}. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.workType = "salary_contract"
billie.pay = 4000
print(billie.get_pay())
print(billie.__str__())


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.workType = "hourly_contract"
charlie.pay = 25
charlie.no_of_hours = 100
print(charlie.get_pay())
print(charlie.__str__())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.workType = "salary_contract"
renee.pay = 3000
renee.commissionType = "contract"
renee.no_of_contract = 4
renee.commission = 200
print(renee.get_pay())
print(renee.__str__())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.workType = "hourly_contract"
jan.pay = 25
jan.no_of_hours = 150
jan.commissionType = "contract"
jan.no_of_contract = 3
jan.commission = 220
print(jan.get_pay())
print(jan.__str__())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.workType = "salary_contract"
robbie.pay = 2000
robbie.commissionType = "bonus"
robbie.commission = 1500
print(robbie.get_pay())
print(robbie.__str__())

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.workType = "hourly_contract"
ariel.pay = 30
ariel.no_of_hours = 120
ariel.commissionType = "bonus"
ariel.commission = 600
print(ariel.get_pay())
print(ariel.__str__())
