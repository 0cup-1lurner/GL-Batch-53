# Coordinates

class Coordinates():

    # What are the data attributes?
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.x},{self.y}>"

    def distance(self, other):
        """ Assumes other as a Coordinates data type"""
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5  # Distance between 2 points in 2D coord system
    
    

