import random


# this script will be a minesweeper implentation in python
# Also learning vim while i'm at it 

# randomly place mines w/o overlap
# in each non-mine cell calculate # of mines in neighboring cells
# automatically reveal all cells w/o any neighboring mines
# handle flags & revealing mines
#     
# { # = covered cell}
# { * = mine}
# { ! = flag}
# { o = empty tile}


# oop

class MineField:
    def __init__(self):
        self.mineField = []

    def makeMineField(self, size:int ) -> None:
        createdMines: int = 0 

        for y in range(size):
            for x in range(size):
                self.mineField.append(Cell(x, y, self.mineField))


        while createdMines != 9:
            selectedMine = self.mineField[random.randrange(len(self.mineField))]
            if selectedMine.bottom != "*":
                selectedMine.bottom = "*"
                createdMines += 1


    def displayMineField(self) -> str:
        padding: int = len(str(max(self.mineField, key=lambda cell: cell.x).x))
        lidLength: int = 5 if max(self.mineField, key=lambda cell: cell.x).x > 9 else 4

        for num in range(max(self.mineField, key=lambda cell: cell.x).x + 1):
            lidLength += len(str(num))
            if max(self.mineField, key=lambda cell: cell.x).x < 10:
                lidLength += 1
            else:
                lidLength += 1 if len(str(num)) > 1 else 2

        output: list[str] = [" "*(((lidLength+2)//2)-int(15*(0.009*lidLength))), "**MINESWEEPER**", "\n"]

        output.extend(["╭", "─"*(lidLength), "╮"])
        output.extend(["\n", "│", " "*(padding+3)])
        if padding == 1:
            for num in range(max(self.mineField, key=lambda cell: cell.x).x + 1): output.extend([str(num), " "]) 
        else:
            for num in range(max(self.mineField, key=lambda cell: cell.x).x + 1): output.extend([str(num), " "*(3-len(str(num)))]) 
        
        for i, cell in enumerate(self.mineField):
            if cell.y == self.mineField[i-1].y:
                output.extend([cell.bottom, " "*padding])   #"[" + str(cell.x) + ", " + str(cell.y) + "]"
            else:
                horizontalPadding: str = " " if cell.y > 9 else "  "
                output.extend(["│", "\n", "│", " "*(padding), str(cell.y), horizontalPadding, cell.bottom, " "*padding]) #"[" + str(cell.x) + ", " + str(cell.y) + "]"
        
        output.extend(["│", "\n"])
        output.extend(["╰", "─"*(lidLength), "╯"])
        return "".join(output)
    
 

class Cell:
    def __init__(self, x: int, y: int, parent: list, top: str = "#", bottom: str = "o"):
        self.parent = parent
        self.top = top
        self.bottom = bottom
        self.x = x
        self.y = y


            
    








# vars 

gamerunning: bool = True



# functions


    
    





        



# main game loop

def gameLoop() -> None:
    mineField = MineField()
    mineField.makeMineField(10)
    print(mineField.displayMineField())













gameLoop()