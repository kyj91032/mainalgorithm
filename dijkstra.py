# 다익스트라 알고리즘: 간선의 가중치가 양수인 그래프에서, 특정한 노드에서 출발하여 다른 모든 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.

distance[w] = min(distance[w], distance[u] + weight[u][w])

# Dijkstra의 기본적인 동작 과정과 코드
'''
Dijkstra는 start로 시작하여 인접 노드 중 현재로서 최선의 거리인 노드 now를 확정지어 나가는 것이므로 기본적으로 그리디 알고리즘으로 분류된다.
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.

3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다. # 여기서 선형탐색, 우선순위 큐 2가지 방식으로 나뉜다
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 초기화한다.

5. 3, 4를 큐가 빌 때 까지 반복. (인접노드를 확인한다는 점은 BFS와 유사)
'''
# Dijkstra 최단 경로_ 선형 탐색 O(V^2)

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
    
    
# Dijkstra 최단 경로_ 우선순위 큐 O(ElogV)
# 우선순위 큐를 이용한다는 점에서 최단 경로 문제를 제외하고도 우선순위 큐를 필요로 하는 다른 문제 유형과도 흡사하다. ex) prim 알고리즘

import heapq # 우선순위 큐 라이브러리 (파이썬에서는 최소 힙) **힙은 삽입시간 logN, 삭제시간 logN. 리스트는 삽입시간 O(1), 삭제시간 O(N)
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
# visited 방문 처리 리스트가 필요 없음. now가 방문 했던 노드라면 더 큰 거리로 큐에 존재하기 때문
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = [] # 큐 생성
  heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 시작노드를 큐에 삽입.
  distance[start] = 0
  while q: # 큐가 빌 때까지 반복
    dist, now = heapq.heappop(q) # 최소 큐로 가장 최단거리가 짧은 노드의 정보 꺼내기
    if distance[now] < dist: # 이미 처리된 적 있는 노드라면 무시. visited는 필요 없음
      continue
    for i in graph[now]: # now의 인접 노드 확인
      cost = dist + i[1] # 인접노드까지의 비용
      if cost < distance[i[0]]: # 더 작다면 최단 거리 테이블 갱신
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) # 갱신 후 우선순위 큐에 추가. 다음 최소 큐를 위해

dijkstra(start)

