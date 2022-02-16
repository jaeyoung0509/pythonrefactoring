"""
Vehichle registration system
Origin :https://github.com/ArjanCodes/2021-more-code-smells/blob/main/before.py
"""



from dataclasses import dataclass
from datetime import datetime
from enum import Enum ,auto
from random import *
from string import *
from typing import Optional, Tuple 



class FuelType(Enum):
    """Type of fuel used in a vehicle"""

    ELECTRONIC  = auto()
    PETROL = auto()


class RegistryStatus(Enum):
    """Possible statuses for the vehichle  registry system"""
    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()

taxes = {FuelType.ELECTRONIC : 0.02   , FuelType.PETROL : 0.05}

@dataclass
class VehicleInfoMissingError(Exception):
    """Custom error that is raised when vehicle informaition is missing for a particular brand"""

    band : str 
    model : str
    message : str = "Vehicle information is missing"

@dataclass
class VehicleModelInfo:
    """Class that contains basic information about a vehicle model."""

    brand : str
    model : str
    catalogue_price  : int 
    fuel_type : FuelType = FuelType.ELECTRONIC
    production_year : int = datetime

    @property
    def tax(self) -> float:
        """Tax to be paid when registering a vehicle of this type."""
        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def get_info_str(self) -> str:
        """String representation of this instance"""
        return f"brand : {self.brand}  - type : {self.model} - tax: {self.tax}"

@dataclass
class Vehicle:
    """Class representing  a vehicle(electronic or fossil fuel"""

    vehichle_id : str
    license_plate : str
    info : VehicleModelInfo

    def to_string(self) -> str:
        """String representaition of the instance"""
        info_str = self.info.get_info_str()
        return f"Id {self.vehichle_id} License plate : {self.license_plate} . Info : {info_str}"


class VehicleRegistry:
    """Class representing a basic vehicle registration system"""
    """
    Tuple can not modify it's value  so it is faster  and has less memory than list
    """
    def __init__(self) -> None:
        self.vehicle_models : dict[Tuple[str,  str] ,VehicleModelInfo] = {}
        self.online = True

    def add_vehicle_model_info(self,model_info : VehicleModelInfo) -> None:
        """Helper method for adding a VehicleModelInfo object to a list."""
        self.vehicle_models[(model_info.brand , model_info.model)] = model_info

    def generate_vehicle_id(self, length: int) -> str:
        """Helper method for generating a random vehicle id."""
        """choices function makes random num"""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """Helper method for generating a vehicle license number."""
        return f"{_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate."""
        """ 
        ':=' 바다 코끼리 연산자?
        표현식에 이름을 부여하고 재사용 할 수 있도록 하는것 
        바다코끼리 연산자를 사용하면 할당과 테스트를 한단계로 줄일 수 있음.
        """
        if not   (vehicle_model := self.find_model_info(brand, model)):
            raise VehicleInfoMissingError(brand, model)
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, vehicle_model)
        

    def find_model_info(self ,brand :str , model :str) -> Optional[VehicleModelInfo]:
        """Find Vehicle model info for a brand and model If no ifno can be found , None is returned """
        return self.vehicle_models.get((brand , model))

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        return (
            RegistryStatus.OFFLINE
            if not self.online
            else RegistryStatus.CONNECTION_ERROR
            if len(self.vehicle_models) == 0
            else RegistryStatus.ONLINE
        )

if __name__ == "__main__":

    # create a registry instance
    registry = VehicleRegistry()

    # add a couple of different vehicle models
    registry.add_vehicle_model_info(VehicleModelInfo("Tesla", "Model 3", 50000,  2021))
    registry.add_vehicle_model_info(VehicleModelInfo("Volkswagen", "ID3", 35000,  2021))
    registry.add_vehicle_model_info(VehicleModelInfo("BMW", "520e", 60000, FuelType.PETROL, 2021))
    registry.add_vehicle_model_info(VehicleModelInfo("Tesla", "Model Y", 55000, 2021))

    # verify that the registry is online
    print(f"Registry status: {registry.online_status()}")

    # register a new vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")

    # print out the vehicle information
    print(vehicle.to_string())
