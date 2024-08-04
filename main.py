from heap import MinHeap
from list import SortedLinkedList
from list import LinkedList
import matplotlib.pyplot as plt
from tabulate import tabulate
import random
import time



# TEST MIN HEAP
def t_insert_mh(num):
    mh = MinHeap()
    start_time = time.time()
    for i in range(num):
        mh.insert(random.randint(1,num))
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_search_mh(num):
    key = random.randint(1,num)
    mh = MinHeap()
    for i in range(num):
        mh.insert(random.randint(1,num))
    start_time = time.time()
    mh.search(key)
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_delete_mh(num):
    key = random.randint(1,num)
    mh = MinHeap()
    for i in range(num):
        mh.insert(random.randint(1,num))
    start_time = time.time()
    mh.delete(key)
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_min_mh(num):
    mh = MinHeap()
    for i in range(num):
        mh.insert(random.randint(1,num))
    start_time = time.time()
    mh.extract_min()
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

# TEST LISTE CONCATENATE

def t_insert_ll(num):
    ll = LinkedList()
    start_time = time.time()
    for i in range(num):
        ll.insert(random.randint(1,num))
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_search_ll(num):
    key = random.randint(1,num)
    ll = LinkedList()
    for i in range(num): #c
        ll.insert(random.randint(1,num))
    start_time = time.time()
    ll.search(key)
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_delete_ll(num):
    key = random.randint(1,num)
    ll = LinkedList()
    for i in range(num):
        ll.insert(random.randint(1,num))
    start_time = time.time()
    ll.delete(key)
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_min_ll(num):
    ll = LinkedList()
    for i in range(num):  # creo il mio mh
        ll.insert(random.randint(1,num))
    start_time = time.time()
    ll.extract_min()
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

# TEST LISTE CONCATENATE ORDINATE

def t_insert_sll(num):
    sll = SortedLinkedList()
    start_time = time.time()
    for i in range(num):
        sll.insert(random.randint(1,num))
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_search_sll(num):
    key = random.randint(1,num)
    sll = SortedLinkedList()
    for i in range(num):
        sll.insert(random.randint(1,num))
    start_time = time.time()
    sll.search(key)
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_delete_sll(num):
    key = random.randint(1,num)
    sll = SortedLinkedList()
    for i in range(num):
        sll.insert(random.randint(1,num))
    start_time = time.time()
    sll.delete(key)
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

def t_min_sll(num):
    sll = SortedLinkedList()
    for i in range(num):
        sll.insert(random.randint(1,num))
    start_time = time.time()
    sll.extract_min()
    end_time = time.time()
    test_time = end_time - start_time
    return test_time

time_test=0
ll_time_insert = []
sll_time_insert = []
mh_time_insert = []
ll_time_search = []
sll_time_search = []
mh_time_search = []
ll_time_delete = []
sll_time_delete = []
mh_time_delete = []
ll_time_min = []
sll_time_min = []
mh_time_min = []
N = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000]

for num in N:
    time_test = 0
    for i in range(100):
        time_test += t_insert_mh(num)
    mh_time_insert.append(time_test/100)
    time_test = 0

    for i in range(100):
        time_test += t_search_mh(num)
    mh_time_search.append(time_test/100)
    time_test = 0

    for i in range(100):
        time_test += t_delete_mh(num)
    mh_time_delete.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_min_mh(num)
    mh_time_min.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_insert_ll(num)
    ll_time_insert.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_search_ll(num)
    ll_time_search.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_delete_ll(num)
    ll_time_delete.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_min_ll(num)
    ll_time_min.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_insert_sll(num)
    sll_time_insert.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_search_sll(num)
    sll_time_search.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_delete_sll(num)
    sll_time_delete.append(time_test / 100)
    time_test = 0

    for i in range(100):
        time_test += t_min_sll(num)
    sll_time_min.append(time_test / 100)
    time_test = 0


# grafico confronto tra le 3 strutture

plt.plot(N, mh_time_insert, label='Min Heap')
plt.plot(N, ll_time_insert, label='Lista Concatenata')
plt.plot(N, sll_time_insert, label='Lista Concatenata Ordinata')
plt.xlabel('Numero di elementi')
plt.ylabel('Tempo di esecuzione (secondi)')
plt.title('Andamento temporale durante inserimento')
plt.legend()
plt.show()

plt.plot(N, mh_time_search, label='Min Heap')
plt.plot(N, ll_time_search, label='Lista Concatenata')
plt.plot(N, sll_time_search, label='Lista Concatenata Ordinata')
plt.xlabel('Numero di elementi')
plt.ylabel('Tempo di esecuzione (secondi)')
plt.title('Andamento temporale durante la ricerca')
plt.legend()
plt.show()

plt.plot(N, mh_time_delete, label='Min Heap')
plt.plot(N, ll_time_delete, label='Lista Concatenata')
plt.plot(N, sll_time_delete, label='Lista Concatenata Ordinata')
plt.xlabel('Numero di elementi')
plt.ylabel('Tempo di esecuzione (secondi)')
plt.title('Andamento temporale durante la cancellazione')
plt.legend()
plt.show()

plt.plot(N, mh_time_min, label='Min Heap')
plt.plot(N, ll_time_min, label='Lista Concatenata')
plt.plot(N, sll_time_min, label='Lista Concatenata Ordinata')
plt.xlabel('Numero di elementi')
plt.ylabel('Tempo di esecuzione (secondi)')
plt.title('Andamento temporale durante la estrazione del minore')
plt.legend()
plt.show()

# creazione tabelle in latex

data_insert = list(zip(N, mh_time_insert, ll_time_insert, sll_time_insert))
data_search = list(zip(N, mh_time_search, ll_time_search, sll_time_search))
data_delete = list(zip(N, mh_time_delete, ll_time_delete, sll_time_delete))
data_min = list(zip(N, mh_time_min, ll_time_min, sll_time_min))

headers = ["Dimensioni", "Min Heap", "Lista Concatenata", "Lista Concatenata Ordinata",]
table_insert = tabulate(data_insert, headers=headers, tablefmt="latex")
print(table_insert)
table_search = tabulate(data_search, headers=headers, tablefmt="latex")
print(table_search)
table_delete = tabulate(data_delete, headers=headers, tablefmt="latex")
print(table_delete)
table_min = tabulate(data_min, headers=headers, tablefmt="latex")
print(table_min)
