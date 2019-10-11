import time
from datetime import datetime 
import os 
# import counting

clear = lambda: os.system('clear')
exit = lambda: os.system('exit')


def verificador(x):
    if x == 1000:
        time_elapsed = datetime.now() - start_time 
        mil = 'MIL =  (hh:mm:ss.ms) {}'.format(time_elapsed)
        return mil

    elif x == 10000:
        time_elapsed = datetime.now() - start_time 
        dez_mil = 'DEZ MIL =  (hh:mm:ss.ms) {}'.format(time_elapsed)      
        return dez_mil
        
    elif x == 100000:
        time_elapsed = datetime.now() - start_time 
        cem_mil = 'CEM MIL = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return cem_mil

    elif x == 1000000:
        time_elapsed = datetime.now() - start_time 
        milhao = '1 MILHÃO = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return milhao

    elif x == 10000000:
        time_elapsed = datetime.now() - start_time 
        dez_milhoes = 'DEZ MILHÕES = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return dez_milhoes

    elif x == 100000000:
        time_elapsed = datetime.now() - start_time 
        cem_milhoes = 'CEM MILHÕES = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return cem_milhoes

    elif x == 100000000:
        time_elapsed = datetime.now() - start_time 
        bilhao = '1 BILHÃO = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return bilhao
    elif x == 100000000:
        time_elapsed = datetime.now() - start_time 
        dez_bilhoes = '10 BILHÕES (hh:mm:ss.ms) {}'.format(time_elapsed)
        return dez_bilhoes

    elif x == 1000000000:
        time_elapsed = datetime.now() - start_time 
        cem_bilhoes = '100 BILHÕES = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return cem_bilhoes

    elif x == 1000000000:
        time_elapsed = datetime.now() - start_time 
        trilhao = '1 TRILHÃO = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return trilhao
    else:
        return x
 
decimais = []

start_time = datetime.now() 
for i in range(1, 100001):
    decimais.append(verificador(i))
    # clear()

for a in decimais:
    print(a)
    time.sleep(0.05)
    




