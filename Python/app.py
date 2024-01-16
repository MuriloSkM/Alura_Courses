import os

restaurantes = [{'nome' : 'Outback', 'categoria':'Confort Food','ativo' : False},
                {'nome':'Doralice', 'categoria':'Health Food','ativo' : True},
                {'nome' : 'Cia Burguer', 'categoria' : 'Fast Food','ativo' : False}
]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções disponíveis'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsável por encerrar o app'''
    exibir_subtitulo('Encerrando o app')

def opcao_invalida():
    '''Essa função é responsável por exibir a mensagem de opção inválida'''
    print('Opção inválida')
    voltar_ao_menu_principal()

def cadastra_restaurante():
    '''Essa Função é responsável por cadastrar um novo restaurante
        Inputs:
        -Nome do restaurante
        -Categoria

        Outputs:
        -Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria , 'ativo' : False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def lista_restaurante():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Restaurantes Cadastrados: ')

    print(f'{'Nome do restaurante'.ljust(23)} || {'Categoria'.ljust(20)} || Status')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-> {nome_do_restaurante.ljust(20)} || {categoria.ljust(20)} || {ativo}')
    voltar_ao_menu_principal()
    
def ativa_desativar_restaurante():
    '''Essa função é responsável por ativar ou destivar os restaurantes'''
    os.system('cls')
    exibir_subtitulo('Ativar/Desativar Restaurantes')
    nome_do_restaurante = input(f'Nome do Restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar para o menu principal quando necessário'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o título'''
    os.system('cls') #para windows. para mac é os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    '''Essa função é responsável por selecionar o valor do menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastra_restaurante()
        elif opcao_escolhida == 2 :
            lista_restaurante()
        elif opcao_escolhida == 3 :
            ativa_desativar_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é responsável por iniciar o sistema'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()