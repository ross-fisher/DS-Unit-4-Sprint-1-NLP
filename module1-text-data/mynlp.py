#from spacy.tokenizer import Tokenizer
#tokenizer = Tokenizer(nlp.vocab)
import pandas as pd
from collections import Counter
import spacy
from spacy.tokenizer import Tokenizer

nlp = spacy.load('en_core_web_lg')
tokenizer = Tokenizer(nlp.vocab)

def create_wordcount_table(tokens_column):
    """tokens: sequence of strings"""
    word_counts = Counter()
    appears_in = Counter()
    
    for tokens in tokens_column:
        word_counts.update(tokens)
        appears_in.update(set(tokens))

    temp = zip(word_counts.keys(), word_counts.values())
    wc = pd.DataFrame(temp, columns=['word', 'count'])
    wc['rank'] = wc['count'].rank(method='first', ascending=False)
    total = wc['count'].sum()
    assert total > 0

    wc['freq'] = wc['count'].apply(lambda x: x / total)
    wc = wc.sort_values(by='rank')

    wc['cumfreq'] = wc['freq'].cumsum()

    t2 = zip(appears_in.keys(), appears_in.values())
    ac = pd.DataFrame(t2, columns=['word', 'appears_in_count'])
    wc = ac.merge(wc, on='word')
    wc['appears_in_freq'] = wc['appears_in_count'].apply(lambda x: x / len(wc))

    return wc.sort_values(by='rank')



