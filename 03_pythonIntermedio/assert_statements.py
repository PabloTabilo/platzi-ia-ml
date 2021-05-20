def divisors(num):
    divisor=[]
    for i in range(1, num + 1):
        if num%i==0:
            divisor.append(i)
    return divisor

def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un num"
    print(divisors(int(num)))
    print("end")
    print("Debes ingresar un num")

if __name__ == '__main__':
    run()