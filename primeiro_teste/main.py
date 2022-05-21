import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.tripadvisor.com.br')

sleep(2)


#button_aceitar = navegador.find_element_by_id('onetrust-accept-btn-handler')
#button_aceitar.click()


primeiro_input = navegador.find_elements_by_tag_name('button')[-27]
primeiro_input.click()


campo_pesquisa = navegador.find_element_by_id('menu-item-0')
campo_pesquisa.click()


button_aceitar = navegador.find_element_by_id('onetrust-accept-btn-handler')
button_aceitar.click()
sleep(2)

pesquisar = navegador.find_element_by_xpath('//*[@id="lithium-root"]/header/div/nav/div/div[1]/div/div/form/input[1]')
pesquisar.click()
pesquisar.send_keys('Belo Horizonte')
pesquisar.submit()

sleep(1)


page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')


turismo = site.find('div', attrs={'class': 'ui_column is-12 content-column result-card result-card-default'})

print(turismo.prettify())

turismo_titulo = turismo.find('div', attrs={'class': 'result-title'})
turismo_descricao = turismo.find('span', attrs={'class': 'geo-description'})
turismo_localizacao = turismo.find('div', attrs={'class': 'mobile-address-text'})


print(turismo_descricao)