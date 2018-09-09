# In[]
import os
import subprocess as sp
import sys

# The directory in which all the repos will be stored
target_repo_location = r'C:/Users/hpp/Documents/PycharmProjects/git_repos'


# In[]
if len(sys.argv)>1:
    ip_addr = sys.argv[1]
else:
    ip_addr = input("Please provide remote IP(leave blank if none): ")

# In[]
fi = open('git_repo_list.txt', mode = 'r',  encoding='utf-8', errors='ignore')
repo_list = [i.replace('\n','').replace('$(REMOTE_IP)',ip_addr).strip() for i in fi.readlines() if i != '\n']
print(repo_list)

# In[] -- Make the repo target directory if it does not exist
if not os.path.isdir(target_repo_location):
    os.makedirs(target_repo_location)

# In[]
for repo in repo_list:
    # Get the name of the parent folder as the name for the repo and append git
    target_repo_name = os.path.split(repo)[0]\
    .split(os.path.sep)[-1] + '.git'
    os.chdir(target_repo_location)
    
    repo = repo.replace(os.path.sep, '/')
    
    # Tree name variable
    target_tree = os.path.join(target_repo_location, target_repo_name)
    
    # If the repo does not exist then clone otherwise remove the directory and clone
    git_command = 'git clone --mirror "%s" "%s"' %(repo, target_tree)
    if not os.path.isdir(target_tree):
        pass
    else:
        print("Deleting the existing local repo: ", target_tree)
        if sys.platform[:3].lower()=='win':
            dummy = sp.run('rmdir /Q /S "' + target_tree + '"', shell=True)
        else:
            dummy = sp.run("rm -rf " + target_tree, shell=True)
    
    
    print(git_command)
    try:
        dummy2 = sp.run(git_command, shell=True)
        rc = dummy2.returncode
        if rc==0:
            print("Cloning successful for ", target_repo_name, '\n\n')
        else:
            print("Cloning failed for ", target_repo_name, '\n\n')
    except Exception as e:
        print("Cloning of - ", target_repo_name, " - failed due to python error: ", e)
    