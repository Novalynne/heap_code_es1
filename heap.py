class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    # metodo che mi permette di inserire un elemento nell'heap
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    # metodo che mi estrae l'elemento minimo dell'heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop() #funzione pop mi restituisce l'ultimo elemento dell'heap
        self.min_heapify(0)
        print(root)
        return root


    # metodo che mi permette di risalire l'albero correggendo le posizioni degli elementi man mano
    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # metodo che mi permette di scendere l'albero correggendo le posizioni degli elementi man mano
    def min_heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    # metodo che mi permette di cercare un elemento nell'heap
    def search(self, key):
        return self.search_recursive(key, 0) #parto a cercare dalla radice

    def search_recursive(self, key, index):
        if index >= len(self.heap):
            return False
        if self.heap[index] == key:
            print("Key found at index: " + str(index))
            return True
        if key < self.heap[index]: #se key è più piccola dell'index vuol dire che doveva essere tra i padri di index che però ho già controllato, quindi non c'è
            return False
        left = self.left_child(index)
        right = self.right_child(index)
        return self.search_recursive(key, left) or self.search_recursive(key, right) #controllo nei figli

    # metodo per cancellare un elemento dall'heap
    def delete(self, key):
        if self.search(key)==True:
            index = self.heap.index(key) #mi restituisce la posizione di key

            # muovo l'ultimo elemento nella posizione di quello eliminato
            last_element = self.heap.pop()
            if index < len(self.heap):
                self.heap[index] = last_element
                parent_index = self.parent(index)

                # risistemo l'heap
                if index > 0 and self.heap[index] < self.heap[parent_index]:
                    self.heapify_up(index)
                else:
                    self.min_heapify(index)
            print("Key successfully deleted")
            return True
        else:
            print("Key not found")
            return False