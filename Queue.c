#include <stdio.h>
#include <stdlib.h>
#include "intqueue.h"

int initialize(intqueue *q, int max)
{
	q->num = q->front = q->rear = 0;
	if((q->que = calloc(max, sizeof(int))) == NULL){
		q->max = 0;
		return -1;
	}
	q->max = max;
	return 0;
}

int enque(intqueue *q, int x)
{
	if(q->num >= q->max)
		return -1;
	else {
		q->num++;
		q->que[q->rear++] = x;
		if(q->rear == q->max)
			q->rear = 0;
		return 0;
	}
}
 
int deque(intqueue *q, int *x)
{
	if(q->num <= 0)
		return -1;
	else {
		q->num--;
		*x = q->que[q->front++];
		if(q->front == q->max)
			q->front = 0;
		return 0;
	}
}

int Peek(const intqueue *q, int *x)
{
	if(q->num <= 0)
		return -1;
	*x = q->que[q->front];
	return 0;
}
 
void clear(intqueue *q)
{
	q->num = q->front = q->rear = 0;
}
 
int capacity(const intqueue *q)
{
	return q->num;
}
 
int size(const intqueue *q)
{
	return q->num;
}
 
int isfull(const intqueue *q)
{
	return q->num >= q->max;
}
 
int search(const intqueue *q, int x)
{
	int i, idx;
	for(i=0; i < q->num; i++){
		if(q->que[idx = (i + q->front) % q->max] == x)
			return idx;
	}
	return -1;
}
 
int search2(const intqueue *q, int x)
{
	int i, idx;
 
	for(i=0; i < q->num; i++){
		if(q->que[idx = (i + q->front) % q->max == x])
			return idx - q->front;
	}
	return -1;
}
 
void print(const intqueue *q)
{
	int i;
	for(i=0; i < q->num; i++)
		printf("%d ", q->que[i + q->front % q->max]);
	putchar('\n');
}
 
void terminate(intqueue *q)
{
	if(q->que != NULL)
		free(q->que);
	q->max = q->num = q->front = q->rear = 0;
}
 
 
