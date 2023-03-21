from mycroft import MycroftSkill, intent_file_handler


class BreathingExercise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('exercise.breathing.intent')
    def handle_exercise_breathing(self, message):
        self.speak_dialog('exercise.breathing')


def create_skill():
    return BreathingExercise()

