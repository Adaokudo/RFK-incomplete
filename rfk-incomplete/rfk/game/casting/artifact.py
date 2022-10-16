from game.casting.actor import Actor


# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """The responsibility of an Artifact is to provide a message about the actor.
    Attributes:

            _text (string): The text to display
           
            _font_size (int): The font size to use.

            _color (Color): The color of the text.

            _position (Point): The screen coordinates.
     
        """
    def __init__(self):
          """
          Constructs a new Artifact, inheriting from Actor 

        """
          self._actor = {}

    def get_message(self,):
      self._message = " "
      return self.get_message

    def set_text(self):
     
      return self.set_text

    def get_points(self):

      return self.get_points
    