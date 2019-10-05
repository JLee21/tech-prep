"""

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

import heapq
import collections

"""
Solution #1 Brute Force
Runtime: for loop + sort = n + n log(n)
Space: for loop + sort array = O(n)
"""


def kClosest(points, K):
    saved_list = []

    for point in points:
        distance = (point[0]**2 + point[1]**2) ** 0.5
        saved_list.append((distance, point))

    # sort saved_list
    saved_sort = sorted(saved_list)

    return [point[1] for point in saved_sort[:K]]


"""
Solution #2 Brute Force
Runtime: sort = n log(n)
Space: for loop + sort array = O(n)
"""


def kClosest(points, K):
    points.sort(key=lambda P: P[0]**2 + P[1]**2)
    return points[:K]


points = [[1, 3], [-2, 2]]
K = 1
print(kClosest(points, K))

points = [[3, 3], [5, -1], [-2, 4]]
K = 2
print(kClosest(points, K))

"""
Solution #3 min-heap sort using heapq.
heapq uses binary tree sorting so pop and add are log(n) runtimes
"""


def kClosest3(points, K):
    heap = []
    for point in points:
        # note we do not have to do the sqrt
        distance = point[0]**2 + point[1]**2
        heapq.heappush(heap, (distance, point))
    return [point[1] for point in heapq.nsmallest(K, heap)]


points = [[3, 3], [5, -1], [-2, 4]]
K = 2
print(kClosest3(points, K))

"""
Solution #4 max-heap sort using heapq
In contrast to the previous min-heap solution, The diffefernce between this solution and the above solution
is that me restrict the size of the binary tree / list? to be K long.
So, a add or remove is only nlog(k)... I think? B/c aren't we iterating through
the entire list though?
"""


def kClosest4(points, K):
    heap = []
    for point in points:
        print('heap-->', heap)
        distance = (point[0]**2 + point[1]**2)
        if len(heap) <= K - 1:
            heapq.heappush(heap, (distance, point))
        else:
            if distance > heap[0][0]:
                heapq.heapreplace(heap, (distance, point))
    return [point[1] for point in heap]


points = [[3, 3], [5, -1], [-2, 4]]
K = 2
print(kClosest4(points, K))


def kClosest5(points, K):
    # https://leetcode.com/problems/k-closest-points-to-origin/discuss/348171/Python3-sort-O(NlogN)-minimum-heap-O(NlogN)-and-maximum-heap-O(NlogK)
    h = []
    for p in points:
        if len(h) <= K-1:
            heapq.heappush(h, (-p[0]**2-p[1]**2, p))
        else:
            if -p[0]**2-p[1]**2 > h[0][0]:
                heapq.heapreplace(h, (-p[0]**2-p[1]**2, p))
    res = []
    for i in range(K):
        res.append(heapq.heappop(h)[1])
    return res


points = [[3, 3], [5, -1], [-2, 4]]
K = 2
print(kClosest5(points, K))
