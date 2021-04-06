import heapq

heap = [12, 4, 5, 231, 35, 6]


#(cost, vrednost)

heapq.heapify(heap) # O(N)
print(heap)
# Vedno je najmanjši heap[0]
heapq.heappush(heap, 0) # O(log n)
print(heap[0])
print(heap)
print(heapq.heappop(heap)) # O(log n)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))


print("-|-".join( ["a", "b", "c", "d"]))
