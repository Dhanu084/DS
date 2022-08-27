class Garage:

    def __init__(self) -> None:
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        return self.cars[index]
    
    def __repr__(self) -> str:
        return f'<Garage {self.cars}>'
    
    # def __str__(self) -> str:
    #     return f'Garage Object with {len(self)} cars'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))

for car in ford:
    print(car)

print(ford)