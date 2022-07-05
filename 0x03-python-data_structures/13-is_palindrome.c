#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the reversed list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *nxt;

	prev = NULL;
	curr = *head;

	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is
 * a palindrome
 * @head: head node of the listint_t  linked list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp = *head;
	listint_t *duplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			duplicate = slow->next;
			break;
		}
		if (!fast->next)
		{
			duplicate = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&duplicate);

	while (duplicate && temp)
	{
		if (temp->n == duplicate->n)
		{
			duplicate = duplicate->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!duplicate)
		return (1);

	return (0);
}
