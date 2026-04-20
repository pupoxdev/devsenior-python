class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self._raza = raza
        self.__edad = edad
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa")
        
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self._raza}")
        print(f"Edad: {self.__edad} años")
        print("-" * 20)
        
def main():
        perro1 = Perro("Firulais", "Golden Retriever", 7)
        perro1.mostrar_info()
        
        perro1.set_edad(-5)
        perro1.mostrar_info()
        
        perro2 = Perro("Luna", "Siames", 2)
        perro2.mostrar_info()

if __name__ == "__main__": main()
    