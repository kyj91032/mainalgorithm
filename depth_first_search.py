# DFS의 동작 과정과 코드
'''
구체적인 동작 과정: 인접 노드를 시작으로 깊게 기억하면서 전체를 점령함 (stack).

1. 탐색 시작 노드를 스택에 삽입하고 기억 처리를 한다.(push(호출)와 기억처리)
2. 스택의 최상단 노드에, 기억하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 기억 처리를 한다.(인접노드 push(재귀호출)와 기억처리)
3. 기억하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.(pop(종료))
'''
#(재귀)
# dfs 함수 정의. 매개변수(그래프 graph, 노드 포인터 v, 기억 공간 visited[v] = 0 or 1)
def dfs(graph, v, visited): # 1. 탐색 시작 노드 v를 스택에 삽입하고,
  visited[v] = True # 기억처리를 한다.
  print(v, end = ' ')
  for i in graph[v]: # 2. 최상단 노드 v의 인접 노드들 graph[v]에서
    if not visited[i]: # 기억하지 않은 인접 노드가 있으면 
      dfs(graph, i, visited) # 그 인접 노드를 스택에 넣고 기억처리 한다(재귀).
			     # 3. 인접 노드들 중 기억하지 않은 인접노드가 없을 시 함수는 끝나므로(=최상단 스택이 pop) 최후방 함수의 호출이 종료.

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
visited = [False] * 9 #기억 정보 데이터 리스트로 초기화.
dfs(graph, 1, visited) #DFS
#결과 1 2 7 6 8 3 4 5


# 음료수 얼려 먹기. dfs예제 (bfs로 접근하면 인접 노드들을 먼저 방문해야 하는데 그 때 인접 노드의 포인터를 어떻게 표현할지 문제가 발생(?). for i in [상 하 좌 우] 하면 되긴 할 거 같음.)

N, M = map(int, input().split())

graph = []
for i in range(N):
	graph.append(list(map(int, input()))) # **map은 iteralbe의 요소마다 지정된 함수를 적용시켜준다. list(string)은 각 문자가 요소가 되는 리스트로 변환된다.

def dfs(x, y): # dfs의 매개변수. (graph(한 개로 정해져 있으니 매개변수로 넣지 않아도 됨), 노드 포인터 (x, y), 기억처리(= 얼음 여부 0, 1))
	if x <= -1 or x >= n or y <= -1 or y >= m:
		return False
	if graph[x][y] == 0: # 문제 특성 상(기억 처리 되어있는 노드가 처음부터 있음) 재귀를 위해 첫 노드부터 기억 여부 판단한 것. 원래는 바로 기억처리.
			     # push는 했는데 기억처리가 되어있어서 바로 pop..
		graph[x][y] = 1 # 기억처리
		dfs(x - 1, y) # 인접노드 push와 기억처리
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False # pop종료 (노드 x, y가 기억처리 되어있을 때)

result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True: # 한 얼음 노드가 노드 포인터가 됬을 때, 그 얼음 덩어리를 틀 처리 해버려서 중복 없이 얼음 모양의 개수를 셀 수 있다.
			result += 1
print(result)
