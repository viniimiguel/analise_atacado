from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import openpyxl


class Carrefour():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = 'https://mercado.carrefour.com.br/mercearia#crfimt=home|mercado|hotbar|mercearia|091023|9'
        self.site_map = {
            'XP':{
                'cep': 'zipcode',
                'buscar': '/html/body/div[5]/div/div/div/div[2]/div/section/div/div[2]/div/div/form/button'
            }
        }
        self.cep = '55660000'

    def main(self):
        self.abre()
        sleep(2)
        self.cidade()
        sleep(2)
        self.raspagem()
        sleep(123123123)

    def abre(self):
        self.driver.get(self.link)
        self.driver.maximize_window()
        sleep(4)
    
    def cidade(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys('\n').perform()
            sleep(3)
            self.driver.find_element(By.NAME, self.site_map['XP']['cep']).click()
            sleep(3)
            ce = self.driver.find_element(By.NAME, self.site_map['XP']['cep'])
            ce.send_keys('55660000')
            sleep(3)
            self.driver.find_element(By.XPATH, self.site_map['XP']['buscar']).click()


        except NoSuchElementException:
            print('elemento nao encontrado!')

        except Exception as e:
            print(f'error as {e}')
    def down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)

    def raspagem(self):
        global armazena_nome, armazena_preco
        contador = 1
        armazena_nome = []
        armazena_preco = []
        while True:
            self.down()
            my_dict = {
                'XP':{
                    'nome': f'/html/body/div[2]/main/section[2]/div[2]/div[2]/div[5]/div[1]/ul/li[{contador}]/article/div[1]/section/div[2]/h3/span/a',
                    'preco': f'/html/body/div[2]/main/section[2]/div[2]/div[2]/div[5]/div[1]/ul/li[{contador}]/article/div[1]/section/div[4]',
                    'passa': f'/html/body/div[2]/main/section[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div/div[6]/a/button',
                                
                            
                }
            }
            try:
                nome = self.driver.find_element(By.XPATH, my_dict['XP']['nome'])
                preco = self.driver.find_element(By.XPATH, my_dict['XP']['preco'])

                nome_text = nome.text
                preco_text = preco.text

                print(nome_text)
                print(preco_text)
                print(contador)
                
                contador += 1

                sleep(1)

            except NoSuchElementException:
                print('nao tem mais elementos na tela')
                try:
                    self.driver.find_element(By.XPATH, my_dict['XP']['passa']).click()

                except NoSuchElementException:
                    break
                except Exception as e:
                    print(f'error {e}')
            
            except Exception as e:
                print(f'error {e}')

   
     


carrefour = Carrefour()
carrefour.main()