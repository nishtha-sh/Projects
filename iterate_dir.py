from pathlib import Path

path1 = Path('/Users/nishtha/PythonProjects/Practice/P')

#both methods list files/dir in provided path: glob returns nothing when path does not exist 
files = path1.glob('*.py')
for f in files:
    print(f)

#iterdir gives error when path does not exist
try:
    for i in path1.iterdir():
        print(i)

except FileNotFoundError:
    print('Path provided does not exist')


