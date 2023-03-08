#!/bin/env python3

# Multiple Strings Tester :: MUSTR-tester
# O funcionamento deste script é bem simples. Para o funcionamento do script é nesscesarrio dois argumentos, o nome do arquivo que contem
# o texto, que logo sera transformado em um array, onde o fim de um elemento é uma quebra de linha (\n), assim cada linha do texto é um elemento
# no array. E a frase para testar.
#
# De uma forma mais simples, o script testa uma certa frase em um conjunto de frases, se uma frase desses conjuntos de frases for diferente da frase que está testando,
# o script encerra a verificação e mostra a o usuário a frase diferente e a linha que essa frase está.


from sys import argv

def check(phr_tt, phrases): # Verifica se existe uma frase diferente em um conjunto de frases (phrases). "phr_tt" é a frase que testa as outras.
    line = 1
    phrase = None 

    for phrase in phrases:
        print(f'Testing: [ {phr_tt} ] :: [ {phrase} ] :: Line [ {line} ]')

        if phr_tt != phrase: # Se alguma frase for diferente de "phr_tt", informa o usuário e encerra o loop. 
            print(f'Found!: \"{phrase}\" in line {line}')
            break 

        line += 1
        
    return (phrase, line)

def get_from_file(filename):
    with open(filename, 'r') as f:
        return str(f.read()).split('\n') # Transforma o texto de um arquivo em um array separando linhas. Cada linha é um elemento no array.

if len(argv) < 2:
    print('Insufficient arguments.')
    exit(1)

print(check(argv[2], get_from_file((argv[1]))))

