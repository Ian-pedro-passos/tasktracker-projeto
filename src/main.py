"""TaskTracker - Gerenciador de tarefas via linha de comando (CLI).

Bootcamp II - Fase 2 (Etapa Intermediária).
Implementação do algoritmo planejado na Fase 1 (docs/planejamento_logico.pdf).
"""

from datetime import date, datetime

TAMANHO_MAXIMO_TITULO = 60

# Aceita "Média" ou "Media", em qualquer combinação de maiúsculas/minúsculas.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

# Ordem usada na listagem (RN08): Alta, depois Média, depois Baixa.
ORDEM_PRIORIDADE = {"Alta": 1, "Média": 2, "Baixa": 3}


# ---------------------------------------------------------------------------
# Leitura e validação das entradas
# ---------------------------------------------------------------------------

def ler_titulo():
    """RN01: o título é obrigatório e tem no máximo 60 caracteres."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if not titulo:
            print("[ERRO] O título não pode ficar vazio.")
        elif len(titulo) > TAMANHO_MAXIMO_TITULO:
            print(f"[ERRO] O título deve ter no máximo {TAMANHO_MAXIMO_TITULO} caracteres.")
        else:
            return titulo


def ler_prioridade():
    """RN02: a prioridade aceita apenas Alta, Média ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida: digite Alta, Média ou Baixa.")


def ler_data_limite():
    """RN03: data no formato DD/MM/AAAA, existente no calendário e não anterior a hoje."""
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data_limite = datetime.strptime(entrada, "%d/%m/%Y").date()
        except ValueError:
            print("[ERRO] Data inválida. Use o formato DD/MM/AAAA.")
            continue
        if data_limite < date.today():
            print("[ERRO] A data limite não pode ser anterior a hoje.")
            continue
        return data_limite


def ler_id(mensagem):
    """Lê um número inteiro de ID; devolve None se não for um número."""
    entrada = input(mensagem).strip()
    if not entrada.isdigit():
        return None
    return int(entrada)


def ler_confirmacao(mensagem):
    """Aceita apenas S ou N, em maiúscula ou minúscula."""
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ("S", "N"):
            return resposta
        print("[ERRO] Responda apenas S (sim) ou N (não).")


def buscar_tarefa(tarefas, id_tarefa):
    """Procura na lista a tarefa com o ID informado."""
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None


# ---------------------------------------------------------------------------
# Receitas do sistema (seções 3.2 a 3.6 do planejamento)
# ---------------------------------------------------------------------------

def cadastrar_tarefa(tarefas, proximo_id):
    """3.2 Cadastro de tarefa. Devolve o próximo ID disponível."""
    print("\n--- CADASTRAR TAREFA ---")
    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()
    categoria = input("Categoria (em branco = Geral): ").strip() or "Geral"

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "categoria": categoria,
        "status": "Pendente",  # RN05
        "data_conclusao": None,
    }
    tarefas.append(tarefa)
    print(f"\nTarefa cadastrada com sucesso! (ID: {proximo_id})")
    # RN04: o contador só aumenta, então um ID nunca é reaproveitado.
    return proximo_id + 1


def exibir_tabela(tarefas):
    """Mostra as tarefas ordenadas por prioridade e data limite (RN08)."""
    ordenadas = sorted(
        tarefas,
        key=lambda t: (ORDEM_PRIORIDADE[t["prioridade"]], t["data_limite"]),
    )
    print(f"\n{'ID':<4} | {'Título':<30} | {'Prioridade':<10} | {'Data limite':<11} | Status")
    print("-" * 78)
    for t in ordenadas:
        print(
            f"{t['id']:<4} | {t['titulo'][:30]:<30} | {t['prioridade']:<10} | "
            f"{t['data_limite'].strftime('%d/%m/%Y'):<11} | {t['status']}"
        )


def contar_status(tarefas):
    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")
    return pendentes, concluidas


def visualizar_tarefas(tarefas):
    """3.3 Visualização das tarefas."""
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:  # RN09
        print("Nenhuma tarefa cadastrada até o momento.")
        return
    exibir_tabela(tarefas)
    pendentes, concluidas = contar_status(tarefas)
    print(f"\nTotal: {len(tarefas)} tarefas | Pendentes: {pendentes} | Concluídas: {concluidas}")


def concluir_tarefa(tarefas):
    """3.4 Conclusão de uma tarefa."""
    print("\n--- CONCLUIR TAREFA ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada até o momento.")
        return
    exibir_tabela(tarefas)

    pendentes, _ = contar_status(tarefas)
    if pendentes == 0:
        print("\nNão há tarefas pendentes para concluir.")
        return

    id_tarefa = ler_id("\nID da tarefa a concluir: ")
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa is None:  # RN07
        print("[ERRO] Não existe tarefa com o ID informado.")
        return
    if tarefa["status"] == "Concluída":  # RN06
        print("Esta tarefa já foi concluída.")
        return

    tarefa["status"] = "Concluída"
    tarefa["data_conclusao"] = date.today()
    print(f"Tarefa {tarefa['id']} ({tarefa['titulo']}) concluída com sucesso!")


def remover_tarefa(tarefas):
    """3.5 Remoção de uma tarefa, sempre com confirmação (RN10)."""
    print("\n--- REMOVER TAREFA ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada até o momento.")
        return
    exibir_tabela(tarefas)

    id_tarefa = ler_id("\nID da tarefa a remover: ")
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa is None:  # RN07
        print("[ERRO] Não existe tarefa com o ID informado.")
        return

    resposta = ler_confirmacao(f"Confirma a remoção de '{tarefa['titulo']}'? (S/N): ")
    if resposta == "N":
        print("Operação cancelada. Nenhuma tarefa foi removida.")
        return

    tarefas.remove(tarefa)
    print(f"Tarefa {tarefa['id']} removida do sistema.")


def exibir_resumo(tarefas):
    """3.6 Resumo geral."""
    print("\n--- RESUMO GERAL ---")
    pendentes, concluidas = contar_status(tarefas)
    pendentes_alta = sum(
        1 for t in tarefas if t["status"] == "Pendente" and t["prioridade"] == "Alta"
    )
    print(f"Total de tarefas             : {len(tarefas)}")
    print(f"Pendentes                    : {pendentes}")
    print(f"Concluídas                   : {concluidas}")
    print(f"Pendentes de prioridade Alta : {pendentes_alta}")


# ---------------------------------------------------------------------------
# Fluxo principal (seção 3.1)
# ---------------------------------------------------------------------------

def exibir_menu():
    print("\n========== TASKTRACKER ==========")
    print("1 - Cadastrar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Resumo")
    print("6 - Sair")
    print("=================================")


def main():
    tarefas = []
    proximo_id = 1
    print("Bem-vindo ao TaskTracker!")

    while True:  # RN12: só encerra na opção 6
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(tarefas, proximo_id)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            exibir_resumo(tarefas)
        elif opcao == "6":
            print("Obrigado por usar o TaskTracker. Até logo!")
            break
        else:  # RN11
            print("[ERRO] Opção inválida. Escolha um número de 1 a 6.")


if __name__ == "__main__":
    main()
