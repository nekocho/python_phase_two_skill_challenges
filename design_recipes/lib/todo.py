def check_todo(text):
    if text == "":
        raise Exception("No text found!")
    elif "#TODO" in text:
        return True
    else:
        return False