class dog:
    species="Bulldog"

    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

    def dis(self):
        print("NAME:", self.name)
        print("BREED:", self.breed)
        print("SPECIES:", dog.species)


d1=dog("TOM", "AMERICAN BULLDOG")
d2=dog("MAX","ENGLISH BULLDOG")


print("DETAILS OF DOG 1:")
d1.dis()
print("DETAILS OF DOG 2:")
d2.dis()

