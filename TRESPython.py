#3- Elabore um programa de computador que realize o cálculo de notas. Este programa deverá solicitar o nome do aluno e quatro notas, todo este conjunto deverá estar contido em um laço que confirme se deseja encerrar o programa ou continuar solicitando outros nomes e notas.
#Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno e a sua média, se a nota for  menor que 6 imprimir Reprovado, senão, se a nota for igual ou maior que 6, imprimir Aprovado.

while True:
    nome = input("Insira o nome do aluno (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break 

    notas = []
    for i in range(4):
        nota = float(input("Insira a nota {}: ".format(i+1)))
        notas.append(nota)

    media = sum(notas) / len(notas)
    status = 'Aprovado' if media >= 6 else 'Reprovado'

    print("Aluno: {}".format(nome))
    print("Média: {:.1f}".format(media))
    print("Situação: {}".format(status))
