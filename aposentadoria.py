nome = str(input("Qual é o seu nome? \n"))
pessoaIdade = int(input("Qual a sua idade? \n"))
pessoaSexo = str(input("Qual é o seu sexo? \n"))
pessoaRenda = float(input("Qual a sua renda atual? \n"))


if (pessoaIdade >= 60 and pessoaSexo == "Feminino" or pessoaIdade >= 65 and pessoaSexo == "Masculino"):
	print(f"Obrigado, {nome}! Sua aposentadoria foi liberada no valor de R${pessoaRenda*0.7}")
if (pessoaIdade < 60 and pessoaSexo == "Feminino"):
	print(f"Você ainda não pode se aposentar, faltam {(60)-pessoaIdade} anos.") 
if (pessoaIdade < 65 and pessoaSexo == "Masculino"):
	print(f"Você ainda não pode se aposentar, faltam {(65)-pessoaIdade} anos.") 
if (pessoaRenda <= 0):
	print("Erro: É necessário informar o valor da sua renda")
	
	

	
	