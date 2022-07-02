 #딕셔너리의 키를 이해
class node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

tree1 = {}

def p_order(tree:dict, item:str):
    left = tree[item].left
    right = tree[item].right

    print(item, end = '')
    if left != '.':
        p_order(tree, left)
    if right != '.':
        p_order(tree, right)

def c_order(tree:dict, item:str):
    left = tree[item].left
    right = tree[item].right

    if left != '.':
        c_order(tree, left)
    print(item, end = '')
    if right != '.':
        c_order(tree, right)

def n_order(tree:dict, item:str):
    left = tree[item].left
    right = tree[item].right

    if left != '.':
        n_order(tree, left)
    if right != '.':
        n_order(tree, right)
    print(item, end = '')


n = int(input())
for i in range(0, n):
    item, left, right = map(str, input().split())
    tree1[item] = node(item, left, right)
p_order(tree1, 'A')
print('\n', end = '')
c_order(tree1, 'A')
print('\n', end = '')
n_order(tree1, 'A')
print('\n', end = '')
