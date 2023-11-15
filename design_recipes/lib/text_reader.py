def text_reader(text):
    if len(text.split()) > 0:
        time_taken_to_read = len(text.split()) / 200
        return f"It would take you {time_taken_to_read} minutes to read this text"
    else:
        raise Exception("No text entered")