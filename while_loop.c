#include <stdio.h>

int main()
{
	int x = 0; /* Dont forget to declare variables */

	while ( x < 100 ) { /* while x is less than 10 */
		printf( "%d\n", x );
		x ++; /* update x so the condition can be met eventually */
	}
	getchar();

}
