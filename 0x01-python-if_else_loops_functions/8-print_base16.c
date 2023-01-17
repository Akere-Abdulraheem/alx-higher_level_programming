#include <stdio.h>
#include <string.h>

/**
 * main -entry point
 *
 * a code that prints all the numbers of base 16 in lowercase using putchar
 *
 * Return: Always 0 (sucess)
 */

int main(void)
{
	char ch;

	for (ch = '0'; ch <= '9'; ch++)
	{
		putchar(ch);
	}
	for (ch = 'a'; ch <= 'f'; ch++)
	{
		putchar(ch);
	}
	putchar('\n');

return (0);
}
