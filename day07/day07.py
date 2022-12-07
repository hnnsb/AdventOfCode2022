from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
from aocd.models import Puzzle


fileName = basename(__file__)
day = int(findall(r"[1-9]+",fileName)[0])
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
data = []
with open("day07/test.txt", "r") as f:
    data = f.read().splitlines()

data = puzzle.input_data.splitlines()

sizeOfSmallDirs = 0
class Base:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def getSize():
        return 0

class Dir(Base):
    def __init__(self, name, parent):
        self.children:list(Base) = []
        Base.__init__(self,name,parent)

    def getSize(self):
        sum:int = 0
        for child in self.children:
            sum += child.getSize()
        self.size = sum
        if sum < 100_000: 
            global sizeOfSmallDirs 
            sizeOfSmallDirs += sum
        return sum

    def isChild(self, name):
        for child in self.children:
            if child.name == name:
                return True
        return False

    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise FileNotFoundError("CHild not found")

class File(Base):
    def __init__(self, name, parent: Dir, size:int):
        Base.__init__(self,name,parent)
        self.size = int(size)
    
    def getSize(self)-> int:
        return int(self.size)
        
    
root = Dir("/", None)
cDir = root
i = 1
while i< len(data):
    cmd = data[i]
    if cmd == "$ cd ..":
        cDir = cDir.parent
    if cmd.startswith("$ cd"):
        name = cmd.split(" ")[-1]
        if cDir.isChild(name):
            cDir = cDir.getChild(name)
    if cmd.startswith("$ ls"):
        subs = []
        while (i + 1 < len(data)) and (not data[i+1].startswith("$")):
            c = data[i+1]
            if c.startswith("dir"):
                subs.append(Dir(c.split(" ")[-1],parent=cDir))
            else:
                subs.append(File(c.split(" ")[-1],cDir, int(c.split(" ")[0])))
            i +=1
            
        cDir.children += subs
    i +=1
root.getSize() 
print(sizeOfSmallDirs)
puzzle.answer_a = sizeOfSmallDirs


TOTAL_DISK_SPACE = 70_000_000
sizeRoot = root.getSize()
unused = TOTAL_DISK_SPACE - sizeRoot
REQUIRED = 30_000_000

#unused + deleted dir > REQUIRED
smallest = 100000000000000000
def findSmallestDir(dir):
    if type(dir) == File:
        return
    global smallest
    if dir.size < smallest and (dir.size + unused) > REQUIRED:
        smallest = dir.size
    for child in dir.children:
        findSmallestDir(child)
findSmallestDir(root)
print(smallest)

puzzle.answer_b = smallest