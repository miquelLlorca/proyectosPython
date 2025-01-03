from clock import Clock

# Modos del display
CLOCK_MODE = 'clk_md'
ANIMATION_MODE = 'anim_md'

# Tipos de reloj
BACKGROUND = 'fnd'
CLOCK_SEGMENT = 'clk'

# gestiona un display de relojes
# este contendra un reloj digital
# y un fondo

class ClockManager:
    def __init__(self, dims, clock_tam):
        self.dims = dims+[]
        self.mode = CLOCK_MODE
        self.clock = None

        self.display = []
        for i in range(dims[0]):
            self.display.append([])
            for j in range(dims[1]):
                x = clock_tam + clock_tam*2*i
                y = clock_tam + clock_tam*2*j
                self.display[i].append(
                    [Clock(x,y,clock_tam), BACKGROUND])
    
    def SetTime(self, time):
        self.clock.SetTime(time)
        self.UpdateBigClock()

    def SetBigClock(self, clock):
        self.clock = clock
        self.UpdateBigClock()
        
    def UpdateBigClock(self):
        for i in range(self.clock.tam[0]):
            for j in range(self.clock.tam[1]):
                x = self.clock.pos[0] + i
                y = self.clock.pos[1] + j
                self.display[x][y][1] = CLOCK_SEGMENT
                state = self.clock.GetStates([x,y])
                self.display[x][y][0].SetTarget(state)

    
    def Update(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                self.display[i][j][0].Update()
        return
    
    def Draw(self, pantalla):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                self.display[i][j][0].Draw(pantalla)
        return
