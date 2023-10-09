from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium.common.exceptions import NoSuchElementException


class Atacadao():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.site_link = 'https://www.atacadao.com.br/mercearia/'
        self.cidade = '55660000'
        self.site_map = {
            'XP':{
                'cep': '/html/body/div[7]/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/input',
                'confirmar': '/html/body/div[7]/div/div/div/div/div/div/div[2]/div/div[3]/button[2]'
            }
        }

    def main(self):
        self.abre()
        sleep(1)
        self.cep()
        sleep(12312312)

    def abre(self):
        self.driver.get(self.site_link)
        self.driver.maximize_window()

    def cep(self):
        cidade = self.driver.find_element(By.XPATH, self.site_map['XP']['cep'])
        sleep(1)
        cidade.send_keys(self.cidade)
        sleep(3)
        self.driver.find_element(By.XPATH, self.site_map['XP']['confirmar']).click()
        sleep(5)
    



atacadao = Atacadao()
atacadao.main()
