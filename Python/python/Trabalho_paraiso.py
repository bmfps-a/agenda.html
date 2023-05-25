#   senha admin = 1234
#   Alunos : Bernardo Tai, Bruno Pires e Pedro Felix
precoRefri = 5

nota10_maquina = 10
nota5_maquina = 10
nota2_maquina = 10

moeda1real_maquina = 5
moeda50c_maquina = 5
moeda25c_maquina = 5
moeda10c_maquina = 5
moeda5c_maquina = 5

def troco_total(troco_notas,troco,nota_maquina,dinheiro_maquina_inserido):
    if troco_notas > nota_maquina:
        troco_notas = nota_maquina
    nota_maquina = nota_maquina -  troco_notas
    troco = troco - (troco_notas * 10)
    dinheiro_maquina_inserido = dinheiro_maquina_inserido - troco

dinheiro_maquina_inserido = (nota10_maquina * 10) + (nota5_maquina * 5) + (nota2_maquina * 2) + (moeda10c_maquina * 0.10) + moeda1real_maquina + (moeda50c_maquina * 0.50) + (moeda25c_maquina * 0.25) + (moeda5c_maquina * 0.05)

while True :
        escolha_usuario = input('Seja Bem-Vindo! Deseja entrar como Administrador ou Cliente ? (Escolha entre "c(cliente)" , "a(admin))" e s(sair) --> ')
        while escolha_usuario != 'c' and escolha_usuario != 'C' and escolha_usuario != 'a' and escolha_usuario != 'A' and escolha_usuario != 's' and escolha_usuario != 'S' :
            escolha_usuario = str(input('Erro! Digite uma letra válida (c = cliente ou a = admin) --> '))
        if escolha_usuario == 's' or escolha_usuario =='S':
            break
        elif escolha_usuario == 'c' or escolha_usuario == 'C':
            print('Cardápio')
            print('Coca - Cola : R$ 5.00 ')
            print('Observação! A máquina só aceita notas de 2, 5 e 10 reais, ou moedas de 1 real, 50, 25, 10 e 5 centavos! AVISO!! A MÁQUINA POSSUI O LIMITE DE NO MAXIMO 50 REAIS DE TROCO NO TOTAL!')
            confirmacao_de_compra = input('Gostaria de comprar ? (s = sim) ou n = não):')
            if confirmacao_de_compra == 'n' or confirmacao_de_compra == 'N':
                print('OK! Obrigado e volte sempre!')
                break
            elif confirmacao_de_compra == 's' or confirmacao_de_compra == 'S':
                
                nota10_inserida = int(input("Insira a quantidade de notas de 10: "))
                nota10_maquina += nota10_inserida

                nota5_inserida = int(input("Insira a quantidade de notas de 5: "))
                nota5_maquina += nota5_inserida

                nota2_inserida = int(input("Insira a quantidade de notas de 2: "))
                nota2_maquina += nota2_inserida

                moeda1real_inserida = int(input("Insira a quantidade de moedas de 1 real: "))
                moeda1real_maquina += moeda1real_maquina

                moeda50c_inserida = int(input("Insira a quantidade de moedas de 50 centavos: "))
                moeda50c_maquina += moeda50c_inserida

                moeda25c_inserida = int(input("Insira a quantidade de moedas de 25 centavos: "))
                moeda25c_maquina += moeda25c_inserida

                moeda10c_inserida = int(input("Insira a quantidade de moedas de 10 centavos: "))
                moeda10c_maquina += moeda10c_inserida

                moeda5c_inserida = int(input("Insira a quantidade de moedas de 5 centavos: "))
                moeda5c_maquina += moeda5c_inserida

                dinheiro_do_cliente = (nota10_inserida * 10) + (nota5_inserida * 5) + (nota2_inserida * 2) + (moeda10c_inserida * 0.10) + moeda1real_inserida + (moeda50c_inserida * 0.50) + (moeda25c_inserida * 0.25) + (moeda5c_inserida * 0.05)
            if dinheiro_do_cliente < precoRefri:
                print("Compra invalida, insira uma quantidade maior que 5 reais ")
            troco = dinheiro_do_cliente - precoRefri
            if troco > 50:
                print('ERRO! Quantidade limite ultrapassada!')
                break
            if troco > 0:
                print("Compra realizada, aqui está seu troco:", troco)

                troco_notas_10 = int(troco / 10)
                troco_total(troco_notas_10,troco,nota10_maquina,dinheiro_maquina_inserido)
                
                troco_notas_5 = int(troco / 10)
                troco_total(troco_notas_5,troco,nota5_maquina,dinheiro_maquina_inserido)
                

                troco_notas_2 = int(troco / 10)
                troco_total(troco_notas_2,troco,nota2_maquina,dinheiro_maquina_inserido)
                
                troco_moedas_1 = int(troco / 10)
                troco_total(troco_moedas_1,troco,moeda1real_maquina,dinheiro_maquina_inserido)

                troco_moedas_50 = int(troco / 10)
                troco_total(troco_moedas_50,troco,moeda50c_maquina,dinheiro_maquina_inserido)

                troco_moedas_25 = int(troco / 10)
                troco_total(troco_moedas_25,troco,moeda25c_maquina,dinheiro_maquina_inserido)

                troco_moedas_10 = int(troco / 10)
                troco_total(troco_moedas_10,troco,moeda10c_maquina,dinheiro_maquina_inserido)

                troco_moedas_5 = int(troco / 10)
                troco_total(troco_moedas_5,troco,moeda5c_maquina,dinheiro_maquina_inserido)

                if troco_notas_10 >= 1:
                    print("Notas de R$10:", troco_notas_10)
                if troco_notas_5 >= 1:
                    print("Notas de R$5:", troco_notas_5)
                if troco_notas_2 >= 1:
                    print("Notas de R$2:", troco_notas_2)
                if troco_moedas_1 >= 1:
                    print("Moedas de R$1:", troco_moedas_1)
                if troco_moedas_50 >= 1:
                    print("Moedas de R$0.50:", troco_moedas_50)
                if troco_moedas_25 >= 1:
                    print("Moedas de R$0.25:", troco_moedas_25)
                if troco_moedas_10 >= 1:
                    print("Moedas de R$0.10:", troco_moedas_10)
                if troco_moedas_5 >= 1:
                    print("Moedas de R$0.05:", troco_moedas_5)
            else:
                (" Compra realizada com sucesso! ")
        
        elif escolha_usuario == 'a' or escolha_usuario == 'A':
            tentativa_senha = int(input('Digite a senha numérica para logar :'))
            while tentativa_senha != 1234:
                tentativa_senha = int(input('Senha Incorreta! Tente novamente --> '))
            if tentativa_senha == 1234:
                while True:
                    print('=' * 20)
                    print('Acesso liberado.')
                    print('Pressione 1 para visualizar a quantidade de dinheiro na máquina (Cédulas e Moedas).')
                    print('Pressione 2 para modificar o valor de unidades.')
                    print('Pressione 3 para retornar ao menu inicial.')
                    print('=' * 20)
                    resposta_adm = int(input('--> '))
                    if resposta_adm == 2:
                        print(f'A máquina possui : {dinheiro_maquina_inserido}')
                        print('Coloque a quantidade necessária de dinheiro na máquina : ')
                        # NOTAS

                        nota10_inserida = int(input("Insira a quantidade de notas de 10: "))
                        nota5_inserida = int(input("Insira a quantidade de notas de 5: "))
                        nota2_inserida = int(input("Insira a quantidade de notas de 2: "))
                        # MOEDAS
                        moeda1real_inserida = int(input("Insira a quantidade de moedas de 1 real: "))
                        moeda50c_inserida = int(input("Insira a quantidade de moedas de 50 centavos: "))
                        moeda25c_inserida = int(input("Insira a quantidade de moedas de 25 centavos: "))
                        moeda10c_inserida = int(input("Insira a quantidade de moedas de 10 centavos: "))
                        moeda5c_inserida = int(input("Insira a quantidade de moedas de 5 centavos: "))

                        dinheiro_inserido = (nota10_inserida * 10) + (nota5_inserida * 5) + (nota2_inserida * 2)
                        dinheiro_inserido = float(dinheiro_inserido)
                        dinheiro_inserido = (moeda1real_inserida * 1) + (moeda50c_inserida * 0.5) + (moeda25c_inserida * 0.25) + (moeda10c_inserida * 0.1) + (moeda5c_inserida * 0.05) + dinheiro_inserido

                        dinheiro_maquina_inserido += + dinheiro_inserido

                        nota5_maquina += nota5_maquina
                        nota10_maquina += nota10_maquina 
                        nota2_maquina += nota2_inserida

                        moeda1real_maquina += moeda1real_inserida
                        moeda50c_maquina += moeda50c_inserida
                        moeda25c_maquina += moeda25c_inserida
                        moeda10c_maquina += moeda10c_inserida
                        moeda5c_maquina += moeda5c_inserida
                        
                        print(f'Valores adicionados! A máquina possui : {dinheiro_maquina_inserido} reais.')
                        print('\nDeseja continuar? (S/N)')
                        continuar = input()
                        if continuar == 'N' or continuar == 'n':
                            break

                    elif resposta_adm == 1:
                        print('Dinheiro Máquina : ', dinheiro_maquina_inserido, 'Reais')
                        print('Notas de 10 reais : ', nota10_maquina, 'Cédulas')
                        print('Notas de 5 reais : ', nota5_maquina, 'Cédulas')
                        print('Notas de 2 reais : ', nota2_maquina, 'Cédulas')
                        print('Moedas de 1 real : ', moeda1real_maquina, 'Moedas')
                        print('Moedas de 0,50 centavos : ', moeda50c_maquina, 'Moedas')
                        print('Moedas de 0,25 centavos : ', moeda25c_maquina, 'Moedas')
                        print('Moedas de 0,10 centavos : ', moeda10c_maquina, 'Moedas')
                        print('Moedas de 0,5 centavos : ', moeda5c_maquina, 'Moedas')
                    elif resposta_adm == 3:
                        break