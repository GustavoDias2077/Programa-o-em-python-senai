#1
 
try:
    numero = int((input('Digite um numero inteiro: ')))
    print('Numero digitado:', numero)
except ValueError:
    print('Erro! Voce deve digitar um numero inteiro')    