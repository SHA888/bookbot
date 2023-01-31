with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    print(f"The file frankenstein.txt has about {num_words} words.")