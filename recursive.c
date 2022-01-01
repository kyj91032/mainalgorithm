// 컴퓨터 내부에서 재귀함수의 수행은 스택 자료구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다.(후입선출)
// 따라서 스택 자료구조를 활용해야 하는 상당수의 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. ex) DFS

/* 파이썬에서 재귀함수

def factorial_iterative(n): #반복문으로 구현한 n!
  result = 1 #누적변수
  for i in range(1, n + 1):
    result *= i
  return result

def factorial_recursive(n): #재귀적으로 구현한 n!. 재귀함수가 수학의 점화식(특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것)을 그대로 소스코드로 옮긴 것.
                            #점화식의 초기조건은 재귀함수의 종료조건이다. n이 0 혹은 1일때 fac(n)이 1인 것.
  if n <= 1: #재귀함수의 종료조건. 재귀함수 내에서 특정 조건일 때 더 이상 재귀적으로 함수를 호출하지 않고 종료하도록 if문을 이용하여 꼭 종료조건을 구현해주어야 한다. 
    result 1
  return n * factorial_recursive(n - 1)

*/

//유클리드 호제법

#include <stdio.h>

int gcd(int x, int y) { //x와 y의 최대공약수
	
	if(y == 0) //재귀함수의 종료조건
		return x;
	else
		return gcd(y, x % y); //점화식

	return 0;
}

//하노이의 탑

#include <stdio.h>

void move(int no, int x, int y) //no는 원반 개수, x와 y는 각각 시작 기둥과 목표 기둥의 번호
{
	if(no > 1) //재귀함수의 종료조건
		move(no - 1, x, 6 - x - y); //그룹을 시작 기둥에서 중간 기둥으로

	printf("원반 [%d]를 %d 기둥에서 %d 기둥으로 옮김\n", no, x, y);
	
	if(no > 1)
		move(no - 1, 6 - x - y, y); //그룹을 중간 기둥에서 목표 기둥으로
  
	return 0;
} //점화식이 없다? no 원반개수만 받아서 n 원반 옮기는 개수를 구한다면 점화식이 존재. 위의 함수는 리턴값이 없는 그냥 기둥의 이동을 출력하는 함수.

int hanoi(int n)
{
	if (n == 1) {
		return n; //1 리턴. 재귀함수의 종료조건
	}
	else {
		return hanoi(n - 1) + hanoi(n - 1) + 1; //hanoi(n) = hanoi(n - 1) + 1 + hanoi(n - 1) 점화식
	}
}

// 8퀸 문제

