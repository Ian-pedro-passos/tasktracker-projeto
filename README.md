# TaskTracker

Aplicação de linha de comando (CLI) em Python para gerenciar tarefas: cadastrar, visualizar,
concluir, remover e acompanhar um resumo geral.
Projeto desenvolvido no **Bootcamp II** — Fase 2 (Etapa Intermediária), implementando o
planejamento lógico da Fase 1 ([docs/planejamento_logico.pdf](docs/planejamento_logico.pdf)).

## Descrição funcional

O TaskTracker oferece um menu contínuo no terminal, que só encerra quando o usuário escolhe Sair:

1. **Cadastrar tarefa** — título, descrição (opcional), prioridade, data limite e categoria.
   O sistema gera um ID único e grava a tarefa com status `Pendente`.
2. **Visualizar tarefas** — tabela ordenada por prioridade (Alta → Média → Baixa) e, em caso de
   empate, pela data limite mais próxima, com os totais ao final.
3. **Concluir tarefa** — muda o status de `Pendente` para `Concluída` pelo ID.
4. **Remover tarefa** — exclui uma tarefa pelo ID, após confirmação (S/N).
5. **Resumo** — total de tarefas, pendentes, concluídas e pendentes de prioridade Alta.
6. **Sair**

### Regras de negócio

| Regra | Descrição |
|-------|-----------|
| RN01 | Título obrigatório (não aceita vazio nem só espaços), com até 60 caracteres. |
| RN02 | Prioridade aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`. |
| RN03 | Data limite no formato DD/MM/AAAA, existente no calendário e não anterior a hoje. |
| RN04 | ID único e sequencial, nunca reaproveitado, mesmo após remoção. |
| RN05 | Toda tarefa nova nasce com status `Pendente`. |
| RN06 | Uma tarefa já concluída não pode ser concluída de novo. |
| RN07 | ID inexistente gera mensagem de erro e volta ao menu. |
| RN08 | Listagem ordenada por prioridade e depois por data limite. |
| RN09 | Lista vazia gera aviso em vez de tabela vazia. |
| RN10 | Remoção só acontece após confirmação S/N. |
| RN11 | Opção de menu inválida gera aviso e o menu é exibido novamente. |
| RN12 | O sistema só encerra na opção Sair. |

Categoria é opcional; se ficar em branco, assume `Geral`. Nesta fase as tarefas ficam em memória
enquanto o programa está aberto (a gravação em arquivo está prevista para a Fase 3).

## Vídeo de apresentação

Demonstração do repositório e da aplicação em execução: https://youtu.be/IDK_kGNmDz0

## Tecnologias utilizadas

- Python 3 (somente biblioteca padrão)
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
git clone https://github.com/Ian-pedro-passos/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

## Autor

Ian Pedro Passos de Santana — Análise e Desenvolvimento de Sistemas (CEUB),
Bootcamp II, polo Asa Norte, Turma A.
