'''
Counter

- implement your Counter not using collection modules

'''
from collections import Counter

class myCounter():
    dict = {}

    ##### DON'T NEED TO KNOW #####

    def __init__(self, values={}, **kwargs):
        if kwargs:
            self.dict = kwargs

        elif type(values) is dict:
            self.dict = values.copy()

        elif type(values) is str or type(values) is list:
            mapping = {}
            for i in values:
                if i in mapping.keys():
                    mapping[i] += 1
                else:
                    mapping[i] = 1
            self.dict = mapping
    
    def __getitem__(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 0

    def __str__(self):
        if bool(self.dict) is False:
            _print = f'Counter()'
        else: 
            _print = f'Counter({self.dict})'
        return _print
    
    ##### DON'T NEED TO KNOW #####
    
    def most_common(self, n):
        pass

    def total(self):
        pass

    def elements():
        pass
    

def test():
    print('---------- test #1 (most_common) --------------')
    testCounter = myCounter('abracadabra')
    answerCounter = Counter('abracadabra')
    print('your answer:', testCounter.most_common(3))
    print('     answer:', answerCounter.most_common(3))

    print('---------- test #2 (total) --------------')
    testCounter = myCounter(a=10, b=5, c=0)
    answerCounter = Counter(a=10, b=5, c=0)
    print('your answer:', testCounter.total())
    print('     answer:', answerCounter.total())

    print('---------- test #3 (elements) --------------')
    testCounter = myCounter(a=4, b=2, c=0, d=-2)
    answerCounter = Counter(a=4, b=2, c=0, d=-2)
    print('your answer:', sorted(testCounter.elements()))
    print('     answer:', sorted(answerCounter.elements()))
