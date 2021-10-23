
#Testando e conhecendo Python

linguagem = 'Python'
texto = 'Olá meu nome é Fernando'
curso = '    Python    Fundamentals    '
print('_______________1________________________')
print(linguagem.upper())
print(linguagem.lower())
print('_______________2________________________')
print(texto.split())
print(texto.split('é'))
print('_______________3_______________________')
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
print(curso.lstrip().rstrip() == curso.strip())
print(curso.replace(' ','_'))
print(curso.replace(' ', '_').strip('_'))