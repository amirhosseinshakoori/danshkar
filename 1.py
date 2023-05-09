"""
This code opens a text file, searches for English numbers up to twenty and converts them to their Persian equivalents. Then, for each line in which these changes have been made, a new line is created and, finally, the result is saved in an output file.
"""

with open("Zen.txt", "r") as input_file:
    text = input_file.read()


number_words = {
    "one ": "1",
    "two ": "2",
    "three ": "3",
    "four ": "4",
    "five": "5",
    "six ": "6",
    "seven ": "7",
    "eight ": "8",
    "nine ": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20"
}


lines = text.split("\n")
new_lines = []


for line in lines:
    index = line.find(")")
    if index != -1:
        text_before_parenthesis = line[:index]
        for word, number in number_words.items():
            if word in text_before_parenthesis:
                line = line.replace(word, number)
    new_lines.append(line)


new_text = "\n".join(new_lines)


with open("output.txt", "w") as output_file:
    output_file.write(new_text)