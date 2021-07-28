from inttree import *

T = tree([1, 2, 3, 4, 5])
tree_insert(T,(1, 4))
tree_insert(T,(2, 5))
tree_print(T)
tree_remove(T,(1, 4))
tree_print(T)
tree_insert(T,(1, 3))
print(tree_intersect(T, 3))


