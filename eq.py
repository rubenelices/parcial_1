"""El método __eq__() en Python es un método especial que se utiliza para
 comparar objetos y determinar si son iguales. Este método es invocado automáticamente
   cuando se utiliza el operador de igualdad (==) para comparar dos objetos de una clase."""


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

# Crear dos objetos Punto
punto1 = Punto(1, 2)
punto2 = Punto(1, 2)                                                                                  
punto3 = Punto(3, 4)

# Comprobar si los puntos son iguales
print(punto1 == punto2)  # True
print(punto1 == punto3)  # False


"""En este ejemplo, la clase Punto define el método __eq__(), que compara las coordenadas
x e y de dos puntos para determinar si son iguales. Cuando se llama al operador de igualdad
(==), Python invoca automáticamente el método __eq__() de la primera instancia (punto1) y
pasa la segunda instancia (punto2) como argumento. Si el método __eq__() devuelve True, 
se considera que los puntos son iguales; de lo contrario, se consideran diferentes."""