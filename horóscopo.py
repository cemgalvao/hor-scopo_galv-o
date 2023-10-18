####  ------ Projeto Horóscopo--------######

# ------------  entrada  ------------------

print('\n\n ####  ------ Projeto Horóscopo--------######\n\n')
#
dia = int(input('indique uma data começando pelo dia:\n'))
mês = int(input('indique agora número do  mês:\n'))



# ----------  processamento e saída  ---------------

import datetime

# definoinsdo data de início do ciclo do horóscopo


Aquário = datetime.date(2023,1, 20)
Peixes = datetime.date(2023,2, 19)
Áries = datetime.date(2023,3, 21)
Touro = datetime.date(2023, 4, 20)
Gêmeos = datetime.date(2023, 5 , 21)
Cancêr = datetime.date(2023, 6,22)
Leão   = datetime.date(2023, 7,23)
Virgem = datetime.date(2023,8 ,23)
Libra = datetime.date(2023, 9,23)
Escorpião = datetime.date(2023, 10,23)
Sagitário = datetime.date(2023,11,22)
Capricórnio = datetime.date(2023,12, 22)


#definiar a data escolhida
data_escolhida = datetime.date(2023,mês,dia)


# mitigando erros de datas
if data_escolhida < Aquário:
    Aquário('capricórnio')

elif mês==12 and dia>22:
    print('capricórnio')

else:
    signos = [Aquário, Peixes, Áries, Touro,Gêmeos,Cancêr,Leão,Virgem,Libra,Escorpião,Sagitário,Capricórnio]
    nome_dos_signos = ['Aquário', 'Peixes', 'Áries', 'Touro','Gêmeos','Cancêr','Leão','Virgem',
'Libra','Escorpião','Sagitário','Capricórnio']
    x =0
    while True:
        if signos[x] <= data_escolhida < signos[x+1]:
            print(f'o signo é: {nome_dos_signos[x]}')
            break
        else:
            x = x+1
