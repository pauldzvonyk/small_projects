from temperature import Temperature


class Calorie:
    """
    Calculates how many calories one needs, based on one's weight, height, age, and current temperature of the location.
    """

    def __init__(self, weight, height, age, temperature):
        """
        Initializes a Calorie object with user-specific information.

        Parameters:
        - weight (float): User's weight in kilograms.
        - height (float): User's height in centimeters.
        - age (int): User's age in years.
        - temperature (float): Current temperature of the location in Celsius.
        """
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        """
        Calculates the recommended daily calorie intake using the Harris-Benedict equation.

        Returns:
        - result (float): Recommended daily calorie intake.
        """
        result = 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age) + (10 * self.temperature)
        return result


if __name__ == "__main__":
    # Fetching the local temperature using the 'Temperature' class from the 'temperature' module.
    local_temperature = Temperature(website='https://www.timeanddate.com/weather/', country='italy', city='rome').get()

    # Creating a 'Calorie' object with user-specific information and the fetched temperature.
    calories = Calorie(weight=85, height=190, age=42, temperature=local_temperature)

    # Printing the calculated recommended daily calorie intake.
    print(calories.calculate())
