import time
import timeit


def alguma_funcao():
    for i in range(1, 5):
        time.sleep(1)

inicio = timeit.default_timer()
alguma_funcao()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))