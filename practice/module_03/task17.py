
#convert a price in Kr
def sek_to_euro(price_sek,exchange_rate ):
    return price_sek/exchange_rate

#Saved search

class Saved_search:
    def __init__(self,max_price,district):
        self.max_price = max_price
        self.district = district
        def matches(self,home):
            return (
                home["price"] <= self.max_price
                and home["district"] == self.district)

def median_price(homes):
    prices = sorted(home["price"] for home in homes)
    n = len(prices)

    if n % 2 == 1:
        return prices[n // 2]
    else:
        #runs when n is even
        return (prices [n // 2 - 1] + prices[n // 2]) /2

class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        self.items.remove(item)
    def total(self):
        return sum(item["price"] for item in self.items)
