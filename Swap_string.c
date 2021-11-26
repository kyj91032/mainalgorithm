#include <stdio.h>


void swap_str(char *x, char *y)
{
	char *temp;
	while (*x && *y) {					/* 짧은 문자열의 끝까지 문자열을 교환 */
		char t = *x; *x++ = *y; *y++ = t;
	}
	if (*x) {							/* x가 더 긴 문자열이라면 */
		temp = x;
		while (*x) { *y++ = *x++; }		/* x의 나머지를 y로 복사 */
		*temp = *y = '\0';
	}
	else if (*y) {						/* y가 더 긴 문자열이라면 */
		temp = y;
		while (*y) { *x++ = *y++; }		/* y의 나머지를 x로 복사 */
		*temp = *x = '\0';
	}
	else {
		*x = *y = '\0';
	}
}
