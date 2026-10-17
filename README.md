# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas.
Projeto desenvolvido no **Bootcamp II** — Fase 2 (Etapa Intermediária).

## Descrição funcional

O TaskTracker oferece um menu contínuo no terminal com as opções:

1. **Cadastrar nova tarefa** — informa título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas** — lista todas as tarefas com seus dados.
3. **Sair da aplicação**

### Regras de negócio

| Campo        | Regra                                                                 |
|--------------|-----------------------------------------------------------------------|
| Título       | Obrigatório. Entradas vazias ou só com espaços são rejeitadas.        |
| Descrição    | Texto livre.                                                          |
| Prioridade   | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`.                 |
| Data limite  | Texto livre (sugestão: DD/MM/AAAA).                                   |
| Status       | Definido automaticamente como `Pendente` no cadastro.                 |

Se não houver tarefas cadastradas, a listagem exibe uma mensagem informando isso.

## Tecnologias utilizadas

- Python 3
- Git e GitHub

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Instalação e execução

Pré-requisito: [Python 3](https://www.python.org/downloads/) instalado.

```bash
git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

## Autor(a)

SEU NOME COMPLETO — Bootcamp II, polo SEU POLO.
