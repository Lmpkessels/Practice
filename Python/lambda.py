def calc(m):
    """Calculating minutes and calories to see if user has earned a bonus."""
    if m <= 60:
        return m * 10
    elif m > 60:
        return m * 11

# Doing the same calculation as above only shorter.
# 
# Calculating minutes, each minute burns 10 callories, if 60+ minutes then,
# user get's 10% calorie burned bonus.
calculation = lambda m: m * 10 if m <= 60 else m * 11


# A list with prices.
prices = [10, 20, 30, 40]

# Here we use lambda to add tax to the price.
add_tax = lambda price: price * 1.21

# Here we create a new list, then we use map to get access to the function 
# lambda, then we take the list prices to add the calculation in lambda.
with_tax = list(map(add_tax, prices))


# List of weight user uses in app.
weights = [50, 60, 70, 80]

# Adding weight to make user gain more strength.
add_weight = lambda weight: weight + 2.5

# Using add_weight to increase the weights.
new_weight = list(map(add_weight, weights))


# List of salaries.
salaries = [2200, 2500, 3100, 4000]

# Here we give a raise of 7% and round it to a whole number.
add_raise = lambda a_raise: round(a_raise * 1.07)

# Here we modify the list with salaries.
new_salary = list(map(add_raise, salaries))


# List of steps by user.
steps = [3000, 10250, 8900, 4000, 15000, 7200]

# Filter users with 8000+ steps, giving them 10 point bonus per 1000 extra 
# steps, and calculating the full amount of points.
print(sum(map(lambda c: c // 1000 * 10, filter(lambda f: f > 8000, steps))))


invetory = [12, 18, 7, 25, 5]

print(list(map(lambda b: b // 6, invetory)))