# DFS
'''
구체적인 동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에, 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 

'''


def dfs(graph, v, visited):
  visited[v] = True #현재 노드 방문처리
  print(v, end = ' ') #방문한 노드 출력
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
  




graph = [ #인접 리스트 방식으로 그래프 표현.
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

visited = [False] * 9 #방문 정보 데이터 리스트로.

dfs(graph, 1, visited)
