# 크루스칼 알고리즘: 최소 신장 트리 알고리즘 중 하나로, 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘이다.
# 신장 트리(spanning tree) : 하나의 그래프가 있을 때 모든 노드를 포함하면서, 사이클이 존재하지 않는 부분 그래프이다. 이는 트리의 성립 조건과도 같아서 일종의 트리 자료구조라고 할 수 있다.

# kruskal algorithm의 기본 동작 과정과 코드
'''
1. 간선 데이터를 비용에 따라 오름차순으롤 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다. 발생시키는 경우만 최소 신장 트리에 포함시킨다.
서로소 집합 자료구조를 이용하므로 무방향 그래프에서만 사용이 가능한 알고리즘이다.
'''

# kruskal 최소 신장 트리

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # 재귀호출로 부모 노드를 거스르는 과정에서 부모 테이블을 루트 테이블로 갱신하고 루트를 리턴함.
  return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합을 합치는 union 함수(= 최종적으로 disjoint set을 새로 만드는 함수. 그래프에서 부모 테이블을 고려하면 disjoint set임).
  a = find_parent(parent, a) # 원소 a의 루트
  b = find_parent(parent, b) # 원소 b의 루트
  if a > b:
    parent[b] = a # 루트 노드의 번호가 더 작은 집합을 부모로 합침.
  else:
    parent[a] = b

v, e = map(int, input().split()) # 노드의 개수 v, 간선의 개수 e
parent = [0] * (v + 1) # 부모 테이블
for i in range(1, v + 1): # 부모 테이블 초기화
  parent[i] = i

edges = []
result = 0

for _ in range(e):
  a, b, cost = map(int, input().split()) # 간선 정보 입력받기 (무방향 그래프)
  edges.append((cost, a, b)) # 정렬을 위해 비용을 첫번째 원소로

edges.sort() # 간선을 비용순으로 정렬

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는 경우에만
    union_parent(parent, a, b) # 집합에 포함
    result += cost # 최소 비용 누적 계산

print(result)
