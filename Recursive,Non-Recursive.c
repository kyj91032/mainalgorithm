#include <stdio.h>

void recur(int n)
{
  if (n > 0) {
    recur(n-1);
    printf("%d\n", n);
    recur(n-2);
  }
}


void nonrecur(int n)
{
  intstack stk;
  initialize(&stk, 100);
Top :
  if(n>0) {
    push(&stk, n);
    n = n - 1;
    goto Top;
  }
  if(!isempty(&stk)){
    pop(&stk, &n);
    printf("%d\n", n);
    n = n - 2;
    goto Top;
  }
  terminate(&stk);
}
