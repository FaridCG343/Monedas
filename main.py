comV = []
dicM = {}
mcm = {}
m = [10, 15, 20, 25, 50, 100]
ValorB = 100


def agregarMcM():
    for x in comV:
        aux = []
        for cn in x:
            aux.append(cn)
        for y in mcm:
            for a in mcm[y]:
                cvqc = y // a
                if aux.count(a) >= cvqc:
                    ltemp = aux.copy()
                    for b in range(cvqc):
                        ltemp.remove(a)
                    for c in mcm[y]:
                        ltemp2 = ltemp.copy()
                        if c != a:
                            for d in range(y // c):
                                ltemp2.append(c)
                            ltemp2.sort(reverse=True)
                            if ltemp2 in comV:
                                pass
                            else:
                                comV.append(ltemp2.copy())


def maximo_comun_divisor(a, b):
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


def crearMcM(m1):
    for x in range(len(m1)-1):
        for y in range(x+1, len(m1)):
            mcmtemp = int(minimo_comun_multiplo(m1[x], m1[y]))
            if mcmtemp <= ValorB:
                if mcmtemp in m1:
                    pass
                else:
                    z = mcm.keys()
                    if mcmtemp in z:
                        au = {0}
                        au.update(mcm[mcmtemp])
                        au.add(m1[x])
                        au.add(m1[y])
                        au.remove(0)
                        mcm[mcmtemp] = au
                    else:
                        mcm[mcmtemp] = {m1[x], m1[y]}


def agregar(temporal):
    settemp = {0}
    for a in temporal:
        settemp.add(a)
    settemp.remove(0)
    for sus in settemp:
        if sus in dicM.keys():
            temporal.remove(sus)
            for sus2 in dicM[sus]:
                temporal2 = temporal.copy()
                for sus3 in sus2:
                    temporal2.append(sus3)
                temporal2.sort(reverse=True)
                if temporal2 in comV:
                    pass
                else:
                    suma = 0
                    for sux in temporal2:
                        suma += sux
                    if suma == ValorB:
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
                su = 0
                for x in comV[a]:
                    su += x
                if su != ValorB:
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
                if len(comM) == 0:
                    pass
                else:
                    for a in range(len(comM)):
                        if len(comM[a]) == 1:
                            comM.pop(a)
                            i = True
                            break
            if not comM:
                pass
            else:
                dicM[moneda[x]] = comM
            del comM


moneda = [x for x in m if 0 < x <= ValorB]
moneda.sort(reverse=True)
crearMcM(moneda)
crearDicM(moneda)
print(dicM)
print(mcm)
crearcomV(moneda)
agregarMcM()
i = 1
for x in comV:
    suma = 0
    for y in x:
        suma += y
    print(i, suma, x)
    i += 1
