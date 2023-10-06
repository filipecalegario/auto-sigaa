import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Carregue a planilha
df = pd.read_excel("template.xlsx")
print('Planilha carregada com sucesso!')
print(df.dtypes)

# Inicie o navegador
driver = webdriver.Chrome()
print('Navegador iniciado com sucesso!')

# Abra a página
driver.get("https://sigaa.ufpe.br/")
print('Página aberta com sucesso!')

input("Faça o login e navegue até a página de lançamento de notas. Pressione Enter quando estiver na página de lançamento de notas...")

for index, row in df.iterrows():
    try: 
        # Supondo que você tem uma coluna "NOME" e uma coluna "NOTA" em sua planilha
        estudante = row["NOME"]
        nota = row["NOTA"]

        # Localize o elemento TD que contém o nome atual da lista de estudantes
        td_aluno = driver.find_element(By.XPATH, f"//td[contains(text(), '{estudante}')]")
        print(f"achou: {td_aluno.text}")

        duration = 0.5

        # A partir do TD, navegue até o TR pai e depois localize o input de nota que está no próximo TD
        input_nota = td_aluno.find_element(By.XPATH, "./following-sibling::td/input")

        # Agora, o Selenium irá interagir com o input para preencher a nota
        # É preciso multiplicar por 10, por conta da entrada de dados do SIGAA que já adicionar a vírgula automaticamente
        input_nota.send_keys(str(nota*10)) 
        time.sleep(duration)
    except:
        print(f"Erro ao tentar achar: {estudante}")

print("Script finalizado com sucesso!")
print("Verifique se as notas foram lançadas corretamente.")
print("LEMBRE-SE DE APERTAR O BOTÃO SALVAR NO SIGAA!")
input("Pressione Enter para fechar o browser...")
driver.close()