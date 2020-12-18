class EvalTree:
    def __init__(self, l=None, r=None, op=None):
        self.l = l
        self.r = r
        self.op = op

    def evaluate(self):
        left = self.l if type(self.l) == int else self.l.evaluate()
        right = self.r if type(self.r) == int else self.r.evaluate()
        return self.op(left, right)     
    
def construct_eval_tree(expression):
    tree = EvalTree()
    i = 0
    start = True
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
            subtree = construct_eval_tree(subexpression)
            if start: 
                tree.r = subtree
                start=False
            else:
                tree.l = subtree
                new = EvalTree(r=tree)
                tree = new
            i=j-1
        if c == '+':
            tree.op = int.__add__
        if c == '*': 
            tree.op = int.__mul__
        if c.isdigit():
            if start:
                tree.r = int(c)
                start = False
            else:
                tree.l = int(c)
                new = EvalTree(r=tree)
                tree = new
        i+=1
    return tree.r

print(sum([construct_eval_tree(line).evaluate() for line in open('input.txt', 'r')]))
