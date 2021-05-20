import random

def throw_dice(m):
    seqThrows=[]
    for _ in range(m):
        seqThrows.append(random.choice([1,2,3,4,5,6]))
    return seqThrows

def main(n,m):
    experiments=[]
    for _ in range(n):
        experiments.append(throw_dice(m))
    pbb_1_e=[]
    contador=0
    for e in experiments:
        contador+=1
        res = 0
        for i in e:
            if i==1:
                res+=1
        pbb_1 = res/len(e)
        pbb_1_e.append(pbb_1)
        print(f"La pbb de encontrar 1 en el experimento {contador} es {pbb_1}")
    print(f"La pbb promedio de obtener 1 en cada experimento es {sum(pbb_1_e)/len(pbb_1_e)}")


if __name__ == '__main__':
    m = int(input("Num throws: "))
    n = int(input("Num experiments: "))

    main(n,m)
