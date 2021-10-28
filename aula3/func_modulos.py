import sys
from random import randint

print(randint(0, 9))
print(randint(0, 9))
print(randint(0, 9))
print(randint(0, 9))
print(randint(0, 9))
print(randint(b=9, a=0))

print('---- LISTAR MODULOS IMPORTADOS ----')
print(sys.modules.get('random'))

#Modules é um dicionario, podemos fazer ações de dicionario
print(sys.modules['random'])