class MiLista:
    def __init__(self):
        self.data = []

    def agregar(self, x):
        self.data.append(x)

    def eliminar(self, x):
        if x in self.data:
            self.data.remove(x)
        else:
            print(f"{x} no está en la lista")

    def mostrar(self):
        print(self.data)

if __name__ == "__main__":
    L = MiLista()
    L.agregar(5)
    L.agregar(10)
    L.mostrar()     
    L.eliminar(5)
    L.mostrar()      
