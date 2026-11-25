import sys
import math

input = sys.stdin.readline
write = sys.stdout.write

"""
       +-------------------+
      /        j          /|
     /    (top: b * c)   / |
    +-------------------+  |
    |                   |  |
  i |        k          |  +
(4) |   (front: c * a)  | /
    |        (6)        |/
    +-------------------+

Given face areas (i, j, k):
  i = a * b   (left face   = 4)
  j = b * c   (top face    = 6)
  k = c * a   (front face  = 6)

Solving for edge lengths (a, b, c):
  (i * k) / j = (a * b * c * a) / (b * c) = a^2
  => a = sqrt((i * k) / j)   -> sqrt((4 * 6) / 6) = 2
  => b = i / a               -> 4 / 2 = 2
  => c = k / a               -> 6 / 2 = 3

Total sum of all 12 edges:
  (a * 4) + (b * 4) + (c * 4) = (a + b + c) * 4
  => (2 + 2 + 3) * 4 = 28
"""

i, j, k = map(int, input().strip().split())

a = math.sqrt((i * k) / j)
b = i / a
c = k / a

print(round((a + b + c) * 4))
