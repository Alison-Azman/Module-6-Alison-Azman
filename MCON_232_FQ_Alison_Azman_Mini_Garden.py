
class Flower:
    def __init__(self, name, petals, color, height):
        self.name=name
        self.petals=petals
        self.color=color
        self.height=height

    def describe(self):
        return f"{self.name} is {self.color}, has {self.petals} petals, and is {self.height} cm tall."

    def grow(self, amount):
        self.height+=amount


rose=Flower("Rose", 12, "red", 4)
tulip=Flower("Tulip", 4, "pink", 2)
daisy=Flower("Daisy", 8, "yellow", 3)
lily=Flower("Lily", 14, "purple", 6)

print(rose.describe())
print(tulip.describe())
print(daisy.describe())
print(lily.describe())

print()

rose.grow(2)
tulip.grow(1)
daisy.grow(3)
lily.grow(4)

print(rose.describe())
print(tulip.describe())
print(daisy.describe())
print(lily.describe())
print()
garden=[]
garden.append(rose)
garden.append(tulip)
garden.append(daisy)
garden.append(lily)

for flower in garden:
    print("\nBefore new growth")
    print(flower.describe())
    flower.grow(2)
    print(flower.describe())
