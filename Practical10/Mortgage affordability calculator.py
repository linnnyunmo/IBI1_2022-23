# This function take two parameters, value and salary
def can_buy_house(value, salary):
    # if the value of the house is less than or equal to 5 times the salary, the person can afford to buy this house
    return value <= 5 * salary
# Assume the total value of house is 180000
value = 180000
# Assume the salary of people is 35000
salary = 35000
# Print if purchaser could afford this house
print(can_buy_house(value, salary))
