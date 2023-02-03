#include <stdio.h>

int main()
{
	int x;

	x = 0;
	do{
		/* Hello World is printed atleast one time even though the condition is false */
		printf("Hello World\n");
	}while ( x != 0 );
	getchar();

}
