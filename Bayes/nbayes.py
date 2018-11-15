import math

from collections import defaultdict

class NBayes(object):
    def __init__(self, trainSet):
        self.data = trainSet
        self.tags = defaultdict(int)
        self.tagwords = defaultdict(int)
        self.total = 0

    def _tokenizer(self, sent):
    	return list(sent)

    def train(self):
    	for tag, doc in self.data
    	words = self._tokenizer()
