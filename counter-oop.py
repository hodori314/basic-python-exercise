'''
Counter

- implement your Counter not using collection modules
- compared to `counter.py`, you have to implement constructor that support various cases of initialzation
- there would be empty counter, counter from an iterable, counter from a mapping, counter from keyword args.

'''
from collections import Counter

class myCounter():
    dict = {}

    def __init__(self, _):
        # TODO including arguments of __init__
        pass
    
    ##### DON'T NEED TO CONSIDER #####
    
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
    
    ##### DON'T NEED TO CONSIDER #####
    
    def most_common(self, n):
        # TODO
        pass

    def total(self):
        # TODO
        pass

    def elements():
        # TODO
        pass
    

def test():
    print('---------- test #1-1 (init empty) --------------')
    print('your answer:', myCounter())
    print('     answer:', Counter())

    print('---------- test #1-2 (init iterable) --------------')
    print('your answer:', myCounter('gallahad'))
    print('     answer:', Counter('gallahad'))

    print('---------- test #1-3 (init mapping) --------------')
    print('your answer:', myCounter({'red': 4, 'blue': 2}))
    print('     answer:', Counter({'red': 4, 'blue': 2}))

    print('---------- test #1-4 (init keyword arguments) --------------')
    print('your answer:', myCounter(cats=4, dogs=8))
    print('     answer:', Counter(cats=4, dogs=8)) 

    print('---------- test #2 (most_common) --------------')
    testCounter = myCounter('abracadabra')
    answerCounter = Counter('abracadabra')
    print('your answer:', testCounter.most_common(3))
    print('     answer:', answerCounter.most_common(3))

    print('---------- test #3 (total) --------------')
    testCounter = myCounter(a=10, b=5, c=0)
    answerCounter = Counter(a=10, b=5, c=0)
    print('your answer:', testCounter.total())
    print('     answer:', answerCounter.total())

    print('---------- test #4 (elements) --------------')
    testCounter = myCounter(a=4, b=2, c=0, d=-2)
    answerCounter = Counter(a=4, b=2, c=0, d=-2)
    print('your answer:', sorted(testCounter.elements()))
    print('     answer:', sorted(answerCounter.elements()))
