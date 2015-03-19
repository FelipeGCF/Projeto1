#Pedra ganha de tesoura, perde de papel, ganha de lizard e perde de spock.
#Papel perde de tesoura, perde de lizard, ganha de pedra e ganha de spock.
#Tesoura perde de pedra, ganha de papel, ganha de lizard e perde de spock.
#Lizard perde de pedra, perde de tesoura, ganha de papel e ganha de spock.
#Spock ganha de pedra, perde de papel, perde de lizard e ganha de tesoura.
#Obs:Empate não quebra a sequencia de tres vitorias seguidas.
print("Bem vindo ao jogo!!Quem tiver primeiro três vitorias seguidas, vence!!")
computer_score = 0
user_score = 0
turns=0
    
while computer_score<3 and user_score<3:
    import random
    Z=("pedra", "papel", "tesoura", " lizard", " spock")
    y=random.choice(Z)
    x=input("Escolha entre pedra, papel, tesoura, lizard e spock!!")
    print("Usuario ", x)
    print("Computador", y)
    

    if x == "pedra" and y == "papel":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu ")
    if x == "pedra" and y == "tesoura":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "pedra" and y == "lizard":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "pedra" and y == "spock":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce perdeu!!")
    if x == "papel" and y == "tesoura":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu!!")
    if x == "papel" and y == "lizard":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu!!")
    if x == "papel" and y == "spock":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "tesoura" and y == "lizard":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "tesoura" and y == "spock":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu!!")
    if x == "lizard" and y == "spock":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "papel" and y == "pedra":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "tesoura" and y == "pedra":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu!!")
    if x == "lizard" and y == "pedra":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu!!")
    if x == "spock" and y == "pedra":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "tesoura" and y == "papel":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "lizard" and y == "papel":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "spock" and y == "papel":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu!!")
    if x == "lizard" and y == "tesoura":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu !!")
    if x == "spock" and y == "tesoura":
     user_score += 1
     computer_score-=1
     turns+=1
     print("Voce ganhou!!")
    if x == "spock" and y == "lizard":
     user_score -= 1
     computer_score+=1
     turns+=1
     print("Voce perdeu !!")
    if x == "tesoura" and y == "tesoura":
     turns += 1
     print("Voce empatou!!")
    if x == "pedra" and y =="pedra" :
     turns += 1
     print("Voce empatou!!")
    if x == "papel" and y == "papel" :
     turns += 1
     print("Voce empatou!!")
    if x == "lizard" and y =="lizard" :
     turns += 1
     print("Voce empatou!!")
    if x =="spock" and y =="spock" :
     turns += 1
     print("Voce empatou!!")

if computer_score==3:
    print("Mas que pena, voce perdeu o jogo!!Tente novamente")
if user_score == 3:
    print("Parabéns, voce ganhou o jogo!!")
    
