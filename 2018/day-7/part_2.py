import sys

REQS = {}

def iterate_nodes(num_workers):
    done = []
    in_stack = []
    in_queue = [-1] * num_workers
    in_stack += possible_nodes(done, in_stack)
    while len(done) != 26:
        done.append(in_stack.pop())
        in_stack += possible_nodes(done, in_stack)
        in_stack.sort(reverse = True)
    print(possible_nodes(done, in_stack))
    return done


def possible_nodes(done, in_stack):
    new_nodes = []
    for key, value in REQS.items():
        if done == [] and value == []:
            new_nodes.append(key)
        elif set(value).issubset(set(done)) and key not in in_stack and key not in done:
            new_nodes.append(key)
    return new_nodes

def main():
    for val in open(sys.argv[1]).readlines():
        split_val = val.split(' ')
        step = split_val[7]
        req_step = split_val[1]
        if step not in REQS:
            REQS[step] = [req_step]
        else:
            REQS[step].append(req_step)

        if req_step not in REQS:
            REQS[req_step] = []

    print(REQS)
    done = iterate_nodes()
    print(''.join(done))

if __name__ == "__main__":
    main()
