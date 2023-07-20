#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * main - Entry point
 *
 * print the last digit of the number stored in the variable n.
 * Return: Always return 0.
 */
int main(void)
{
	int n, last_digit;

	srand(time(0));
	n = rand() - RAND_MAX / 2;

	printf("Last digit of %d is ", n);

	/* get last digit of n */
	last_digit = n % 10;

	/* print the last digit */
	printf("%d and is ", last_digit);

	if (last_digit > 5)
		printf("greater than 5\n");
	else if (last_digit == 0)
		printf("0\n");
	else
		printf("less than 6 and is not 0\n");

	return (0);
}
