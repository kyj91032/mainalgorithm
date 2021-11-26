#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bis(int a[], int b[], int n)
{
  int i, j;
  int tmp;

  for(i=1; i<n; i++)
  {
    tmp = a[i];
    int pl = 0;
    int pr = i-1;
    int pc;
    
    while(pl <= pr)
    {
      pc = (pl + pr)/2;
      if(a[pc] < tmp)
        pl = pc + 1;
      
      if(a[pc] > tmp)
        pr = pc - 1;
      
      if(a[pc] == tmp)
      {
        for(j=i; j>pc; j--)
          a[j] = a[j-1];
        a[j-1] = tmp;
        break;
      }
    }
    
    if(a[pc] <= tmp) {
      memmove(a+pc+1, b+i, sizeof(int));
    }

    if(a[pc] > tmp) {
      memmove(a+pc, b+i, sizeof(int));
    }
  }
  return 0;
}
