from mycroft import MycroftSkill, intent_file_handler
import time

 

class BreathingExercise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

 

    @intent_file_handler('exercise.breathing.intent')
    def handle_exercise_breathing(self, message):
        self.speak_dialog('exercise.breathing', wait=True)
        time.sleep(1)
        self.wait_while_speaking()

 

def create_skill():
    return BreathingExercise()
