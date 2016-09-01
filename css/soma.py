import os,sys
a = open('claro.csv','r')
fone = '51 9177-9814'
texto = 'Int. Regional'
texto1 = 'Claro-Fixo'
texto2 = 'Claro-Outras Op.'
texto3 = 'Claro-Claro'
texto4 = 'Pacote Internet Ilimitado'
texto5 = 'Assinatura Plano Sob Medida'
texto6 = 'Tarifa Zero'
texto7 = 'Serviço Claro DDD Nac'
texto8 = 'Torpedos'
texto9 = 'Int. Nacional'
texto10 = 'À Cobrar'
texto11 = 'Secretária Claro'
texto12 = 'Outros Serviços Telecom'

soma = 0.0
valor1 = 0.0
valor2 = 0.0
soma1 = 0.0
soma2 = 0.0

for i in a.readlines():
        if(i.split(';')[0]==fone):
                
                if(texto in i.split(';')[1] or texto1 in i.split(';')[1] or texto2 in i.split(';')[1] or texto3 in i.split(';')[1] or texto9 in i.split(';')[1] or texto10 in i.split(';')[1] or texto12 in i.split(';')[1] or texto11 in i.split(';')[1]):
                        valor1 = i.split(';')[9].replace(',','.')
                        soma1 = soma1 + float(valor1)
                        
                        if(soma1 < 18.66):
                                soma1 = 18.66
                                print(soma1)
                if(texto4 in i.split(';')[1] or texto5 in i.split(';')[1] or texto6 in i.split(';')[1] or texto7 in i.split(';')[1] or texto8 in i.split(';')[1]):
                        valor2 = i.split(';')[9].replace(',','.')
                        soma2 = soma2 + float(valor2)
                        
                soma = soma1 + soma2 + 12.00
                
a.close()


print(soma) 

