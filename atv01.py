# Atividade 01

nomealuno =str(input('Digite o nome do aluno desejado -'))
prova01 =float(input('Prova 01 -'))
prova02 =float(input('Prova 02 -'))
prova03 =float(input('Prova 03 -'))
media =(prova01 + prova02 + prova03) / 3

print('Olá {}, sua nota nas provas 01,02 e 03 foi de {:.2f}, {:.2f}, {:.2f}, logo sua media foi de {:.2f}' .format(nomealuno,prova01,prova02,prova03,media))