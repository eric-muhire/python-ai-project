from apartments import apartments
from home import Home
from practice.module_03.home import Home

homes = []
for apartment in apartments:
    home = Home(
        apartment["listing_id"],
        apartment["district"],
        apartment["living_area"],
        apartment["price"],
    )
    homes.append(home)
affordable = [home for home in homes if home.is_within(2_000_000)]
for home in affordable:
    print("Affordable: ",home)