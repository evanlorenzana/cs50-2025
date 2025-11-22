def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(meal_price):
   
   meal_price = meal_price.replace("$", "")

   return float(meal_price)

def percent_to_float(tip_percent):

    tip_percent = tip_percent.replace("%", "")
    
    return float(tip_percent) / 100


main()