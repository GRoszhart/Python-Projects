class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print (self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    
    #code added for question 5 below:    
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'

def study_spell(Spell):
    print (Spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print (Accio())


#Questions:
    #Question 1:
        #Parent class is Spell, child classes are Accio and Confundo
    #Question 2:
        #Base class is Spell, subclasses are Accio and Confundo
    #Question 3:
        #Accio
        #Summoning Charm Accio
        #No description
        #Confunus Charm Confundo
        #"Causes the victim to become confused and befuddled."
    #Question 4:
        #It calls its own get_description method instead of the superclass' method
    #Question 5:
        #I added the following code to the Accio class:
            #def get_description(self):
                #return 'This charm summons an object to the caster, potentially over a significant distance'
        #You would also need to remove from the Spell class __str__:
            #self.name + ' ' + self.incantation + '\n' +
        #In order for it to only display the description and nothing else