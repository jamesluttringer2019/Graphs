def earliest_ancestor(ancestors, starting_node):
    parents = {}
    for p, c in ancestors:
        
        if c in parents:
            parents[c].add(p)
        else:
            parents[c] = set([p])
    if starting_node not in parents:
        return -1
    stack = [[starting_node]]
    longest = [starting_node]
    while stack != []:
        print(stack)
        p = stack.pop()
        curr = p[-1]
        
        if len(p) > len(longest):
            longest = p
        elif len(p) == len(longest) and curr < longest[-1]:
            longest = p

        if curr in parents:
            for i in parents[curr]:
                stack.append(p+[i])
    return longest[-1]