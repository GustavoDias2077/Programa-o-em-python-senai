#1
numero = int(input("Digite um numero: "))

if numero > 0 :
    print('E positivo')
elif numero < 0 :
    print('E negativo')
else:
    print('E zero')  

#2

idade = int(input('Digite sua idade: '))  

if idade >= 18:
    print('Pode votar')
else:
    print('Não pode votar')    

#3

numero1 = 10

if numero1 % 2 == 0:
    print('numero e par')
elif numero1 % 2 != 0:
    print('numero e impar')
else:
    print("numero invalido")


#4

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 == lado2 == lado3:
    print("E um triangulo equilatero")
elif lado1 == lado2 != lado3:
    print('E um triangulo isosceles')
else:
    print('E um triangulo escaleno') 

#5       

n1 = int(input('Escolha um numero: '))

if n1 % 5 == 0 and n1 % 7 == 0:
    print("E multiplo de 5 e 7")
else:
    print("Não e multiplo de 5 e 7")    

#6

n2 = int(input('Digite um numero: '))
if n2 >= 1:
    print("e positivo e menor que 10")
elif n2 > 10:
    print("e positivo e maior que 10") 
else:
    print("nao e positivo e nem maior que 10")   

#7

n3 = int(input('Digite um numero: '))

if n3 % 3 == 0 and n3 % 5 == 0:
    print('E divisivel por 3 e 5')
else:
    print('Nao e divisivel')

    

