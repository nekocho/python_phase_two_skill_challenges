def grammar_check(text):
    if text == "":
        raise Exception("No text provided!")
    elif text[-1] != ".":
        return text.capitalize() + "."
    elif text[0].isupper() == False:
        return text.capitalize()
    else:
        return text