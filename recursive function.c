// 컴퓨터 내부에서 재귀함수의 수행(함수가 쌓임)은 스택 자료구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다.
// push = 재귀함수의 재귀 호출, pop = 재귀함수의 호출 종료.
// 따라서 스택 자료구조를 활용해야 하는 상당수의 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. ex) DFS

/***
Top down: 재귀함수를 사용한다. 종료조건이 필요하다.
	  코드가 간결하며, 직관적이다.

Bottom up: 반복문을 사용한다. 초깃값과 반복조건이 필요하다.
	   스택 공간을 사용하지 않기 때문에 더 빠르다.
***/


/* 팩토리얼(파이썬)

def factorial_iterative(n): # 반복문으로 구현한 n! (바텀 업)
  result = 1 # 초깃값
  for i in range(1, n + 1): # 반복조건
    result *= i
  return result

def factorial_recursive(n): # 재귀적으로 구현한 n! (탑 다운)
  if n <= 1: # 재귀함수의 종료조건.
    result 1
  return n * factorial_recursive(n - 1)

*/

//유클리드 호제법

#include <stdio.h>

int gcd(int x, int y) { // x와 y의 최대공약수
	
	if(y == 0) // 재귀함수의 종료조건 
		return x;
	else
		return gcd(y, x % y);

	return 0;
}

//하노이의 탑

#include <stdio.h>

void move(int no, int x, int y) // no는 원반 개수, x와 y는 각각 시작 기둥과 목표 기둥의 번호
{
	if(no > 1) // 재귀함수의 종료조건
		move(no - 1, x, 6 - x - y); // 그룹을 시작 기둥에서 중간 기둥으로

	printf("원반 [%d]를 %d 기둥에서 %d 기둥으로 옮김\n", no, x, y);
	
	if(no > 1)
		move(no - 1, 6 - x - y, y); // 그룹을 중간 기둥에서 목표 기둥으로
  
	return 0;
} // 점화식이 없다. 위의 함수는 리턴값이 없는 그냥 기둥의 이동을 출력하는 함수.

int hanoi(int n)
{
	if (n == 1) {
		return n; // 1 리턴. 재귀함수의 종료조건
	}
	else {
		return hanoi(n - 1) + hanoi(n - 1) + 1; // hanoi(n) = hanoi(n - 1) + 1 + hanoi(n - 1) 원반 옮기는 횟수를 구하는 점화식
	}
}

// 8퀸 문제
















