s = input()

hello = "hello"
pointer = 0

for char in s:
    if char == hello[pointer]:
        pointer += 1
        if pointer == len(hello):
            print("YES")
            break

if pointer != len(hello):
    print("NO")