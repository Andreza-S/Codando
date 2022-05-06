"""Descrição
Há muitas notícias falsas circulando na internet. Há também muitos sites que se dedicam a investigar as famigeradas fake news e revelar a "verdade". A saber:

www.e-farsas.com
boatos.org
acrediteounao.com
naoacredite.com
Faça um programa para julgar notícias falsas. Cada notícia será julgada pelo seguinte critério:
Se a notícia for marcada como falsa nos 4 sites ela deve ser dada como "certamente falsa"
Se a notícia for marcada como falsa em 3 dos 4 sites ela deve ser dada como "provavelmente falsa"
Se a notícia for marcada como falsa em 2 dos 4 sites ela deve ser dada como "pode ser falsa"
Se a notícia for marcada como falsa em 1 dos 4 sites ela deve ser dada como "indeterminado"
Se a notícia não for marcada como falsa em nenhum dos sites ela deve ser dada como "verdadeira"
Receba uma quantidade de notícias informado pelo usuário. No final, informe o percentual de notícias falsas apresentadas.

Formato de entrada

Primeiro, o programa deve receber a quantidade de notícias que serão analisadas.

Para cada notícia, deve ser recebido a URL da notícia original.

Em seguida, o programa deve receber 4 vereditos que determinam em ordem, quais sites analisam a notícia como falsa. Por exemplo:

f

v

v

f

Dessa forma, a notícia tem 2 votos como falsa e 2 votos como verdadeira, sendo marcada como "pode ser falsa".



Formato de saída

Se a notícia for marcada como falsa nos 4 sites ela deve ser dada como "certamente falsa"
Se a notícia for marcada como falsa em 3 dos 4 sites ela deve ser dada como "provavelmente falsa"
Se a notícia for marcada como falsa em 2 dos 4 sites ela deve ser dada como "pode ser falsa"
Se a notícia for marcada como falsa em 1 dos 4 sites ela deve ser dada como "indeterminado"
Se a notícia não for marcada como falsa em nenhum dos sites ela deve ser dada como "verdadeira"

Além disso, imprima o percentual de notícias falsas apresentadas (as que foram marcadas como certamente falsa ou provavelmente falsa) com uma casa decimal de aproximação."""



n_noticias = int (input())

n_falsas = 0


for i in range (n_noticias):
    url = input()
    ver1 = input()
    ver2 = input()
    ver3 = input()
    ver4 = input()

    sites_falsas = 0

    if (ver1 == "f"):
        sites_falsas += 1
    if (ver2 == "f"):
        sites_falsas += 1
    if (ver3 == "f"):
        sites_falsas += 1
    if (ver4 == "f"):
        sites_falsas += 1
    
    if (sites_falsas == 4):
        n_falsas += 1
        print ( url + " - certamente falsa")
    if (sites_falsas == 3):
        n_falsas += 1
        print ( url + " - provavelmente falsa")
    if (sites_falsas == 2):
        print ( url + " - pode ser falsa")
    if (sites_falsas == 1):
        print ( url + " - indeterminado")
    if (sites_falsas == 0):
        print ( url + " - verdadeira")

    percentual = ((n_falsas/n_noticias) * 100)

print ("percentual de not�cias falsas {:.1f}".format (percentual))