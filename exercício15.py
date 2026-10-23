ganho_hr=float(input("insira seu ganho por hora:"))
hora=int(input("insira a quantidade de horas que voce trabalha em um mes:"))
salarioBruto=(ganho_hr*hora)
print(f"salario bruto igual a: R$ {salarioBruto}")

ir=(salarioBruto*(0.11))
print(f"seu imposto de renda ficou igual a: R$ {ir}")

inss=(salarioBruto*(0.08))
print(f"seu inss ficou igual a: R$ {inss}")

sindicato=(salarioBruto*(0.05))
print(f"o sindicato vai descontar: R$ {sindicato}")

salarioLiquido=(salarioBruto-ir-inss-sindicato)
print(f"com todos os descontos o seu salario liquido ficou igaul a: R$ {salarioLiquido}")