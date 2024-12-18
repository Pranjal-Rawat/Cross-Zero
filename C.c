#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *front = NULL;
struct node *rear = NULL;

void enqueue(int data) {
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = NULL;

    if (front == NULL && rear == NULL) {
        front = rear = new_node;
    } else {
        rear->next = new_node;
        rear = new_node;
    }
}

int dequeue() {
    if (front == NULL && rear == NULL) {
        printf("Queue is empty\n");
        return -1;
    } else {
        int data = front->data;
        front = front->next;
        if (front == NULL) {
            rear = NULL;
        }
        return data;
    }
}

void display() {
    struct node *temp = front;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    enqueue(34);
    enqueue(22);
    enqueue(75);
    enqueue(99);
    enqueue(27);

    printf("Circular Queue: ");
    display();

    int data = dequeue();
    printf("Circular Queue After dequeue: ");
    display();

    return 0;
}