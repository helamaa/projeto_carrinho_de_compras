# 🛒 Carrinho de Compras em Python

Programa de linha de comando desenvolvido em Python que simula um carrinho de compras, permitindo adicionar, visualizar, remover itens e calcular o valor total da compra.

## 📋 Sobre o Projeto

Este projeto foi criado como exercício prático para consolidar conceitos fundamentais de **listas** em Python, incluindo criação, manipulação, percurso (loops), listas paralelas e remoção de itens. O programa simula um fluxo real de uso: o usuário interage por meio de um menu, e todas as informações são armazenadas em memória durante a execução.

## ✨ Funcionalidades

- **Adicionar item**: insere um novo produto no carrinho, informando nome e preço.
- **Ver carrinho**: exibe todos os itens adicionados, com preço formatado em reais.
- **Remover item**: permite remover um item específico pelo número exibido na listagem.
- **Calcular o total**: soma os preços de todos os itens e exibe o valor total da compra.
- **Validação de entrada**: trata erros ao digitar preços ou índices inválidos, evitando que o programa quebre.
- **Menu interativo em loop**: o programa continua rodando até que o usuário escolha sair.

## 🧠 Conceitos de Python Aplicados

- Criação e manipulação de **listas** (`list`)
- **Listas paralelas** (`nomes` e `precos` sincronizadas pelo mesmo índice)
- Laços de repetição (`while` e `for`) e uso de `range(len(...))`
- Tratamento de exceções com `try` / `except` (`ValueError`)
- Formatação de strings com **f-strings** (`f"{variavel:.2f}"`, alinhamento de texto)
- Uso do operador `+=` para acumular valores
- Métodos de lista: `append()` e `pop()`
- Estruturas condicionais (`if` / `elif` / `else`)
- Boas práticas de nomenclatura (nomes de variáveis no plural para listas)

## 🚀 Como Executar

### Pré-requisitos
- [Python 3](https://www.python.org/downloads/) instalado na máquina

### Passos

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/nome-do-repositorio.git

# Acesse a pasta do projeto
cd nome-do-repositorio

# Execute o programa
python carrinho.py
```

> Substitua `carrinho.py` pelo nome real do arquivo do seu script.

## 💻 Exemplo de Uso

```
========================================
 Bem-vindos ao Programa de Carrinho de Compras!
========================================

Selecione uma das seguintes ações:
1. Adicionar item
2. Ver carrinho
3. Remover item
4. Calcular o total
5. Sair
Por favor, insira uma ação: 1
Qual item você gostaria de adicionar? Arroz
Qual é o preço de 'Arroz'? R$ 22.50
O item 'Arroz' foi adicionado ao carrinho.
```

## 📂 Estrutura do Projeto

```
├── carrinho.py       # Código-fonte principal do programa
└── README.md         # Documentação do projeto
```

## 🔧 Possíveis Melhorias Futuras

- [ ] Salvar os dados do carrinho em um arquivo (JSON ou CSV) para persistência
- [ ] Adicionar quantidade de cada item, além do preço unitário
- [ ] Aplicar descontos ou cupons
- [ ] Criar uma interface gráfica (com Tkinter, por exemplo)
- [ ] Escrever testes automatizados com `pytest`

## 🛠️ Tecnologias Utilizadas

- **Python 3**

## 👤 Autor

Desenvolvido por [Seu Nome](https://github.com/seu-usuario) como parte de estudos em lógica de programação e estruturas de dados em Python.

---

⭐️ Se este projeto te ajudou de alguma forma, considere deixar uma estrela no repositório!
