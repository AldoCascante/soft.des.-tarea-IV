from order_interface import *
from workers_interface import *

if __name__ == "__main__":
    ordenes = []
    cadena_de_trabajo = Baker()
    cadena_de_trabajo.set_next(Barista())

    print("=== Simulacion de Cafeteria ===")

    print("Cliente: Ana")
    ordenes.append(Order_Composite("Bebida", "Cafe"))
    ordenes[0].add_component(Order_Component("Ingrediente", "leche"))
    ordenes[0].add_component(Order_Component("Ingrediente", "canela"))
    print("Ordena un " + ordenes[0].get_name())

    ordenes.append(Order_Composite("Reposteria", "Croissant"))
    ordenes[1].add_component(Order_Component("Ingrediente", "relleno de chocolate"))
    print("Ordena un " + ordenes[1].get_name())

    print("\nCliente: Carlos")
    ordenes.append(Order_Composite("Bebida", "Te verde"))
    print("Ordena un " + ordenes[2].get_name())

    ordenes.append(Order_Composite("Bebida", "Cafe"))
    ordenes[3].add_component(Order_Component("Modificacion", "doble espresso"))
    ordenes[3].add_component(Order_Component("Ingrediente", "crema"))
    print("Ordena un " + ordenes[3].get_name() + "\n")

    for orden in ordenes:
        cadena_de_trabajo.handle(orden)

    print("\n[Sistema]: Se notifican los clientes cuando sus pedidos estan listos.")
