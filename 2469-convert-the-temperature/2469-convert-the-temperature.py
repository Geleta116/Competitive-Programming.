class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        converted_temp = []
        converted_temp.append(celsius + 273.15)
        converted_temp.append(celsius * 1.80 + 32.00)
        return converted_temp
        