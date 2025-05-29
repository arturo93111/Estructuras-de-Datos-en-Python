from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, elemento):
        print(f"Encolando: {elemento}")
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            elemento = self.items.popleft()
            print(f"Desencolando: {elemento}")
            return elemento
        else:
            print("La cola está vacía. No se puede desencolar.")

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Cola (frente → final):")
        for i, item in enumerate(self.items):
            print(f"  [{i}] {item}")


if __name__ == "__main__":
    cola = Cola()

    cola.encolar("Cliente 1")
    cola.encolar("Cliente 2")
    cola.encolar("Cliente 3")

    cola.mostrar()

    cola.desencolar()
    cola.mostrar()

    cola.desencolar()
    cola.desencolar()
    cola.desencolar() 
