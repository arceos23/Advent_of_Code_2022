class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.name_to_subdir = {}
        self.files_size = 0
        self.total_size = 0

TOTAL_DISK_SPACE = 70_000_000
UNUSED_SPACE_NEEDED = 30_000_000

def update_dir_sizes(dir):
    subdirs_total_file_size = 0
    subdirs_total_size = 0
    for subdir in [dir.name_to_subdir[i] for i in dir.name_to_subdir]:
        update_dir_sizes(subdir)
        subdirs_total_file_size += subdir.files_size
        subdirs_total_size += subdir.total_size
    dir.total_size = dir.files_size + subdirs_total_size

def get_smallest_del(dir, memory_needed, min_del):
    if dir.total_size < memory_needed:
        return min_del

    for subdir in [dir.name_to_subdir[i] for i in dir.name_to_subdir]:
        min_del = min(min_del, get_smallest_del(subdir, memory_needed, min_del))
    return min(min_del, dir.total_size)

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

update_dir_sizes(root)
max_update_memory = TOTAL_DISK_SPACE - UNUSED_SPACE_NEEDED
memory_needed = root.total_size - max_update_memory

print(get_smallest_del(root, memory_needed, float('inf')))