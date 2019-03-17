import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    cnt = 0
    while heap[0]<K:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        mix = min1 + (min2*2)
        heapq.heappush(heap, mix)
        cnt = cnt + 1
        if len(heap) == 1 and heap[0]<K:
            return -1
    return cnt
