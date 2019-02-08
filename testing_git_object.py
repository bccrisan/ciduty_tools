import git
import os
import datetime
import string
from random import randint, choice
import time
import shutil
import sh

def generate_string():
    characters = string.ascii_letters + string.punctuation + string.digits
    result = "".join(choice(characters) for x in range(randint(8, 16)))
    return result



def todo_job():
    test_string = generate_string()
    f = open("demofile.txt", "w")
    f.write("Updated on:" + str(datetime.datetime.utcnow()) + ". Generated string: " + test_string)
    f.close()


def handle_git():
    # repo = git.Repo.clone_from("https://github.com/bccrisan/ciduty_tools", os.path.join(os.getcwd(), 'testing_ciduty_tools'), branch='master')

    # empty_repo = git.Repo.init(os.path.join(os.getcwd(), 'testing_ciduty_tools'))
    # origin = empty_repo.remote("origin")
    # origin.fetch()  # assure we actually have data. fetch() returns useful information
    # origin.pull()   # Pull from remote origin the last known and good state of the code.

    todo_job()      # The job to do before pushing.
    
    # # Generate the path for the modified files. (in this case it is hardcoded)
    # path = "E:\\bcrisan\\repos\\bcrisan\\testing_git_clonning\\testing_ciduty_tools\\demofile.txt"
    
    # # Add the path of the modified file to the repo. (similar with "git add "specific file" ")
    # repo.index.add([path])

    # # Commiting changes with a generated commit message (git commit -m "Test commit + UTCNOW Date (GMT + 0)")
    # repo.index.commit("Test commit: " + str(datetime.datetime.utcnow()))
    
    # #Pushing the commit to the origin. (master branch,)
    # origin.push()
    
    # os.system("git add .")
    # time.sleep(1)
    data = str(datetime.datetime.utcnow())
    commit_message = "commit - m \"Test commit: " + data + "\""
    # os.system("git commit - m \"Test commit: " + data + "\"")
    # time.sleep(1)
    # os.system("git push origin master")
    
    git("add .")
    commit_command = "commit -m " + commit_message
    git(commit_command)

    git("push origin master")
    # pbs.Command("git add .")
    # pbs.Command(commit_command)
    # pbs.Command("git push origin master")



if __name__ == "__main__":
    # path = os.getcwd()
    # path = path + "\\testing_ciduty_tools"
    # print(path)   
    handle_git()
    
    # os.system("rmdir /S /Q \"{}\"".format(path))