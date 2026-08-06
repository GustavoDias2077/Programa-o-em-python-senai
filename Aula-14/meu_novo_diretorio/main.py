with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Informaçoes")
print("Arquivo 'dados' criado.")

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo lido do arquivo:")
    print(f"-> {conteudo.strip()}")

#2

import os

os.makedirs('meu_novo_diretorio', exist_ok=True)
print("Diretório criado com sucesso!")

#3

#import os

#os.rename('meu_novo_diretorio', 'diretorio_novo1')
#print('Diretorio renomeado')


#4

itens = os.listdir('.')
print("Itens encontrados no diretório:")
for item in itens:
    print(f"- {item}")

#5

import shutil

shutil.copy('main.py', 'meu_novo_diretorio')
print("Arquivo copiado com sucesso!")


#6

import os
import shutil

if os.path.exists('diretorio_novo1') and not os.listdir('diretorio_novo1'):
    os.rmdir('diretorio_novo1')
    print("Diretório vazio removido.")