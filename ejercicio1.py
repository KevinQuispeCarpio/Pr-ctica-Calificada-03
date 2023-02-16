# 1. Crea un programa en Python que simule una lista de compras. 
#El programa debe permitir al usuario agregar productos al final de la lista, eliminar productos del inicio de la lista y mostrar todos los productos en la lista en orden de compra.
###______________________________________________________________________________###

class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_producto(self, producto): # permitir al usuario agregar productos al final de la lista
        nuevo_nodo = Nodo(producto)

        if self.ultimo is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

        print(f"{producto} ha sido agregado a su lista de compras.")

    def eliminar_producto(self): # eliminar productos del inicio de la lista
        if self.primero is not None:
            primer_producto = self.primero.producto
            self.primero = self.primero.siguiente

            if self.primero is None:
                self.ultimo = None

            print(f"{primer_producto} ha sido eliminado de la lista de compras.")
        else:
            print("La lista de compras está vacía.")

    def mostrar_productos(self): # mostrar todos los productos en la lista en orden de compra.
        if self.primero is not None:
            print("___________ Lista de Compras __________")
            nodo_actual = self.primero

            while nodo_actual is not None:
                print("- " + nodo_actual.producto)
                nodo_actual = nodo_actual.siguiente
        else:
            print("Verifique su lista.\n¡¡¡¡esta vacia!!!!")

# Crear una lista enlazada vacía para almacenar los productos
lista_de_compras = ListaEnlazada()

# Ejecutar el programa
while True:
    print("\nElija la opción a realizar")
    print("1 - Agregar un producto a la lista")
    print("2 - Eliminar un producto de la lista")
    print("3 - Mostrar todos los productos en la lista")
    print("4 - Salir del programa")

    opcion = input("Ingresa el número de la opción que realizaras: ")

    if opcion == "1":
        producto = input("Ingrese el producto que esta comprando?: ")
        lista_de_compras.agregar_producto(producto)
    elif opcion == "2":
        lista_de_compras.eliminar_producto()
    elif opcion == "3":
        lista_de_compras.mostrar_productos()
    elif opcion == "4":
        print("¡Gracias por su compra!")
        break
    else:
        print("¡Opción inválida!.\nVerifique el numero seleccionado.")