import time
import random
import heapq

N = 10_000_000  # πλήθος τιμών
M = 1_000  # εύρος ακεραίων τιμών από 1 μέχρι και Μ
TOP = 10

random.seed(1234)
nums = [random.randint(1, M) for _ in range(N)]

my_map = {}
for k in nums:
    my_map[k] = my_map.get(k, 0) + 1

start_time = time.time()  # έναρξη χρονομέτρησης
hq = [(my_map[k] * -1, k) for k in my_map]
heapq.heapify(hq) # δημιουργία σωρού ελαχίστων

for _ in range(TOP):
    kv = heapq.heappop(hq)
    print(f"{kv[0]*(-1)} εμφανίσεις της τιμής {kv[1]}")
print(f"{time.time() - start_time:.4f} δευτερόλεπτα") # τερματισμός χρονομέτρησης

# 10347 εμφανίσεις της τιμής 131
# 10345 εμφανίσεις της τιμής 361
# 10304 εμφανίσεις της τιμής 323
# 10272 εμφανίσεις της τιμής 380
# 10265 εμφανίσεις της τιμής 837
# 10262 εμφανίσεις της τιμής 898
# 10249 εμφανίσεις της τιμής 111
# 10248 εμφανίσεις της τιμής 554
# 10244 εμφανίσεις της τιμής 106
# 10238 εμφανίσεις της τιμής 994
# 1.79 δευτερόλεπτα