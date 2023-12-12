from temperature import Temperature


class Calorie:
    """
    Calculates how many calories one needs, based on one's weight, height, age, and current temperature of the
    location.
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age) + (10 * self.temperature)
        return result


if __name__ == "__main__":
    local_temperature = Temperature(website='https://www.timeanddate.com/weather/', country='italy', city='rome').get()
    calories = Calorie(weight=85, height=190, age=42, temperature=local_temperature)
    print(calories.calculate())
