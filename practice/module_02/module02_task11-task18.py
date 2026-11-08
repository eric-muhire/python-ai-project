from pathlib import Path

import path
import json

from apartments import apartments
from statistics import median
from practice.module_01 import price_per_sqm
from pathlib import Path
import csv
from collections import Counter



#exercise 11
price_per_sqm = [round(apartment["price"] / apartment["living_area"]) for apartment in apartments]
print(price_per_sqm)

#exercise 12

def price_per_sqm(apartment):
    return round(apartment["price"] / apartment["living_area"])
assert price_per_sqm({"price": 7_000_000,"living_area": 70}) == 100_000

for apartment in apartments:
    print(apartment["listing_id"], price_per_sqm(apartment))

print("*******************************************")
#exercise 13
def within_budget(apartments,budget):
    return [apartment for apartment in apartments if apartment["price"] <= budget]

assert len(within_budget(apartments,1_000_000)) == 2
assert within_budget(apartments,0) == []

for apartment in within_budget(apartments,2_000_000):
    print(apartment["listing_id"],apartment["price"])
print("*****************************")
#exercise 14
def media_price(apartments):
    return median([apartment["price"] for apartment in apartments])
assert media_price([{"price": 1},{"price":2},{"price":9}]) ==2
print(f"{media_price(apartments):,.0f} SEK")

print("********************************")

#exercise 15


path = Path(__file__).parent.parent / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

print(len(rows))
print(rows[0])
print(rows[0]["district"], rows[0]["price"])
print("*******************************************")

#exercise 16
path = Path(__file__).parent.parent / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

per_district = Counter([row["district"] for row in rows])
for district, count in per_district.most_common():
    print(district, count)
print("***********************************")
#exercise 17

path = Path(__file__).parent.parent / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

affordable = [row for row in rows if int(row["price"]) <= 2_000_000]
text = json.dumps(affordable, ensure_ascii=False, indent=2)
json_path = Path("practice") / "data" / "affordable.json"
json_path.write_text(text, encoding="utf-8")
print(len(affordable), "apartments saved in practice/data/affordable.json")

#exercise 18