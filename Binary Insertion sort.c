#include <stdio.h>
#include <stdlib.h>

int bis(int a[], int n)
{
  int i, j;
  int tmp;

  for(i=1; i<n; i++)
  {
    tmp = a[i];
    int pl = 0;
    int pr = i-1;
    int pc;
    printf("%c\n", 'a');
    
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
    printf("%c\n", 'b');
    
    if(a[pc] <= tmp) {
      for(j=i; j>pc+1; j--){
        a[j] = a[j-1];
      }
      a[pc+1] = tmp;
    }

    if(a[pc] > tmp) {
      for(j=i; j>pc; j--){
        a[j] = a[j-1];
      }
      a[pc] = tmp;
    }

    printf("%c\n", 'c');
  }
  return 0;
}
