import pygit2
import os
from pygit2 import GIT_SORT_TOPOLOGICAL
SOURCE_DIR_NAME = 'resource'
PROJECT_NAME = 'git'


parent_path = os.path.abspath(os.pardir)
project_dir = os.path.join(parent_path, SOURCE_DIR_NAME, PROJECT_NAME)


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

    def get_commit_length(self):
        pass


app = Repo(project_dir)
branch = app.get_branch()


