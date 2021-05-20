def divisors(num):
    divisor=[]
    for i in range(1, num + 1):
        if num%i==0:
            divisor.append(i)
    return divisor

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("end")
    except ValueError:
        print("Debes ingresar un num")

if __name__ == '__main__':
    run()