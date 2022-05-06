"""Descrição
Faça um programa que leia um caractere da entrada padrão e verifique se ele é uma vogal.

Se o usuário digitar mais ou menos de 1 caractere, exiba uma mensagem de erro.

Em Python 3, você pode verificar quantos caracteres tem um string com a função len(). Procure como fazer!

Formato de entrada

Um caractere da entrada padrão. O caractere pode ser maiúsculo ou minúsculo.



Formato de saída

"Eh vogal", se a entrada tiver apenas 1 caractere e for vogal
"Nao eh vogal", se a entrada tiver apenas 1 caractere e não for vogal
"1 caractere, por favor!", se a entrada tiver mais de 1 caractere"""


Car = input ()
if (len (Car) > 1):
    print ("1 caractere, por favor!")
elif (Car == "a" or Car == "A" or 
Car == "e" or Car == "E" or 
Car == "i"  or Car == "I" or 
Car == "o" or Car == "O" or 
Car == "u"  or Car =="U"):
    print ("Eh vogal")
else:
    print ("Nao eh vogal")