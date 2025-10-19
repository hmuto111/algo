mapping = {
    "(": ")",
    "[": "]",
    "{": "}",
}

def is_balanced(s: str) -> bool:
    stack = []

    for ch in s:
        if ch in mapping:
            stack.append(ch)
        else:
            if not stack:
                return False

            op = stack.pop()
            if mapping[op] != ch:
                return False
    
    return not stack

def main() -> None:
    s = "[[[["
    print(is_balanced(s))

main()
