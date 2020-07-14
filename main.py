from typing import List

def insert(min_heap: List[int], x: int) -> None:
    min_heap.append(x)
    i = len(min_heap)-1
    while i > 0:
        parent_idx = (i-1) // 2
        if min_heap[parent_idx] <= min_heap[i]:
            break
        else:
            min_heap[parent_idx], min_heap[i] = min_heap[i], min_heap[parent_idx]
            i = parent_idx

def extract_min(min_heap: List[int]) -> int:
    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    min_value = min_heap.pop()
    i = 0
    while i < len(min_heap):
        if 2*i+2 < len(min_heap) and min_heap[2*i+2] <= min_heap[2*i+1]:
            smallest_child_idx = 2*i+2
        elif 2*i+1 < len(min_heap):
            smallest_child_idx = 2*i+1
        else:
            break

        if min_heap[smallest_child_idx] < min_heap[i]:
            min_heap[smallest_child_idx], min_heap[i] = min_heap[i], min_heap[smallest_child_idx]
            i = smallest_child_idx
        else:
            break

    return min_value
