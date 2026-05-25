import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar

# CONFIG SELENIUM
options = Options()

# comenta esta línea si Google bloquea el clima
# options.add_argument("--headless")

options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
)

options.add_argument('--disable-blink-features=AutomationControlled')

driver_path = ChromeDriverManager().install()

if os.path.basename(driver_path) != "chromedriver":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver")

    if os.path.exists(binary_path):
        driver_path = binary_path

os.chmod(driver_path, 0o755)

driver = webdriver.Chrome(
    service=Service(driver_path),
    options=options
)

def procesar_input(user_input):

    user_input = user_input.lower()

    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima

    elif (
        "precio" in user_input
        or "accion" in user_input
        or "valor" in user_input
    ):
        return obtener_precio_accion

    return None


print("Chatbot listo. Escribe 'salir' para terminar")

while True:

    try:
        user_input = sanitizar(input("---> "))

        if user_input in ["salir", "exit", "quit"]:
            print(">>> Bye")
            break

        funcion = procesar_input(user_input)

        if funcion is None:
            print(">>> No entendí eso")

        else:
            respuesta = funcion(driver, user_input)
            print(">>>", respuesta)

    except KeyboardInterrupt:
        print("\n>>> Bye")
        break

    except Exception as e:
        print(">>> Error:", e)

driver.quit()