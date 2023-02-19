# python3
# Alens Ilgavižs 221RDB312 4.grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, 1):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            # Process opening bracket, write your code here

        if next in ")]}":
            if not opening_brackets_stack:
                return i
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i
        # Process closing bracket, write your code here
        if opening_brackets_stack:
            top = opening_brackets_stack.pop()
            return top.position

        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    bruh = input()
    if bruh == "I":
        text = input()
        main()
    else:
        with open() as f:
            for line in f:
                text = line.strip()
                mismatch = find_mismatch(text)
                print(mismatch)
