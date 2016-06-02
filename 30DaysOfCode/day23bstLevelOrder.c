#include<stdio.h>
#include<stdlib.h>

typedef struct _tnode {
	int data;
	struct _tnode *left;
	struct _tnode *right;
}tnode;

typedef struct _qnode {
	tnode *tree;
	struct _qnode *next;
}qnode;

void bst_destroy (tnode *tree)
{
	if (tree == NULL)
		return;
	bst_destroy(tree->left);
	bst_destroy(tree->right);
	free(tree);
}

void print_postorder (tnode *list)
{
	if (list == NULL)
		return;
	print_postorder(list->left);
	print_postorder(list->right);
	printf("%d ", list->data);
}

tnode *createNewNode(int data)
{
	tnode *new_node = (tnode *)malloc(sizeof(tnode));
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->data = data;
	return new_node;
}

tnode *insert(tnode *root, int data)
{
	if (root == NULL) {
		return createNewNode(data);
	}
	if (data <= root->data) {
		root->left = insert(root->left, data);
	}
	else {
		root->right = insert(root->right, data);
	}
	return root;
}


qnode *createNewQueue(tnode *root)
{
	qnode *new_queue = (qnode *)malloc(sizeof(qnode));
	new_queue->tree = root;
	new_queue->next = NULL;
	return new_queue;
}

void enqueue(qnode **q, tnode *root)
{
	qnode *new_node = createNewQueue(root);
	qnode dummy;
	dummy.next = *q;
	qnode *prev = &dummy;
	qnode *curr = *q;
	while (curr != NULL) {
		prev = curr;
		curr = curr->next;
	}
	prev->next = new_node;
	new_node->next = curr;
	*q = dummy.next;
}

qnode *dequeue(qnode **q)
{
	qnode *removed_node = *q;
	*q = (*q)->next;
	removed_node->next = NULL;
	return removed_node;
}

void levelOrder(tnode *root) 
{
	if (root == NULL)
		return;
	qnode *q = NULL;
	enqueue(&q, root);
	while (q != NULL) {
		qnode *removed_node = dequeue(&q);
		printf("%d ", removed_node->tree->data);
		if(removed_node->tree->left != NULL) {
			enqueue(&q, removed_node->tree->left);		
		}
		if(removed_node->tree->right != NULL) {
			enqueue(&q, removed_node->tree->right);
		}
		free(removed_node);
	}
}

int main(int argc, char **argv) {
	tnode* root = NULL;
	int T, data;
	printf("Enter number of elements in Binary Search Tree\n");\
	scanf("%d", &T);
	printf("Enter %d numbers of the bst\n", T);
	while(T-- > 0) {
		scanf("%d", &data);
		root = insert(root, data);	
	}
	print_postorder(root);
	printf("\n");
	levelOrder(root);
	printf("\n");
	bst_destroy(root);
	return EXIT_SUCCESS;
}

