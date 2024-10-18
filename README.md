# Desafio 01: Automação de Aulas - OneBitCode

Este projeto foi desenvolvido como parte do Desafio 01 da Comunidade OneBitCode, onde o objetivo é automatizar a marcação de aulas em uma nova plataforma de cursos. O script utiliza o Selenium para facilitar o processo de conclusão de aulas, permitindo que os alunos marquem suas aulas como concluídas automaticamente.

## 🛠️ O Problema

Com a mudança para a nova plataforma, os alunos perderam o histórico de progresso. A solução mais simples seria marcar as aulas manualmente, mas como programadores, podemos criar um "robô" para fazer isso por nós!

## 💡 A Solução

Este script de automação do navegador permite que os alunos marquem como concluídas as aulas de um curso e módulos automaticamente, com um delay de 5 segundos por aula.

## Pré-requisitos

Antes de executar o projeto, você precisará ter o seguinte instalado:

- Python 3.x
- Selenium
- WebDriver para o navegador que você deseja usar (por exemplo, ChromeDriver para Google Chrome)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/desafio01_automacao_aulas_onebitcode.git
   cd desafio01_automacao_aulas_onebitcode
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install selenium
   ```

3. Baixe o WebDriver correspondente ao seu navegador e adicione-o ao seu PATH.

## Configuração

Antes de executar o script, você precisará configurar algumas variáveis no arquivo `main.py`:

- **email**: Insira seu e-mail aqui.
- **senha**: Insira sua senha aqui.
- **url_aula**: Insira a URL da primeira aula do curso.

```python
email = "SEU_EMAIL_AQUI"  # Insira seu e-mail aqui
senha = "SUA_SENHA_AQUI"  # Insira sua senha aqui
url_aula = "URL_DA_PRIMEIRA_AULA_AQUI"  # Insira a URL da primeira aula aqui
