def loteria():
  print('     **** LOTERIA ****')
  print()
  num1 = input('Digite um número de 4 dígitos: ')
  if num1 .isnumeric():
    num1 = int(num1) #checar se o número é válido.
    print('Ok!')
  else:
    while not num1 .isnumeric(): #loop para digitar o número válido
      num1 = input('Digite um número válido: ')
      if num1 .isnumeric():
        num1 = int(num1)
        print('Ok!')
        break
      else:
        print('Número inválido.')
  print()
  import time #tempo de impressão na tela
  time.sleep(0.5)
  print('Agora vamos ver qual o número a máquina escolheu.')
  
  time.sleep(1)
  import random #gerar o numero aleatório método random
  s = '0123456789'
  passwordlen = 4
  password = "".join(random.sample(s,passwordlen))
  print(password)

  print() #calcular a diferença entre o input e o random
  result = num1 - int(password)
  time.sleep(1)
  print('Diferença de', result)

  time.sleep(0.5)
  if result == 0:
    print()
    print('Seu número foi',num1,'e a máquina colocou',password)
    print('*** BINGO! *** Você é o Mestre.')

  elif result > 0 and result <= 10:
    print()
    print('Noossa, você chegou muito perto.')

  elif result >10 and result <= 50:
    print()
    print('Você chegou perto!')

  elif result > -50 and result < -10:
    print()
    print('Você chegou perto!')
  
  elif result > -10 and result < 0:
    print()
    print('Noossa, você chegou muito perto.')   
  
  else:
    print()
    print('Diferença muito grande. Tente novamente!')
  print()
  print('Developed by @JorgeJah. ©')
  
  import datetime #gerar a data atual
  today = datetime.date.today()
  print(today)  
  print()

loteria()

import time
time.sleep(1)
novojogo = input('Aperte qualquer tecla para jogar novamente ou digite "sair" para finalizar. ')
print('\x1b[2J')
print()
if novojogo == 'sair':
  print('Ok. Jogo Encerrado. Até mais!')
  print('Developed by @JorgeJah. ©')
  import datetime #gerar a data atual
  today = datetime.date.today()
  print(today)
else:
  while novojogo != 'sair':
    loteria()
    novojogo = input('Aperte qualquer tecla para jogar novamente ou digite "sair" para finalizar. ')
    print('\x1b[2J')
  print('Ok. Jogo Encerrado. Até mais!')
  print('Developed by @JorgeJah. ©')
  import datetime #gerar a data atual
  today = datetime.date.today()
  print(today)
