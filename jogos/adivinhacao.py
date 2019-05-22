print("*******************")
print("Jogo de adivihnação")
print("*******************")

numero_secreto=15

chute=input("Qual o seu chute?")
chute_inteiro = int(chute)

if(chute_inteiro==numero_secreto):
	print("Parabéns, você acertou o número secreto")
elif(chute_inteiro<numero_secreto):
	print("Não foi dessa vez. Seu chute foi abaixo do numero secreto")
elif(chute_inteiro>numero_secreto):
	print("Não foi dessa vez. Seu número está acima do número secreto")
else:
	print("Não foi dessa vez")

