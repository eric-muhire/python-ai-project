from sys import path

import rows

from apartments import apartments
import csv
from pathlib import Path



price = 2_453_000
rooms = 2.0
district = "Majorna"
has_elevator = False
year_built = None
district = "Majorna"
price = 2_453_000
living_area = 50

print(type(price))
print(type(rooms))
print(type(district))
print(type(has_elevator))
print(type(year_built))

print(f"{district}:{price:,} SEK")
print(f"Price per square meter:{price / living_area:,.0f} SEK")

prices = [2_453_000, 1_933_000, 5_053_000]
location = (57.70, 11.97)
apartment = {"district": "Majorna", "living_area": 50, "price": 2_453_000}
districts = {"Majorna", "Centrum", "Majorna"}


print(prices[0])

for apartment in apartments:
    if apartment["price"] < 1_000_000:
        print(apartment['listing_id'], apartment["district"], apartment["price"])

        price = []
        for apartment in apartments:
            price.append(apartment["price"])


def price_per_square_meter(apartment):
    return apartment["price"]/ apartment["living_area"]

example = {"price": 2_500_000, "living_area": 50}
assert price_per_square_meter(example) == 50_000
print(price_per_square_meter(example))

print("----------------------------------")

path = Path(__file__).parent.parent / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

print(rows[0]["district"], rows[0]["price"])

first = apartments[0]
print(f"{first['district']}: {first['price']:,} SEK")
