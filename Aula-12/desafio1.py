import statistics

def media(notas):
    return statistics.mean(notas)

def moda(notas):
    return statistics.mode(notas)

def desvio(notas):
    return statistics.stdev(notas)

def menor(notas):
    return min(notas)

def maior(notas):
    return max(notas)

notas = [6, 7, 8, 4, 3, 2, 8, 6]

print('Media', media(notas))
print('moda', moda(notas))
print('desvio padrao', desvio(notas))
print('Menor nota', menor(notas))
print('Maior nota', maior(notas))