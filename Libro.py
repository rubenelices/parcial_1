class Libro():
    def __init__(self,titulo,autor,fecha,editorial,ISBN):
        self.titulo=titulo
        self.autor=autor
        self.fecha=fecha
        self.editorial=editorial
        self.ISBN=ISBN

    #GETTERS
    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getFecha(self):
        return self.Fecha

    def getEditorial(self):
        return self.editorial

    def getISBN(self):
        return self.ISBN
    
    #SETTERS
    def setTitulo(self,titulo):
        self.titulo=titulo

    def setAutor(self,autor):
        self.autor=autor

    def setFecha(self,fecha):
        self.fecha=fecha

    def setEditorial(self,editorial):
        self.editorial=editorial

    def setISBN(self,ISBN):
        self.ISBN=ISBN

    def __str__(self):
        """Retorna una representación en cadena del libro."""
        return f"Libro: {self.titulo}, Autor: {self.autor}, Fecha: {self.fecha}, Editorial: {self.editorial}, ISBN: {self.ISBN}"
    
    # Creando una instancia de la clase Libro
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "1967", "Editorial Sudamericana", "978-84-376-0494-7")

# Imprimiendo la representación de la instancia
print(mi_libro)
