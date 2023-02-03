#include <stdio.h>

/**
 * main - Entry point
 *
 * Return: 0.
 */
void playgame()
{
	printf("play game called" );
}
void loadgame()
{
	printf("load game called" );
}
void playmultiplayer()
{
	printf("play multiplayer game called" );
}

int main()
{
	int input;

	printf("1, Play game\n");
	printf("2, Load game\n");
	printf("3, Play multiplayer\n");
	printf("Exit\n");
	printf("selection: ");
	scanf("%d\n", &input);
	switch (input){
case 1:
	playgame();
	break;
case 2:
	loadgame();
	break;
case 3:
	playmultiplayer();
	break;
case 4:
	printf("Thanks for playing\n");
	break;
default:
	printf("Bad input, quitting\n");
	break;
	}
	getchar();
}
