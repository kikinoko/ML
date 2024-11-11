import math
import sys
import time

def calculate_distance_matrix(points):
    n = len(points)
    distance_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                dist = 0.0
            else:
                dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            row.append(dist)
        distance_matrix.append(row)
    return distance_matrix

def main():
    n = int(input().strip())
    points = [tuple(map(float, input().strip().split())) for _ in range(n)]

   