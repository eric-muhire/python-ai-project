from home import House, Home

class Villa(House):
    def __init__(
            self,
            listing_id: str,
            district: str,
            living_area: int,
            price: int,
            plot_area: int,
            has_pool: bool
    ):
        super().__init__(
            listing_id,
            district,
            living_area,
            price,
            plot_area
        )
        self.has_pool = has_pool

    def describe(self) -> str:
        pool_text = "with a pool" if self.has_pool else "without a pool"

        return (
            f"{self.listing_id}: a villa in {self.district}, "
            f"{self.living_area} m², {self.price:,} kr, "
            f"on a {self.plot_area} m² plot, {pool_text}"
        )
villa =Villa(
    "V001",
    "Nödinge",
    180,
    6_500_000,
    800,
    True
)
print(villa.describe())

