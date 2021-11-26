// 1 //

#include <stdio.h>

void swap_ptr (char **x, char **y)
{
	char *tmp = *x;
	*x = *y;
	*y = tmp;
}

int main(void)
{
	char *s1 = "ABCD";
	char *s2 = "EFGH";

	swap_ptr(&s1, &s2);

	printf("%s %s", s1, s2);

	return 0;
}


// 2 //

#include <stdio.h>

void swap_ptr (char *x, char *y)
{
	char *tmp = x;
	x = y;
	y = tmp;
}

int main(void)
{
	char *s1 = "ABCD";
	char *s2 = "EFGH";

	swap_ptr(s1, s2);

	printf("%s %s", s1, s2);

	return 0;
}


// 3 //

#include <stdio.h>
#define swap(type, x, y)  do { type t = x; x = y; y = t; } while (0)

int main(void)
{
	char *s1 = "ABCD";		
	char *s2 = "EFGH";

	swap(char*, s1, s2);

	printf("%s %s", s1, s2);

	return 0;
}
