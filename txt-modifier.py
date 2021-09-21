from re import sub
# sub(old_word, new_word, text.read())

def readingfile(text, word):
    c = 0
    with open(text) as file:
        fileread = file.readlines()
        for lines in fileread:
            if word in lines:
                c += 1   
    return (int(c))

def substitutingfile(old_word, new_word, text):
    with open(text) as file:
        new_file = file.read()
        if old_word in new_file:
            new_file = sub(old_word, new_word, new_file)
    return new_file
    
def rewritingfile(text, new_text):
    with open(text, 'w') as file:
        file.write(new_text)
    
    final_file = open(text, 'r')
    print(final_file.read())
    final_file.close()

choice = input(f"Você deseja modificar alguma parte do texto do seu arquivo txt? Digite 's' para sim ou 'n' para não.\n")
if choice == 's':
    word = input(f"\nQual palavra ou frase você deseja modificar?\n") 
    reading = readingfile('readme.txt', word)
    if reading == 0:
        print(f"\nNão encontramos a palavra ou frase procurada, portanto, não há como modificar o arquivo.")
    else:
        print(f'\nO termo {word.capitalize()} foi encontrado {reading} vezes.\n')
        new_word = input(f"Por qual palavra ou frase você deseja modificar o termo anterior?\n")
        print(f'\n...\nO texto modificado ficou assim: \n')
    
        rewriting = rewritingfile('readme.txt', substitutingfile(word, new_word, 'readme.txt'))