from apartments import apartments


#Task04
#apartments_in_the_list =apartments[-1]

print(len(apartments))
print(apartments[-1] ["listing_id"],apartments[-1]["price"])
#print(apartments_in_the_list)

#Task05


sorted_list = {apartment["district"] for apartment in apartments}
print(sorted(sorted_list))



#Task06
#location =(57.70,11.97)
#location[0]=57.71

"""

TypeError: 'tuple' object does not support item assignment 
"""


#Task07
apartment = apartments[0]
#print(apartment().get("balcony"))
print(apartment.get("balcony", "unknown"))

#Task08
for apartment in apartments:
    if apartment["district"] == "Angered":
        angered_apartment = apartment["listing_id"],apartment["price"]
        print(angered_apartment)

#Task09
apartments_with_elevator = 0
for apartment in apartments:
    if apartment["elevator"] == "yes":
        apartments_with_elevator += 1
print("apartment with elevator = ", apartments_with_elevator,"st")




#Task10
cheap_apartment_price=apartments[0]
for apartment in apartments:
    if apartment["price"] < cheap_apartment_price["price"]:
        cheap_apartment_price = apartment
print(cheap_apartment_price["listing_id"],cheap_apartment_price["district"],cheap_apartment_price["price"])
