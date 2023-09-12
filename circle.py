class Circle:
    def __init__(self, position: dict):
        self.position = {'x': position['x'], 'y': position['y']}
        self.next = None


    def change_position(self, new_position: dict):
        self.position['x'] = new_position['x']
        self.position['y'] = new_position['y']

