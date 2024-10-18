from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Função para imprimir informações do elemento
def print_element_info(element, name):
    print(f"{name} encontrado:")
    print(f"Texto: {element.text}")
    print(f"Atributo 'class': {element.get_attribute('class')}")
    print(f"Atributo 'aria-label': {element.get_attribute('aria-label')}\n")

# Variáveis de configuração
email = "SEU_EMAIL_AQUI"  # Insira seu e-mail aqui
senha = "SUA_SENHA_AQUI"  # Insira sua senha aqui
url_login = "https://comunidade.onebitcode.com/users/sign_in?post_login_redirect=https%3A%2F%2Fcomunidade.onebitcode.com%2Ffeed#email"

# URL da aula (substitua pela URL da primeira aula do curso)
url_aula = "URL_DA_PRIMEIRA_AULA_AQUI"  # Insira a URL da primeira aula aqui

# Inicializa o WebDriver
driver = webdriver.Chrome()  # ou o driver que você estiver usando
driver.maximize_window()  # Coloca o navegador em tela cheia

try:
    # Acessa a página de login
    driver.get(url_login)

    # Localiza o input de email e insere o email
    email_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/form/div[1]/div[2]/input')
    email_input.send_keys(email)
    print_element_info(email_input, "Campo de Email")

    # Localiza o input de senha e insere a senha
    password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div[2]/input')
    password_input.send_keys(senha)
    print_element_info(password_input, "Campo de Senha")

    # Clica no botão de login
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/form/div[4]/button')
    login_button.click()
    print_element_info(login_button, "Botão de Login")

    # Aguardar 4 segundos
    time.sleep(4)
    
    # Acessa a URL da aula (apenas uma vez)
    driver.get(url_aula)

    # Adiciona uma espera explícita para garantir que o elemento esteja presente
    contador_elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Aula") and contains(text(), "de")]'))
    )
    contador_inicial = contador_elemento.text
    print(f"Contador inicial: {contador_inicial}")

    while True:
        try:
            # Adiciona uma espera explícita para garantir que o botão esteja presente
            botao_concluir = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[text()="Concluída" or text()="Concluir aula"]'))
            )
            texto_botao = botao_concluir.text
            print(f"Botão encontrado: {texto_botao}")  # Adiciona print quando o botão é encontrado

            if texto_botao == "Concluída":
                botao_concluir.click()
                time.sleep(2)  # Aguarda 2 segundos
                driver.refresh() # Atualiza a página
            elif texto_botao == "Concluir aula":
                botao_concluir.click()
                time.sleep(4)  # Aguarda a página carregar a próxima aula

                # Obtém o novo contador de aulas
                contador_elemento = driver.find_element(By.XPATH, '//span[contains(text(), "Aula") and contains(text(), "de")]')
                contador_final = contador_elemento.text
                print(f"Contador final: {contador_final}")

                # Aqui você pode adicionar uma condição para sair do loop se todas as aulas forem concluídas
                # Exemplo: se contador_final for igual a "Aula 326 de 326", você pode sair do loop

        except Exception as inner_e:
            print(f"Ocorreu um erro ao tentar localizar o botão: {inner_e}")
            break  # Sai do loop se ocorrer um erro

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    driver.quit()
    print("Finalizou a automação.")
