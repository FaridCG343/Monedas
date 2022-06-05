import math

comV = []
dicM = {}
m = [8, 6, 7]
ValorB = 95


def combinacion(monedas, num1=ValorB, comM=[]):
    if len(monedas) > 0:
        if len(monedas) == 1:
            for x in range(math.floor(num1 / monedas[0]), 0, -1):
                if (num1 - (x * monedas[0])) == 0:
                    for y in range(x, 0, -1):
                        comM.append(monedas[0])
                    comV.append(comM.copy())
                    comM.clear()
        else:
            for x in range(math.floor(num1 / monedas[0]), 0, -1):
                if (num1 - (x * monedas[0])) == 0:
                    for y in range(x, 0, -1):
                        comM.append(monedas[0])
                    comV.append(comM.copy())
                    comM.clear()
                else:
                    mtemp = monedas.copy()
                    mtemp.remove(monedas[0])
                    for y in range(x, 0, -1):
                        comM.append(monedas[0])
                    print("ComM",comM)
                    num1-=(monedas[0]*x)
                    mtemp2=monedas.copy()
                    for a in range(0,len(mtemp2)):
                        if monedas[a] <= num1:
                            combinacion(monedas=mtemp2.copy(), num1=num1, comM=comM.copy())
                            break
                        else:
                            mtemp2.remove(monedas[a])
                comM.clear()


moneda = [x for x in m if ValorB >= x > 0]
moneda.sort(reverse=True)
while len(moneda)>0:
    combinacion(monedas=moneda)
    moneda.pop(0)
    print(moneda)
for x in comV:
    suma=0
    for y in x:
        suma+=y
    print(suma,x)
