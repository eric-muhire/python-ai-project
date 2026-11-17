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
homes.sort(key=lambda home: home.price_per_sqm())
for home in homes[:3]:
    print(f"{home.listing_id} per square meter :{home.price_per_sqm():,} SEK")