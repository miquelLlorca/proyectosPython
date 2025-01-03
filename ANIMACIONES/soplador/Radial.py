
class Radial:
    def __init__(self, c):
        self.c = c + []

    
    def GetRadioPos(self, pos):
        v = [self.c[i] - pos[i] for i in [0, 1]]
        n = (v[0]**2 + v[1]**2)**0.5
        return [(v[i]/n if v[i]!=0 else 0) for i in [0, 1]]

    def GetRadioNeg(self, pos):
        v = [pos[i] - self.c[i] for i in [0, 1]]
        n = (v[0]**2 + v[1]**2)**0.5
        return [(v[i]/n if v[i]!=0 else 0) for i in [0, 1]]

    def GetDistancia(self, pos):
        v = [pos[i] - self.c[i] for i in [0, 1]]
        n = (v[0]**2 + v[1]**2)**0.5
        return n