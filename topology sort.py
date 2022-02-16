# 위상 정렬: 정렬 알고리즘의 일종이며, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것이다. 그래프상에서 선후관계가 있다면, 위상 정렬을 수행하여 모든 선후 관계를 지키는 전체 순서를 계산할 수 있다.

# 진입차수(Indegree): 특정한 노드로 들어오는 간선의 개수.

# topology sort의 기본 동작 과정과 코드
'''
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 반복한다.
- 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
- 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
'''
# 위상 정렬 알고리즘

from collections import deque

v, e = map(int, input().split()) # 노드와 간선의 개수
indegree = [0] * (v + 1) # 모든 노드의 진입차수 리스트
graph = [[] for i in range(v + 1)] # 인접 리스트 방식의 그래프 초기화

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) # graph에 간선 정보 추가
  indegree[b] += 1 # 진입차수 갱신

def topology_sort():
  result = [] # 정렬 결과 넣을 리스트
  q = deque() # 큐 생성
  
  for i in range(1, v + 1):
    if indegree[i] == 0: # 진입차수가 0인 노드 큐에 추가
      q.append(i)
  
  while q:
    now = q.popleft() 
    result.append(now) # 진입차수가 0인 노드부터 정렬
    for i in graph[now]:
      indegree[i] -= i # 인접 노드들의 진입차수 1 빼기 (방향 그래프이기 때문에 인접 노드는 들어가는 간선 가짐)
      if indegree[i] == 0: # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
        q.append(i)

for i in result:
  print(i, end = ' ')

topology_sort()
