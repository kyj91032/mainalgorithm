// 최대값, 최소값 구하는 알고리즘

int max(const int a[], int n) {
	
	int M = a[0]; //최댓값 저장하는 변수 M을 초기에 a[0]으로 설정.
	int i;
	
	for(i = 1; i < n; i++) { //배열 순서대로 조사하면서(for) 최댓값 M에 업데이트(if).
		if(a[i] > M)
			M = a[i];
	}
	
	return M;
}


/*
파이썬에서.

# 최대최소 최신화하며 구하는 방법. 자료구조 변수 하나면 됨. 원래는 리스트에 모아놓고 min max함수
data = list(map(int, input().split())
min_value = a //초기값 부여
for i in data:
	min_value = min(min_value, i) //min(이전값, 현재값) 으로 계속 최솟값 최신화
	
	
# search_min_index. 최솟값의 인덱스를 구하는 알고리즘

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
min_index = 0

for i in range(len(array)):
	if array[min_index] > array[i]: # 최소 갱신.
		min_index = i # 최솟값의 인덱스 저장.

print(min_index) # 결과 3

*/
