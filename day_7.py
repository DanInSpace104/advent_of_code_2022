from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Dir:
    name: str = ''
    parent: Optional['Dir'] = None
    dirs: dict = field(default_factory=dict)
    files: dict = field(default_factory=dict)
    _size: int = -1

    @property
    def total_size(self):
        if self._size == -1:
            self._size = sum(self.files.values())
            self._size += sum([d.total_size for d in self.dirs.values()])

        return self._size

    def cd(self, path) -> 'Dir':
        if path == '..':
            return self.parent or self.cd('/')
        if path == '/':
            if self.parent:
                return self.parent.cd('/')
        return self.dirs[path]


def collect_filesystem(s: str):
    root = Dir('/')
    all_dirs = [root]
    dir = root
    for line in s.splitlines()[1:]:
        if line.startswith('$ cd'):
            dir = dir.cd(line.split()[-1])
        elif line.startswith('dir'):
            new_dir = Dir(line.split()[-1], dir)
            all_dirs.append(new_dir)
            dir.dirs[line.split()[-1]] = new_dir
        elif line == '$ ls':
            continue
        else:
            size, name = line.split()
            dir.files[name] = int(size)
    return root, all_dirs


def part_one(s: str) -> int:
    _, all_dirs = collect_filesystem(s)
    return sum((d.total_size for d in all_dirs if d.total_size <= 100000))


def part_two(s: str) -> int:
    root, all_dirs = collect_filesystem(s)
    need_to_free = (root.total_size + 30000000) - 70000000
    return min((d.total_size for d in all_dirs if d.total_size >= need_to_free))


test_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''


assert part_one(test_input) == 95437
assert part_two(test_input) == 24933642

with open('inputs/day_7.input') as fl:
    content = fl.read()
    print(part_one(content))
    print(part_two(content))
