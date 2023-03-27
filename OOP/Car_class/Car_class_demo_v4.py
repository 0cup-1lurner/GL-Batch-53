""" Create a Car class.
2 Instance attributes:
i)color
ii)horse_power
"""

class Car():

    def __init__ (self,color,horse_power,maker, mileage, car_type, \
                  transmission = "Manual"):
        self.color = color
        self.horse_power = horse_power
        self.maker = maker
        self.mileage = mileage
        self.car_type = car_type
        if transmission.lower() not in ("manual", "auto"):
            raise ValueError("Transmission has to be either manual or auto only.")
        self.transmission = transmission

    

    

    
