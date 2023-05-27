class BinarySearch:
    """
    The passed array shoud be sorted
    """
    def __init__(self,arr) -> None:
        self.arr = arr
    
    def binary_search(self,element):
        index = None
        low , high = 0 , len(self.arr)-1
        while low <= high:
            mid = (low+high)//2
            if self.arr[mid] == element:
                index = mid
                break
            elif self.arr[mid] < element:
                low = mid+1
            elif self.arr[mid] > element:
                high = mid-1
        return f"{element} not found" if index == None else index
    
    def binary_search_rec(self,low,high,element):
        index = None
        mid = (low+high)//2
        if low > high:
            return
        if self.arr[mid] == element:
            index = mid
        elif self.arr[mid] < element:
            index = self.binary_search_rec(mid+1,high,element)
        elif self.arr[mid] > element:
            index = self.binary_search_rec(low,mid-1,element)
        return f"{element} not found" if index == None else index

b = BinarySearch([10,20,30,40,50]) 
print(b.binary_search(40))
print(b.binary_search(20))
print(b.binary_search(120))
print(b.binary_search_rec(0,4,20))
        