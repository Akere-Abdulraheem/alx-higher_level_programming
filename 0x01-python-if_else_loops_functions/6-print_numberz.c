#include <stdio.h>
#include <string.h>

/**
 * main -entry point
 *
 * a code that print alphabet in lowercase using putchar
 *
 * Return: Always 0 (sucess)
 */

int main(void)
{
	int  ch;

	for (ch = '0'; ch <= '9'; ch++)
	{
		putchar(ch);
	}
	putchar('\n');

return (0);
}
