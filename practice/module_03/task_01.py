from home import Home

A01 = Home("A01","Nödinge",110,3_000_075 )
A02 = Home("A06", "Angered", 67, 1_481_000)
print(f"A01: {A01.district}, {A01.price:,} SEK")
print(f"A06: {A02.district}, {A02.price:,} SEK")