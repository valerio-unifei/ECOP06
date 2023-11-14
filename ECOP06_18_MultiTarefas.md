# Multi Tarefas
Documentação: https://docs.python.org/3.8/library/threading.html

Fonte: https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29

Execução Concorrente: 

<img src="https://miro.medium.com/max/720/1*0_KY5zM4OlYpEdxpMqjEmQ.webp"/>

Paralelismo: 

<img src="https://miro.medium.com/max/640/1*iuM9nenj01Tv-mfQ36c_1g.webp"/>

Paralelismo concorrente: 

<img src="https://miro.medium.com/max/720/1*dNdE7O8exRHD0NKnq3eWJQ.webp"/>

Um thread é uma sequência de instruções que estão sendo executadas dentro do contexto de um processo. 
Um processo pode gerar vários threads, mas todos eles compartilharão a mesma memória.

Ao experimentar multi-threading em Python em tarefas vinculadas à CPU, 
você notará que a execução não é otimizada e pode até ficar mais lenta quando vários threads são usados. 
Normalmente, a expectativa seria que o uso de um código multi-threaded em uma máquina multi-core 
deveria aproveitar os núcleos disponíveis e, assim, aumentar o desempenho geral.

Na verdade, um processo Python não pode executar threads em paralelo, 
mas pode executá-los simultaneamente por meio de troca de contexto 
durante operações de limite de E/S.

Essa limitação é realmente aplicada pelo Python Global Interpreter Lock (GIL). 
O GIL impede que threads dentro do mesmo processo sejam executadas ao mesmo tempo.
O GIL é necessário porque o interpretador do Python não é thread-safe.

```python
import time
import threading
import multiprocessing 
import requests
from queue import Queue

def calc_square(numeros):
    for n in numeros:
        print(f'{n} ^ 2 = {n*n}')
        time.sleep(0.1)

def calc_cube(numeros):
    for n in numeros:
        print(f'{n} ^ 3 = {n*n*n}')
        time.sleep(0.1)

def atividade1(numeros):
    print('Atividade 1')
    start = time.time()

    calc_square(numeros)
    calc_cube(numeros)

    end = time.time()
    print('Execution Time: {}'.format(end-start))

def atividade2(numeros):
    print('Atividade 2')
    start = time.time()

    square_thread = threading.Thread(target=calc_square, args=(numeros,))
    cube_thread = threading.Thread(target=calc_cube, args=(numeros,))

    square_thread.start()
    cube_thread.start()

    square_thread.join()
    cube_thread.join()

    end = time.time()
    print('Execution Time: {}'.format(end-start))

def baixar(fila):
	while True:
		img_url = fila.get()

		res = requests.get(img_url, stream=True)
		filename = f"{img_url.split('/')[-1]}.jpg"

		with open(filename, 'wb') as f:
			for block in res.iter_content(1024):
				f.write(block)
		fila.task_done()
        

def atividade3(tarefas=1):
    print('Atividade 3')
    start = time.time()

    images = [
    	'https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7',
    	'https://images.unsplash.com/photo-1587620962725-abab7fe55159',
    	'https://images.unsplash.com/photo-1493119508027-2b584f234d6c',
    	'https://images.unsplash.com/photo-1482062364825-616fd23b8fc1',
    	'https://images.unsplash.com/photo-1521185496955-15097b20c5fe',
    	'https://images.unsplash.com/photo-1510915228340-29c85a43dcfe',
    ]
    fila = Queue()
    for img_url in images * 5:
        fila.put(img_url)

    for t in range(tarefas):
        worker = threading.Thread(target=baixar,args=(fila,))
        worker.daemon = True
        worker.start()

    fila.join()
    end = time.time()
    print('Execution Time: {}'.format(end-start))

def atividade4(numeros, processos=1):
    """
    ## Multi-Processamento
    Multi-Processamento é um pacote que oferece suporte a processos de desova usando uma API semelhante ao módulo threading. 
    O pacote Multi-Processamento oferece simultaneidade local e remota, 
    contornando efetivamente o GIL usando subprocessos em vez de threads. 
    Devido a isso, o módulo permite que o programador aproveite totalmente vários processadores em uma determinada máquina. 
    Ele roda em Unix e Windows.

    Documentação: https://docs.python.org/3.8/library/multiprocessing.html
    """
    print('Atividade 4')
    start = time.time()

    resp = []
    with multiprocessing.Pool(processes=processos) as pool:
        resp = pool.starmap(calc_cube,numeros)
    print(resp)

    end = time.time()
    print('Execution Time: {}'.format(end-start))


if __name__ == '__main__':
    numeros = [2, 3, 5, 8]
    #atividade1(numeros)
    #atividade2(numeros)
    #atividade3()
    atividade4(numeros)
```
