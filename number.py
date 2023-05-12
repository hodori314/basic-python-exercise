import doctest

class ComplexNumber:
    a = 0; b = 0  # a + bi
    def __init__(self, a_, b_):
        '''
        Initialize ComplexNumber class

        Example
        -------
        >>> print(ComplexNumber(10, 20))
        10 + 20i
        '''
        pass

    def __str__(self):
        '''
        Print ComplexNumber class

        Example
        -------
        >>> print(ComplexNumber(10, 20))
        10 + 20i
        '''
        pass
     
    def __add__(self, anotherComplexNumber):
        '''
        Add two complex number

        Example
        -------
        >>> print(ComplexNumber(10, 20) + ComplexNumber(20,10))
        30 + 30i
        '''
        pass

    def __iadd__(self, anotherComplexNumber):
        '''
        Add two complex number and save to the origin

        Example
        -------
        >>> C = ComplexNumber(10, 20); C += ComplexNumber(20, 10); print(C)
        30 + 30i
        '''
        pass

class NaturalNumber(ComplexNumber):
    def __init__(self, _):
        '''
        Initialize Natural Number class
        If given number is not natural number, then raise NotImplementedError

        Example
        -------
        >>> print(NaturalNumber(10))
        10
        '''
        pass


    def __str__(self):
        '''
        Print NaturalNumber class

        Example
        -------
        >>> print(NaturalNumber(10))
        10
        '''
        pass
    
    def __add__(self, n):
        '''
        Add two natural number

        Example
        -------
        >>> print(NaturalNumber(10) + NaturalNumber(20))
        30
        '''
        pass
    
    def __iadd_(self, n):
        '''
        Add two natural number and save to the origin

        Example
        -------
        >>> N = 5; N += 10; print(N)
        15
        '''
        self.a += n
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
