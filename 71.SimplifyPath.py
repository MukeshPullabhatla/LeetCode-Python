def simplifyPath(path: str) -> str:
    stack = []
    path = path.split("/")
    for p in path:
        if stack and p == "..":
            stack.pop()
        elif p not in [".","",".."]:
            stack.append(p)
    return "/"+"/".join(stack)

path = "/home/"
path1 = "/../"
path2 = "/home//foo/"
print(simplifyPath(path))
print(simplifyPath(path1))
print(simplifyPath(path2))