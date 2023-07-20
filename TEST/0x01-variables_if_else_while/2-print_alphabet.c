#include <stdio.h>

/**
 * main - Entry point
 *
 *@c: write a program that prints the alphabet in lower case.
 *
 * Return: Always return 0.
 */
/*int main(void)
{
	int i;

	for (i = 97; i > 122; i++)
	{
		putchar(i);
	}
	putchar('\n');
	
	return(0);
}*/
int main(void)
{
	char i;

	for (i = 'a'; i <= 'z'; i++)
	{
		putchar(i);
	}
	putchar('\n');

	return(0);
}
