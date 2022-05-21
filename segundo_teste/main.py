import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.yellowpages.com')

sleep(2)

elemento = navegador.find_element_by_link_text('Dentists')
elemento.click()

dentista = navegador.find_element_by_id('lid-467511214')
dentista.click()


