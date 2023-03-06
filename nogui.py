import helpers
import sys

modpacks_path = sys.argv[1]
mods_dir = sys.argv[2]

def main():

    print("Hello!")
    print("You have these modpacks available:\n")

    subdirs = helpers.getSubDirs(modpacks_path)
    num_dirs = 0

    for i, dir in enumerate(subdirs):
        print(f'{i+1}: {dir[len(modpacks_path):]}')
        num_dirs = i+1
    

    passed = False
    while not passed:
        option = input("\nWhich modpack would you like to use?")

        if not all([char in "123456789" for char in option]):
            print("That option is not valid")
            continue

        option = int(option)

        if not option in range(1,num_dirs+1):
            print("That option is not in the list")
            continue
        
        helpers.changeFolder(subdirs[option-1], mods_dir)

        passed=True

        print("Modpack Switched!")
main()