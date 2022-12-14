from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()


fileName = basename(__file__)
day = int(findall(r"[1-9]+", fileName)[0])
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
data = []
with open("day07/test.txt", "r") as f:
    data = f.read().splitlines()

data = puzzle.input_data.splitlines()

sizeOfSmallDirs = 0


class Base:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent

    def getSize() -> int:
        return 0


class Dir(Base):
    def __init__(self, name: str, parent):
        self.children: list(Base) = []
        Base.__init__(self, name, parent)

    def getSize(self) -> int:
        sum: int = 0
        for child in self.children:
            sum += child.getSize()
        self.size = sum
        if sum < 100_000:
            global sizeOfSmallDirs
            sizeOfSmallDirs += sum
        return sum

    def isChild(self, name: str) -> bool:
        for child in self.children:
            if child.name == name:
                return True
        return False

    def getChild(self, name: str) -> Base:
        for child in self.children:
            if child.name == name:
                return child
        raise FileNotFoundError("Child not found")


class File(Base):
    def __init__(self, name: str, parent: Dir, size: int):
        Base.__init__(self, name, parent)
        self.size = int(size)

    def getSize(self) -> int:
        return self.size


# Build directory tree with cmds.
root = Dir("/", None)
cwd = root
i = 1
while i < len(data):
    cmd = data[i]
    if cmd == "$ cd ..":
        cwd = cwd.parent
    if cmd.startswith("$ cd"):
        name = cmd.split(" ")[-1]
        if cwd.isChild(name):
            cwd = cwd.getChild(name)
    if cmd.startswith("$ ls"):
        subs = []
        while (i + 1 < len(data)) and (not data[i+1].startswith("$")):
            c = data[i+1]
            if c.startswith("dir"):
                subs.append(Dir(c.split(" ")[-1], parent=cwd))
            else:
                subs.append(File(c.split(" ")[-1], cwd, int(c.split(" ")[0])))
            i += 1

        cwd.children += subs
    i += 1
root.getSize()
print(sizeOfSmallDirs)
puzzle.answer_a = sizeOfSmallDirs


TOTAL_DISK_SPACE = 70_000_000
sizeRoot = root.getSize()
unused = TOTAL_DISK_SPACE - sizeRoot
REQUIRED = 30_000_000

# unused + deleted dir > REQUIRED
smallest = int(1e20)


def findSmallestDir(dir, lowerBound):
    """Find size of smallest dir that is bigger than the lower bound in dir and all children of dir."""
    if type(dir) == File:
        return
    global smallest
    if dir.size < smallest and (dir.size + unused) > lowerBound:
        smallest = dir.size
    for child in dir.children:
        findSmallestDir(child, lowerBound)


findSmallestDir(root, REQUIRED)
print(smallest)

puzzle.answer_b = smallest
