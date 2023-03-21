from mycroft import MycroftSkill, intent_file_handler
import time 
class BreathingExercise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)     @intent_file_handler('exercise.breathing.intent')
    def handle_exercise_breathing(self, message):
        self.speak_dialog('exercise.breathing')
        time.sleep(1)  # wait for 1 second
        self.wait_while_speaking(timeout=10)  # wait for 10 seconds before continuing 
def create_skill():
    return BreathingExercise()
