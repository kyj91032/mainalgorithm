# DFS의 동작 과정과 코드
'''
구체적인 동작 과정: 인접 노드를 시작으로 깊게 기억하면서 전체를 점령함 (stack).

1. 탐색 시작 노드를 스택에 삽입하고 기억 처리를 한다.(push(호출)와 기억처리)
2. 스택의 최상단 노드에, 기억하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 기억 처리를 한다.(인접노드 push(재귀호출)와 기억처리)
3. 기억하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.(pop(종료))
'''
# dfs 함수 정의. 매개변수(그래프 graph, 노드 포인터 v, 기억 공간 visited[v] = 0 or 1). 하나로 정해져 있는 건 매개변수 안써도 됨.
def dfs(graph, v, visited): # 1. 탐색 시작 노드 v를 호출하고(스택에 삽입),
			    # (stack.append(v)가 시작으로서 탐색시작 노드v의 push이어야하지만, 스택 자료구조이므로 재귀함수 알고리즘으로 바꾸면 함수의 호출 자체가 push가 된다.)
  visited[v] = True # 기억처리를 한다.
  print(v, end = ' ')
  for i in graph[v]: # 2. 최상단 노드 v의 인접 노드들 graph[v]에서
    if not visited[i]: # 기억처리 되어있지 않은 인접 노드가 있으면
      dfs(graph, i, visited) # 그 인접 노드들을 재귀호출(스택에 삽입)하고 기억처리 한다.
			     # 3. 인접 노드들 중 기억처리 되어있지 않은 인접노드가 없을 시 함수는 끝나므로 함수의 호출이 종료(=최상단 스택이 pop).

graph = [ # 인접 리스트 방식.
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
visited = [False] * 9 # 기억 정보 데이터 리스트로 초기화.
dfs(graph, 1, visited) # DFS
# 결과 1 2 7 6 8 3 4 5


# 음료수 얼려 먹기. dfs예제 (bfs로 접근하면 인접 노드들을 먼저 방문해야 하는데 그 때 인접 노드의 포인터를 어떻게 표현할지 문제가 발생(?). for i in [상 하 좌 우] 하면 되긴 할 거 같음.)

N, M = map(int, input().split())

graph = []
for i in range(N):
	graph.append(list(map(int, input()))) # **map은 iteralbe의 요소마다 지정된 함수를 적용시켜준다. list(string)은 각 문자가 요소가 되는 리스트로 변환된다.

def dfs(x, y): # dfs의 매개변수: 시작 노드 포인터 (x, y) # push와
	if x <= -1 or x >= n or y <= -1 or y >= m:
		return False
	if graph[x][y] == 0: # (노드 x, y가 기억처리 되어있지 않은 경우) **재귀함수 호출을 포함한 모든 시작노드가 기억처리가 되어있을 수 있기 때문에 처음부터 기억처리를 하지 않음.
								    # ?????????????어케바꾼거야..
		graph[x][y] = 1 # 기억처리
		dfs(x - 1, y) # 인접노드 push와 기억처리
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False # pop종료 (노드 x, y가 기억처리 되어있는 경우)

result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True: # 한 얼음 노드가 노드 포인터가 됬을 때, 그 얼음 덩어리를 틀 처리 해버려서 중복 없이 얼음 모양의 개수를 셀 수 있다.
			result += 1
print(result)
