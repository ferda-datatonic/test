def simplifyPath(self, path: str) -> str:
    if path[-1] == "/":
        path = path[:-1]
    if path[0]!="/":
        path = "/"+path 
    indices = []

    for i in range(len(path)):
        if path[i] == "/":
            indices.append(i)
    path = list(path)
    for i in range(len(indices[::-1])):
        if i == len(indices)-1:
            pass
        else:
            if abs(indices[i]-indices[i+1])==1:
                path.pop(indices[i])
    stack = []
    while path != []:
        curr = path.pop(0)
        if stack == []:
            stack.append(curr)
        elif curr != "." and curr !="_":
            stack.append(curr)
        else:
            continue
    return "".join(stack)