print ("2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.\n")


def verificar_str(x):
   count = x.lower().count("a")
   
   if count > 0:
      return f"A letra 'a' aparece {count} vezes na string."
   
   else:
      return "Não existe a letra 'a' na string"
   
texto = "hoje eu fui na padaria e comprei um café"

print(verificar_str(texto))
