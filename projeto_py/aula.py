#programa notas
#data=: 2023/09/01 
#autor : iori
#versão : 1.0

#criando variavel
#str - literal - 
#float - numerica - real
linhas_com_zero = [0]*5
A = [ linhas_com_zero ] * 5
A[1][1] = 2
print(linhas_com_zero)
nome = str(input("digite o nome do aluno(a)"))
materia = str(input("digite a materia:"))
nota1 = float(input("digite a nota do 1º bimestre: "))
while ((nota1 < 0 ) or (nota1 > 10)):
    print("nota do 1º bimestre invalida! verifique:")
    nota1 = float(input("digite a nota do 1º bimestre: "))

nota2 = float(input("digite a nota do 2º bimestre: "))
while ((nota2 < 0 ) or (nota2 > 10)):
    print("nota do 2º bimestre invalida! verifique:")
    nota2 = float(input("digite a nota do 2º bimestre: "))

nota3 = float(input("digite a nota do 3º bimestre: "))
while ((nota3 < 0) or (nota3 > 10)):
    print("nota do 3º bimestre invalida! verifique:")
    nota3 = float(input("digite anota do 3º bimestre: "))

nota4 = float(input("digite a  nota do 4º bimestre: "))
while ((nota4 < 0) or (nota4 > 10)):
    print("nota do 4º bimestre invalida! verifique:")
    nota4 = float(input("digite a nota do 4º bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if ((media >10) or (media < 0)):
    print("meida invalida !!! erro critico")
elif (media >= 7):
    print(nome, " ", media, " aprovado")
elif (media >= 4):
    print(nome, " ", media, " recuperação")
else:
    print(nome, " ", media, " reprovado")


