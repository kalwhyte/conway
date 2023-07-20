#include <stdio.h>

/**
 * main: Entry point.
 *
 * Return- Always return 0.
 */

int mult(int x, int y);

/**
 * main - main entry
 * @x: first operand
 * @y: second operand
 */
int main(void)
{
	int x;
	int y;

	printf("Enter the two integers to be multiplied: ");
	scanf("%d", &x);
	scanf("%d", &y);
	printf("product of two integers %d\n", mult(x, y));
	getchar();

}

/**
 * mult - prints (x * y)
 */
int mult(int x, int y)
{
	return (x * y);
}
