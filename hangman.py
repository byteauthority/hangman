

def def_word():
    the_word = (input("Enter the word/phrase to guess: ")).lower()
    for i in the_word:
        if i not in 'abcdefghijklmnopqrstuvwxyz ':
            return 'bad'
    if len(the_word) <= 1:
        print("Cannot accept this word")
        return 'bad'
    
    else:
        return the_word

def draw_hangman():
    print("""
              |--------|        
              |        |        
              |        |        
              |       000  
              |      00000  
              |       000  
              |        |
              |   -----|------  
              |        |  
              |        | 
              |        |  
              |       | |  
              |      |   |  
              |      |     |  
              |  
              |  
              |  
              |  
          
          \n\n""")


def game(word):
    empty = []
    for char in word:
        if char != ' ': # checks for spaces in the string and shift it to a '-'
            empty.append('_') 
        else:
            empty.append('-')
    # new = ''.join(empty) # list to string
    # print(empty)
    print(f"{' '.join(empty)}\n\n")
    return empty #, new
    
while True:
    g = 0 # guesses
    usr = (def_word()).lower()
    
    if usr != 'bad':
        # print('alright')
        usr_l = list(usr)
        blank = game(usr)


        while True:
            letter = (input("Enter (only one letter) you'd like to guess: ")).lower()
            if len(letter) > 1:
                print("Only one letter please!")
            elif letter not in 'abcdefghijklmnopqrstuvwxyz':
                print("A letter please")
            else:
                if letter in usr and letter not in blank:   
                    for i in usr:
                        if i == letter:
                            # print(i)
                            let_index = usr_l.index(i)
                            # print(let_index)
                            blank[let_index] = letter
                            usr_l[let_index] = '0'

                    print(f"{' '.join(blank)}\n\n")
                    if '_'not in blank:
                        print(f"\n\n\nYOU WON!\n\nThe word\phrase is: {usr}\n\n")
                    # print(usr_l)
                elif letter in usr and letter in blank:
                    print("\nThis letter is already guessed!\n")
                else:
                    print("\nWrong letter\n\n")
                    hang = 'HANGMAN'
                    g +=1
                    print(f"{hang[:g]}\n\n")
                    
    
                    if g == 7:
                        draw_hangman()
                        break
                    

    else:
        print("Enter a real word please\n")

    


