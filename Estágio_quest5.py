print("""5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?\n""")

resposta = """Resposta = Na primeira ida:

- Ligo o interruptor  1 por 5 minutos e o desligo, ligo oo interruptor 2 e na mesma hora vou até uma das 3 salas
- Se a lampada estiver acessa, pertence ao interruptor 2, se estiver desligada e quente pertence ao interruptor 1, se estiver desligada e fria pertence ao interruptor 3.

Na segunda ida:
- Sabendo já a qual pertence um interruptor, apenas deixo um ligado e outro desligado entre o restantes
- Vou até outra sala e descubro os outros dois."""

print(resposta)