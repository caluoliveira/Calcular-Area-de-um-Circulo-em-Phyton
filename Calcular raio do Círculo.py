#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio=float(input("Informe o RAIO círculo \n")) # 'float' antes do 'input' é a operação de conversão: o que entra em 'string' automaticamente vai para 'float'
area=   3.1415926535898 * (raio * 2)
print("A ÁREA do círculo informado é: \n", "%.2f" % area) #O "%.2f" entre aspas indica quantas casas decimais a variável "area" irá mostrar após a vírgula.