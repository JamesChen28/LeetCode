
import os
import re

# get all folder names
all_folders = os.listdir(os.getcwd())
all_folders.remove('.git')
all_folders.remove('README.md')
all_folders.remove('statistics_problems.py')

# mypath = os.getcwd()
# [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(mypath) for f in filenames]

# get all file names and their paths
all_files = []
for folder in all_folders:
    all_files.append(str(os.getcwd()) + '\\' + str(folder) + '\\' + os.listdir(folder)[0])

# specify difficulty and pattern
pattern1 = 'Difficulty = Easy'
pattern2 = 'Difficulty = Medium'
pattern3 = 'Difficulty = Hard'

# record each problem difficulty
total_easy = 0
total_medium = 0
total_hard = 0

for file in all_files:
    f = open(all_files[0], 'r')
    text = f.read()
    # print(text)
    f.close()
    
    result1 = re.search(pattern1, text)
    result2 = re.search(pattern2, text)
    result3 = re.search(pattern3, text)
    if result1:
        total_easy = total_easy + 1
    if result2:
        total_medium = total_medium + 1
    if result3:
        total_hard = total_hard + 1

# overwrite  difficulty in README.md
f = open('README.md')
text = f.read()
print(text)

pattern_easy = r'Easy = \d  \n'
pattern_mediun = r'Medium = \d  \n'
pattern_hard = r'Hard = \d  \n'

new_value_easy = 'Easy = ' + str(total_easy) + '  \n'
new_value_medium = 'Medium = ' + str(total_medium) + '  \n'
new_value_hard = 'Hard = ' + str(total_hard) + '  \n'

sub_result_easy = re.sub(pattern_easy, new_value_easy, text)
sub_result_medium = re.sub(pattern_mediun, new_value_medium, sub_result_easy)
sub_result_hard = re.sub(pattern_hard, new_value_hard, sub_result_medium)
f.close()

f = open('README.md', 'w')
f.write(sub_result_hard)
f.close()
