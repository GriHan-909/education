import math

class Figure:
    sides_count = 0

    def __init__(self, list_colors, *list_sides):
        self.__sides = list(list_sides)
        self.__color = list_colors
        self.filled = True
        
    
    def get_color(self):
        return list(self.__color)
    
    def __is_valid_color(self, r,g,b):
        if int(r)<0 or int(r)>255:
            return False
        if int(g)<0 or int(g)>255:
            return False
        if int(b)<0 or int(b)>255:
            return False
        return True


    
    def set_color(self, r,g,b):        
        rgb = r,g,b
        if self.__is_valid_color(r,g,b):
            self.__color = list(rgb)

    def __is_valid_sides(self, side):
        if len(side) == len(self.__sides):
            for i in side:
                if not isinstance(i, int) or i<0:
                    return False
            return True

    def set_sides(self, *side):        
        if self.__is_valid_sides(side):
            self.__sides = list(side)



    def get_sides(self):
        return self.__sides            

    def __len__(self):        
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, list_colors, *list_sides):        
        if len(list_sides)==self.sides_count:
            super().__init__(list_colors, *list_sides)
            self.__radius = list_sides[0]/(2*math.pi)
        else:
            super().__init__(list_colors, 1)
            

    
    def get_square(self):
        return math.pi * self.__radius**2
    

class Triangle(Figure):
    sides_count = 3

    def __init__(self, list_colors, *list_sides):        
        if len(list_sides)==self.sides_count:
            super().__init__(list_colors, *list_sides)
            a, b, c = list_sides
            p = (a+b+c)/2
            self.__S = (p*(p-a)*(p-b)*(p-c))**0.5
            self.__height = 2*self.__S/a
        else:
            super().__init__(list_colors, 1,1,1)  
            

    
    def get_square(self):
        return self.__S


class Cube(Figure):
    sides_count = 12

    def __init__(self, list_colors, *list_sides):        
        
        if len(list_sides) != self.sides_count and len(list_sides) > 1:
            super().__init__(list_colors, *([1] * self.sides_count))
            
        else:            
            super().__init__(list_colors, *([list_sides[-1]] * self.sides_count)) 
            


    def get_volume(self):
        value = super().get_sides()        
        return value[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle1 = Triangle((200, 200, 100), 10,6,10)
print(triangle1.get_sides(), 'Произвольный треугольник')
print('Площадь треугольника:', triangle1.get_square())