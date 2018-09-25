#3)Linguagem: Python

def analise(frase):
 
    #escolhemos o alfabeto maiusculo
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
    
    resultado = 'Resultado:\n'

    #criamos o array que sera preenchido posteriormente para saber a distancia da letra mais frequente até o a letra A
    arrayy = []
 
    #varremos cada letra do alfabeto definido acima
    for i in alfabeto:
        contador = 0
       
        #varremos cada letra da frase que foi dada
        for j in frase.upper():
           

            #comparamos quando elas sao iguais
            if i == j:

                #quando elas forem iguais adicionamos ao contador 1 unidade
                contador += 1
                
           
        #o resultado é impresso na tela atraves do contador*100 dividido pela quantidade de letras da frase
        resultado += 'Letra %s: %.2f%%\n'%(i, (contador*100/len(frase)))
        arrayy.append(contador)

    #imprimimos a frequencia e o array            
    print(resultado)
    print(arrayy)

    #descobrimos o valor maximo do array e onde ele está, assim ele será nossa chave,pois é a distancia dele até a letra A
    valor_maximo = max(arrayy)
    maximo_index = arrayy.index(valor_maximo)
    chave=maximo_index
    print('chave: ',chave)
    
    #chamamos a funçao que decripta a frase dada com a chave que descobrimos previamente
    descriptar(chave,frase)

#funcao que decripta a frase dada
def descriptar(key,frase):
    fraseDecriptada = ''
    #for para pegar todas as letras da frase
    for i in range(0, len(frase)):
        #pega o código numérico do caractere da posiçao i
        novoCaractere = ord(frase[i])
        #diminuimos a chave desse codigo para encontrarmos o caractere correto
        novoCaractere -= key
        #se o novo x for menor que o codigo numerico do A que é 65 somamos 26 a ele para estar dentro do intervalo das maiusculas (65 ate 90)
        if novoCaractere < ord('A'):
            novoCaractere += 26
        #adicionamos a frase decriptada o novo caractere
        fraseDecriptada += chr(novoCaractere)
    #imprimimos a frase completa
    print(fraseDecriptada)


#e na main pedimos a frase e chamamos a funcao analise que acha a key e logo apos chama a de decriptar que decripta com a key e imprime na tela
def main():
 
    mensagem = input("Digite a mensagem a ser decriptada: ")
 
 
    analise(mensagem)
 
   
 
main()
