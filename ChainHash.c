#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int no;
	char name[20];
} Member;

#define MEMBER_NO 1
#define MEMBER_NAME 2


typedef struct __node {
	Member data;
	struct __node *next;
} Node;

typedef struct {
	int size;
	Node **table; //*Node 를 가르키기 때문에 이중포인터 **table
} ChainHash;

static int hash(int key, int size)
{
	return key % size;
}

static void SetNode(Node *n, Member *x, const Node *next)
{
	n->data = *x;
	n->next = next;
}

int Initialize (ChainHash *h, int size)
{
	int i;
	if((h->table = calloc(size, sizeof(Node *))) == NULL) {
		h->size = 0;
		return 0;
	}
	h->size = size;
	for(i=0; i < size; i++)
		h->table[i] = NULL;
	return 1;
}

Node *Search (const ChainHash *h, const Member *x)
{
	int key = hash(x->no, h->size);//검색하는 값의 해시값
	Node *p = h->table[key];

	while(p != NULL) {
		if(p->data.no == x->no)
			return p;
		p = p->next;
	}
	return NULL;
}

int Add(ChainHash *h, const Member *x)
{
	int key = hash(x->no, h->size);//추가하는 값의 해시값
	Node *p = h->table[key]; //선택한 노드
	Node *temp;
	while(p != NULL) {
		if(p->data.no == x->no)
			return 1; //이미 있으면 종료
		p = p->next;
	}//연결 리스트 끝까지 조사
	if((temp = calloc(1, sizeof(Node))) == NULL)
		return 2;
	SetNode(temp, x, h->table[key]); //temp 에 추가 data 와 next(첫 요소 가르키게 함)
	h->table[key] = temp; //버킷이 temp 가르키게 해서 맨앞에 추가됨
	return 0;
}

int Remove(ChainHash *h, const Member *x)
{
	int key = hash(x->no, h->size);//삭제하는 값의 해시값
	Node *p = h->table[key]; //선택한 노드
	Node **pp = &h->table[key]; //선택한 노드에 대한 포인터
	while(p != NULL) {
		if(p->data.no == x->no) {
			*pp = p->next;
			free(p);
			return 0; //왜 이중으로 갈까?
		}
		pp = &p->next;
		p = p->next;
	}
	return 1;
}

void Dump(const ChainHash *h)
{
	int i;
	for(i=0; i < h->size; i++){
		Node *p = h->table[i];
		printf("%02d  ", i);
		while(p != NULL) {
			printf("%d %s", p->data.no, p->data.name);
			p = p->next;
		}
		putchar('\n');
	}
}

void Clear (ChainHash *h)
{
	int i;
	for(i=0; i < h->size; i++){
		Node *p = h->table[i];
		while(p != NULL){
			Node *next = p->next;
			free(p);
			p = next;
		}
		h->table[i] = NULL;
	}
}

void Terminate(ChainHash *h)
{
	Clear(h);
	free(h->table);
	h->size = 0;	
}
