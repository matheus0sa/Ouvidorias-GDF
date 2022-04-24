from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import Keys
from time import sleep
import os

def baixar_csv():

    driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
    os.chdir(r"C:\Users\mathe\Downloads")
    arquivos0 = os.listdir()
    driver.get("http://www.painel.ouv.df.gov.br/dashboard")

    exportar = '/html/body/app-root/app-nav-wrapper/div/div[2]/div[2]/app-visao-geral/app-content-page/div[1]/div[1]/app-container-filtro/div[1]/div[2]/div[2]'
    WebDriverWait(driver, timeout=180).until(EC.presence_of_element_located((By.XPATH, exportar)))
    exportar = driver.find_element(by=By.XPATH, value=exportar)
    sleep(1)
    exportar.click()

    baixar = '/html/body/div[2]/div/div[3]/button[1]'
    WebDriverWait(driver, timeout=180).until(EC.presence_of_element_located((By.XPATH, baixar)))
    sleep(1)
    baixar = driver.find_element(by=By.XPATH, value=baixar)
    baixar.click()
    contador = 0
    while contador < 1:
        arquivos1 = os.listdir()
        for arquivo in arquivos1:
            if (arquivo in arquivos0):
                pass

            elif arquivo.endswith('.csv'):
                driver.quit()
                contador = 1
                return  arquivo



if __name__ == '__main__':
    baixar_csv()
