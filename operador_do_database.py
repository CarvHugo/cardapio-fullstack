import sqlite3

conexao = sqlite3.connect("cardapio.db")
cursor = conexao.cursor()

def listagem():
    while True:
        print('-' * 58)
        print('\033[33mMENU PRINCIPAL\033[m'.center(65))
        print('-' * 58)
        opcoes = ['Ver alimentos cadastrados.',
                  'Cadastrar novo alimento.',
                  'Deletar registro.',
                  'Sair do sistema.']
        
        for numero, opcao in enumerate(opcoes):
            print(f'\033[33m{numero + 1}\033[m - \033[34m{opcao}\033[m')
        print('-' * 58)

        try:
            escolha = int(input('\033[32mSua Opção: \033[m'))
            if 1 > escolha or escolha > 4:
                print('\033[31mEscolha um valor inteiro válido de "1" a "4".\033[m')
        
        except ValueError:
            print('\033[31mDigite um número inteiro!\033[m')
        
        except KeyboardInterrupt:
            print('O usuário encerrou o programa de forma manual.')
            break
        
        else:
            if escolha == 1:
                print('-' * 58)
                print('\033[33mALIMENTOS CADASTRADOS\033[m'.center(65))
                print('-' * 58)
                cursor.execute("""SELECT * FROM produtos""")
                rows = cursor.fetchall()
                print(f' {"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
                for id, nome, categoria, preco in rows:
                    print(f' {id:<5} {nome:<26} {categoria:<15}R$ {preco:<10.2f}')
            
            elif escolha == 2:
                print('-' * 58)
                print('\033[33mNOVO CADASTRO\033[m'.center(65))
                print('-' * 58)
                while True:
                    try:
                        nome_alimento = str(input('Nome: '))
                        if not nome_alimento.replace(' ','').isalpha():
                            raise ValueError
                    
                    except ValueError:
                        print('\033[31mDigite um nome com caracteres alfabéticos!\033[m')
                    
                    except KeyboardInterrupt:
                        print('O usuário encerrou o programa de forma manual.')
                    
                    else:
                        break
                
                while True:
                    try:
                        categoria_alimento = str(input('Categoria: '))
                    except ValueError:
                        print('\033[31mDigite uma categoria com caracteres alfabéticos!\033[m')
                    
                    except KeyboardInterrupt:
                        print('O usuário encerrou o programa de forma manual.')
                    else:
                        break
                
                while True:
                    try:
                        preco_alimento = str(input('Preço R$: ')).replace(',', '.')
                        preco_alimento = float(preco_alimento)
                    
                    except ValueError:
                        print('\033[31mDigite apenas números!\033[m')
                    
                    except KeyboardInterrupt:
                        print('O usuário encerrou o programa de forma manual.')
                    
                    else:
                        break
                
                cursor.execute(f"""INSERT INTO produtos (nome, categoria, preco)
                VALUES
                ('{nome_alimento}', '{categoria_alimento}', {preco_alimento})"""
                )       
                conexao.commit()
                print('\033[32mBanco de dados atualizado com sucesso!\033[m')
            
            elif escolha == 3:
                print('-' * 58)
                print(f'\033[31mDELEÇÃO DE REGISTROS\033[m'.center(65))
                print('-' * 58)
                print('\033[33mPara deletar um registro da tabela, digite o número ID do \nalimento desejado.\033[m')
                print('\n\033[34mDigite v para voltar ao MENU PRINCIPAL.\033[m')
                
                numero_id = str(input('\nID: '))
                if numero_id.isnumeric():
                    numero_id = int(numero_id)
                    cursor.execute(f"""DELETE FROM produtos WHERE id = {numero_id};""")
                    conexao.commit()
                    print('\n\033[32mProduto deletado!\033[m')
                
                elif numero_id.isalpha() and numero_id in ('V','v'):
                    print('\nVoltando...')
                
                else:
                    print('\033[31mEntrada inválida! Digite apenas o número ID ou v.\033[m')
            
            elif escolha == 4:
                print('-' * 58)
                print('Saindo do sistema... Até logo!')
                print('-' * 58)
                break