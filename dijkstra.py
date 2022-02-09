# 다익스트라 알고리즘: 간선의 가중치가 양수인 그래프에서, 특정한 노드에서 출발하여 다른 모든 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.

# Dijkstra의 기본적인 동작 과정과 코드
'''
매번 가장 적은 비용의 노드를 선택해서 임의의 과정을 반복하므로 기본적으로 그리디 알고리즘으로 분류된다.
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.

3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 초기화한다.

5. 3, 4를 큐가 빌 때 까지 반복. (인접노드를 확인한다는 점은 BFS와 유사)
'''
# Dijkstra 최단 경로_ 선형 탐색

import sys
input = sys.stdin.readline # 빠른 입력 받기(개행문자는 split으로 사라짐)
INF = int(1e9) # 무한의 값을 의미. 10억으로 설정

n, m = map(int, input().split()) # 노드의 개수n, 간선의 개수m
start = int(input()) # 시작 노드의 번호
graph = [[] for i in range(n + 1)] # 인접 리스트 방식의 그래프 정의 (2차원 리스트)
visited = [False] * (n + 1) # 방문 처리(최단거리 확정) 체크하는 1차원 리스트
distance = [INF] * (n + 1) # 최단 거리 테이블 모두 무한으로 초기화 (최초에 갱신할 때를 위해)

for _ in range(m):
  a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c일 때
  graph[a].append((b, c)) # 인접 리스트 방식으로 그래프 초기화

def get_smallest_node(): # 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드의 번호를 리턴
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True # start 노드부터 출발
  for j in graph[start]:
    distance[j[0]] = j[1] # 시작 노드의 인접 노드부터 최단 거리 테이블 갱신
  for i in range(n - 1): # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복 (어차피 한번씩 확인하므로 횟수반복도 됨)
    now = get_smallest_node()
    visited[now] = True # now 노드부터 다시 출발
    for j in graph[now]:
      cost = distance[now] + j[1] # 현재 노드 거쳐서 다른 노드로 이동하는 비용
      if cost < distance[j[0]]: # 더 작다면 최단 거리 테이블 갱신
        distance[j[0]] = cost

dijkstra(start) # start부터 다익스트라 알고리즘 실행
    
    
    
    
