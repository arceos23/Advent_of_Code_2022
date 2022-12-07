class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.name_to_subdir = {}
        self.files_size = 0

SMALL_DIR_SIZE = 100_000

small_dirs_total_size = 0
def calc_small_dirs_total_size(dir):
    global small_dirs_total_size

    subdirs_total_size = 0
    for subdir in [dir.name_to_subdir[i] for i in dir.name_to_subdir]:
        calc_small_dirs_total_size(subdir)
        subdirs_total_size += subdir.files_size
    dir_total_size = dir.files_size + subdirs_total_size
    if dir_total_size <= SMALL_DIR_SIZE:
        small_dirs_total_size += dir_total_size

file = open('day7_input.txt', 'r')
terminal_output = file.readlines()
file.close()

# Construct file system
root = Dir(None)
current_dir = None
for line in terminal_output:
    tokens = line.strip().split()
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '/':
                current_dir = root
            elif tokens[2] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.name_to_subdir[tokens[2]]
    else:
        if tokens[0] == 'dir':
            current_dir.name_to_subdir[(tokens[1])] = Dir(current_dir)
        else:
            current_dir.files_size += int(tokens[0]) # Processes files from ls cmd

calc_small_dirs_total_size(root)
print(small_dirs_total_size)