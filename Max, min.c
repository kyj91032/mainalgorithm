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
