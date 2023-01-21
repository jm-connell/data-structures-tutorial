# Trees
## Introduction
Trees have much in common with [linked lists](2-linked-list.md), the main difference being that each element in a linked list only points to a single element, while a tree can have multiple pointers on each element or **node**.<br>
In programming, trees are most often implemented as **binary trees** where each node can only lead to at most 2 other nodes. A **binary search tree (BST)** is a binary tree where the data is organized in a specific way to allow for efficient search.<br>
![Diagram of a Binary Search Tree](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-Diagram-2-7.png)
<br>*Binary Search Tree - Credit to GeeksforGeeks.org*<br><br>
For example, if we want to look for node 7, we start at the **root**, which in this case is node 8. If we're looking for 7, we know that 7 is less than 8, so we will take the path with the lower value from node 8. This takes us to node 3 where we repeat the process. 7 is greater than 3, so we take the path with the higher value to node 6. Repeat the proces one more time, and we arrive at node 7. 

## Performance
If we are looking to see if a value is in a data set there are more efficient data structures, such as a dictionary. However, binary search trees are much faster for adding and removing any given node. In a BST, you can add or remove a node at an efficiency of O(log n). This is because each time you perform the comparision operation and move down a layer in the tree, you are effectively cutting your search pool in half. This means if you double your data set size, it would only require one additional operation to find the correct location.<br>
It's important to note that in order to achieve maximum efficiency, a **balanced binary search tree** must be used. A balanced BST requires that the length from the root to any given two leaves cannot be significantly different. In general the difference in length from root to leaf, or **height**, should be less than 2.

## Uses
Binary search trees are very useful in maintaining a data set that is easily searchable but is also flexible in allowing frequent changes. Imagine you have a data set with 20,000 elements that are constantly changing. If you tried to use a list or a set, you would run into efficiency problems in searching and maintaining the data.<br>

## Python
Python does not have a built-in class for creating binary search trees, however you can install packages that allow for easier use of BST's. A common example from *pypi.org* is [bintrees](https://pypi.org/project/bintrees/) which can be installed using the `pip install bintrees` command in the terminal. The newer version of bintrees from *pypi.org* is called [sortedcontainers](https://pypi.org/project/sortedcontainers/).<br>
The most common operations used with BST's are inserting/removing nodes, contains(*value*), height(*node*), traverse forward/backward, size(), and empty().