area=float(input("insira o tamanho da area em m2 que vc quer cobrir:"))
tinta1lata=(18*3)
import math
latas= math.ceil(area/tinta1lata)
print(f"serao necessarias {latas} latas")
preço=(latas*80)
print(f"as {latas} irao custar R$ {preço}")

