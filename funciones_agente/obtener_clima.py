from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_clima(driver, consulta):
    ciudad = (
        consulta
        .replace("clima", "")
        .replace("temperatura", "")
        .strip()
    )
    try:
        driver.get(f"https://wttr.in/{ciudad}?format=3&lang=es")
        resultado = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        ).text
        return resultado
    except Exception as e:
        return f"No se pudo obtener el clima: {e}"