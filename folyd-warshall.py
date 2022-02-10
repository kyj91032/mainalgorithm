# 플로이드-워셜 알고리즘: 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘이다.

# floyd-warshall의 기본적인 동작 과정과 코드
'''
1. 인접 행렬 그래프를 초기화한다.
2. 점화식(Dab = min(Dab, Dak + Dkb))을 모든 노드에서 반복하며 graph에 간선 정보 갱신 (다이나믹 프로그래밍)
'''
# floyd-warshall 최단 경로

INF = int(1e9)

n = int(input()) # 노드의 개수 n
m = int(input()) # 간선의 개수 m
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트로 그래프 인접 행렬 표현(distance 리스트 따로 안써도 됨), 모든 값을 무한으로 초기화 (초기에 최솟값을 넣기 위해). n + 1인 이유는 노드 번호와 인덱스 값을 맞추기 위해

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0 # 자기 자신과의 비용 0으로 초기화.
      
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c # 주어진 간선 정보 저장

for k in range(1, n + 1): # 모든 노드 1 ~ n에 대하여
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # n-1P2(= nP2)의 모든 조합을 점화식에 따라(다이나믹 프로그래밍) 최단 거리를 인접 행렬 graph에 갱신
