from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import re
import codecs

class FrequencySummarizer:
    def __init__(self, low_thresh=0.1, high_thresh=0.9):
        """
         Initialize the text summarizer.
         Words that have a frequency term lower than low_thresh 
         or higer than high_thresh will be ignored.
        """
        ignore = ['fig','figure','ibid', 'et al','cf','NB','N.B.']
        
        self._low_thresh = low_thresh
        self._high_thresh = high_thresh 
        self._stopwords = set(stopwords.words('english') + list(punctuation) + list(ignore))

    def _compute_frequencies(self, word_tk):
        """Input: tokenized words.
        Output: a dictionary containing a bunch of words and frequencies for those words."""
        freq = defaultdict(int)
        for s in word_tk:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        # frequencies normalization and fitering
        m = float(max(freq.values()))
        for w in freq.keys():
            freq[w] = freq[w]/m
            if freq[w] >= self._high_thresh or freq[w] <= self._low_thresh:
                del freq[w]
        return freq

    def result(self, text, word="secretary"):
        """
            Return a list of n sentences 
            which represent the summary of text.
        """
        text = unicode(text, errors='ignore')
        sents = sent_tokenize(text)
        word_tk = [word_tokenize(s.lower()) for s in sents if word in s.lower()]
        return self._compute_frequencies(word_tk)