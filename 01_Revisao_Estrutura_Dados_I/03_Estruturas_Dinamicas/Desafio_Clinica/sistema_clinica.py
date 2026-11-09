
# Desafio da Aula 03 - Sistema de Atendimento de uma Clínica

fila_pacientes = []


def adicionar_paciente():
    nome = input("Nome do paciente: ").strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return

    try:
        idade = int(input("Idade: "))
        if idade < 0:
            print("A idade não pode ser negativa.")
            return
    except ValueError:
        print("Digite uma idade válida.")
        return

    prioridade = input("Prioridade (Normal/Prioridade): ").strip().lower()

    if prioridade not in ("normal", "prioridade"):
        print("Prioridade inválida.")
        return

    paciente = {
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade.capitalize()
    }

    fila_pacientes.append(paciente)
    print(f"\nPaciente {nome} adicionado à fila!")


def listar_pacientes():
    if not fila_pacientes:
        print("\nNão há pacientes aguardando.")
        return

    print("\n--- PACIENTES AGUARDANDO ---")
    for posicao, paciente in enumerate(fila_pacientes, start=1):
        print(
            f"{posicao}. {paciente['nome']} | "
            f"{paciente['idade']} anos | "
            f"{paciente['prioridade']}"
        )


def atender_paciente():
    if not fila_pacientes:
        print("\nNão há pacientes para atender.")
        return

    paciente = fila_pacientes.pop(0)
    print(f"\nPaciente atendido: {paciente['nome']}")


def verificar_fila():
    if not fila_pacientes:
        print("\nA fila está vazia.")
    else:
        print("\nAinda existem pacientes aguardando.")


def quantidade_pacientes():
    print(f"\nPacientes aguardando: {len(fila_pacientes)}")


def menu():
    while True:
        print("\n===== SISTEMA DA CLÍNICA =====")
        print("1 - Adicionar paciente")
        print("2 - Listar pacientes")
        print("3 - Atender paciente")
        print("4 - Verificar se a fila está vazia")
        print("5 - Quantidade de pacientes")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            atender_paciente()
        elif opcao == "4":
            verificar_fila()
        elif opcao == "5":
            quantidade_pacientes()
        elif opcao == "0":
            print("\nEncerrando sistema...")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    menu()
