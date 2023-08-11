#ifndef LINKED_LIST_H
#define LINKED_LIST_H

// Type definitions
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

// Function prototypes
listint_t *insert_node(listint_t **head, int number);

#endif /* LINKED_LIST_H */
