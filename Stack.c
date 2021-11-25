#include <stdio.h>
#include <stdlib.h>
#include "intstack.h"

typedef struct {
	int max;
	int ptr;
	int *stk;
} intstack;

int initialize(intstack *s, int max);

int push(intstack *s, int x);

int pop(intstack *s, int *x);

int peek(const intstack *s, int *x);

void clear(intstack *s);

int capacity(const intstack *s);

int size(const intstack *s);

int isempty(const intstack *s);

int isfull(const intstack *s);

int search(const intstack *s, int x);

void print(const intstack *s);

void terminate(intstack *s);

int initialize(intstack *s, int max)
{
	s->ptr = 0;
	if(s->stk = calloc(max, sizeof(int)) == NULL){
		s->max = 0;
		return -1;
	}
	s->max = max;
	return 0;
}

int push(intstack *s, int x)
{
	if(s->ptr >= s->max)
		return -1;
	s->stk[s->ptr++] = x;
	return 0;
}

int pop(intstack *s, int *x)
{
	if(s->ptr <= 0)
		return -1;
	*x = s->stk[s->ptr--];
	return 0;
}

int Peek(const intstack *s, int *x)
{
	if(s->ptr <= 0)
		return -1;
	*x = s->stk[s->ptr - 1];
	return 0;
}

void clear(intstack *s)
{
  s->ptr = 0;
}

int capacity(const intstack *s)
{
  return s->max;
}

int size(const intstack *s)
{
  return s->ptr;
}

int isempty(const intstack *s)
{
  return s->ptr <= 0;
}

int isfull(const intstack *s)
{
  return s->ptr >= s->max;
}

int search(const intstack *s, int x)
{
  int i;
  for(i = s->ptr - 1; i >= 0; i--)
    if(s->stk[i] == x)
      return i;
    return -1;
}

void print(const intstack *s)
{
  int i;
  for(i=0; i<s->ptr; i++)
    printf("%d ", s->stk[i]);
  putchar('\n');
}

void terminate(intstack *s)
{
  if(s->stk != NULL)
    free(s->stk);
  s->max = s->ptr = 0;
}
