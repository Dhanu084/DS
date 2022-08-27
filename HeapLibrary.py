from heapq import heapify,heappush,heappop

lst = [17,27,17,3,12,7]

heapify(lst)
print(lst)
heappush(lst, 5)
# while(len(lst)):
#     print(heappop(lst))


max_heap_lst = [-x for x in lst]

heapify(max_heap_lst)
while(len(max_heap_lst)):
    print(heappop(max_heap_lst)*-1)
