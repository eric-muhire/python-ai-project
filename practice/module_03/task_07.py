from home import Home

a01 = Home("A01", "Majorna", 50, 2_453_000)
a01.lower_price(100_000)
print("After the first lowering:", a01)

a01.lower_price(5_000_000)