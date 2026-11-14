from home import Home

a01 = Home("A01", "Majorna", 50, 2_453_000)
a06 = Home("A06", "Angered", 67, 1_481_000)

print(f"A01 per square meter: {a01.price_per_sqm():,} SEK")
print(f"A06 per square meter: {a06.price_per_sqm():,} SEK")