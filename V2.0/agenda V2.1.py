# --- FUNÇÕES DO SISTEMA ---

def agendar_tarefas():
    print("#"*20)
    acao = input("Tarefa: ").strip().title()
    # Validação da Data
    data = validar_data()
    # Validação da Hora
    hora_input = validar_hora()

    print("#"*20)
    
    tarefa = {"tarefa": acao, "data": data, "hora": hora_input}
    
    # Gravando apenas a nova tarefa para evitar duplicados
    with open('agenda.txt', 'a') as arquivo:
        linha = f"{tarefa['tarefa']};{tarefa['data']};{tarefa['hora']}\n"
        arquivo.write(linha)

def validar_data():

    while True:
        data = input("data(DD/MM): ").strip()
        if "/" in data:
            partes = data.split("/")
            if len(partes) == 2:
                dia = partes[0]
                mes = partes[1]
                if dia.isdigit() and mes.isdigit():
                    dia_int = int(dia)
                    mes_int = int(mes)
                    if 1 <= dia_int <= 31 and 1 <= mes_int <= 12:
                        return data
        print("Formatação incorreta tente novamente (Ex: 15/03)")

def validar_hora():
    while True:
        hora_input = input("hora(00:00): ").strip()
        if ":" in hora_input:
            partes = hora_input.split(":")
            if len(partes) == 2:
                h = partes[0]
                m = partes[1]
                if h.isdigit() and m.isdigit():
                    hora_int = int(h)
                    minuto_int = int(m)
                    if 0 <= hora_int <= 23 and 0 <= minuto_int <= 59:
                        return hora_input
        print("Formatação incorreta tente novamente (Ex: 14:30)")
    
def visualiza_agendar_tarefas():
    try:
        with open('agenda.txt', 'r') as arquivo:
            atividades = arquivo.readlines()
    except FileNotFoundError:
        print("Agenda Vazia!(agenda ainda não existe)")
        return
    
    if not atividades:
        print("Agenda Vazia!")
        
    else:
        print("-" * 40)
        print(f"{'ID':<3} | {'TAREFA':<15} | {'DATA':<6} | {'HORA'}")
        print("-" * 40)
        
        for indice, tarefa in enumerate(atividades, 1):
            partes = tarefa.strip().split(";")
            if len(partes) == 3:
                nome, data, hora = partes
                print(f"{indice:02d} | {nome:<15} | {data} | {hora}")

def remover_tarefa_agenda():
    try:
        with open('agenda.txt', 'r') as arquivo:
            atividades = arquivo.readlines()
    except FileNotFoundError:
        print("Erro:agenda ainda não existe")

    if len(atividades) == 0:  
        print("Lista vazia!")
        return # Adicionado para não pedir índice se estiver vazia
    try:
        indice = int(input("informe o indice da tarefa --> ")) - 1
        
        if 0 <= indice < len(atividades):
            tarefa_removida = atividades.pop(indice).strip()
            
            with open('agenda.txt', 'w') as arquivo:
                arquivo.writelines(atividades)
            
            print(f"A tarefa {tarefa_removida} foi removida com sucesso!")
        else:
            print("Erro: Índice inválido!") 
    except ValueError:
        print("Entrada Invalida! Digite apenas numeros inteiros!")
        
def editar_agenda():
    try:
        with open('agenda.txt', 'r') as arquivo:
            atividades = arquivo.readlines()
    except FileNotFoundError:
        print("Erro:agenda ainda não existe")

    if not atividades:
        print("Não há tarefas para editar.")
        return
    
    visualiza_agendar_tarefas()

    try:
        indice = int(input("informe o indice da tarefa --> ")) - 1
    
        if 0 <= indice < len(atividades):
            print("--- Insira os novos dados ---")
            nova_acao = input("Nova Tarefa: ").strip().title()
            nova_data  = validar_data()
            nova_hora = validar_hora()

            

            # FINALIZANDO A EDIÇÃO: Substitui na lista e grava no arquivo
            atividades[indice] = f"{nova_acao};{nova_data};{nova_hora}\n"
            
            with open('agenda.txt', 'w') as arquivo:
                arquivo.writelines(atividades)
            
            print("Tarefa editada com sucesso!")
        else:
            print("Índice inválido!")
    except ValueError:
        print("ERRO: Valor inserido não é valido!")
        
# --- MENU ---

while True:
    opcao = input("""
Escolha uma opção:
1. adicionar tarefa
2. visualizar tarefas
3. remover tarefa 
4. editar tarefa
5. Sair
--> """)

    if opcao == "1":
        agendar_tarefas()
    elif opcao == "2":
        visualiza_agendar_tarefas()
    elif opcao == "3":
        remover_tarefa_agenda()
    elif opcao == "4":
        editar_agenda()
    elif opcao == "5":
        print("Finalizando Agenda de tarefas")
        break
    else:
        print("Opção inválida!")