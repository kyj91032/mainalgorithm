#BFS의 동작 과정과 코드
'''
구체적인 동작 과정 (큐)
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
'''
def bfs(graph, start, visited): # 너비 우선 탐색 함수 정의. 매개변수(그래프 graph, 노드 포인터 v, 방문 여부 기억공간 visited[v] = 0 or 1)
  queue = deque([start]) # 1. 탐색 시작 노드를 큐에 삽입하고
  visited[start] = True # 방문 처리를 한다.
  while queue:
    v = queue.popleft() # 2. 큐에서 노드를 pop하고
    printf(v, end = ' ')
    for i in graph[v]: # 해당 노드의 인접 노드들 중에서
      if not visited[i]: # 방문하지 않은 노드를
        queue.append(i) # 큐에 삽입하고
        visited[i] = True # 방문 처리를 한다.


graph = [ #인접 리스트 방식(?)으로 그래프 표현.
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9 #방문 정보 데이터 리스트로 초기화.
bfs(graph, 1, visited) #BFS

# 결과 1 2 3 8 7 4 5 6
