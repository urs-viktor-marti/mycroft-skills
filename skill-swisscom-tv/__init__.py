# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'Urs-Viktor Marti, Swisscom PMK-TV-EDQ'

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.
LOGGER = getLogger(__name__)

class SwisscomTVSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(SwisscomTVSkill, self).__init__(name="SwisscomTVSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    def initialize(self):
        turn_tv_on_intent = IntentBuilder("TurnTVOn").requre("TurnTVOn").build()
        self.register_intent(turn_tv_on_intent, self.handle_turn_tv_on_intent)
        turn_tv_off_intent = IntentBuilder("TurnTVOff").requre("TurnTVOff").build()
        self.register_intent(turn_tv_off_intent, self.handle_turn_tv_off_intent)

    def handle_turn_tv_on_intent(self, message):
        self.speak_dialog("turn.tv.on")

    def handle_turn_tv_off_intent(self, message):
        self.speak_dialog("turn.tv.off")

    def stop(self)
        pass


    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return SwisscomTVSkill()
