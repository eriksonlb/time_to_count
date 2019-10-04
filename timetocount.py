from time import time
from datetime import datetime 
import os 

clear = lambda: os.system('clear')
exit = lambda: os.system('exit')


def verificador(x):
    if x == 1000:
        time_elapsed = datetime.now() - start_time 
        mil = 'MIL =  (hh:mm:ss.ms) {}'.format(time_elapsed)
        return mil

    if x == 10000:
        time_elapsed = datetime.now() - start_time 
        dez_mil = 'DEZ MIL =  (hh:mm:ss.ms) {}'.format(time_elapsed)      
        return dez_mil
        
    if x == 100000:
        time_elapsed = datetime.now() - start_time 
        cem_mil = 'CEM MIL = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return cem_mil

    if x == 1000000:
        time_elapsed = datetime.now() - start_time 
        milhao = '1 MILHÃO = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return milhao

    if x == 10000000:
        time_elapsed = datetime.now() - start_time 
        dez_milhoes = 'DEZ MILHÕES = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return dez_milhoes

    if x == 100000000:
        time_elapsed = datetime.now() - start_time 
        cem_milhoes = 'CEM MILHÕES = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return cem_milhoes

    if x == 100000000:
        time_elapsed = datetime.now() - start_time 
        bilhao = '1 BILHÃO = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return bilhao
    if x == 100000000:
        time_elapsed = datetime.now() - start_time 
        dez_bilhoes = '10 BILHÕES (hh:mm:ss.ms) {}'.format(time_elapsed)
        return dez_bilhoes

    if x == 1000000000:
        time_elapsed = datetime.now() - start_time 
        cem_bilhoes = '100 BILHÕES = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return cem_bilhoes

    if x == 1000000000:
        time_elapsed = datetime.now() - start_time 
        trilhao = '1 TRILHÃO = (hh:mm:ss.ms) {}'.format(time_elapsed)
        return trilhao
 
decimais = []

start_time = datetime.now() 
for i in range(1, 1000000000001):
    if len(decimais) > 0:
        for n in decimais:
            print(n)
    print(i)
    clear()
    




