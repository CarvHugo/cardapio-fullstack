import sqlite3
import os
from time import sleep
import sys

conexao = sqlite3.connect("cardapio.db")
cursor = conexao.cursor()

def estrutura_de_menu(titulo):
    os.system('cls')
    print('-' * 58)
    sleep(0.03)
    print(titulo.center(65))
    sleep(0.03)
    
    if titulo not in ('\033[33mMENU PRINCIPAL\033[m', '\033[33mNOVO CADASTRO\033[m', '\033[33mALIMENTOS CADASTRADOS\033[m'):
        print('-' * 58)
        sleep(0.03)
        print('ou')
        sleep(0.03)
        print('\033[34mPressione ENTER para voltar\033[m')
        sleep(0.03)
        
    print('-' * 58)
    sleep(0.03)

opcoes_menu_principal = [
    'Ver alimentos cadastrados',
    'Cadastrar novo alimento.',
    'Deletar registro.',
    'Editar registro.',
    'Sair do sistema.'
]
    
def mostrar_opcoes(opcoes):
    for numero, opcao in enumerate(opcoes):
        print(f'\033[33m{numero + 1}\033[m - \033[34m{opcao}\033[m')
        sleep(0.03)
    print('-' * 58)
    
    
def retornar(voltar=''):
    while voltar == 'manualmente':
        voltar = input('\033[34mPressione ENTER para voltar \033[m')
        os.system('cls')
    
    while voltar not in ('manualmente', ''):
        voltar = input('\033[31mDigite apenas ENTER para voltar\033[m')
        os.system('cls')
        
    for ciclo in range(2):
                for pontos in range(4):
                    print('\rVoltando' + '.' * pontos, end='', flush=True)
                    sleep(0.03)
                os.system('cls')

def listagem():
    erro_menu = ''
    while True:
        estrutura_de_menu('\033[33mMENU PRINCIPAL\033[m')
        mostrar_opcoes(opcoes_menu_principal)
        
        if erro_menu:
            sleep(0.03)
            print(erro_menu)
            sleep(0.03)
        
        erro_menu = ''

        try:
            escolha = int(input('\033[32mSua Opção: \033[m'))
            
            if 1 > escolha or escolha > 5:
                os.system('cls')
                erro_menu = '\033[31mEscolha um número inteiro válido de "1" a "5".\033[m'
        
        except ValueError:
            os.system('cls')
            erro_menu = '\033[31mDigite um número inteiro!\033[m'
        
        except KeyboardInterrupt:
            os.system('cls')
            print('O usuário encerrou o programa de forma manual.')
            break
        
        else:
            if escolha == 1:
                estrutura_de_menu('\033[33mALIMENTOS CADASTRADOS\033[m')
                cursor.execute("""SELECT * FROM produtos;""")
                rows = cursor.fetchall()
                print(f' {"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
                for id, nome, categoria, preco in rows:
                    print(f' {id:<5} {nome:<26} {categoria:<15}R$ {preco:<10.2f}')
                    sleep(0.03)
                print('-' * 58)
                retornar('manualmente')
            
            if escolha == 2:
                erro_cadastro = ''
                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    if erro_cadastro:
                        print(erro_cadastro)
                        sleep(0.03)
                        erro_cadastro = ''
                    try:
                        nome_alimento = ' '.join(input('Nome: ').split()).title()
                        if not nome_alimento.replace(' ', '').replace('-', '').isalpha():
                            raise ValueError
                    
                    except ValueError:
                        erro_cadastro = '\033[31mDigite um nome com caracteres alfabéticos!\033[m'
                        
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                    
                    else:
                        estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                        print(f'Nome: {nome_alimento}')
                        break

                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    print(f'Nome: {nome_alimento}')
                    
                    if erro_cadastro:
                        sleep(0.03)
                        print(erro_cadastro)
                        sleep(0.03)
                        erro_cadastro = ''
                    
                    try:
                        categoria_alimento = ' '.join(input('Categoria: ').split()).title()
                        if not categoria_alimento.replace(' ', '').replace('-', '').isalpha():
                            raise ValueError
                    
                    except ValueError:
                        erro_cadastro = '\033[31mDigite uma categoria com caracteres alfabéticos!\033[m'
                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                    
                    else:
                        estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                        print(f'Nome: {nome_alimento}')
                        sleep(0.03)
                        print(f'Categoria: {categoria_alimento}')
                        break
                
                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    print(f'Nome: {nome_alimento}')
                    sleep(0.03)
                    print(f'Categoria: {categoria_alimento}')
                    
                    if erro_cadastro:
                        sleep(0.03)
                        print(erro_cadastro)
                        sleep(0.03)
                        
                        erro_cadastro = ''
                    
                    try:
                        preco_alimento = str(input('Preço: R$ ')).replace(',', '.')
                        preco_alimento = float(preco_alimento)
                    
                    except ValueError:
                        erro_cadastro = '\033[31mDigite apenas números!\033[m'

                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                    
                    else:
                        estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                        def informacoes_produto():
                            sleep(0.03)
                            print(f'Nome: {nome_alimento}')
                            sleep(0.03)
                            print(f'Categoria: {categoria_alimento}')
                            sleep(0.03)
                            print(f'Preço: R$ {preco_alimento:.2f}')
                            sleep(0.03)
                        informacoes_produto()
                        break
                
                confirmacao = None
                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    informacoes_produto()
                    
                    if confirmacao not in('S', 'N', None):
                        erro_cadastro = '\033[31mDigite apenas S ou N.\033[m'
                        print(erro_cadastro)
                        sleep(0.03)
                        erro_cadastro = ''
                        
                    confirmacao = str(input('Você confirma? [S/N] ')).upper().strip()
                    
                    if confirmacao == 'N':
                        os.system('cls')
                        retornar()
                        break
                    
                    elif confirmacao =='S':
                        cursor.execute(f"""INSERT INTO produtos (nome, categoria, preco)
                        VALUES
                        ('{nome_alimento}', '{categoria_alimento}', {preco_alimento});"""
                        )       
                        conexao.commit()
                        sleep(0.03)
                        print('\033[32mBanco de dados atualizado com sucesso!\033[m')
                        sleep(0.03)
                        retornar('manualmente')
                        break


listagem()