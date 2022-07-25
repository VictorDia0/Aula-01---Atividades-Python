# Faça um programa que calcule o IMC

print('Vamos calcular se indice de massa corporal')
nome =str(input('Digite seu Nome - '))
peso =float(input('Digite seu peso em Kg - '))
altura =float(input('Digite sua alura em metros - '))

imc = peso / altura**2
 
print("Olá {}, seu IMC é: {:.4f} e você está " .format(nome,imc))
 
if imc < 16:
	print("Magreza grave")
elif imc < 17:
	print("Magreza moderada")
elif imc < 18.5:
	print("Magreza leve")
elif imc < 25:
	print("Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")
