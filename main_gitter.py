# In[]
import os

# The directory in which all the repos will be stored
target_repo_location = 'F:/College/Programming and stuff/Bin/cpp-chronicles/codeblocks/git_repos'
# In[]
fi = open('git_repo_list.txt', mode = 'r',  encoding='utf-8', errors='ignore')
repo_list = [i.replace('\n','').strip() for i in fi.readlines() if i != '\n']
print(repo_list)

# In[]
if not os.path.isdir(target_repo_location):
    os.makedirs(target_repo_location)

# In[]
for repo in repo_list:
    # Get the name of the parent folder as the name for the repo and append git
    target_repo_name = os.path.split(repo)[0]\
    .split(os.path.sep)[-1] + '.git'
    os.chdir(target_repo_location)
    
    # Tree name variable
    target_tree = os.path.join(target_repo_location, target_repo_name)
    
    # If the repo does not exist then clone otherwise pull --rebase
    if not os.path.isdir(target_tree):
        git_command = 'git clone --mirror "%s" "%s"' %(repo, target_tree)
        print(git_command)
    else:
        git_command = 'git pull --rebase "%s"' %(repo)
        print(git_command)
    
    os.popen(git_command)
    