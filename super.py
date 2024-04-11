"""En Python, super() es una función que se utiliza para llamar métodos de la clase
base o superclase desde una subclase. Permite acceder a los métodos y atributos de
la clase base en la jerarquía de herencia de manera dinámica y flexible"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("¡El animal hace un sonido!")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        super().hacer_sonido()
        print("Guau! Guau!")

# Crear una instancia de la subclase Perro
mi_perro = Perro("Fido", "Labrador")
mi_perro.hacer_sonido()


"""En este ejemplo, la clase Perro hereda de la clase Animal.
Cuando se llama al método hacer_sonido() en una instancia de Perro, super().hacer_sonido()
llama al método hacer_sonido() de la clase base Animal, y luego se imprime "Guau! Guau!".
Esto permite que la funcionalidad de la clase base se extienda o modifique en la subclase
según sea necesario, manteniendo al mismo tiempo la lógica de la clase base intacta."""