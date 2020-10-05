class rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, value: int):
        value = self.length
    
    def get_width(self, value: int):
        value = self.width
    
    def perimeter(self):
        return self.length*2 + self.width*2
    
    def area(self):
        return self.length*self.width
