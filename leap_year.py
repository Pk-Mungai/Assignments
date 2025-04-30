def leap_year(year) -> bool:
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter the year:"))
print(leap_year(year))
leap: bool = leap_year(year)

if leap == True:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
