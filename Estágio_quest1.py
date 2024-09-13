print("1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.\n")


def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
    
def pertence_fibonacci(num):
    i = 0
    while True:
        fib = fibonacci(i)
        if fib == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        elif fib > num:
            return f"O número {num} não pertence à sequência de Fibonacci."
        i += 1
    
numero = int(input("Insira um número: "))

print (pertence_fibonacci(numero))
