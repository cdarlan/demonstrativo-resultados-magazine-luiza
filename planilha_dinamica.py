# Demonstrativo de Resultados da Magazine Luiza

# Passo 1: Entrar em https://ri.magazineluiza.com.br/
# Passo 2: Clicar em "planilha Dinâmica"
# Passo 3: Clicar em "Clique aqui para fazer o download"

from selenium import webdriver

navegador = webdriver.Firefox(executable_path=r'./geckodriver.exe')

navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img').click()
navegador.find_element_by_xpath('//*[@id="bWtQ7n6RcQdDDDCgCcH3yg=="]').click()
