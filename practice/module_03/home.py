
class Home:
    def __init__(self, listing_id,district,living_area,price):
        self.listing_id = listing_id
        self.district = district
        self.living_area = living_area
        self.price = price
    def price_per_sqm(self):
        return round(self.price/self.living_area)