"""
Employee management system
Origin : https://github.com/ArjanCodes/2021-code-smells/blob/main/
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from multiprocessing import managers
from typing  import List
from enum import Enum , auto

FIXED_VACATION_DAYS_PAYOUT=  5

class Role(Enum):
    """Employee Rules"""
    PRESIDENT = auto()
    VICEPRESIDENT= auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto() 

@dataclass
class Employee(ABC):
    name : str
    role :  Role
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
    @abstractmethod
    def pay(self) -> None:
        """Method to call when paying an employee"""


@dataclass
class HourlyEmployee(Employee):
    """Employee that 's paid based on number of worked hours"""
    hourly_rate_won : float = 50
    hours_worked : int = 10
    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a hourly rate of \
            ${self.hourly_rate_won} for {self.hours_worked} hours."
            )

@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid on a fixed montly salry"""
    monthly_salary : float = 5000

    def pay(self)->None:
        print(
            f"Paying employee {self.name} a monthly  salary of a ${self.monthly_salary}."
        )


class Company :
    """Represents a company with employees"""
    def __init__(self) -> None:
        self.employees  : List[Employee] = []

    def add_employee(self ,employee : Employee ) -> None:
        """Add an employee to the list of employees"""
        self.employees.append(employee)
    
    def find_employees(self, role  : Role) -> List[Employee]:
        """FInd all employees with a particular role"""
        return [employee for employee in self.employees if employee.role is role]



def main()-> None:
    """Mian function"""
    company = Company()

    company.add_employee(SalariedEmployee(name="jaeyoung", role=Role.INTERN))
    company.add_employee(HourlyEmployee(name="chulsu", role=Role.LEAD))
    company.add_employee(HourlyEmployee(name="babamba", role=Role.PRESIDENT))

    print(company.find_employees(role=Role.INTERN))
    print(company.find_employees(role=Role.LEAD))
    print(company.find_employees(role=Role.MANAGER))

    company.employees[0].pay()
    company.employees[0].take_a_holiday(False)


if __name__ == "__main__":
    main()