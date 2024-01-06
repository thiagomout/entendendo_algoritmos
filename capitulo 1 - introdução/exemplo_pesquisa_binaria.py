def pesquisa_binaria(lista, item):
    baixo = 0
    alto = lista[4] - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio #achamos o item
        
        if chute > item:
            alto = meio - 1 #chute foi alto demais, precisamos diminuir o máximo

        else:
            baixo = meio - 1

    return None # o item não existe

minha_lista = [1, 3, 5, 7, 9]

print (pesquisa_binaria(minha_lista, 3)) 
print (pesquisa_binaria(minha_lista, -1))