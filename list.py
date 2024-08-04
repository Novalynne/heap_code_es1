
# lista concatenata e ordinata

class ListNode:
    # costruttore nodo
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    # costruttore lista
    def __init__(self):
        self.head = None

    # metodo per inserire un elemento in una lista
    def insert(self, key):
        new_node = ListNode(key)
        new_node.next = self.head
        self.head = new_node

    # metodo per cercare un elemento nella lista
    def search(self, key):
        current = self.head  # parto dalla testa della lista
        found = False
        while current is not None:  # scorro la lista fino a che non trovo key o arrivo alla coda della lista
            if current.key == key:
                found = True
                print("Key found")
            current = current.next
        return found

    # metodo per stampare la lista
    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.key, end=" -> ")
            current = current.next
        print("None")

    #metodo di cancellare un elemento nella lista odinata
    def delete(self, key):
        if self.head is None: #se la lista è vuota non ho niente da cancellare
            return
        if self.head.key == key: #se la testa è il nodo che devo eliminare
            self.head = self.head.next #rimuovo la testa spostando il puntatore al prossimo nodo
            return
        current = self.head
        while current.next is not None and current.next.key != key: # cerco dentro la lista scorrendo
            current = current.next #current è il nodo precedente a quello che sto ispezionando, esco dal while con current.next che è il mio nodo da eliminare
        if current.next is not None: #se il nodo da eliminare esiste
            print("Key Succefully deleted")
            current.next = current.next.next #sostituisco il nodo da eliminare con il suo prossimo
        else:
            print("Key not found")
            return

    # metodo per estrarre il minore dalla lista non ordinata
    def extract_min(self):
        if self.head is None:
            return None  # Lista vuota

        smallest = self.head
        smallest_prev = None

        current = self.head.next
        prev = self.head

        while current is not None:
            if current.key < smallest.key:
                smallest = current
                smallest_prev = prev
            prev = current
            current = current.next
        if smallest_prev is None:
            self.head = smallest.next
        else:
            smallest_prev.next = smallest.next
        print(smallest.key)
        return smallest.key





class SortedLinkedList(LinkedList):

    # metodo per inserire un elemento nella lista ordinata
    def insert(self, key):
        new_node = ListNode(key)
        if self.head is None or self.head.key >= key:  #fin quando vengono inseriti numeri minori della testa o la lista è vuota
            new_node.next = self.head #nodo messo in cima alla lista
            self.head = new_node #il nuovo nodo diventa la testa
        else:
            current = self.head
            while current.next is not None and current.next.key < key: #scorro la lista (ordinata grazie all'if sopra) fino a che non trovo il suo posto giusto
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # metodo per estrarre il minore dalla lista ordinata
    def extract_min(self):
        root = self.head
        self.head = self.head.next
        return root.key
