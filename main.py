import random
pontosSeus= 0
pontosDeles= 0
while True:
  numero_atual = random.randint(1,100)
  print(f"o numero atual é{numero_atual}.")
  proximo_numero = random.randint(1,100)
  escolha =  input("o próximo número sera maior ou menor?")
  if escolha == "maior" and proximo_numero > numero_atual:
    print('você acertou!')
  elif escolha == "menor" and proximo_numero > numero_atual:
    print('você acertou!')
    pontos_seus = pontosSeus +1
  else:
    print('você errou!')
    pontos_deles = pontosDeles +1
    print('o numero era', numero_atual)
    print(f"VOCÊ{pontos_seus}x PC{pontos_deles},")
