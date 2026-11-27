from dataclasses import dataclass


@dataclass
class Home:
    listing_id: str
    district: str
    living_area: int
    price: int