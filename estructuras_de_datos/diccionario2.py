def mostrar_diccionario(dic):
    print("\nContenido del diccionario:")
    for clave, valor in dic.items():
        print(f"  {clave}: {valor}")


mi_dic = {}


mi_dic["nombre"] = "Carlos"
mi_dic["edad"] = 25
mi_dic["ciudad"] = "Lima"

mostrar_diccionario(mi_dic)


mi_dic["edad"] = 26
print("\nEdad actualizada a 26")


clave = "nombre"
if clave in mi_dic:
    print(f"\nValor de '{clave}': {mi_dic[clave]}")

del mi_dic["ciudad"]
print("\nClave 'ciudad' eliminada.")

mostrar_diccionario(mi_dic)
