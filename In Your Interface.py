class Teams:
    
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    #solution to question 1)
    def __contains__(self, substring):
        if substring in self.__myTeam:
            return True
        else:
            return False
    
    #solution to question 2)
    def __iter__(self):
        self.current_index = 0
        return self
    
    def __next__(self):
        if self.current_index < len(self.__myTeam):
            x = self.__myTeam[self.current_index]
            self.current_index += 1
            return x
        raise StopIteration

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))
    
    #running contains method of question 1)
    print ('Tim' in classmates)
    print ('Sam' in classmates)
    
    #running iteration method of question 2)
    iter_classmates = classmates.__iter__()
    try:
        print(iter_classmates.__next__())
        print(iter_classmates.__next__())
        print(iter_classmates.__next__())
    except:
        pass
    
main()

#Question 3)
    #Yes, the class 'classmates' implements the __len__ method defined above.
    #The program will not be able to recognize the length of the classmates class
    #without that __len__ method

#Question 4)
    #The difference between interfaces and implementation are as follows:
    #The interface describes the 'what?' of a structure, while
    #implementation describes the 'how?' of the structure. The interface will
    #only tell us a list of supported operations and arguments. The implementation
    #however, shows us the definitions of the algorithms that implement said operations
    #and arguments. There can also be multiple
    #ways to implement any given interface. For example, a list interface can
    #be implemented using an array or using pointer-based structures

#Question 5)
    #I would design an interface that allows you to choose and allocate which specific
    #data is stored in a certain way, based on user preference and storage capabilities.
    #It would be able to tell the user how storing certain data in a certain implementation
    #would affect the applications overall performance, as well as the ability for it to read and
    #write the data. 