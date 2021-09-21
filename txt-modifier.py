from re import sub
# sub(old_word, new_word, text.read())

class TextModifier:

    #função dedicada à leitura e contagem de vezes em que o termo aparece.
    def readingfile(text, word):
        c = 0
        with open(text) as file:
            fileread = file.readlines()
            for lines in fileread:
                if word in lines:
                    c += 1   
        return (int(c))

    #função dedicada a substituir a palavra selecionada por uma nova.
    def substitutingfile(old_word, new_word, text):
        with open(text) as file:
            new_file = file.read()
            if old_word in new_file:
                new_file = sub(old_word, new_word, new_file)
        return new_file

    #função dedicada à persistência dessa mudança.
    def rewritingfile(text, new_text):
        with open(text, 'w') as file:
            file.write(new_text)

        final_file = open(text, 'r')
        print(final_file.read())
        final_file.close()

choice = input(f"Você deseja modificar alguma parte do texto do seu arquivo txt? Digite 's' para sim ou 'n' para não.\n")
if choice == 's':
    word = input(f"\nQual palavra ou frase você deseja modificar?\n") 
    reading = TextModifier.readingfile('readme.txt', word)
    if reading == 0:
        print(f"\nNão encontramos a palavra ou frase procurada, portanto, não há como modificar o arquivo.")
    else:
        print(f'\nO termo {word.capitalize()} foi encontrado {reading} vezes.\n')
        new_word = input(f"Por qual palavra ou frase você deseja modificar o termo anterior?\n")
        print(f'\n...\nO texto modificado ficou assim: \n')
    
        rewriting = TextModifier.rewritingfile('readme.txt', TextModifier.substitutingfile(word, new_word, 'readme.txt'))