print("Hotel trivago")

cliente1 = input("Digite seu Nome:")
idade1 = int(input("Digite sua idade: "))
quarto1 = input("Quarto (simples, duplo ou luxo): ")
dias1 = int(input("Quantos dias ficará? "))

if quarto1 == "simples":
    valor1 = dias1 * 100
elif quarto1 == "duplo":
    valor1 = dias1 * 150
elif quarto1 == "luxo":
    valor1 = dias1 * 250
else:
    valor1 = 0

#cliente 2

cliente2 = input("Digite seu Nome:")
idade2 = int(input("Digite sua idade: "))
quarto2 = input("Quarto (simples, duplo ou luxo): ")
dias2 = int(input("Quantos dias ficará? "))

if quarto2 == "simples":
    valor2 = dias2 * 100
elif quarto2 == "duplo":
    valor2 = dias2 * 150
elif quarto2 == "luxo":
    valor2 = dias2 * 250
else:
    valor2 = 0

#Listas de clientes

listas_clientes = [cliente1, cliente2]

print("--Reservas--")
print(cliente1, 'idade', idade1)
print("Quarto", quarto1)
print('Valor a pagar: R$', valor1)
print()

print(cliente2, 'idade', idade2)
print("Quarto", quarto2)
print('Valor a pagar: R$', valor2)
print()

print('Clientes cadastrados', listas_clientes)