class Student:
    '''A student class that says hello and raises their hand to get attention.'''
    
    def hello(self):
        '''Says a brief greeting.'''
        print("Hey there! I'm so excited to learn stuff.")
    
    def raise_hand(self):
        '''Respectfully tries to get the teacher's attention.'''
        print("Pick me!")

class ChattyStudent(Student):
    '''A student that is chatty and raises their hand multiple times.'''
    
    def hello(self):
        '''Says a greeting, then tries to spoil a TV show.'''
        print("Hey there! I'm so excited to learn stuff.")
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        '''Respectfully tries to get the teacher's attention ten times.'''
        for _ in range(10):
            print("Pick me!")
