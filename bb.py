import time

def jogo_pistas():
    # Pista 1
    while True:
        resposta1 = input("Pista 1: Onde nos encontramos? ")
        if resposta1.lower() == "roblox" or resposta1.lower() == "mic up":
            print("Correto!")
            time.sleep(1) #Pausa após correto
            break
        else:
            print("Tenta denovo!")

    # Pista 2
    while True:
        resposta2 = input("Pista 2: Dia que nos conhecemos? (dd/mm) ")
        if resposta2 == "2/12":
            print("Correto!")
            time.sleep(1) #Pausa após correto
            break
        else:
            print("Tenta denovo!")

    # Pista 3
    while True:
        resposta3 = input("Pista 3: Onde nos vamos morar? ")
        if resposta3.lower() == "suiça":
            print("Correto!")
            time.sleep(1) #Pausa após correto
            break
        else:
            print("Tenta denovo!")

    # Pista 4
    while True:
        resposta4 = input("Pista 4: o quanto seu nenem te ama de 0 a infinito? ")
        if resposta4.lower() == "infinito":
            print("Correto!")
            time.sleep(1) #Pausa após correto
            break
        else:
            print("Tenta denovo!")

    # Pista 5
    while True:
        resposta5 = input("Pista 5: Qual a comida favorita do seu nenem? ")
        if resposta5.lower() == "massa com camarão":
            print("Correto!")
            time.sleep(1) #Pausa após correto
            break
        else:
            print("Tenta denovo!")

    print("EBAAAAA PARABENS NENEMZINHA DI MEU COLAÇAO")

jogo_pistas()