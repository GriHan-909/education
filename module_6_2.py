class Vehicle:
    __COLOR_VARIANTS = [ 'dark_red', 'yelow', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):
        return f'Модель: {self.__model}'
    
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    
    def get_color(self):
        return f'Цвет: {self.__color}'
    
    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep='\n')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()            
        else:
            print(f'Нельзя сменить цвет на {new_color.lower()}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, __model, __engine_power, __color):
        super().__init__(owner, __model, __engine_power, __color)
       


vehicle1 = Sedan('Greg', 'Toyota Mark II', 900, 'red')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Grey')
vehicle1.set_color('YelOw')
vehicle1.owner = 'Artur'

# Проверяем что поменялось
vehicle1.print_info()