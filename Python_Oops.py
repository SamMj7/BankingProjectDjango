class Microwave:
    def __init__(self, brand: str, rating: str)-> None:
        self.brand = brand
        self.rating = rating
        self.turned_on: bool = False

    def turn_on(self)-> None:
        if self.turned_on:
            print(f"Microwave {self.brand} is already turned on.")
        else:
            self.turned_on: bool = True
            print(f"Microwave {self.brand} is now turned on.")

    def turn_off(self)-> None:
        if self.turned_on:
            self.turned_on: bool = False
            print(f"Microwave {self.brand} is now turned off.")
        else:
            print(f"Microwave {self.brand} is already turned off.")

    def run(self, seconds: int):
        if self.turned_on:
            print(f'Microwave {self.brand} runs for {seconds} "seconds".')
        else:
            print(f"Microwave is off, turn it on.")

    def __add__(self, other):
        return f"{self.brand} + {other.brand}"

    def __str__(self)-> str:                    #string dunder method
        return f'{self.brand} (Rating: {self.rating})' #even a kid should read it.

    def __repr__(self)-> str:           #representation dunder method--> developers should read it.
        return f'Microwave(brand = "{self.brand}", rating = "{self.rating}")'

smeg: Microwave = Microwave('Smeg', 'B')
bosch: Microwave = Microwave('bosch','C')

print(repr(smeg))
print(bosch)


