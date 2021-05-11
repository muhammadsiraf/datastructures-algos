array = [12039,9012,5423,4534,4343,3934,453,212,123,123,123,90,34,12,5,5,4,3,2,2,1]
array2 = [1,2,2,3,3,4222,1233,22,34,566,12222,3245,122,34,34,90,83,43,2,2,1,532,3,1]


def buble_sorting(data):
    loop=True
    jum=0
    while loop:
        maks = None
        loop = False
        for i in range(0, len(data)):
            if maks == None:
                maks = data[i]
            if maks > data[i]:
                data[i-1] = data[i]
                data[i]=maks
                loop = True
            if maks < data[i]:
                maks = data[i]
            jum+=1
            print(jum)
    return data
                
def select_sort(data):
    for i in range(0,len(data)):
        # if i == 0:
        j_at=0
        mins = data[i]
        # print(data[i])
        for j in range(i+1, len(data)):
            # print(j)
            if mins > data[j]:
                # print(mins)
                mins = data[j]
                j_at=j
            
        print("j at: ", j_at)
        print("i: ", i)
        print("data i ", data[i])
        print("data j ", data[j_at])
        
        data[j_at]=data[i]
        data[i]=mins
        
        print("sudah data i", data[i])
        print("sudah data j", data[j_at])
    return data
        
def sorting_select(data):
    for i in range(len(data)):
        mins = i
        
        for j in range(i+1, len(data)):
            if data[j]<data[mins]:
                mins = j
        
        if mins != i:
            temp = data[i]
            data[i]=data[mins]
            data[mins]=temp
                
    return data
# sorted = buble_sorting(array)

def bubble_sort(data):
    run = True
    while run:
        maks = None
        run = False
        for i in range(0, len(data)):
            if i == 0:
                maks = data[i]
            if maks > data[i]:
                data[i-1] = data[i]
                data[i] = maks
                run = True
            if maks < data[i]:
                maks = data[i]
    
    return data

def select_sort(data):
    for i in range(len(data)):
        mins = i
        for j in range(i+1, len(data)):
            if data[mins]>data[j]:
                mins = j
                
        if mins!=i:
            temp = data[mins]
            data[mins]=data[i] 
            data[i]=temp           
            
            
def select_sort2(data):
    for i in range(len(data)):
        index_min = i
        for j in range(i+1,len(data)):
            if data[index_min]>data[j]:
                index_min = j
                
        if index_min != i:
            temp = data[index_min]
            data[index_min]=data[i]
            data[i]=temp
            
    return data

def boolean_sort(data):
    flag=True
    
    while flag:
        flag=False
        maks = None
        for i in range(0, len(data)):
            if i == 0:
                maks = data[i]
            elif data[i]<maks:
                data[i-1] = data[i]
                data[i] = maks
                flag = True
            elif data[i]>maks:
                maks = data[i]
    return data


def insertion_sort(data):
    # flag = None
    for i in range(1, len(data)):
        temp = data[i]
        j = i-1
        
        while j>=0 and temp < data[j]:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1]=temp

    return data


def insertion_sort2(data):
    for i in range(1, len(data)):
        
        temp = data[i]
        j = i-1
        while j>=0 and temp<data[j]:
            data[j+1]=data[j]
            j-=1
        
        data[j+1] = temp
        
    return data


def insertion_sort3(data):
    
    for i in range(1, len(data)):
        temp = data[i]
        j = i-1
        
        while j>=0 and temp<data[j]:
            data[j+1] = data[j]
            j -= 1
            
        data[j+1]=temp
        
    return data


def mergeSort(arr):
    # arr = data
    if len(arr)>1:
        # print("hai")
        mid = int(len(arr)/2)
        
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
                
            elif R[j] <= L[i]:
                arr[k] = R[j]
                j+=1
                
            k+=1
            
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
            
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
            
    return arr


def mergeSort2(data):
    if len(data) > 1:
        
        mid = len(data)//2
        L = data[:mid]
        R = data[mid:]
        
        mergeSort2(L)
        mergeSort2(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] <  R[j]:
                data[k] = L[i]
                i+=1
            else:
                data[k] = R[j]
                j+=1
            k+=1
            
        while i < len(L):
            data[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            data[k]=R[j]
            j+=1
            k+=1
            

sorted2 = mergeSort2(array)
print(array)