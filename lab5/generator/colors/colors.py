from termcolor import colored


def paintText(text, color):
    if (len(color)):
        painted = colored(text, color)
        return painted
    else:
        return text


def textFileSaver(filename, text):
    with open(filename, "w") as file:
        file.write(text)
    print(f"text  was saved into {filename}")
