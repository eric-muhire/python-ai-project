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

homes_per_district = {}
for home in homes:
    count_so_far = homes_per_district.get(home.district,0)
    homes_per_district[home.district] = count_so_far + 1
print("homes_per_district:", homes_per_district)