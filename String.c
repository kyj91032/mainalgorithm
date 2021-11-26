#include <stdio.h>
#include <string.h>

char *str_chr (const char *s, int c)
{
	c = (char)c; // 표준 라이브러리 함수에서 '문자'를 주고받을 때는 char형이 아니라 int 형으로 주고 받는다. 초기의 C언어는 함수로 전달하는 매개변수로 char형이나 short형 등의 값을 먼저 int형으로 변환했기 때문. (컴퓨터에 저장 자체는 ascii코드표를 보면 알 수 있듯이 숫자로 했기 때문인듯함)
	while(*s != c) { //검색 반복 실행
		if(*s == '\0') //검색 실패
			return NULL; //검색 실패 시 바로 NULL리턴
		s++;
	}
	return (char *)s;//검색 성공 시 key문자 포인터 리턴
}


int str_cmp (const char *s1, const char *s2)
{
	while(*s1 == *s2) {
		if(*s1 == '\0') //둘다 널이면 0리턴
			return 0;
		s1++;
		s2++;
	}
	return (unsigned char)*s1 - (unsigned char)*s2;
}
/*
int str_cmpic(const char *s1, const char *s2)
{
	while (toupper(*s1) == toupper(*s2)) {
		if (*s1 == '\0')			
			return 0;
		s1++;
		s2++;
	}
	return (unsigned char)toupper(*s1) - (unsigned char)toupper(*s2);
}
*/

size_t str_len1 (const char *s) //size_t 자료형은 unsigned int 라고 취급
{
	size_t len = 0;

	while(s[len]) //조건반복문 while. '/0'만날 때 까지 문자 개수 세기
		len++;
	return len;
}

size_t str_len2 (const char *s)
{
	size_t len = 0;

	while(*s++) //연산자 우선순위 *보다 ++이 우선. 조건반복문 while. '/0'만날 때 까지 문자 개수 세기
		len++;
	return len;
}

size_t str_len3 (const char *s)
{
	const char *p = s; //문자 개수를 세는 변수인 len을 정의하기 보다는 시작지점 포인터 변수 p를 만들어서 s-p값을 리턴하여 문자 거리(개수)를 리턴함
	while(*s)
		s++;
	return s - p;
}


int str_ncmp(const char *s1, const char *s2, size_t n)
{
	while (n && *s1 && *s2) {
		if (*s1 != *s2)
			return (unsigned char)*s1 - (unsigned char)*s2;
		s1++;
		s2++;
		n--;
	}
	if(!n) return 0; //n이 0일때(n길이만큼 일치 시) 실행됨.
	if(*s1) return 1; //왜있지 ?
	return -1; //왜있지?
}
/*
int str_ncmpic(const char *s1, const char *s2, size_t n)
{
	while (n && *s1 && *s2) {
		if (toupper(*s1) != toupper(*s2))			
			return (unsigned char)toupper(*s1) - (unsigned char)toupper(*s2);
		s1++;
		s2++;
		n--;
	}
	if (!n)  return 0;
	if (*s1) return toupper(*s1);
	return toupper(*s2);
}
*/


char *str_rchr(const char *s, int c)
{
	const char *p = NULL;

	c = (char)c;
	while(1) {
		if(*s == c)
			p = s;
		if(*s == '\0')
			break;
		s++;
	}
	return (char *)p;
}


char *str_str(const char *s1, const char *s2)
{
	const char *p1 = s1; //이걸 왜 정의??
	const char *p2 = s2;

	while (*p1 && *p2) {
		if (*p1 == *p2) {
			p1++;
			p2++;
		}
		else {
			p1 -= p2 - s2 - 1;
			p2 = s2;
		}
	}
	return *p2 ? NULL : (char *)(p1 - (p2 - s2));
}

