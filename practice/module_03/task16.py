from animals import Animal, Cow,Horse


animals =[
    Cow("Daisy"),
    Horse("Anna",180),
    Horse("mark",170),
    Animal("don´t know")
]
# Count horses
horse_count = 0
for animal in animals:
    if isinstance(animal, Horse):
        horse_count += 1
print("Number of horses:", horse_count)


print("Is a Horse an Animal?", isinstance(animals[1], Animal))


