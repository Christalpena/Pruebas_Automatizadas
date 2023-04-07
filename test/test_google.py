from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_google(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')
        time.sleep(10)

    def test01_barra_navegacon(self):
        self.nav=self.driver.find_element(By.NAME, "q")
        self.driver.save_screenshot("test/img/barra/barra.png")

        self.nav.send_keys("Twilight" + Keys.ENTER)
        self.driver.save_screenshot("test/img/barra/Busqueda_en_barra.png")
        time.sleep(5)

    def test02_informacion(self):
        self.test01_barra_navegacon()
        time.sleep(15)
        self.driver.save_screenshot("test/img/inf/siguiendo_el_link.png")
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/div/a/h3").click()
        self.driver.save_screenshot("test/img/inf/despues_del_link.png")

        time.sleep(5)

    def test03_imagen(self):
        self.test01_barra_navegacon()
        self.driver.find_element(By.XPATH, "//*[@id='hdtb-msb']/div[1]/div/div[2]/a").click()
        self.driver.save_screenshot("test/img/sele_imag/viendo_img.png")
        self.driver.find_element(By.XPATH, "//*[@id='islrg']/div[1]/div[1]/a[1]/div[1]/img").click()
        self.driver.save_screenshot("test/img/sele_imag/seleccionando_img.png")
        time.sleep(10)

    def test04_videos(self):
        self.test01_barra_navegacon()
        self.driver.find_element(By.XPATH, "//*[@id='hdtb-msb']/div[1]/div/div[3]/a").click()
        self.driver.save_screenshot("test/img/video/pagina_video.png")
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/a/h3").click()
        self.driver.save_screenshot("test/img/video/seleccionando_video.png")

        time.sleep(10)


    def test05_filtros(self):
        self.test01_barra_navegacon()
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div[4]/div/div[1]/div/div[2]/div").click()
        self.driver.save_screenshot("test/img/filtros/seleccionando_herramienta.png")
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div[4]/div/div[2]/div/span[1]/g-popup/div[1]/div/div/div").click()
        self.driver.save_screenshot("test/img/filtros/seleccionando_idioma.png")
        self.driver.find_element(By.XPATH, "//*[@id='lb']/div/g-menu/g-menu-item[2]/div/a").click()
        time.sleep(8)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()






