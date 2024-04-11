class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  

    # Getter para obtener la edad
    def get_edad(self):
        return self._edad

    # Setter para establecer la edad
    def set_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad

# Ejemplo de uso
persona = Persona("Juan", 53)

# Obtener la edad usando el getter
print(persona.get_edad())  # Salida: 53

# Establecer la edad usando el setter
persona.set_edad(58)

# Intentar establecer una edad negativa (lo que generará una excepción)
try:
    persona.set_edad(-5)
except ValueError as e:
    print(e)  # Salida: La edad no puede ser negativa


"""Exactamente. Los getters y setters en Python son una forma de controlar el acceso
y la modificación de los atributos de una clase. Aunque Python no tiene verdaderos atributos
"privados" como en otros lenguajes de programación orientada a objetos, la convención es usar
la barra baja _ al principio de un nombre de atributo para indicar que es "protegido", lo que
significa que no se debe acceder o modificar directamente desde fuera de la clase."""


"""En resumen, los getters y setters en Python son una forma de implementar encapsulación y 
control de acceso, permitiendo que algunos atributos sean tratados como "privados" y
proporcionando métodos públicos para interactuar con ellos. Esto ayuda a mantener un diseño
limpio y modular, y facilita la gestión y modificación de los objetos de la clase en el futuro."""