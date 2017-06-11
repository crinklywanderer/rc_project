import nltk
import time

contentArray = ['i am aayush sonkar.', 'I AM AAYUSH SONKAR7.', ]


def process_language():
    try:
        for item in contentArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print(tagged)

            named_ent = nltk.ne_chunk(tagged)
            named_ent.draw()

            time.sleep(1)

    except Exception, e:
        print(str(e))
process_language()
