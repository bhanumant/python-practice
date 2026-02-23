

#Priority queue ===small element high priority, big element low priority


import heapq
H=[10,20,30,40,50,60]

heapq.heappush(H, 20)
heapq.heappush(H, 500)
heapq.heappush(H, 800)
heapq.heappush(H, 8000)
heapq.heappush(H, 9000)
print(H)



heapq.heappop(H)
print(H)
heapq.heappop(H)
print(H)
heapq.heappop(H)
print(H)



heapq.heapify(H)
print(H)


print(heapq.nlargest(2, H))

print(heapq.nsmallest(2, H))