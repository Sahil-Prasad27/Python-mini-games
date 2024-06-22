#game to guess the word which is hidden

max =5
tries=0

word = "Country" #change the word as you need 

word = word.lower()


while True:
    key = input("Guess the letter: ")
    if key in word:
        print(key  + " cointains in the word ")
        word = word.replace(key,"")
        print(len(word))
        if(len(word)==0):
            print("You win")
            break
    else:
        print("wrong")
        tries = tries +1
        if tries >= max:
            print("you lost")
            break
        