#programa simple en python
import time
def comprobarcantidades():
    if a == 0 or b == 0:
        print("ERROR: no se puede dividir entre 0")
    else:
        print(a/b)

print("-Calculadora simple de divisiones-")

a = int(input("Inserte el primer valor"))
b = int(input("Inserte el siguiente valor"))


comprobarcantidades()
time.sleep(100)


