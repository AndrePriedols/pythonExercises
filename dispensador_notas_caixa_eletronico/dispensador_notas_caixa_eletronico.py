# coding=utf-8

valor_saque = 1 # incializa valor do saque

while valor_saque != 0:    
    # verifica se valor inserido é valido
    while True: 
        while True: # verifica se o tipo inserido é inteiro
            try:
                valor_saque = int(input("Insira o valor a ser sacado (deve ser inteiro positivo múltiplo de 10):"))
            except:
                print("Valor digitado inválido. Valor deve ser número inteiro múltiplo de 10.")
            else:
                break
            
        if valor_saque % 10 != 0 or valor_saque < 0: # verifica se inteiro inserido não é negativo e é múltiplo de 10
            print("Valor do saque não pode ser negativo e deve ser multiplo de R$10,00.")
        else:
            break

    num_opcao = 0 # inicializa variável a ser usada na impressão das opções
    print("\n")
    print("Valor do saque:", valor_saque,"\n")

    # os condicionais avaliam se é possível uma solução que inclua o valor da nota avaliada. Caso seja impossível, segue para outro valor de nota.
    if valor_saque >= 100:
        num_opcao += 1 # atribui o valor da opção à variável que será usada na impressão   
        notas_100 = valor_saque // 100 # verifica quantas notas de 100 são possíveis
        valor_restante = valor_saque - notas_100 * 100 # elimina do total o valor obtido com as notas de 100
        notas_50 = valor_restante // 50 # repete o processo com as notas seguintes. Caso não seja divisível, valor restante não é alterado por esta nota.
        valor_restante = valor_restante - notas_50 * 50
        notas_20 = valor_restante // 20
        valor_restante = valor_restante - notas_20 * 20
        notas_10 = valor_restante // 10
        print("Opcao", num_opcao) # usa variável já com o número correto da opção.
        if notas_100 > 0: print("Notas de 100:", notas_100) # só imprime quantidade de notas se elas de fato forem usadas, por causa do condicional antes do print.
        if notas_50 > 0: print("Notas de 50:", notas_50)
        if notas_20 > 0: print("Notas de 20:", notas_20)
        if notas_10 > 0: print("Notas de 10:", notas_10)
        print("\n")

    # repete o processo verificando outras opções
    if valor_saque >= 50:
        num_opcao += 1
        notas_50 = valor_saque // 50
        valor_restante = valor_saque - notas_50 * 50
        notas_20 = valor_restante // 20
        valor_restante = valor_restante - notas_20 * 20
        notas_10 = valor_restante // 10
        print("Opcao", num_opcao)
        if notas_50 > 0: print("Notas de 50:", notas_50)
        if notas_20 > 0: print("Notas de 20:", notas_20)
        if notas_10 > 0: print("Notas de 10:", notas_10)
        print("\n")
        
    if valor_saque >= 20:
        num_opcao += 1
        notas_20 = valor_saque // 20
        valor_restante = valor_saque - notas_20 * 20
        notas_10 = valor_restante // 10
        print("Opcao", num_opcao)
        if notas_20 > 0: print("Notas de 20:", notas_20)
        if notas_10 > 0: print("Notas de 10:", notas_10)
        print("\n")
        
    if valor_saque >= 10:
        num_opcao += 1
        notas_10 = valor_saque // 10    
        print("Opcao", num_opcao)
        if notas_10 > 0: print("Notas de 10:", notas_10)
        print("\n")

print("Fim do programa.")
