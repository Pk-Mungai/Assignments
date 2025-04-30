
class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# Adjust the months Jan and Feb
    def calculate_day_of_week(self):
        if self.month < 3:
            self.month +=12 #For month Jan=13 and Feb=14
            self.year -= 1 #For the year to be the previous one

# Set variables
        q = self.day
        m = self.month
        k = self.year % 100
        j = self.year // 100

# Zeller's formula
        h = (q + (13 * (m+1) // 5) + k   + (k//4) + (j//4) + (5*j)) % 7 # Uses floor division to return an integer instead of a float

        days = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"
        }

        return days[h]

# Example
if __name__ == "__main__":
    calc = DateCalculator(2050,1,30)
    day_of_week = calc.calculate_day_of_week()
    print("January 30th, 2050 is a " + day_of_week)
