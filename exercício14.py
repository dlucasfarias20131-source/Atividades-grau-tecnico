pesototal=float(input("insira o peso total de seus peixes:"))

if pesototal > 50:
    execesso= (pesototal-50)
    multa= (execesso*4)
    print(f"excedeu {execesso} -  multa sera de R$ {multa}")
   
else:
    print("nao excedeu, eita bixo sabido")
