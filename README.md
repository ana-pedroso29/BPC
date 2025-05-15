# bpc_transparencia

Este é um projeto Django para buscar informações sobre o Benefício de Prestação Continuada (BPC) por município, utilizando dados do Portal da Transparência do Governo Federal. A busca é realizada através da seleção de Estado e Município, com o código IBGE sendo obtido dinamicamente através da API do IBGE.

## Funcionalidades

* **Busca por Estado e Município:** Os usuários podem selecionar um estado e, em seguida, um município para refinar a busca.
* **Utilização da API do IBGE:** O código IBGE do município selecionado é obtido automaticamente através da API do Instituto Brasileiro de Geografia e Estatística (IBGE).
* **Integração com a API do Portal da Transparência:** Os dados do BPC para o município e mês/ano especificados são buscados na API do Portal da Transparência.
* **Exibição de Resultados:** Os resultados da busca (nome do beneficiário, NIS, valor) são exibidos em uma tabela.

## Pré-requisitos

* **Python 3.x** instalado no seu sistema.
* **pip** (gerenciador de pacotes do Python) instalado.

## Instalação

1.  **Clone o repositório (se aplicável):**
    ```bash
    git clone git clone [https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
cd bpc_transparencia
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv bpc_env
    source bpc_env/bin/activate   # No Linux/macOS
    bpc_env\Scripts\activate.bat  # No Windows (prompt de comando)
    .\bpc_env\Scripts\Activate.ps1 # No Windows (PowerShell)
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    (Certifique-se de ter gerado o arquivo `requirements.txt` conforme explicado anteriormente.)

4.  **Aplique as migrações do Django:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o painel de administração (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

## Execução

1.  **Inicie o servidor de desenvolvimento do Django:**
    ```bash
    python manage.py runserver
    ```

2.  **Acesse a aplicação no seu navegador:**
    * Abra o seu navegador e vá para `http://127.0.0.1:8000/buscar/`.

## Uso

1.  Na página inicial, selecione o **Estado** desejado no primeiro campo de seleção.
2.  O campo de **Município** será carregado dinamicamente com os municípios do estado selecionado. Escolha o município desejado.
3.  Informe o **Mês e Ano** de referência no formato `AAAAMM` (ex: `202412`).
4.  Clique no botão **Buscar**.
5.  Os resultados da busca serão exibidos na página seguinte, mostrando informações sobre os beneficiários do BPC naquele município e mês/ano.

## Próximos Passos (Ideias para Melhorias)

* Melhorar a interface do usuário com CSS e talvez um framework como Bootstrap.
* Implementar paginação para lidar com grandes volumes de dados.
* Adicionar opções de filtro nos resultados da busca.
* Implementar tratamento de erros mais robusto para falhas na API.
* Permitir que o usuário exporte os resultados para formatos como CSV.

## Contribuição

Se você tiver ideias para melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

[Adicione aqui a licença do seu projeto, se houver. Por exemplo, MIT License, Apache 2.0, etc.]
