class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        print(f"Apilando: {elemento}")
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            print(f"Desapilando: {elemento}")
            return elemento
        else:
            print("La pila está vacía. No se puede desapilar.")

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Pila (base → tope):")
        for i, item in enumerate(self.items):
            print(f"  [{i}] {item}")


