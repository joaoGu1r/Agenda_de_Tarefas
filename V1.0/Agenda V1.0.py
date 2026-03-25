# --- FUNÇÕES ---

def agendar_tarefas():
    print("#" * 20)
    # Pegamos os dados e limpamos espaços extras com .strip()
    acao = input("Tarefa: ").strip().title()
    data = input("Data (DD/MM): ").strip()
    hora = input("Hora (00:00): ").strip()
    print("#" * 20)

    # Criamos o dicionário que representa uma tarefa
    tarefa = {"tarefa": acao, "data": data, "hora": hora}
    
    # Adicionamos à lista global 'agenda'
    agenda.append(tarefa)
    print(f"Sucesso: '{acao}' adicionada à memória!")

def visualiza_agendar_tarefas(lista_agenda):
    if len(lista_agenda) == 0:
        print("\n--- A agenda está vazia na memória! ---")
    else:
        print("\n=== SUAS TAREFAS ===")
        for i, item in enumerate(lista_agenda, 1):
            # i+1 no enumerate para o usuário ver índices começando em 1
            print(f"ID: {i:02d} | Tarefa: {item['tarefa']}")
            print(f"      Data: {item['data']} | Hora: {item['hora']}")
            print("-" * 20)

def remover_tarefa_agenda(lista_agenda):
    if len(lista_agenda) == 0:
        print("Nada para remover, a lista está vazia.")
        return

    visualiza_agendar_tarefas(lista_agenda)
    
    indice = int(input("\nInforme o ID da tarefa para REMOVER --> ")) - 1
    
    # Validação de segurança para o índice
    if 0 <= indice < len(lista_agenda):
        # Removemos o dicionário da lista
        removida = lista_agenda.pop(indice)
        print(f"A tarefa '{removida['tarefa']}' foi apagada com sucesso!")
    else:
        print("Erro: Esse ID não existe na lista.")

def editar_agenda(lista_agenda):
    if len(lista_agenda) == 0:
        print("Não há tarefas para editar.")
        return

    visualiza_agendar_tarefas(lista_agenda)
    
    indice = int(input("\nInforme o ID da tarefa para EDITAR --> ")) - 1

    if 0 <= indice < len(lista_agenda):
        print("\n--- Insira os novos dados para esta tarefa ---")
        # Atualizamos as chaves do dicionário diretamente no índice da lista
        lista_agenda[indice]['tarefa'] = input("Novo nome da Tarefa: ").strip().title()
        lista_agenda[indice]['data'] = input("Nova Data (DD/MM): ").strip()
        lista_agenda[indice]['hora'] = input("Nova Hora (00:00): ").strip()
        
        print("Tarefa atualizada com sucesso!")
    else:
        print("Erro: ID inválido.")

# --- MENU PRINCIPAL ---

# A nossa lista global que guardará os dicionários
agenda = []

while True:
    print("\nMENU DE GERENCIAMENTO")
    opcao = input("""
    1. Adicionar tarefa
    2. Visualizar tarefas
    3. Remover tarefa
    4. Editar tarefa
    5. Sair
    --> Escolha uma opção: """)

    if opcao == "1":
        agendar_tarefas()

    elif opcao == "2":
        visualiza_agendar_tarefas(agenda)

    elif opcao == "3":
        remover_tarefa_agenda(agenda)

    elif opcao == "4":
        editar_agenda(agenda)

    elif opcao == "5":
        print("Finalizando programa... Os dados da memória serão perdidos.")
        break

    else:
        print("Opção inválida, tente novamente!")