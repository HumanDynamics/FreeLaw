from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation

class FrequencySummarizer:
    def __init__(self, text, low_thresh=0.2, high_thresh=0.7):
        """
         Initialize the text summarizer.
         Words that have a frequency term lower than low_thresh 
         or higer than high_thresh will be ignored.
        """
        ignore = ['fig','figure','ibid', 'et al','cf','NB','N.B.']
        
        self._low_thresh = low_thresh
        self._high_thresh = high_thresh 
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ignore)
        self.text = unicode(text, errors='ignore')
        self.sents = sent_tokenize(self.text)
        self._frequencies = {}

    def _compute_frequencies(self, word_tk):
        """Input: tokenized words.
        Output: a dictionary containing a bunch of words and frequencies for those words."""
        return [self.frequency(word) for word in word_tk]

    def cooccurence(self, word):
        """
        Returns other words that are frequently used in the same sentence as the input word.
        """
        word_tk = [word_tokenize(s.lower()) for s in self.sents if word in s.lower()]
        return self._compute_frequencies(word_tk)

    def sentiment(self):
        """Checks the sentiment of the text document. 
        IMPORTANT! MAXIMUM 80,000 CHARACTERS!
        Note: this relies on being able to do an os call, and having installed
        pexpect. pexpect is not a standard part of python, which is why the
        import is kept here, away from the critical parts."""
        from pexpect import run as OSCall
        string = 'curl -d "text=' + self.text + '" http://text-processing.com/api/sentiment/'
        x = OSCall(string)
        from simplejson import loads
        y = loads(x)['label']
        result = {'pos':'positive','neutral':'neutral','neg':'negative'}[y]+" "+str(loads(x)['probability'][y])
        return result

    def frequency(self,word):
        """Returns the fraction of sentences that contain this word. Autocaches."""
        if not self._frequencies.has_key(word):
            n = len(self.sents)
            self._frequences[word]=sum([1 if word.lower() in sent.lower(
                ) else 0 for sent in self.sents])/n
            if self._frequencies[word] >= self._high_thresh or self._frequencies[word] <= self._low_thresh:
                del self._frequencies[word]
        return self._frequencies[word]

    def jointFrequency(self,wordList,suppressWarnings=0):
        """Returns the number of sentences in which all words in wordList.
        wordList functions best if handed a list of strings."""
        total = 0
        # This function makes liberal abuse of the fact that 0 is false.
        if not len(wordList) and not suppressWarnings:
            print("Warning: wordList is empty.")
        for sent in self.sents():
            # Forgive me Guido, for I have used a for-else loop.
            total=total+1 if all(word.lower() in sent.lower() for word in wordList) else total
            
        if not total and not suppressWarnings:
            print("Warning:"+wordList+"is not found in any sentences.")
        return total/len(sents)

    def PMI(self,firstWord,secondWord):
        """PMI, or pointwise mutual information, is a good way of representing
        how much too words like or dislike each other. It divides
        the probability of both words appearing in a sentence by their 
        independent probabilities, and takes that log. Interpretation taken
        from https://slackprop.wordpress.com/2013/06/03/on-geek-versus-nerd/ .
        """
        firstFrequency = self.frequency(firstWord)
        secondFrequency = self.frequency(secondWord)
        jointFrequency = self.jointFrequency([firstWord,secondWord])
        from math import log
        return log(jointFrequency/(firstFrequency*secondFrequency))

if __name__ == "__main__":
    #May not work with windows.
    x = open("ComputationalLaw/Complete US Code/CompleteUSCode.txt").read()
    y=x[:len(x)/5]
    n = FrequencySummarizer(y)
    a = n.cooccurence("secretary")
    b = n.cooccurence("congress")
    c = n.PMI("secretary","shall")
    #print(n.sentiment())