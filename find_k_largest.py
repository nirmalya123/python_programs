# Find the k largest numbers in an array of n numbers.
class heap:
    def __init__(self):
        self.arr = []
        self.size = 0

    
    def get_smaller_child(self,i,j):
        parent = i
        child = parent * 2 + 1
        if child + 1 <= j and self.arr[child] > self.arr[child + 1]:
            child = child + 1
        if child > j:
            return -1
        return child

    def insert_min_heap1(self,element):
        child = self.size
        parent = (child - 1) // 2
        while child > 0 and element <= self.arr[parent]:
            self.arr[child] = self.arr[parent]
            child = parent
            parent = (child - 1) //2
        self.arr[child] = element
        self.size = self.size + 1

    def insert_min_heap2(self, element):
        parent = 0
        child = self.get_smaller_child(parent, self.size - 1)
        while child >= 0 and element >= self.arr[child]:
            self.arr[parent] = self.arr[child]
            parent = child
            child = self.get_smaller_child(parent,self.size - 1)
        self.arr[parent] = element

    def find_k_largest(self,arr,N,k):
        self.arr = [0 for i in range(k)]
        for x in arr[:k]:
            self.insert_min_heap1(x)
        for x in arr[k:]:
            if x >= self.arr[0]:
                self.insert_min_heap2(x)
        return self.arr
    
h1 = heap()
ar = [10,6,5,20,15,30,40,1,100,1000]
print(len(ar))
print(h1.find_k_largest(ar,len(ar),6))
print(sorted(ar))
print(sorted(h1.arr))