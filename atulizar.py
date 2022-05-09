from datetime import datetime
from tratamento_e_carregamento import tc

hoje = str(datetime.today())[:10]

file = open('log_atualizacao.txt','r')
data = file.read()
teste = data != hoje
print(data)


if data != hoje:
    file.close()
    file = open('log_atualizacao.txt','w')
    print("Precisa atualizar")
    tc()
    file.write(hoje)
    file.close()


