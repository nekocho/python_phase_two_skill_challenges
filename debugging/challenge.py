def get_most_common_letter(text):
    counter = {}
    split_text = text.split()
    text = "".join(split_text)
    for char in text:
        # print(f"This is char in text: {char}")
        counter[char] = counter.get(char, 0) + 1
    print(f"This is counter: {counter}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    #print(f"This is sorted counter: {sorted(counter.items())}")
    print(f"This is letter without the index: {sorted(counter.items(), key=lambda item: item[1])}")
    print(f"This is result of letter: {letter}")

    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")