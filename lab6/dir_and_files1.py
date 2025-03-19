import os

root = r"C:\Users\Мухаммедали\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\kbtu\pp1"

directories = []
files_list = []
all_items = []

for path, subdirs, files in os.walk(root):
    directories.extend(subdirs)
    files_list.extend(files)
    all_items.extend([os.path.join(path, f) for f in files])

with open("directory.txt", "w", encoding="utf-8") as directory:
    directory.write("List of only directories:\n")
    directory.write("\n".join(directories) + "\n")

with open("files.txt", "w", encoding="utf-8") as file:
    file.write("List of only files:\n")
    file.write("\n".join(files_list) + "\n")

with open("all.txt", "w", encoding="utf-8") as all_f:
    all_f.write("List of all directories and files:\n")
    all_f.write("\n".join(all_items) + "\n")

print("Файлы directory.txt, files.txt и all.txt созданы!")


all = open("all.txt", "x")

all.write("list of all directories and files:\n")

for path, subdirs, files in os.walk(root):

    for name in files:

        all.write(os.path.join(path, name) + "\n")

all.close()
