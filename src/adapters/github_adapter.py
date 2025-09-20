# src/adapters/github_adapter.py
import os, subprocess
from github import Github
from .base_adapter import BaseAdapter

class GitHubAdapter(BaseAdapter):
    def __init__(self, token=None):
        token = token or os.environ.get("GITHUB_TOKEN")
        self.gh = Github(token)

    def fetch_pr_metadata(self, repo_full_name: str, pr_number: int):
        repo = self.gh.get_repo(repo_full_name)
        pr = repo.get_pull(pr_number)
        return {
            "clone_url": pr.head.repo.clone_url,
            "head_ref": pr.head.ref,
            "head_repo_full_name": pr.head.repo.full_name,
            "base_branch": pr.base.ref,
            "author": pr.user.login
        }

    def post_overall_review(self, repo_full_name: str, pr_number: int, body: str):
        repo = self.gh.get_repo(repo_full_name)
        pr = repo.get_pull(pr_number)
        pr.create_review(body=body, event="COMMENT")

    def post_inline_comment(self, repo_full_name: str, pr_number: int, file_path: str, line: int, comment: str):
        repo = self.gh.get_repo(repo_full_name)
        pr = repo.get_pull(pr_number)
        pr.create_review_comment(body=comment, commit_id=pr.head.sha, path=file_path, position=line)
