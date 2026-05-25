from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima

def test_chatbot():

    print("--- Iniciando pruebas ---")

    print("\n[Prueba] Precio Microsoft")
    resultado_precio = obtener_precio_accion(None, "precio microsoft")
    print(resultado_precio)

    print("\n[Prueba] Clima CDMX")
    resultado_clima = obtener_clima(None, "clima cdmx")
    print(resultado_clima)

    print("\n--- Fin de pruebas ---")


if __name__ == "__main__":
    test_chatbot()