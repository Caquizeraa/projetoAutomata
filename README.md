# Projeto Automata

O projeto consiste em uma API RESTful implementada utilizando FastApi, que é capaz de gerar e manipular Automatos Finitos, Automatos com Pilha e Máquinas de Turing a partir da interação com a biblioteca Automata.

## Configurando ambiente de execução

1. Instale o Graphviz para gerar as imagens.
2. Clone o repositório .
```
git clone https://github.com/Caquizeraa/projetoAutomata.git
```
3. Crie um ambiente virtual.
```
python -m venv venv
cd venv/Scripts/activate
```
4. Com o ambiente virtual ativo, busque o diretório do projeto.
5. Instale as dependências.
```
pip install -r requirements.txt
```
6. Inicie o servidor.
```
uvicorn main:app --reload
```

## Requisições e documentação
As resquisições a API são realizadas em localhost:8000. A documentação foi gerada com Swagger UI, podendo ser acessada a partir de localhost:8000/docs.

## Requisições Teste 
Podem ser executadas no Postman ou Insomnia.

### Criando um automato finito (strings que terminam em número ímpar de 1's)
Tipo de requisição: POST  
Endpoint: localhost:8000/dfa/  
Json:
```
{
  "states": ["q0", "q1", "q2"],
  "input_symbols": ["0", "1"],
  "transitions": {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q0", "1": "q2"},
    "q2": {"0": "q2", "1": "q1"}
  },
  "initial_state": "q0",
  "final_states": ["q1"]
}
```

### Criando um automato com pilha (strings formadas por a's seguidos pelo mesmo número de b's)
Tipo de requisição: POST  
Endpoint: localhost:8000/dpda/  
Json: 
```
{
  "states": ["q0", "q1", "q2", "q3"],
  "input_symbols": ["a", "b"],
  "stack_symbols": ["0", "1"],
  "transitions": {
    "q0": {
      "a": {
        "0": ["q1", ["1", "0"]]
      }
    },
    "q1": {
      "a": {
        "1": ["q1", ["1", "1"]]
      },
      "b": {
        "1": ["q2", ""]
      }
    },
    "q2": {
      "b": {
        "1": ["q2", ""]
      },
      "": {
        "0": ["q3", ["0"]]
      }
    }
  },
  "initial_state": "q0",
  "initial_stack_symbol": "0",
  "final_states": ["q3"],
  "acceptance_mode": "final_state"
}
```

### Criando uma máquina de Turing (strings formadas por 0's seguidos pelo mesmo número de 1's)
Tipo de requisição: POST  
Endpoint: localhost:8000/dtm/  
Json: 
```
{
  "states": ["q0", "q1", "q2", "q3", "q4"],
  "input_symbols": ["0", "1"],
  "tape_symbols": ["0", "1", "x", "y", "."],
  "transitions": {
    "q0": {
      "0": ["q1", "x", "R"],
      "y": ["q3", "y", "R"]
    },
    "q1": {
      "0": ["q1", "0", "R"],
      "1": ["q2", "y", "L"],
      "y": ["q1", "y", "R"]
    },
    "q2": {
      "0": ["q2", "0", "L"],
      "x": ["q0", "x", "R"],
      "y": ["q2", "y", "L"]
    },
    "q3": {
      "y": ["q3", "y", "R"],
      ".": ["q4", ".", "R"]
    }
  },
  "initial_state": "q0",
  "blank_symbol": ".",
  "final_states": ["q4"]
}
```

### Recuperando um automato finito (strings que terminam em número ímpar de 1's)
Tipo de requisição: GET  
Endpoint: localhost:8000/dfa/dfa_1/

### Recuperando um automato com pilha (strings formadas por a's seguidos pelo mesmo número de b's)
Tipo de requisição: GET  
Endpoint: localhost:8000/dpda/dpda_1/

### Recuperando uma máquina de Turing (strings formadas por 0's seguidos pelo mesmo número de 1's)
Tipo de requisição: GET  
Endpoint: localhost:8000/dtm/dtm_1/

### Testando um automato finito para a string passada (strings que terminam em número ímpar de 1's)
Tipo de requisição: POST  
Endpoint: localhost:8000/dfa/dfa_1/accept  
Json:
```
{
  "input_string": "00111"
}
```
### Testando um automato com pilha para a string passada (strings formadas por a's seguidos pelo mesmo número de b's) 
Tipo de requisição: POST  
Endpoint: localhost:8000/dpda/dpda_1/accept  
Json:
```
{
  "input_string": "ab"
}
```

### Testando uma máquina de Turing para a string passada (strings formadas por 0's seguidos pelo mesmo número de 1's)
Tipo de requisição: POST  
Endpoint: localhost:8000/dtm/dtm_1/accept  
Json:
```
{
  "input_string": "000111"
}
```

### Recuperando o diagrama de um automato finito (strings que terminam em número ímpar de 1's)
Tipo de requisição: GET  
Endpoint: localhost:8000/dfa/dfa_1/image
