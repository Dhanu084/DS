class FixedFloat:

    def __init__(self, amount) -> None:
        self.amount = amount
    @classmethod
    def fixedFloat(cls, amount):
        return cls(amount)

class Euro(FixedFloat):
    def __init__(self, amount) -> None:
        super().__init__(amount)
    
f  = FixedFloat(20)
print(FixedFloat.fixedFloat(20))

euro = Euro(20)
print(Euro.fixedFloat(20))