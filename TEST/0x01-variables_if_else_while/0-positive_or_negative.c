#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * main - Entry point
 *
 * Return: Always return 0.
 */
int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	/* your code goes there */

	if (n > 0)
		printf("is positive %d\n", n);
	else if (n < 0)
		printf("is negative %d\n", n);
	else
		printf("is zero %d\n", n);

	return (0);
}
