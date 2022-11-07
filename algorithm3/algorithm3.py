if __name__ == '__main__':
    lista = []
    lista_nombres = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
        #print(name)
        #print(score)
    #sorting from minor to major
    aux_grade = 0
    aux_name = ''
    #print(lista)
    for y in range(len(lista)):
        for x in range(len(lista)):
            if lista[x][1] > lista[x+1][1]:
                aux_grade = lista[x][1]
                lista[x][1] = lista[x+1][1]
                lista[x+1][1] = aux_grade
                aux_name = lista[x][0]
                lista[x][0] = lista[x+1][0]
                lista[x+1][0] = aux_name
            if x == len(lista)-2:
                break
    #lookig for the second minor value
    c = 1
    for x in range(len(lista)):
        if c == 1:
            if lista[x][1] < lista[x+1][1]:
                lista_nombres.append(lista[x+1][0])
                c = c + 1
        else:
            if lista[x][1] == lista[x+1][1]:
                lista_nombres.append(lista[x+1][0])
            else:
                break
        if x == len(lista)-2:
                break
    #print(lista)
    for x in (sorted(lista_nombres)):
        print(x)
        