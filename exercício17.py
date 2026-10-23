tamanho_do_arquivo_mB=float(input("insira o valor do tamanho do arquivo para download em MB:"))
mbps=float(input("insira a velocidade da conexao de sua internet:"))
tamanho_do_arqueivo_mb=(tamanho_do_arquivo_mB*8)#deve multiplicar o arquivo em Mega Bytes por 8, para transformar em mega bites e igualar as granzas. sem isso o download terminaria 8 vezes mais rapido do que a realidade.
print(f"o tamanho do arquivo em bites fica igual a: {tamanho_do_arqueivo_mb}")
segundos=(tamanho_do_arqueivo_mb/mbps)# o valor sera em segundos por que o mbps é em segundos, entao sera necessario converter para minutos.
minutos=(segundos/60)
print(f"o tempo estimado para seu download é de {minutos} minutos")