#include <stdio.h>
#include <string.h>
#include <limits.h>

int bm_match(const char txt[], const char pat[])
{
	int pt;
	int pp;
	int txt_len = strlen(txt);
	int pat_len = strlen(pat);
	int skip[UCHAR_MAX + 1];
	for(pt = 0; pt <= UCHAR_MAX; pt++)
		skip[pt] = pat_len;
	for(pt = 0; pt < pat_len - 1; pt++)
		skip[pat[pt]] = pat_len - pt - 1;
	
	while(pt < txt_len) {
		pp = pat_len - 1;
		while(txt[pt] == pat[pp]) {
			if(pp == 0)
				return pt; //일치하는거 찾은 경우
			pp--;
			pt--;
		}
		pt += (skip[txt[pt]] > pat_len - pp) ? skip[txt[pt]] : pat_len - pp;
		// 갑자기 왜 대소비교?? 왜 대소비교로 행동을 정하지..?
	}
	return -1;
}
