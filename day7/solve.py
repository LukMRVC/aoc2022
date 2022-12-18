import sys

class INode:
    def __init__(self, name: str, dir: bool = False):
        self.name = name
        self.is_dir = dir
        self.size = 0
        self.parent = None
        self.children: dict[str, INode] = dict()
        

    def calc_size(self) -> int:
        if not self.is_dir:
            return self.size
        self.size = sum(x.calc_size() for x in self.children.values())
        return self.size
    
    def get_sum_atmost(self, atmost: int):
        s = self.size if self.size <= atmost and self.is_dir else 0
        return s + sum(x.get_sum_atmost(atmost) for x in self.children.values())
    
    def get_dir_sizes(self, sizes):
        if self.is_dir:
            sizes.append(self.size)
        for node in self.children.values():
            node.get_dir_sizes(sizes)


current_dir: INode = None
# read_until_command = False

with open('input') as f:
    for line in f:
        line = line.strip()
        if line[0] == '$':
            # read_until_command = True
            # is a command
            if 'cd' in line:
                # next directory
                ndir = line[5:]
                if ndir == '/':
                    current_dir = INode(ndir, True)
                elif ndir == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.children[ndir]
            elif 'ls' in line:
                continue
        else:
            if line.startswith('dir'):
                name = line[4:]
                current_dir.children[name] = INode(name, True)
                current_dir.children[name].parent = current_dir
            else:
                size, name = line.split(' ')
                current_dir.children[name] = INode(name, False)
                current_dir.children[name].size = int(size)
                current_dir.children[name].parent = current_dir


# get to root
while current_dir.parent is not None:
    current_dir = current_dir.parent

root_space = current_dir.calc_size()

print(current_dir.get_sum_atmost(100_000))

dir_sizes = []
current_dir.get_dir_sizes(dir_sizes)

max_space = 70_000_000

unused_space = max_space - root_space

dir_sizes = [d for d in dir_sizes if d + unused_space >= 30_000_000]
print(dir_sizes)
print(min(dir_sizes))