#!/usr/bin/python3

opt = ''
while opt != '3':

#carregar lista de compra
    with open('lista2.txt','r') as fp:
    	lista2 = fp.readlines()

    #Exibir lista de opcoes

    print('1)incluir novos produtos')
    print('2)excluir produtos')
    print('3)para sair')
    opt = input('Escolha uma das opcoes[1]:')


    # se for opcao 1, cadastre um novo produto
    if opt =='1':
        lista2.append(input('Digite um novo produto:') + '\n')

    #se for opcao 2, remova o produto
    elif opt == '2':    
        lista2.remove(input('Digite o produto a ser removido:') + '\n')
        
    elif opt == '3':
       	continue
    else:
        print('cai fora')



    #salve o resultado na lista dentro de um arquivo
    with open('lista2.txt', 'w') as fp:
        fp.writelines(lista2)





