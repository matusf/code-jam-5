class EarthSystem:
    name: str
    unit: str
    min: float
    max: float
    current_value: float

class WaterSystem(EarthSystem):
    unit = 'level'
    min = 0
    max = 100
    # Above avegage
    current_value = 0


class AirSystem(EarthSystem):
    min = 0
    max = 100
    unit = 'degree Celsius'
    current_value = 0