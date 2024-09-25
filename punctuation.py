import string

def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation to None
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

# Example usage
input_text = "Hello, World! Welcome to Python programming."
cleaned_text = remove_punctuation(input_text)
print(cleaned_text)  # Output: Hello World Welcome to Python programming
