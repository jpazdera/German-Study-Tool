class Word_Pair: 
    
    def __init__(self, german_word, english_word):
        assert (type(german_word) == str and type(english_word) == str)
        self.german = german_word
        self.english = english_word
        
    def __str__(self):
        return ("Word_Pair(\'" + self.german + "\', \'" + self.english + "\')")


def Generate_Vocab_List():
    vocab_list = []
    while True:
        new_german_word = raw_input('German word: ')
        if new_german_word == "DONE":
            break
        new_english_word = raw_input('English translation: ')
        if new_english_word == "DONE":
            break
        new_pair = Word_Pair(new_german_word, new_english_word)
        vocab_list = vocab_list + [str(new_pair)]
    print str(vocab_list).replace('\"', '') # remove all double quotes from around Word_Pair() in the printed output; this will format it properly for pasting directly into chapter vocab list