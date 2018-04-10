import numpy

class Noun(object ):
    def __init__(self, word, articles=[]):
        self.word = word
        self.articles = {}
        for article in articles:
            self.articles[article] = 0

    def addArticle(self, art):
        for article in self.articles.keys():
            if art.upper() == article.upper():
                self.articles[article] += 1


    def printCounts(self):
        for art in self.articles.keys():
            if self.articles[art] > 0:
                print ("%s : %d" % ())
    
    def __eq__(self, other):
        if self.word == other:
            return True
        else:
            return False
        

articles = ['der', 'die', 'das', 'den', 'dem', 'des', 'einer', 'ein', 'eine', 'einem', 'einen', 'eines', 'kein', 'keine', 'keiner', 'keinen', 
            'diese', 'dieser', 'diesen', 'diesem', 'dieses',
            'jede', 'jeder', 'jeden', 'jedem', 'jedes',
            'jemand', 'jemander', 'jemanden', 'jemandem', 'jemandes',
            'welche', 'welcher', 'welchen', 'welchem', 'welches',
            'solche', 'solcher', 'solchen', 'solchem', 'solches',
            'mache', 'mancher', 'manchen', 'manchem', 'manches',
            'jene', 'jener', 'jenen', 'jenem', 'jenes',
            'alle', 'aller', 'allen', 'allem', 'alles',
            'beide', 'beider', 'beiden', 'beidem', 'beides',
            'mein', 'meine', 'meinem', 'meiner', 'meines', 'meinen',
            'dein', 'deine', 'deinem', 'deiner', 'deines', 'deinen',
            'sein', 'seine', 'seinem', 'seiner', 'seines', 'seinen',
            'ihr', 'ihre', 'ihrem', 'ihrer', 'ihres', 'ihren',
            'unser', 'unsere', 'unserem', 'unserer', 'unseres', 'unseren',
            'euer', 'euere', 'euerem', 'euerer', 'eueres', 'eueren']

f = open("FAZ.txt", 'r')

library = []

text = f.read()
endOfSentence = True
for word in text.split():
    if word.lower() in articles:
        currentArticle = word
    if word[0].isupper() and not(endOfSentence):
        if (word in library) and (currentArticle != ''):
            library[library.index(word)].addArticle(currentArticle)
        print currentArticle, word
        n = Noun(word)
        if currentArticle != '':
            n.addArticle(currentArticle)
        currentArticle = ''
        library.append(n)

    if word[-1] == '.':
        endOfSentence = True
    else:
        endOfSentence = False

f.close()

for word in library:
    print word.articles
