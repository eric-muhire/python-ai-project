
class Home:
    def __init__(self, listing_id,district,living_area,price):
        if living_area <= 0:
            raise ValueError(f"living_area must be more than 0, not {living_area}")
        if price < 0:
            raise ValueError(f"price cannot be negative, not {price}")

        self.listing_id = listing_id
        self.district = district
        self.living_area = living_area
        self.price = price


    def __repr__(self):
        return (

            f"Home({self.listing_id!r}, {self.district!r}, "
            f"{self.living_area}, {self.price})"
        )


    def price_per_sqm(self):
        return round(self.price/self.living_area)

    def is_within(self, budget):
        return self.price <= budget


    def lower_price(self,amount):
        if amount > self.price:
            raise ValueError(f"cannot lower the price by more than {self.price}")
        self.price = self.price - amount

    def describe(self) -> str:
        return f"{self.listing_id}: a house in {self.district}, {self.living_area} m²" \
               f"{self.price:,} kr, on a {self.plot_area} m² plot"






class Apartment(Home):
    def __init__(
            self,
            listing_id: str,
            district: str,
            living_area: int,
            price: int,
            monthly_fee: int
    ):
        super().__init__(listing_id, district, living_area, price)
        self.monthly_fee = monthly_fee


        self._has_treasure = False
        self.__is_boring = True




class House(Home):
    def __init__(
            self,
            listing_id: str,
            district: str,
            living_area: int,
            price: int,
            plot_area: int
    ):
        super().__init__(listing_id, district, living_area, price)
        self.plot_area = plot_area


    def __str__(self) -> str:
        return f"House with price of {self.price} kr"


    def __repr__(self) -> str:
        return f'House(listing_id="{self.listing_id}", district="{self.district}")'


    def describe(self) -> str:
        return f"{self.listing_id}: a house in {self.district}, {self.living_area} m²" \
               f"{self.price:,} kr, on a {self.plot_area} m² plot"
