### 👠 LadyStore Backend

Servidor que atende às demandas da LadyStore, uma loja de vestuário, nas atividades internas, como o gerenciamento de clientes e fornecedores, além do registro de vendas.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🛠️ Instalação e Configuração

O sistema foi desenvolvido utilizando **Python 3.12**, sendo recomendada a utilização dessa versão para garantir compatibilidade.

#### 1️⃣ Clonar o Repositório

Será necessário adquirir uma cópia local do código-fonte, que pode ser obtida com o seguinte comando:

```bash
git clone https://github.com/DiovanaS/ladystore-backend
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

#### 3️⃣ Executar

Após concluir as etapas anteriores, você poderá inicializar o servidor com o seguinte comando:

```bash
flask --app app run
```

### 📚 Documentação

Em breve...

### ⚖️ Licença

Este repositório adota a **Licença MIT**, permitindo o uso e a modificação do código como desejar. Peço apenas que seja dado o devido crédito, reconhecendo o esforço e o tempo investidos no desenvolvimento.
