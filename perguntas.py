while True:
    print("bem vindo ao jogo de adivinha do jose sergio!")
    print("DICA: pra selecionar a opçao, digite e envie o numero opçao escolhida")
    print("SE VOCE FOSSE UM LEGUME E PUDESSE ESCOLHER PROFISSAO, VOCE SERIA: \n 1 tomate CEO da salada:\n 2 cenoura atleta olimpica:\n 3 batata preguiçosa de sofa:")
    resposta1 = input("1, 2, 3 \n")
    
    if  resposta1 == "1":
        print("se importante demais, vive bancando o chef mais ninguem pediu a opiniao \n")

    elif resposta1 == "2":
        print("Só se importa em se exibir, deve contar medalha até pra cachorro \n")

    elif resposta1 == "3":
        print("É preguiçoso de nível lendário, provavelmente nem levanta pra ir ao banheiro sem reclamar \n")

    print("Se sua geladeira tivesse sentimentos, ela: \n 1 Te odiaria por roubar sorvete à noite \n 2  Ficaria feliz com as sobras de pizza \n 3 Te chantagearia com comida estragada")
    resposta2 = input("1, 2, 3 \n")

    if  resposta2 == "1":
        print("Você é culpado e sente prazer em se meter em confusão, tipo bandido de geladeira \n")

    elif resposta2 == "2":
        print("você é preguiçoso, vive de sobras, mas finge que tá tudo bem \n")

    elif resposta2 == "3":
        print("Você é fácil de manipular, cai em chantagem por qualquer besteira \n")

        
    print("Se o sol tirasse férias, você: \n 1 Compra bronzeador infinito \n 2 Fica com freezer de gelo ligado \n 3 Aproveita pra ver a lua de dia")
    resposta3 = input("1, 2, 3 \n")

    if  resposta3 == "1":
        print("você é paranoico e vive gastando com besteira pra se proteger do óbvio \n")

    elif resposta3 == "2":
        print("Você é do tipo que exagera em tudo e transforma problema pequeno em desastre épico \n")

    elif resposta3 == "3":
        print("Você é doido, vive curtindo coisas inúteis enquanto o mundo queima \n")

    quer_repetir = input("voce quer parar ou quer tentar de novo? (tentar/parar)")
    if quer_repetir == "parar":
        break

