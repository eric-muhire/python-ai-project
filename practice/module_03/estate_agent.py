class EstateAgent:
    def __init__(self, name, district):
        self.name = name
        self.district = district
        self.sales = []

    def __repr__(self):
        return f"EstateAgent({self.name!r}, {self.district!r})"

    def add_sale(self, price):
        if price <= 0:
            raise ValueError(f"a sale must be more than 0, not {price}")
        self.sales.append(price)


kim = EstateAgent("Kim", "Majorna")
print("With print:", kim)
print(f"in an f-string: call{kim}")
print("In a list: ",[kim])

