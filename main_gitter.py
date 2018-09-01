# In[]
import os
import shutil

# The directory in which all the repos will be stored
target_repo_location = 'F:/College/Programming and stuff/Bin/cpp-chronicles/codeblocks/git_repos'
# This is the direcory in which the repos will be staged to prevent data loss in case of abort
stage_repo_location = 'F:/College/Programming and stuff/Bin/cpp-chronicles/codeblocks/git_repos/stage'
#stage_repo_location = 'C:/Users/hpp/Documents/PycharmProjects/git_repos/stage'
# In[]
fi = open('git_repo_list.txt', mode = 'r',  encoding='utf-8', errors='ignore')
repo_list = [i.replace('\n','') for i in fi.readlines() if i != '\n']
print(repo_list)


# In[]
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

# In[]
if not os.path.isdir(target_repo_location):
    os.makedirs(target_repo_location)
    
if not os.path.isdir(stage_repo_location):
    os.makedirs(stage_repo_location)

# In[]
test = repo_list[0]
print(os.path.split(test), os.path.sep, os.path.split(test)[0].split(os.path.sep))
#copyDirectory(test, target_repo_location + '/test.git')    
# In[]
for repo in repo_list:
    # Get the name of the parent folder as the name for the repo and append git
    target_repo_name = os.path.split(repo)[0]\
    .split(os.path.sep)[-1] + '.git'
    
    # Tree name variables
    stage_tree = os.path.join(stage_repo_location, target_repo_name)
    target_tree = os.path.join(target_repo_location, target_repo_name)
    
    # Remove the stage tree and copy the tree
    if os.path.isdir(stage_tree):
        shutil.rmtree(stage_tree)
    copyDirectory(repo, stage_tree)
    
    # Remove the repo tree and copy the tree
    if os.path.isdir(target_tree):
        shutil.rmtree(target_tree)
    copyDirectory(repo, target_tree)
    