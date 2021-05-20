import random
def gen():
    your_pass=""
    for i in range(15):
        notMayus=random.random()
        cnum = chr(random.randint(48, 57))
        cletters = chr(random.randint(97, 122))
        csymb = chr(random.randint(33, 38))
        csymb2 = chr(random.randint(60, 64))
        if notMayus>.5:
            cletters=cletters.upper()
        your_pass+=random.choice(cletters+cnum+csymb+csymb2)
    return your_pass
def main():
    print("Contraseña generada: ", gen())
if __name__ == "__main__":
    main()