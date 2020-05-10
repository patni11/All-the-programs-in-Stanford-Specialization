from heapq import heappush, heappop, heapify
initial_distance = 1_000_000
X = []
Vertices = {}
with open('Main.txt','r') as f:
    lines = f.readlines()
    for each in lines:
        arr = each.split()
        for i in range(1,len(arr)):
            arr[i] = eval(arr[i])
        Vertices[int(arr[0])] = {'edges':arr[1:],'source_path':initial_distance}
        
Vertices[1]["source_path"] = 0

def update_heap(heap,Vertices):
    for each in Vertices:
        if each not in X:
            heap.append(Vertices[each]["source_path"])
            heap_dict[Vertices[each]["source_path"]] = each
    heapify(heap)
    return heap,heap_dict

def greedy(each,val):
    score = each[1] + Vertices[val]["source_path"]
    if score < Vertices[each[0]]["source_path"]:
        Vertices[each[0]]["source_path"] = score


while len(X) < len(Vertices):
    heap = []
    heap_dict = {}
    heap,heap_dict = update_heap(heap,Vertices)
    val = heap_dict[heappop(heap)]
    if val not in X: 
        for each in Vertices[val]["edges"]:
            greedy(each,val)
        X.append(val)

    #Now append in X

req = [7,37,59,82,99,115,133,165,188,197]

for each in req:
    print(each, ":     :",Vertices[each]['source_path'])


#while len(X) < len(Vertices):


