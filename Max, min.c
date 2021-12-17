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

data = list(map(int, input().split())
min_value = a //초기값 부여
for i in data:
	min_value = min(min_value, i) //min(이전값, 현재값) 으로 계속 최솟값 최신화
*/
