import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima
from utils.sanitizar import sanitizar

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

driver_path = ChromeDriverManager().install()
if os.path.basename(driver_path) != "chromedriver.exe":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver.exe")
    if os.path.exists(binary_path):
        driver_path = binary_path

driver = webdriver.Chrome(service=Service(driver_path), options=options)


def procesar_input(user_input):
    user_input = user_input.lower()
    if "clima" in user_input or "temperatura" in user_input:
        return "clima"
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return "accion"
    return None


def main():
    print("Chatbot listo. Escribe 'salir' para terminar")

    while True:
        user_input = sanitizar(input("---> "))

        if user_input in ["salir", "exit", "quit"]:
            print(">>> Bye")
            driver.quit()
            break

        tipo = procesar_input(user_input)

        if tipo is None:
            print(">>> No entendí eso")
        elif tipo == "clima":
            print(">>>", obtener_clima(driver, user_input))
        elif tipo == "accion":
            print(">>>", obtener_precio_accion(driver, user_input))


if __name__ == "__main__":
    main()