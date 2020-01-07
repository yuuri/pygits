import pygit2
import os
from pygit2 import GIT_SORT_TOPOLOGICAL
SOURCE_DIR_NAME = 'resource'
PROJECT_NAME = 'git'


parent_path = os.path.abspath(os.pardir)
project_dir = os.path.join(parent_path, SOURCE_DIR_NAME, PROJECT_NAME)


class CloneRepo(object):
    def __init__(self,url):
        self.url = url

    def clone_repo(self):
        pass


class Repo(object):
    def __init__(self, repo_dir):
        self.repo = self.create_repo_obj(repo_dir)

    @staticmethod
    def create_repo_obj(repo_dir):
        repos = pygit2.Repository(repo_dir)
        return repos

    def get_branch(self):
        branch_obj = self.repo.branches
        branch_list = []
        for i in branch_obj:
            branch_list.append(i)

        return branch_list

    def get_commits(self):
        last = self.repo[self.repo.head.target]
        print(last.id)
        commit_obj = [commit for commit in self.repo.walk(last.id,pygit2.GIT_SORT_TIME)]
        print(commit_obj)
        print(len(commit_obj))
        # for commit in self.repo.walk(last.id, pygit2.GIT_SORT_TIME):
        #     print(commit.message)

    def change_branch(self):
        ret = self.repo.listall_references()
        print(ret)
        # branch_name = 'origin/pu'
        # branch = self.repo.lookup_branch(branch_name)
        # self.repo.checkout(refname=branch)
        # print([i for i in self.repo.branches])
        # print([i for i in self.repo.branches.local])


app = Repo(project_dir)
# branch = app.get_branch()
# print(branch)
app.change_branch()
