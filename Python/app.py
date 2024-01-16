import os

restaurantes = ['Outback','Doralice']

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o app')

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

def cadastra_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Restaurantes Cadastrados: ')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()
    
def ativa_restaurante():
    os.system('cls')
    exibir_subtitulo('Ativar restaurantes')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls') #para windows. para mac é os.system('clear')
    print(texto)
    print()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastra_restaurante()
        elif opcao_escolhida == 2 :
            lista_restaurante()
        elif opcao_escolhida == 3 :
            ativa_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()