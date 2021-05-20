import random
saveUserLetters=[]
def main():
    word="HolaSoyUnaMachine"
    print("\nUsuario, adivina en la letra que yo la machine he seleccionado de la frase: ")
    print(">>> ",word, " <<<")
    letter=input("introduce letra: ").lower()
    selectLetter = random.choice(word.lower())
    intentos=1
    numIntentosMax=4
    win=True
    saveUserLetters.append(letter)
    repeatUser=False
    while(letter!=selectLetter):
        if numIntentosMax <= intentos:
            win=False
            break
        if not repeatUser:
            print("Invalido!")
        print("\nSelecciona otra letra, de la siguiente frase: ")
        print("TIP: te borramos la que nos dijiste antes")
        word = word.replace(letter.lower(),"").replace(letter.upper(),"")
        print(">>> ",word, " <<<")
        letter=input("introduce letra: ").lower()
        if letter in saveUserLetters and intentos!=1:
            print("Usuario, esta la seleccionaste!, te damos otra oportunidad")
            repeatUser=True
            continue
        saveUserLetters.append(letter)
        intentos+=1
        repeatUser=False
    print("\nletras: ", saveUserLetters)
    print("-"*60)
    if win:
        print("Has adivinado, felicidades!!")
    else:
        print("Has perdido, alcanzaste num de intetos max")
        print("La letra que seleccione, yo la machine es: ", selectLetter)
    print("Resumen de usuario: \n1.Num de intentos: ", intentos, "\n2.Num Intentos Max: ", numIntentosMax)
if __name__ == "__main__":
    main()
