# Projeto de cadastro e notas de alunos
# João Vitor Wolff Morfim
# 24/03/2026

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

# funções da classe
    def adc_nota(self):
        try:
            nota = float(input("Nota do aluno: "))
            self.notas.append(nota)
        except ValueError:
            print("Nota inválida!")

    def ver_media(self):
        if len(self.notas) == 0:
            print("O aluno não possui notas!")
            return
        
        media = sum(self.notas) / len(self.notas)
        print(f"Média: {media:.2f}")
        if media >= 7:
            print("O aluno passou!")
        else:
            print("O aluno está de recuperação!")


alunos = []

# menu básico de interação com o usuário
while True:
    print("-----MENU-----")
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota")
    print("3 - Conferir média do aluno")
    print("4 - Ver a lista de alunos")
    print("5 - Sair do sistema")
    print("--------------")

    try:
        escolha = int(input("Digite o que você quer fazer: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if escolha == 1:
        nome = input("Nome do aluno: ")
        aluno = Aluno(nome)
        alunos.append(aluno)


    elif escolha == 2:
        nome = input("Nome do aluno: ")
        for aluno in alunos:
            if aluno.nome == nome:
                aluno.adc_nota()
                break
        if not alunos:
            print("Nenhum aluno cadastrado!")

    elif escolha == 3:
        nome = input("Nome do aluno: ")
        for aluno in alunos:
            if aluno.nome == nome:
                aluno.ver_media()
                break
        if not alunos:
            print("Nenhum aluno cadastrado!")

    elif escolha == 4:
        if not alunos:
            print("Nenhum aluno cadastrado!")
        for aluno in alunos:
            print(f"Aluno: {aluno.nome}")

    elif escolha == 5:
        print("Encerrando sistema...")
        break

    else:
        print('Opção inválida!')