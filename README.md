### 👠 LadyStore Server

Servidor que atende às demandas da LadyStore, uma loja de vestuário, nas atividades internas, como o gerenciamento de clientes e fornecedores, além do registro de vendas.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🛠️ Instalação e Configuração

O sistema foi desenvolvido utilizando **Python 3.12**, sendo recomendada a utilização dessa versão para garantir compatibilidade.

#### 1️⃣ Clonar o Repositório

Será necessário adquirir uma cópia local do código-fonte, que pode ser obtida com o seguinte comando:

```bash
git clone https://github.com/DiovanaS/ladystore-server
```

#### 2️⃣ Instalar as Dependências

No diretório da aplicação, instale as dependências utilizando o `pip`:

```bash
pip install -r requirements.txt
```

Pode ser necessário instalar o pacote `en_core_web_sm`. O comando pode variar conforme o sistema operacional.

- Para sistemas 🐧 **Linux**:

  ```bash
  python3 -m spacy download en_core_web_sm
  ```

- Para sistemas 🪟 **Windows**:

  ```bash
  python -m spacy download en_core_web_sm
  ```

#### 3️⃣ Configurar as Variáveis de Ambiente

Crie um arquivo `.env` com base no modelo fornecido em `.env.example.` Neste arquivo, especifique os seguintes campos:

- `SECRET_KEY` - Chave secreta do servidor, que deve ser longa e conter múltiplos caracteres;
- `ALLOWED_HOSTS` - Uma lista de endereços (ou domínios) permitidos para fazer requisições ao servidor, separados por espaço.

#### 4️⃣ Executar

Após concluir as etapas anteriores, você poderá inicializar o servidor com o seguinte comando:

```bash
flask --app app run
```

### 📚 Documentação

A documentação é gerada conforme o padrão Swagger através do Flask-RESTx e fica disponível na URL base (`/`). Para testes locais, acesse `http://localhost:5000/`.

### ⚖️ Licença

Este repositório adota a **Licença MIT**, permitindo o uso e a modificação do código como desejar. Peço apenas que seja dado o devido crédito, reconhecendo o esforço e o tempo investidos no desenvolvimento.
