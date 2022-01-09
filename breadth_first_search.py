#BFS의 동작 과정과 코드
'''
구체적인 탐색 과정: 인접 노드들을 우선으로 기억하면서 전체를 점령함 (queue).

1. 탐색 시작 노드를 큐에 삽입하고 기억 처리를 한다.(enque와 기억처리)
2. 큐에서 노드를 꺼낸다.(deque)
3. 해당 노드의 인접 노드 중에서 기억하지 않은 노드를 모두 큐에 삽입하고 기억 처리를 한다.(인접노드 enque와 기억처리)
'''
def bfs(graph, start, visited): # 너비 우선 탐색 함수 정의. 매개변수(그래프 graph, 노드 포인터 v, 기억 공간 visited[v] = 0 or 1)
  queue = deque([start]) # 1. 탐색 시작 노드를 큐에 enque하고
  visited[start] = True # 기억 처리를 한다.
  while queue:
    v = queue.popleft() # 2. 큐에서 노드를 deque하고
    printf(v, end = ' ')
    for i in graph[v]: # 해당 노드의 인접 노드들 중에서
      if not visited[i]: # 기억하지 않은 노드를
        queue.append(i) # 큐에 enque하고
        visited[i] = True # 기억 처리를 한다.


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


# 미로 탈출. bfs예제 (dfs랑 뭐가 다른거지..)
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] # 인접 노드 포인터를 얻기 위함.
dy = [0, 0, -1, 1]

def bfs(x, y): # bfs의 매개변수. (graph(한 개로 정해져 있으니 받을 필요 없음), 노드 포인터 (x, y), 방문처리 (0, 1+ 최단거리기록))
	queue = deque()
	queue.append((x, y)) # enque와 기억처리
	while queue:
		x, y = queue.popleft() # duque
		for i in range(4): # 현재 위치에서 네 방향 (인접노드)
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if graph[nx][ny] == 0:
				continue
			if graph[nx][ny] == 1:
				queue.append((nx, ny)) # 인접노드 enque와
				graph[nx][ny] = graph[x][y] + 1 # 기억처리(최단거리 기록) **따로 변수 설정하면 중복되서 값이 더 크게 나옴.
	return graph[n - 1][m - 1] # 최단거리 리턴.

print(bfs(0, 0))
