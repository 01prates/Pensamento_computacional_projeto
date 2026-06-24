'''
um bloco de comentarios
>PO (como dono negocio) preciso de um sistema de vendas de hamburguer para que eu possa vender e lucrar

>QA (como cliente) preciso de um sistema facil de compras para que eu possa comprar de forma pratica

>tech (como progamador) quero um sistema que eu possa implementar funcionalidades basicas para atender o cliente 
de forma pratica 

>dev (como programador) quero um sistema facil e pratico de compras para minha hamburgueria para implementar as
funcionalidades a interface do sistema

>UX (como designer de experiencia do usuario) quero um sistema pratico e facil de usar para que o cliente possa comprar
 de forma pratica e rapida

>IA (como inteligencia artificial) quero um sistema de vendas de hamburguer para que o cliente possa comprar de forma pratica e rapida

'''

p1_nome = "hamburguer piraju"
p1_estoque = 50
p1_preco = 25.00
p1_validade = "05.01.2027"
p1_descricao =  "hamburguer simples e famoso PCQ (Pao de brioche, Hamburguer 150g e queijo)"

p2_nome = "hamburguer santa cruz"
p2_estoque = 51
p2_preco = 27.50
p2_validade = "12.01.2027"
p2_descricao = "para os fans de bacon, pao brioche, 2 discos de smash burguer, Queijo, baconese e fatias de bacon"

p3_nome = "Leme"
p3_estoque = 49
p3_preco = 30.00
p3_validade = "02.12.2027"
p3_descricao = "Pao de brioche, maionese verde, hamburguer de 150g, queijo, alface amaricana, tomate, picles e cebola roxa"





# 
while True:
    print('-' * 48 + '\n')
    print('Bem Vindo ao sistema de vendas a hamburgueria sampaio\n')
    print('1 - cadastrar produto\n')
    print('2 - listar produto')
    print('3 - realizar vendas')
    print('0 - sair')
    print('-----------------------------------------------\n')

    opção = input('digite a opcao desejada:')

    if opção == '1':
        print('cadastrar produto...\n')
        nome_produto = input('digite o nome do produto:  ')
        preco_produto = float(input('digite o preço do produto: '))
        estoque_produto = int(input('digite a quantidade de produto no estoque'))
        validade_produto = input('digite a validade do produto:  ')
        descrição_produto = input('digite a descriçaõ do produto')
        print(f'Produto {nome_produto} cadastrado com sucesso!\n')

    elif opção == '2':


        print('Listando produtos...\n')
        

        
