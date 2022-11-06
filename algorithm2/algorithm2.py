def minion_game(string):
    cont_arr_kevin = 0
    cont_arr_stuart = 0
    array_kevin = []
    array_stuart = []
    syllables_increase = 1
    lenght = len(string)
    #group of vowels
    vowels = ['A','E','I','O','U']
    #kevin strings start with consonants. Stuarts's strings start with vowels
    kevin_score = 0
    stuart_score = 0
    #switch to control arrays inputs
    sw = 0
    #x will manage the number of syllables
    for x in range(lenght):
        syllables_increase = x + 1
        for y in range(lenght):
            sw = 0
            text = string[y:y+syllables_increase]
            if len(text) == syllables_increase: 
                first_letter = text[0:1]
                for v in (vowels):
                    if v == first_letter:
                        array_kevin.append(text)
                        cont_arr_kevin = cont_arr_kevin + 1
                        sw = 1
                #is a consonant
                if sw != 1:
                    array_stuart.append(text)
                    cont_arr_stuart = cont_arr_stuart + 1
                #print('---')
    len_array_kevin = len(array_kevin)
    len_array_stuart = len(array_stuart)
    if len_array_kevin == len_array_stuart:
        print('Draw')
    else:
        if len_array_kevin > len_array_stuart:
            print('Kevin', len_array_kevin)
        else:
            print('Stuart', len_array_stuart)
if __name__ == '__main__':
    s = input()
    minion_game(s)