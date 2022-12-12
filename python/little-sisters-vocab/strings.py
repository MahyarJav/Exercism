"""Functions for creating, transforming, and adding prefixes to strings."""
def add_prefix_un(word):
    new_word = "un"+ word
    return new_word
def make_word_groups(vocab_words):
    return f' :: {vocab_words[0]}'.join(vocab_words)
def remove_suffix_ness(word):
    new_word = word[:-4]
    if new_word[-1] == "i":
        return new_word[:-1]+"y"
    return new_word
def adjective_to_verb(sentence, index):
    split_sentence = sentence.split(" ")[index]
    if split_sentence[-1] == ".":
        return f"{split_sentence[:-1]}en"
    return f"{split_sentence}en"
