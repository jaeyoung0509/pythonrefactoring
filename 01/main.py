"""
Employee management system
Origin : https://github.com/ArjanCodes/2021-code-smells/blob/main/
"""

from dataclasses import dataclass
from multiprocessing import managers
from typing  import List

FIXED_VACATION_DAYS_PAYOUT=  5


@dataclass
class Employee:
    name : str
    role :  str
    vacation_days :int = 25


    def take_a_holiday(self , payout : bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            # check that there are enough vacation days left for a payout
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"you don't have enough holidays left over a payout.\
                        Remaining holidays  : {self.vacation_days}"
                )
            try:
                self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
                print(f"Paying out a holiday . Holiday left :{self.vacation_days}")
            except Exception :
                pass
        else:
            if self.vacation_days < 1:
                raise ValueError(
                    "you don't have any holidays left  .  Now back to work  :("
                )
            self.vacation_days -=1 

@dataclass
class HourlyEmployee(Employee):
    """Employee that 's paid based on number of worked hours"""
    hourly_rate : float = 50
    amount : int = 10 

@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid on a fixed montly salry"""
    monthly_salary : float = 5000


class Company :
    """Represents a company with employees"""
    def __init__(self) -> None:
        self.employees  : List[Employee] = []

    def add_employee(self ,employee : Employee ) -> None:
        """Add an employee to the list of employees"""
        self.employees.append(employee)
    
    def find_managers(self) -> List[Employee] :
        """Find all manager employee"""
        mangers = []
        for employee in self.employees:
            if employee.role == "manager" :
                mangers.append(employee)
        return managers

    def find_vice_presidents(self) ->  List[Employee]:
        """find all vice_presents"""
        vice_presents =  []
        for employee in self.employees:
            if employee.role == "vice_presents" :
                vice_presents.append(employee)
        return managers

    def find_interns(self) -> List[Employee]:
        """Find all interns."""
        interns = []
        for employee in self.employees:
            if employee.role == "intern":
                interns.append(employee)
        return interns


    def pay_employee(self , employee : Employee) -> None:
        """Pay an employee"""
        if isinstance(employee  , SalariedEmployee):
            """isinstance function checks type of two variables """
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Paying employee {employee.name} a hourly rate of \
                ${employee.hourly_rate} for {employee.amount} hours."
            )
            pass

def main()-> None:
    """Mian function"""
    company = Company()

    company.add_employee(SalariedEmployee(name="jaeyoung", role="manager"))
    company.add_employee(HourlyEmployee(name="chulsu", role="president"))
    company.add_employee(HourlyEmployee(name="babamba", role="intern"))

    print(company.find_vice_presidents())
    print(company.find_managers())
    print(company.find_interns())
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(False)


if __name__ == "__main__":
    main()