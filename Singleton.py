class Pizza:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

pizza = Pizza()
pizza.name = 'A delicious pie that may contain meat, cheese, and/or vegetables'
pizza1 = Pizza()
print(pizza.name)
print(pizza1.name)
#both outputs will be the same since only a single instance can be used