#include <stdio.h>

int kmp_match (const char txt[], const char pat[])
{
	int pt = 1; //표를 구할 때 패턴을 텍스트로 봤을때 커서
	int pp = 0;
	int skip[1024];

	skip[pt] = 0;
	while(pat[pt] != '\0') {
		if(pat[pt] == pat[pp])
			skip[++pt] = ++pp;
		else if(pp == 0)
			skip[++pt] = pp;
		else
			pp = skip[pp]; //이 순간 pp는 무조건 중복 나오기 전 커서일 수 밖에 없음. 그래서 결국 skip[pp] 는 무조건 0. 근데 이럴거면 그냥 0 넣음ㄴ 되ㅡㄴ거 아님?
	}

	pt = pp = 0; //다시 검색 위해 초기화
	while(txt[pt] != '\0' && pat[pp] != '\0') {
		if(txt[pt] == pat[pp]) {
			pt++; pp++;
		} else if(pp == 0)
			pt++;
		else
			pp = skip[pp]; //skip(표)에 기억해둔 위치 사용. pp가 5까지 갔다면, skip[5]는 2를 이용해 pp 초기화
	}
	if(pat[pp] == '\0')
		return pt - pp;
	
	return -1;
}
