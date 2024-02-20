import random
from os import system

def print_hangman(tries):
    if(tries==6):
        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
    elif(tries==5):
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
    elif(tries==4):
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
    elif(tries==3):
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("  \  |")
        print("     |")
    elif(tries==2):
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("/ \  |")
        print("     |")
    elif(tries==1):
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|   |")
        print("/ \  |")
        print("     |")
    elif(tries==0):
        print("\n +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
    return""
def co_op():
    who=True #True player1, False player2 kelime girecek
    player1=0
    player2=0
    tries=6
    guessed=False
    score=0
    isthatrue=True
    while isthatrue:
        hint_hak=2
        realword=[]
        guessed_letters=[]
        bluword=[]
        tries=6
        guessed=False
        digit=input("Who wants enter a word 1-Player1 2-Player2\n")
        if digit=="2":
            who=False
            isthatrue=False
        elif digit=="1":
            who=True
            isthatrue=False
        else:
            print("Please enter 1 or 2")
        while who:
            word=input("Please enter a word Player1\n").lower()
            isthatrue=word.isalpha()
            system("clear")
            if isthatrue:
                for i in word:
                    realword.append(i)
                for i in range(len(word)):
                    i=word[i]
                    if i==" ":
                        i="/"
                        bluword.append(i)
                    elif(i=="'"):
                        i="'"
                        bluword.append(i)
                    else:
                        i="_"
                        bluword.append(i)
                print(bluword)
                while (not guessed and tries>0):
                    print(print_hangman(tries))
                    guess=input(f"Guess a letter or word you have {tries} tries Press 1 to Hint you have {hint_hak} hint hakkı\n")
                    if guess.isalpha() and len(guess)==1:
                        if guess in guessed_letters:
                            print("Bunu ztn denemişsin dalga mı geçion")
                        elif guess not in word:
                            print("Kelime de bu harf yok")
                            print(bluword)
                            guessed_letters.append(guess)
                            tries-=1
                        else:
                            
                            guessed_letters.append(guess)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                bluword[index]=guess
                            
                            if "_" not in bluword :
                                print(bluword)
                                print("Player2 bu turu kazandı")
                                
                                guessed=True
                            else:
                                print("Bu harf kelimede var")
                                print(bluword)
                    elif(guess=="1" or guess==1)and hint_hak>0:
                        hebele =True
                        hint_hak-=1
                        while hebele:
                            hint=random.choice(realword)
                            if hint in guessed_letters:
                                continue
                            elif hint in bluword:
                                continue
                            else:
                                hebele=False
                                for i,letter in enumerate(word):
                                    if hint==letter:
                                        index=i
                                        break
                                bluword[i]=hint
                                print(bluword)
                    elif hint_hak<=0:
                        print("You have no more hint")
                        print(bluword)
                    elif guess.isdigit():#
                        print("NOT DİGİT")
                    elif len(guess)>1:
                        if guess==word:
                            print(realword)
                            print("Player2 wins this round")
                            guessed=True
                        else:
                            print("Wrong guess")
                            tries-=1
            if tries<=0:
                print(print_hangman(tries))
                player1+=1
                print(f"You lost this round Player2 Player1's word is {word}")
                again=input("Do you wanna play again (Y/N)\n").upper()
                if again=="Y":
                    
                    isthatrue=True
                    break
                else:
                    print(f"Player1 score: {player1} Player2 score: {player2}")
                    if player1>player2:
                        print("Player1 win")
                    elif player1==player2:
                        print("Draw")
                    else:
                        print("Player2 win")
                    print("Game Over")
                    isthatrue=False
                    break
            elif guessed:
                print(print_hangman(tries))
                player2+=1
                print(f"You win this round Player2")
                again=input("Do you wanna play again (Y/N)\n").upper()
                if again=="Y":
                    
                    isthatrue=True
                    break
                else:
                    print(f"Player1 score: {player1} Player2 score: {player2}")
                    if player1>player2:
                        print("Player1 win")
                    elif player1==player2:
                        print("Draw")
                    else:
                        print("Player2 win")
                    print("Game Over")
                    isthatrue=False
                    break
            else:
                print("Please just enter letters")
        while not who:
            word=input("Please enter a word Player2\n").lower()
            isthatrue=word.isalpha()
            system("clear")
            if isthatrue:
                for i in word:
                    realword.append(i)
                for i in range(len(word)):
                    i=word[i]
                    if i==" ":
                        i="/"
                        bluword.append(i)
                    elif(i=="'"):
                        i="'"
                        bluword.append(i)
                    else:
                        i="_"
                        bluword.append(i)
                print(bluword)
                while (not guessed and tries>0):
                    print(print_hangman(tries))
                    guess=input(f"Guess a letter or word you have {tries} tries Press 1 to Hint you have {hint_hak} hint hakkı\n")
                    if guess.isalpha() and len(guess)==1:
                        if guess in guessed_letters:
                            print("Bunu ztn denemişsin dalga mı geçion")
                        elif guess not in word:
                            print("Kelime de bu harf yok")
                            print(bluword)
                            guessed_letters.append(guess)
                            tries-=1
                        else:
                        
                            guessed_letters.append(guess)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                bluword[index]=guess
                            
                            if "_" not in bluword :
                                print(bluword)
                                print("Player1 bu turu kazandı")
                                
                                guessed=True
                            else:
                                print("Bu harf kelimede var")
                                print(bluword)
                    elif(guess=="1" or guess==1)and hint_hak>0:
                        hebele =True
                        hint_hak-=1
                        while hebele:
                            hint=random.choice(realword)
                            if hint in guessed_letters:
                                continue
                            elif hint in bluword:
                                continue
                            else:
                                hebele=False
                                for i,letter in enumerate(word):
                                    if hint==letter:
                                        index=i
                                        break
                                bluword[i]=hint
                                print(bluword)
                    elif hint_hak<=0:
                        print("You have no more hint hakkı")
                        print(bluword)
                    elif guess.isdigit():
                        print("NOT DİGİT")
                    elif len(guess)>1:
                        if guess==word:
                            print(realword)
                            print("Player1 wins this round")
                            guessed=True
                        else:
                            print("Wrong guess")
                            tries-=1
            if tries<=0:
                print(print_hangman(tries))
                player2+=1
                print(f"You lost this round Player1 Player2's word is {word}")
                again=input("Do you wanna play again (Y/N)\n").upper()
                if again=="Y":
                    
                    isthatrue=True
                    break
                else:
                    print(f"Player1 score: {player1} Player2 score: {player2}")
                    if player1>player2:
                        print("Player1 win")
                    elif player1==player2:
                        print("Draw")
                    else:
                        print("Player2 win")
                    print("Game Over")
                    isthatrue=False
                    break
            elif guessed:
                print(print_hangman(tries))
                player1+=1
                print(f"You win this round Player1")
                again=input("Do you wanna play again (Y/N)\n").upper()
                if again=="Y":
                    
                    isthatrue=True
                    break
                else:
                    print(f"Player1 score: {player1} Player2 score: {player2}")
                    if player1>player2:
                        print("Player1 win")
                    elif player1==player2:
                        print("Draw")
                    else:
                        print("Player2 win")
                    print("Game Over")
                    isthatrue=False
                    break
            else:
                print("Please just enter letters")

    return ""



def osuruk():
    gr=True
    score=0
    while (gr):
        sayi=input("Select difficult 1-Easy 2-Medium 3-Hard\n")
        if sayi=="1":
            fruit = ["kiwi", "plum", "lime", "guava", "apricot", "dates", "papaw", "pomme", "prune", 
            "peach", "berry", "mango", "fig", "olive", "melon", "lychee", "apple", 
            "pear", "grape"]
            animal= ["dog", "cat", "bird", "fish", "frog", "duck", "swan", "bear", "lion", "deer",
            "koala", "mouse", "snake", "zebra", "panda", "shark", "whale", "hippo",
            "horse", "tiger", "goose", "sheep", "goat", "puppy", "kitty", "chimp"]
            nature=["sun", "moon", "star", "sky", "rain", "snow", "wind"]
            category=[fruit,animal,nature]
            category_name=["fruit","animal","nature"]
            sayi56=random.randint(0,2)
            randcat=category[sayi56]
            randcatname= category_name[sayi56]
            randword=random.choice(randcat)
            word=randword.lower()
            score=500
            # print(f"kelime {randcatname} ile alakalı")
            gr=False
            # return randword.lower()
        elif sayi=="2":
            items = ["Chair", "Table", "Lamp", "Bookshelf", "Television", "Sofa", "Refrigerator", "Microwave", "Computer", "Keyboard", "Clock", "Camera", "Painting", "Mirror", "Cushion", "Curtains", "Pillow", "Blender", "Vacuum", "Umbrella"]
            cities = ["New York", "Paris", "Tokyo", "London", "Rome", "Berlin", "Sydney", "Istanbul", "Rio de Janeiro", "Cairo", "Dubai", "Mumbai", "Moscow", "Toronto", "Los Angeles", "Barcelona", "Beijing", "Copenhagen", "Lisbon","Cape Town","Antalya","Siirt"]
            nature=["Mountain", "River", "Forest", "Rainbow", "Ocean","Desert", "Waterfall", "Valley", "Meadow", "Canyon", "Island"]
            category=[items,cities]
            category_name=["items","cities"]
            sayi56=random.randint(0,1)
            randcat=category[sayi56]
            randcatname= category_name[sayi56]
            randword=random.choice(randcat)
            score=1000
            # print(f"kelime {randcatname} ile alakalı")
            gr=False
            word=randword.lower()
            # return randword.lower()
            
        elif sayi=="3":
            disease = ["Idiopathic Hypersomnia", "Labyrinthitis", "Granulomatosis with Polyangiitis", "Pseudotumor Cerebri", "Ehlers-Danlos Syndrome", "Myasthenia Gravis", "Chronic Fatigue Syndrome", "Fibrodysplasia Ossificans Progressiva", "Cushing's Disease", "Moyamoya Disease", "Dercum's Disease", "Polyarteritis Nodosa", "Narcolepsy", "Polymyositis", "Trigeminal Neuralgia", "Wegener's Granulomatosis", "Buerger's Disease", "Kawasaki Disease",]
            medical_equipment = [
            "stethoscope", "endoscope", "electrode", "catheter", "lancet", "hemostat", 
            "prosthesis", "spectroscope", "otoscope", "manometer", "sphygmomanometer", 
            "ophthalmoscope", "calipers", "otoscope", "syringe", "suture", "scalpel", 
            "forceps", "tweezers", "tourniquet"]
            category=[disease, medical_equipment]
            category_name=["disease","medical equitment"]
            sayi56=random.randint(0,1)
            randcat=category[sayi56]
            randcatname= category_name[sayi56]
            randword=random.choice(randcat)
            score=1500
            # print(f"kelime {randcatname} ile alakalı")
            gr=False
            word=randword.lower()
            # return randword.lower()
        else:
            print("PLEASE ENTER 1, 2 OR 3\n")
    bluword=[]
    hint_hak=2
    realword=[]
    guessed_letters=[]
    guessed=False
    
    tries=6
    for i in word:
        realword.append(i)
    for i in range(len(word)):
        i=word[i]
        
        if i==" ":
            i="/"
            bluword.append(i)
        elif(i=="'"):
            i="'"
            bluword.append(i)
        else:
            i="_"
            bluword.append(i)
    print("\n")
    print(bluword)
    print(f"Kelime bu kategoriden {randcatname}")
    
    while (not guessed and tries>0) or ("_" not in bluword) :
        print(print_hangman(tries))
        guess=input(f"Please guess a letter and press 1 to take hint you have {hint_hak} \n").lower()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("Bunu ztn denemişsin dalga mı geçion")
            elif guess not in word:
                print(guess,"Kelime de bu harf yok")
                print(bluword)
                guessed_letters.append(guess)
                tries-=1
                score-=100
            elif guess =="" :
                print("Lütfen bir değer girin")
            else:
                print("Bu harf kelimede var")
                guessed_letters.append(guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    bluword[index]=guess
                
                if "_" not in bluword :
                    print(bluword)
                    print("BRAVO KAZANDIN")
                    return score
                print(bluword)
        elif(guess=="1" or guess==1)and hint_hak>0:
            score-=100
            hebele=True
            hint_hak-=1
            while hebele:
                hint=random.choice(realword)
                if hint in guessed_letters:
                    continue
                elif hint in bluword:
                    continue
                else:
                    hebele=False
                    for i,letter in enumerate(word):
                        if hint==letter:
                            index=i
                            break
                    bluword[i]=hint
                    print(bluword)
        elif hint_hak<=0:
            print("You have no more hint hakkı")
    if ("_" not in  bluword):
        print(bluword)
        print("BRAVO KAZANDIN")
        return score
    else:
        print_hangman(tries)
        score=0
        print(f"You lost your word is {realword}")
                
    return score
system("clear")

print("Welcome the Hangman game")
tr=True
while(tr):
    decision=input("1-Singleplayer 2-Co-op\n")
    if decision=="1":
        
        print(osuruk())
        tr=False
    elif decision=="2":
        print(co_op())
        tr =False
    else:
        print("PLEASE JUST ENTER 1 OR 2\n")