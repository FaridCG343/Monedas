comV = []
dicM = {}
m = [1,5,17]
ValorB = 20


def agregar(temporal):
    settemp={0}
    for a in temporal:
        settemp.add(a)
    for sus in settemp:
        if sus in dicM.keys():
            temporal.remove(sus)
            for sus2 in dicM[sus]:
                temporal2=temporal.copy()
                for sus3 in sus2:
                    temporal2.append(sus3)
                temporal2.sort(reverse=True)
                if temporal2 in comV:
                    pass
                else:
                    suma=0
                    for sum in temporal2:
                        suma+=sum
                    if suma==ValorB:
                        comV.append(temporal2.copy())
                agregar(temporal2.copy())


def crearcomV(monedas):
    for i in range(len(monedas)):
        valor = ValorB
        cmb = []
        for y in range(i, len(monedas)):
            xd = True
            valor2 = monedas[y]
            while xd:
                if valor >= valor2:
                    cmb.append(valor2)
                    valor = valor - valor2
                else:
                    xd = False
        else:
            if valor == 0:
                if cmb in comV:
                    pass
                else:
                    comV.append(cmb)
                agregar(cmb.copy())
                del cmb
    else:
        i = True
        while i:
            for a in range(len(comV)):
                i = False
                if len(comV[a]) == 1:
                    comV.pop(a)
                    i = True
                    break


def crearDicM(monedas):
    for x in (range((len(monedas) - 1))):
        comM = []
        for i in range(1, len(monedas)):
            valor = monedas[x]
            cmb = []
            for y in range(i, len(monedas)):
                xd = True
                valor2 = monedas[y]
                while xd:
                    if valor >= valor2:
                        cmb.append(valor2)
                        valor = valor - valor2

                    else:
                        xd = False
            else:
                if valor == 0:
                    comM.append(cmb)
                    del cmb
        else:
            i = True
            while i:
                i = False
                if len(comM)==0:
                    pass
                else:
                    for a in range(len(comM)):
                        if len(comM[a]) == 1:
                            comM.pop(a)
                            i = True
                            break
            if comM==[]:
                pass
            else:
                dicM[moneda[x]] = comM
            del comM


moneda = [x for x in m if x <= ValorB]
moneda.sort(reverse=True)
crearDicM(moneda)
print(dicM)
crearcomV(moneda)
i=1
for x in comV:
    print(i, x)
    i+=1
