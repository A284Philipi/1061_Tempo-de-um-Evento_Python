a, b = input().split(" ")
teste = str(a)
dia_inicial = int(b)
a, b, c = input().split(" : ")
hora_inicial = int(a)
minuto_inicial = int(b)
segundo_inicial = int(c)
a, b = input().split(" ")
teste = str(a)
dia_final = int(b)
a, b, c = input().split(" : ")
hora_final = int(a)
minuto_final= int(b)
segundo_final = int(c)
dia = int(dia_final - dia_inicial)
if (segundo_final >= segundo_inicial):
    segundo = int(segundo_final - segundo_inicial)
else:
    segundo = int((60 - segundo_inicial) + segundo_final)
    minuto_inicial = minuto_inicial + 1
if (minuto_final >= minuto_inicial):
    minuto = int(minuto_final - minuto_inicial)
else:
    minuto = int((60 - minuto_inicial) + minuto_final)
    hora_inicial = hora_inicial + 1
if (hora_final >= hora_inicial):
    hora = int(hora_final - hora_inicial)
else:
    hora = int((24 - hora_inicial) + hora_final)
    dia_inicial = dia_inicial + 1
dia = int(dia_final - dia_inicial)
print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(minuto))
print("{} segundo(s)".format(segundo))