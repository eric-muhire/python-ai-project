from apartments import apartments
from practice.module_01 import price_per_sqm

#exercise 11
price_per_sqm = [round(apartment["price"] / apartment["living_area"]) for apartment in apartments]
print(price_per_sqm)

#exercise 12

def price_per_sqm(apartment):
    return round(apartment["price"] / apartment["living_area"])
assert price_per_sqm({"price": 7_000_000,"living_area": 70}) == 100_000

for apartment in apartments:
    print(apartment["listing_id"], price_per_sqm(apartment))


#exercise 13


#exercise 14



#exercise 15


#exercise 16

#exercise 17


#exercise 18