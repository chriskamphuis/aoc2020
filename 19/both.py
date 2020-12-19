f = open('input.txt', 'r').read()
cfg, messages = f.split('\n\n')
cfg = {k:v for k, v in [line.strip().split(': ') for line in cfg.split('\n')]}
messages = messages.split('\n')

def is_valid(rules, message):
    if len(rules) == len(message) == 0:
        return True
    elif len(rules) == 0 or len(message) == 0:
        return False
    head = cfg[rules[0]]
    tail = rules[1:]
    if '"' in head:
        letter = head[1]
        return head[1] == message[0] and is_valid(tail, message[1:])
    if '|' in head:
        subs = head.split(' | ')
        return any([is_valid(s.split(' ') + tail, message) for s in subs])
    else:
        return is_valid(head.split(' ') + tail, message)

print(len([1 for msg in messages if is_valid(["0"], msg)]))

cfg['8'] = '42 | 42 8'
cfg['11'] = '42 31 | 42 11 31'

print(len([1 for msg in messages if is_valid(["0"], msg)]))
