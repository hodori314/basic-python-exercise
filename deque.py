'''
Dequeue

- implement your dequeue not using collection modules and existing list methods
  (e.g., Don't call list method append() in your implementation of append)

'''

import collections 

class myDequeue:
    def __init__(self, givenValues=[]):
        self.values = givenValues.copy()

	  ##### DON'T NEED TO KNOW #####

    def __getitem__(self, idx):
        if idx == 0:
            return self.values[0]
        elif idx in range(0, sum([1 for val in self.values])):
            return self.values[idx]
        elif idx == -1:
            return self.values[-1]
        else:
            raise IndexError
    
    def __str__(self):
        _print = f'deque({self.values})'
        return _print
    
    ##### DON'T NEED TO KNOW #####

    def append(self, val):
        # TODO
        pass

    def appendleft(self, val):
        # TODO
        pass

    def pop(self):
        # TODO
        pass

    def popleft(self):
        # TODO
        pass

    def index(self, ele, beg, end):
        # TODO
        pass

    def insert(self, i, a):
        # TODO
        pass

    def remove(self, target):
        # TODO
        pass

    def count(self, target):
        # TODO
        pass

# test your code

def test():
    testDequeue = myDequeue([ i for i in range(10)])
    answerDequeue = collections.deque([ i for i in range(10)])

    print('---------- test #1-1(append) --------------')
    testDequeue.append(10)
    answerDequeue.append(10)
    print('your answer:', testDequeue)
    print('     answer:', answerDequeue)
    print()

    print('---------- test #1-2(appendleft) ----------')
    testDequeue.appendleft(-1)
    answerDequeue.appendleft(-1)
    print('your answer:', testDequeue)
    print('     answer:', answerDequeue)
    print()

    print('---------- test #2-1(pop) -----------------')
    testDequeue.pop()
    answerDequeue.pop()
    print('your answer:', testDequeue)
    print('     answer:', answerDequeue)
    print()

    print('---------- test #2-2(popleft) -------------')
    testDequeue.popleft()
    answerDequeue.popleft()
    print('your answer:', testDequeue)
    print('     answer:', answerDequeue)
    print()

    print('---------- test #3-1(index) ---------------')
    print('your answer:', testDequeue.index(5, beg=0, end=8))
    print('     answer:', answerDequeue.index(5))
    print()

    print('---------- test #4-1(insert) --------------')
    testDequeue.insert(3, 2.5)
    answerDequeue.insert(3, 2.5)
    print('your answer:', testDequeue)
    print('     answer:', answerDequeue)
    print()

    print('---------- test #5-1(remove) --------------')
    testDequeue.remove(2.5)
    answerDequeue.remove(2.5)
    print('your answer:', testDequeue)
    print('     answer:', answerDequeue)
    print()

    print('---------- test #6-1(count) ---------------')
    print('your answer:', testDequeue.count(2.5))
    print('     answer:', answerDequeue.count(2.5))
    print()

    print('---------- test done! ---------------------')

test()
