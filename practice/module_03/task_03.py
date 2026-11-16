from home import Home

a01 = Home("A01", "Majorna", 50, 2_453_000)
a06 = Home("A06", "Angered", 67, 1_481_000)
budget = 2_000_000

print("A01 within the budget:", a01.is_within(budget))
print("A06 within the budget:", a06.is_within(budget))