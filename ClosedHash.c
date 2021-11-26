#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int no;
	char name[20];
} Member;

typedef enum {
	Occupied, Empty, Deleted//0 1 2
} Status;

typedef struct {
	Member data;
	Status stat;//요소의 상태
} Bucket;//체인법에서의 노드 느낌?

typedef struct {
	int size;
	Bucket *table;//해시 테이블의 첫 번째 요소에 대한 포인터. 테이블 배열의 시작
} ClosedHash;


static int hash(int key, int size)
{
	return key % size;
}

static int rehash(int key, int size)
{
	return(key + 1) % size;
}

static void SetBucket (Bucket *n, const Member *x, Status stat)
{
	n->data = *x;
	n->stat = stat;
}


int initialize (ClosedHash *h, int size)
{
	int i;
	if((h->table = calloc(size, sizeof(Bucket))) == NULL) {
		h->size = 0;
		return 0;
	}
	h->size = size;
	for(i = 0; i < size; i++)
		h->table[i].stat = Empty;//모든 버킷을 공백으로 만들기
	return 1;
}

Bucket *Search (const ClosedHash *h, const Member *x)
{
	int i;
	int key = hash(x->no, h->size);//검색할 데이터의 해시 값
	Bucket *p = &h->table[key];//현재 선택한 노드
	for(i=0; p->stat != Empty && i < h->size; i++) {
		if(p->stat == Occupied && p->data.no == x->no)
			return p;
		key = rehash(key, h->size);
		p = &h->table[key];
	}
	return NULL;
}

int Add (ClosedHash *h, const Member *x)
{
	int i;
	int key = hash(x->no, h->size);
	Bucket *p = &h->table[key];
	if(Search(h, x)) //이미 있으면 종료
		return 1;
	for(i=0; i < h->size; i++) {
		if(p->stat == Empty || p->stat == Deleted) {
			SetBucket(p, x, Occupied);
			return 0;
		}
		key = rehash(key, h->size);
		p = &h->table[key];
	}
	return 2;
}

int Remove (ClosedHash *h, const Member *x)
{
	Bucket *p = Search(h, x);
	if(p == NULL)
		return 1;
	p->stat = Deleted;//stat 만 하면 되나?? data는?
	return 0;
}

void Dump (const ClosedHash *h)
{
	int i;
	for(i=0; i < h->size; i++) {
		printf("%02d : ", i);
		switch(h->table[i].stat) {
			case Occupied : printf("%d(%s)\n",
				h->table[i].data.no, h->table[i].data.name); break;
			case Empty : printf("-- 미등록 --\n"); break;
			case Deleted : printf("-- 삭제 마침 --\n"); break;
		}
	}
}

void Clear(ClosedHash *h)
{
	int i;
	for(i=0; i < h->size; i++)
		h->table[i].stat = Empty;
}

void Terminate(ClosedHash *h)
{
	Clear(h);
	free(h->table);
	h->size = 0;
}

