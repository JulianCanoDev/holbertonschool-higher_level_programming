#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: Struct of program
 * Return: 0 no cycle, 1 cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list, *secund = list;

	for (; first && secund && first->next;)
	{
		secund = secund->next;
		first = first->next->next;
		if (secund == first)
		{
			return (1);
		}
	}
	return (0);
}