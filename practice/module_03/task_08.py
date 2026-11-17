from apartments import apartments
from home import Home

homes = []
for apartment in apartments:
    home = Home(
        apartment["listing_id"],
        apartment["district"],
        apartment["living_area"],
        apartment["price"],
    )
    homes.append(home)

print("Homes:", len(homes))
print("The first one:", homes[0])