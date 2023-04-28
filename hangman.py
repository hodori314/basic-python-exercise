'''
Class and Object-Oriented Programming  

- Make hangman game using Class
- Descriptions of methods are commented with methods.
- Implement TODO parts.

'''

class Game():
    # field
    guessWord = set()
    answerWord = ""
    life = 0
    vocabulary = ['apple', 'orange', 'melon', 'library', 'coffee']

    def __init__(self, life):
        ''' 
        randomly choose answerWord from vocabulary
        set life to argument life
        '''
        # TODO
        pass

    def guess(self, c):
        '''
        case 1) already exist: 
          print "You tried it before."
        
        case 2) game finished with correct answer
          print "Correct! The answer was %s"%(answerWord)
        
        case 3) wrong 'c':
          add c to guessWord
          decrease life by 1
          if life become 0 then print "You died!"
          else print "Wrong!"
        
        case 4) right 'c':
          add c to guessWord
          print "Right!"
        '''
        # TODO
        pass

    def printStatus(self):
        '''
        example for
        guessWord = {a, l, e}
        answerWord = "apple"
        life = 5
        
        print below
        +-----------+
        | a _ _ l e |
        +-----------+
         ♥ ♥ ♥ ♥ ♥ 
         a, l, e
        '''
        # TODO
        pass

    def updateVocab(self, newVocabs):
        '''
        newVocabs looks like [ 'vocab1', 'vocab2', ... ]
        add vocab which does not exist in the original vocabulary
        '''
        # TODO

    
    ### DON'T TOUCH ###
        print(self.vocabulary)
    
    def setAnswerWord(self, word):
        self.answerWord = word
    ### DON'T TOUCH ###

def test():
    game1 = Game(5)
    game1.setAnswerWord('apple')

    print('-------------------- TEST 1-1 --------------------')
    print('your answer >>', end="")
    game1.guess('a')
    print('     answer >>', end="")
    print("Right!")

    print('-------------------- TEST 1-2 --------------------')
    print('your answer >>', end="")
    game1.guess('l')
    print('     answer >>', end="")
    print("Right!")

    print('-------------------- TEST 1-3 --------------------')
    print('your answer >>', end="")
    game1.guess('e')
    print('     answer >>', end="")
    print("Right!")

    print('-------------------- TEST 2 --------------------')
    print('your answer >>', end="")
    game1.guess('b')
    print('     answer >>', end="")
    print("Wrong!")

    print('-------------------- TEST 3 --------------------')
    print('your answer >>', end="")
    game1.guess('a')
    print('     answer >>', end="")
    print("You tried it before.")

    print('-------------------- TEST 4 --------------------')
    print('your answer >>')
    game1.printStatus()
    print('     answer >>')
    print('+-----------+')
    print('| a _ _ l e |')
    print('+-----------+')
    print(' ♥ ♥ ♥ ♥ ')
    print(' a, l, e, b')

    print('-------------------- TEST 5 --------------------')
    print('your answer >>', end="")
    game1.guess('p')
    print('     answer >>', end="")
    print ("Correct! The answer was %s"%('apple'))

    game2 = Game(5)
    print('-------------------- TEST 6 --------------------')
    print('your answer >>', end="")
    game2.updateVocab('apple')
    print('     answer >>', end="")
    print('[\'apple\', \'orange\', \'melon\', \'library\', \'coffee\']')

test()
