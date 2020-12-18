from pprint import pprint

def construct_eval_tree_p1(expression): 
    i = 0
    start = True
    ops = []
    while i < len(expression):
        c = expression[i]
        if c == '(':
            j = i + 1
            depth = 0
            while not (expression[j] == ')' and depth == 0):
                c2 = expression[j]
                if c2 == '(':
                    depth+=1
                if c2 == ')':
                    depth-=1
                j+=1
            subexpression = expression[i+1:j]
            ops.append(construct_eval_tree_p1(subexpression))
            i=j
        if c in '+*':
            ops.append(c)
        if c.isdigit():
            ops.append(c)
        i+=1
    return ops

def eval_tree(tree):
    while('+' in tree):
        for i in range(len(tree) - 1):
            if tree[i] == '+':
                a = tree[i-1] if type(tree[i-1]) == str else eval_tree(tree[i-1])
                b = tree[i+1] if type(tree[i+1]) == str else eval_tree(tree[i+1])
                tree = tree[:i-1] + [str(int(a)+int(b))] + tree[i+2:]
                break
    while('*' in tree):
        for i in range(len(tree) - 1):
            if tree[i] == '*':
                a = tree[i-1] if type(tree[i-1]) == str else eval_tree(tree[i-1])
                b = tree[i+1] if type(tree[i+1]) == str else eval_tree(tree[i+1])
                tree = tree[:i-1] + [str(int(a)*int(b))] + tree[i+2:]
                break
    return tree[0]

print(sum([int(eval_tree(construct_eval_tree_p1(line))) for line in open('input.txt', 'r')]))
