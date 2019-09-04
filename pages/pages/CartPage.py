from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class CartPage():

    def __init__(self, app):
        self.app = app

    def home_page(self):
        self.app.get('https://lojavirtualdemo.com')

    def seleciona_produto(self):
        btn_comprar = self.app.find_element_by_xpath('//*[@id="content"]/article/div/div/div/div/section[9]/div/div/div/div/div/div[3]/div/div/ul/li[14]/div/ul/li[5]/a')
        btn_comprar.click()
        sleep(3)
        ver_carrinho = self.app.find_element_by_class_name('wcmenucart')
        ver_carrinho.click()
        sleep(5)
        btn_fechar_compra = self.app.find_element_by_class_name('checkout-button')
        btn_fechar_compra.click()
    
    def preenche_informacoes(self):
        nome = self.app.find_element_by_id('billing_first_name')
        nome.send_keys('João')
        
        sobrenome = self.app.find_element_by_id('billing_last_name')
        sobrenome.send_keys('Barreto')

        endereco = self.app.find_element_by_id('billing_address_1')
        endereco.send_keys('Rua dos Dourados')

        cidade = self.app.find_element_by_id('billing_address_1')
        cidade.send_keys('São Paulo')

        cep = self.app.find_element_by_id('billing_postcode')
        cep.send_keys('04474-160')

        phone = self.app.find_element_by_id('billing_phone')
        phone.send_keys('119980804920')

        email = self.app.find_element_by_id('billing_email')
        email.send_keys('desafioinmetrics@gmail.com')

        btn_fechar_compra_paypal = self.app.find_element_by_id('place_order')
        btn_fechar_compra_paypal.click()

        sleep(5)

    def exibe_alerta(self):
        alerta = self.app.find_element_by_class_name('woocommerce-error')
        alerta.is_displayed()



