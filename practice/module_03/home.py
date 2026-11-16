
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