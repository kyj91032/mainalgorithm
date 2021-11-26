#include <stdio.h>
#include <stdlib.h>
#define swap(type, x, y) do {type t=x; x=y; y=t;} while(0)

int bubble(int a[], int n)
{
  int left = 0;
  int right = n-1;
  int last = right;

  while(left < right)
  {
    int j;
    for(j=right; j>left; j--) {
      if(a[j-1]>a[j]){
        swap(int, a[j-1], a[j]);
        last = j;
      }
    }
    left = last;
    
    for(j=left; j<right; j++) {
      if(a[j+1]<a[j]){
        swap(int, a[j+1], a[j]);
        last = j;
      }
    }
    right = last;
  }
}
