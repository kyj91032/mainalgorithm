#include <stdio.h>
#include <string.h>

int bf_match (const char txt[], const char pat[]) // 문자열 검색 알고리즘
{
	int pt = 0;
	int pp = 0;
	//pt는 txt의 커서, pp는 pat의 커서. 처음은 0으로 초기화
	while(txt[pt] != '\0' && pat[pp] != '\0'){
	// txt가 '\0'이면 문자열 검색 실패, pat이 '\0'면 문자열 검색 성공. 둘다 아닌 경우는 검색이 계속 진행 가능한 상태라는 것
		if(txt[pt] == pat[pp]){
		// 검색 실행 후 성공 시
			pt++;
			pp++; 
			//txt와 pat의 커서 모두 +1 이동
		} else {
		// 검색 실행 후 실패 시
			pt = (pt - pp) + 1;
			// pt는 텍스트에서 패턴 간 만큼 빼고(원위치), +1 이동(다음 검색 차례)
			// 브루트포스 알고리즘의 효율 문제가 발생하는 지점
			pp = 0;
			// pp(패턴 커서)는 처음(0)부터
		}
	}
	if(pat[pp] == '\0') // 검색이 종료되고 pat이 '\0' 이라면 검색 성공이라는 것.
		return pt - pp;
		//검색 성공 시 함수는 pt - pp 즉, 텍스트 속 패턴의 첫 문자의 인덱스를 리턴함
	return -1; // 그게 아니면 검색 실패이므로 -1 리턴
}
