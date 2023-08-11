#!/usr/bin/python3
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current = *head;
    listint_t *prev = NULL;

    // Allocate memory for the new node
    new_node = malloc(sizeof(listint_t));
    if (!new_node) 
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    // If the list is empty or the new node should be inserted at the start
    if (!*head || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    // Iterate to find the correct position for insertion
    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    // Insert the new node at the correct position
    new_node->next = current;
    if (prev)
        prev->next = new_node;

    return (new_node);
}

int main() {
    listint_t *head = NULL;
    listint_t *new_node;

    new_node = insert_node(&head, 5);
    if (!new_node)
        printf("Error inserting node\n");

    // ... Additional code/testing as needed ...

    return 0;
}
