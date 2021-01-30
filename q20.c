#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef int bool; 
#define true 1
#define false 0
#define MAX 10000

struct node_s
{
	char symbol; 
	struct node_s* next; 
}; 
typedef struct node_s node; 

int isEmpty(node** top_ref) {
    if (*top_ref == NULL)
        return 1; 
    return 0; 
}

void push(char symbol, node** top_ref)
{
	node* tmp = NULL; 
	tmp = (node *) malloc(sizeof(node)); 
	tmp->symbol = symbol; 
	tmp->next = *top_ref; 
	*top_ref = tmp;
}

char pop(node** top_ref)
{
	node* tmp = NULL;
    char ret;
    
    if (isEmpty(top_ref))
        return -1;

	tmp = *top_ref; 
	ret = tmp->symbol; 
	*top_ref = (*top_ref)->next; 
	free(tmp); 
	return ret;
}

bool isValid(char *s)
{
	node* stack = malloc(sizeof(node) * MAX);
    node* top = NULL; 		// poin to NULL first 
	int N = strlen(s);

    if (N == 1)
        return false; 

	for (int i = 0; i < N; i++)
	{
		// printf("s[%d] = %c\n", i, s[i]); 

		if (s[i] == 40 || s[i] == 91 || s[i] == 123) {
			push(s[i], &top);
		}
	    else if (s[i] == 41) {
			if (pop(&top) != 40)
				return false; 
		}
		else if (s[i] == 93) {
			if (pop(&top) != 91)
				return false; 
		}
		else if (s[i] == 125) {
			if (pop(&top) != 123)
				return false; 
		}	
	}
    
    if (isEmpty(&top))
	    return true; 
    
    return false; 
}

int main(int argc, char** argv)
{
	//char s[] = "()"; 
	//char s[] = "()[]{}"; 
	//char s[] = "(]"; 
	//char s[] = "([)]"; 
	char s[] = "{[]}"; 
	bool ret = isValid(s); 
	printf("s = %s, ret = %d\n", s, ret); 

	return 0; 
}