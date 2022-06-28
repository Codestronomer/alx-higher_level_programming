#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a
 * cycle in it
 * @list: linked list node
 *
 * Return: 0 if there is no cycle, 1 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			slow = list;
			slow = slow->next;
			fast = fast->next;
			if (slow == fast)
				return (1);
		}
	}
	return (0);
}
