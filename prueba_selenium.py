import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

if os.path.basename(driver_path) != "chromedriver":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver")

    if os.path.exists(binary_path):
        driver_path = binary_path

os.chmod(driver_path, 0o755)

driver = webdriver.Chrome(service=Service(driver_path))

try:
    driver.get("https://www.google.com")
    sleep(2)

    driver.get("https://hybridge.education")
    sleep(2)

    driver.get("https://openai.com")
    sleep(2)

    print("Prueba Selenium completada correctamente")

except Exception as e:
    print("Error Selenium:", e)

finally:
    driver.quit()
