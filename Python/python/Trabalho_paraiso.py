#   senha admin = 1234
#   Alunos : Bernardo Tai, Bruno Pires e Pedro Felix

#refri preço / estoque
precoRefri = 5
estoque_refri = 10
#notas total
nota10_maquina = 10
nota5_maquina = 10
nota2_maquina = 10
#moedas total
moeda1real_maquina = 5
moeda25c_maquina = 5
moeda5c_maquina = 5

valores_cedula_moeda = [10,5,2,1,0.25,0.05]
#função para calcular o troco
def calcular_troco(troco_notas,troco,nota_maquina,dinheiro_maquina_inserido,valor_monetario):
    if troco_notas > nota_maquina:
        troco_notas = nota_maquina
    nota_maquina -=  troco_notas
    troco = troco - (troco_notas * valor_monetario)
    dinheiro_maquina_inserido -= troco

dinheiro_maquina_inserido = (nota10_maquina * 10) + (nota5_maquina * 5) + (nota2_maquina * 2)  + moeda1real_maquina +  + (moeda25c_maquina * 0.25) + (moeda5c_maquina * 0.05)

while True :
        print('=' * 20)
        escolha_usuario = input('Seja Bem-Vindo! Deseja entrar como Administrador ou Cliente ? (Escolha entre "c(cliente)" , "a(admin))" e s(sair) --> ')
        print('=' * 20)
        while escolha_usuario != 'c' and escolha_usuario != 'C' and escolha_usuario != 'a' and escolha_usuario != 'A' and escolha_usuario != 's' and escolha_usuario != 'S' :
            escolha_usuario = str(input('Erro! Digite uma letra válida (c = cliente , a = admin ou s= sair) --> '))
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
                
                if estoque_refri <= 0:
                    print("Não há Refrigerantes no estoque, por favor reponha o estoque.")
                    break
                quant_refri = int(input('Digite quantas latas de refri você gostaria de comprar :'))
                estoque_refri -= quant_refri

                nota10_inserida = int(input("Insira a quantidade de notas de 10: "))
                nota10_maquina += nota10_inserida

                nota5_inserida = int(input("Insira a quantidade de notas de 5: "))
                nota5_maquina += nota5_inserida

                nota2_inserida = int(input("Insira a quantidade de notas de 2: "))
                nota2_maquina += nota2_inserida

                moeda1real_inserida = int(input("Insira a quantidade de moedas de 1 real: "))
                moeda1real_maquina += moeda1real_inserida

                moeda25c_inserida = int(input("Insira a quantidade de moedas de 25 centavos: "))
                moeda25c_maquina += moeda25c_inserida

                moeda5c_inserida = int(input("Insira a quantidade de moedas de 5 centavos: "))
                moeda5c_maquina += moeda5c_inserida

                dinheiro_do_cliente = (nota10_inserida * 10) + (nota5_inserida * 5) + (nota2_inserida * 2)  + moeda1real_inserida + (moeda25c_inserida * 0.25) + (moeda5c_inserida * 0.05)
                if dinheiro_do_cliente < precoRefri:
                    print("Compra invalida, insira uma quantidade maior que 5 reais ")
                    print(f"devolvendo dinheiro inserido :{dinheiro_do_cliente} ")
                
                troco = dinheiro_do_cliente - (precoRefri * quant_refri)
                if troco > 50:
                    print('ERRO! Quantidade limite ultrapassada!')
                    break
                if troco > 0:
                    print("Compra realizada, aqui está seu troco:", troco)

                    troco_notas_10 = int(troco / 10)
                    calcular_troco(troco_notas_10,troco,nota10_maquina,dinheiro_maquina_inserido,valores_cedula_moeda[0])
                    
                    troco_notas_5 = int(troco / 5)
                    calcular_troco(troco_notas_5,troco,nota5_maquina,dinheiro_maquina_inserido,valores_cedula_moeda[1])
                    

                    troco_notas_2 = int(troco / 2)
                    calcular_troco(troco_notas_2,troco,nota2_maquina,dinheiro_maquina_inserido,valores_cedula_moeda[2])
                    
                    troco_moedas_1 = int(troco / 1)
                    calcular_troco(troco_moedas_1,troco,moeda1real_maquina,dinheiro_maquina_inserido,valores_cedula_moeda[3])

                    
                    troco_moedas_25 = int(troco / 0.25)
                    calcular_troco(troco_moedas_25,troco,moeda25c_maquina,dinheiro_maquina_inserido,valores_cedula_moeda[4])

                    
                    troco_moedas_5 = int(troco / 0.05)
                    calcular_troco(troco_moedas_5,troco,moeda5c_maquina,dinheiro_maquina_inserido,valores_cedula_moeda[5])

                    if troco_notas_10 >= 1:
                        print("Notas de R$10:", troco_notas_10)
                    if troco_notas_5 >= 1:
                        print("Notas de R$5:", troco_notas_5)
                    if troco_notas_2 >= 1:
                        print("Notas de R$2:", troco_notas_2)
                    if troco_moedas_1 >= 1:
                        print("Moedas de R$1:", troco_moedas_1)
                    if troco_moedas_25 >= 1:
                        print("Moedas de R$0.25:", troco_moedas_25)
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
                    print("pressione 3 para acessar o estoque")
                    print('pressione 4 para Visualizar a lista de pagamentos por PIX: número do telefone e valor')
                    print('Pressione 5 para retornar ao menu inicial.')
                    print('=' * 20)
                    resposta_adm = int(input('--> '))
                    if resposta_adm == 2:
                        escolha_adm = int(input('Digite 1 para retirar uma quantia da máquina ou 2 para adicionar uma quantia na máquina -->'))

                        if escolha_adm == 2:
                            print(f'A máquina possui : {dinheiro_maquina_inserido}')
                            print('Coloque a quantidade necessária de dinheiro na máquina :')

                            #notas inseridas
                            nota10_inserida = int(input("Insira a quantidade de notas de 10: "))
                            nota5_inserida = int(input("Insira a quantidade de notas de 5: "))
                            nota2_inserida = int(input("Insira a quantidade de notas de 2: "))
                            #moedas inseridas
                            moeda1real_inserida = int(input("Insira a quantidade de moedas de 1 real: "))
                            moeda25c_inserida = int(input("Insira a quantidade de moedas de 25 centavos: "))
                            moeda5c_inserida = int(input("Insira a quantidade de moedas de 5 centavos: "))
                            #dinheiro total inserido
                            dinheiro_inserido = (nota10_inserida * 10) + (nota5_inserida * 5) + (nota2_inserida * 2)
                            dinheiro_inserido = float(dinheiro_inserido)
                            dinheiro_inserido = (moeda1real_inserida * 1) +  (moeda25c_inserida * 0.25) +  (moeda5c_inserida * 0.05) + dinheiro_inserido

                            dinheiro_maquina_inserido += + dinheiro_inserido

                            nota5_maquina += nota5_inserida
                            nota10_maquina += nota10_inserida 
                            nota2_maquina += nota2_inserida

                            moeda1real_maquina += moeda1real_inserida
                            moeda25c_maquina += moeda25c_inserida
                            moeda5c_maquina += moeda5c_inserida
                            
                            print(f'Valores adicionados! A máquina possui : {dinheiro_maquina_inserido} reais.')
                            print('\nDeseja continuar? (S/N)')
                            continuar = input()
                            if continuar == 'N' or continuar == 'n':
                                break
                        elif escolha_adm == 1:  
                            print(f'A máquina possui : {dinheiro_maquina_inserido}')
                            print('Retire a quantidade desejada da máquina:')

                            #notas retiradas
                            nota10_retirada = int(input("Insira a quantidade de notas de 10 que deseja retirar: "))
                            if nota10_retirada > nota10_maquina:
                                print('ERRO! o valor pedido é superior ao valor da máquina.')
                                break
                            nota5_retirada = int(input("Insira a quantidade de notas de 5 que deseja retirar: "))
                            if nota5_retirada > nota5_maquina:
                                print('ERRO! o valor pedido é superior ao valor da máquina.')
                                break
                            nota2_retirada= int(input("Insira a quantidade de notas de 2 que deseja retirar: "))
                            if nota2_retirada > nota5_maquina:
                                print('ERRO! o valor pedido é superior ao valor da máquina.')
                                break
                            #moedas retiradas
                            moeda1real_retirada = int(input("Insira a quantidade de moedas de 1 real que deseja retirar: "))
                            if moeda1real_retirada > moeda1real_maquina:
                                print('ERRO! o valor pedido é superior ao valor da máquina.')
                                break
                            moeda25c_retirada = int(input("Insira a quantidade de moedas de 25 centavos que deseja retirar: "))
                            if moeda25c_retirada > moeda25c_maquina:
                                print('ERRO! o valor pedido é superior ao valor da máquina.')
                                break
                            moeda5c_retirada = int(input("Insira a quantidade de moedas de 5 centavos que deseja retirar: "))
                            if moeda5c_retirada > moeda5c_maquina:
                                print('ERRO! o valor pedido é superior ao valor da máquina.')
                                break

                            dinheiro_retirado = (nota10_retirada * 10) + (nota5_retirada * 5) + (nota2_retirada * 2)
                            dinheiro_retirado = float(dinheiro_retirado)
                            dinheiro_retirado = (moeda1real_retirada * 1) +  (moeda25c_retirada * 0.25) +  (moeda5c_retirada * 0.05) + dinheiro_retirado

                            dinheiro_maquina_inserido -=  dinheiro_retirado

                            nota5_maquina -= nota5_retirada
                            nota10_maquina -= nota10_retirada
                            nota2_maquina -= nota2_retirada

                            moeda1real_maquina -= moeda1real_retirada   
                            moeda25c_maquina -= moeda25c_retirada
                            moeda5c_maquina -= moeda5c_retirada

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
                        print('Moedas de 0,25 centavos : ', moeda25c_maquina, 'Moedas')
                        print('Moedas de 0,5 centavos : ', moeda5c_maquina, 'Moedas')
                    elif resposta_adm == 5:
                        break
                    elif resposta_adm == 3:
                        print('=' * 20)
                        print("pressione 1 para adicionar estoque")
                        print("pressione 2 para retirar estoque")
                        print("pressione 3 para vizualizar o conteúdo do estoque")
                        print('=' * 20)
                        resposta_estoque = int(input("--> "))
                        if resposta_estoque == 1:
                            adicao_estoque = int(input('quantos refrigerantes você deseja adicionar ao estoque(máximo 20 por vez):'))
                            while adicao_estoque <= 0 or adicao_estoque > 20:
                                print('quantidade não permitida')
                                adicao_estoque = int(input('quantos refrigerantes você deseja adicionar ao estoque(máximo 20 por vez):'))
                            if adicao_estoque > 0 and adicao_estoque <= 20:
                                estoque_refri += adicao_estoque
                                print(f'a máquina possui  {estoque_refri} refrigerantes no estoque.')
                                print('Deseja continuar? (S/N)')
                                continuar = input()
                                if continuar == 'N' or continuar == 'n':
                                    break
                        elif resposta_estoque == 2:
                            retiro_estoque = int(input('quantos refrigerantes você deseja retirar do estoque(máximo 20 por vez):'))
                            while retiro_estoque < 0 or retiro_estoque > 20:
                                print('quantidade não permitida')
                                retiro_estoque = int(input('quantos refrigerantes você deseja retirar do estoque(máximo 20 por vez):'))
                            if retiro_estoque > 0 and retiro_estoque <= 20:
                                estoque_refri-= retiro_estoque
                                print(f'a máquina possui  {estoque_refri}  refrigerantes no estoque.')
                                print('Deseja continuar? (S/N)')
                                continuar = input()
                                if continuar == 'N' or continuar == 'n':
                                    break
                        elif resposta_estoque == 3:
                            print(f'a máquina possui {estoque_refri} refrigerantes no estoque.')
                            print('Deseja continuar? (S/N)')
                            continuar = input()
                            if continuar == 'N' or continuar == 'n':
                                break