class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años."


"""En esta clase, hemos definido el método __str__() que devuelve una cadena que describe 
el nombre y la edad de una persona. Ahora, si creamos una instancia de esta clase y llamamos
 a la función str() en ella, el método __str__() se llamará automáticamente"""

persona = Persona("Juan", 53)
print(str(persona))  # Salida: Juan tiene 53 años.


"""El método __str__() es útil para personalizar cómo se muestra la información sobre un objeto,
lo que facilita la depuración y la comprensión del código. Es especialmente útil al trabajar con
clases personalizadas donde queremos tener una representación legible y significativa de los 
objetos de esa clase."""