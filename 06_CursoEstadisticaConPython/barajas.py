import random
import collections

PALOS = ["espada","corazon","rombo","trebol"]
VALORES = ["as","2","3","4","5","6","7","8","9","10","jota","reina","rey"]

def createBaraja():
    barajas=[]
    for p in PALOS:
        for v in VALORES:
            barajas.append((p,v))
    return barajas

def obtenerMano(barajas, sizeHand):
    # Sin reemplazo
    return random.sample(barajas,sizeHand)

def main(sizeHand, n_runSimulation):
    barajas=createBaraja()
    manos=[]
    for _ in range(n_runSimulation):
        manos.append(obtenerMano(barajas,sizeHand))
    pares=0
    for mano in manos:
        val=[]
        for c in mano:
            val.append(c[1])
        counter = dict(collections.Counter(val))
        #print(counter)
        for c in counter.values():
            if c==2:
                pares+=1
                break
    pbb_par = pares/n_runSimulation
    print(f"La pbb de encontrar 1 par en una mano de size {sizeHand} es {pbb_par}")

if __name__ == '__main__':
    n = int(input("Num barajas por mano: "))
    m = int(input("Num experimentos: "))
    main(n,m)