class LinearSearch:
    def __init__(self,arr) -> None:
        self.arr = arr

    def linear_search(self,element):
        i = 0
        index = None
        while i < len(self.arr):
            if self.arr[i] == element:
                index = i
                break
            i += 1
        return f"{element} not found" if index == None else index
    
l = LinearSearch([1,10,2,7,5])
index_present = l.linear_search(2)
index_not_present = l.linear_search(8)
print(index_present)
print(index_not_present)
