class Slider:
    def __init__(self, id,  value):
        self.id = id
        self.value = value

    def __str__(self):
        return "{}: {}".format(self.id, self.value)
