"""
Notes:

decrypt('hgy ok whyngr', 1)
decrypt('hgy ok whyngr', 2)
decrypt('hgy ok whyngr', 3)
...
decrypt('hgy ok whyngr', 25)
"""

"""
asd ka hyhrtw
kds iu okyhgf
iwn is okhsti
...
dog is hungry    => key 7
...
ahmad is fghjk
ths ik okstgr
jug sd plwrdw
cat jh hujgru
"""

import nltk
# nltk.download('words')

original_words_list = nltk.corpus.words.words()
# print(words_list[30000:30100])
words_list = [word.lower() for word in original_words_list]

# For any given sentence, how many english words are there?
def count_words(sentence):
    sentence_words = sentence.split()
    en_word_count = 0

    for word in sentence_words:
        if word.lower() in words_list:
            en_word_count += 1

    return en_word_count

def most_likely(sentences):
    _max = 0
    _max_sentence = ''

    for sentence in sentences:
        if count_words(sentence) > _max:
            _max_sentence = sentence
            _max = count_words(sentence)
    return _max_sentence

if __name__ == "__main__":
    sentence = 'John Is Hungry'
    print(count_words(sentence))
    sentences = [
        'asd ka hyhrtw',
        'kds iu okyhgf',
        'iwn is okhsti',
        'dog is hungry',
        'ahmad is fghjk',
        'ths ik okstgr',
        'jug sd plwrdw',
        'cat jh hujgru'
    ]
    print(most_likely(sentences))
