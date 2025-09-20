# src/adapters/base_adapter.py
from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    @abstractmethod
    def fetch_pr_metadata(self, repo_full_name: str, pr_number: int) -> dict:
        """Return {clone_url, head_ref, head_repo_full_name, base_branch, author}"""
        pass

    @abstractmethod
    def post_overall_review(self, repo_full_name: str, pr_number: int, body: str):
        pass

    @abstractmethod
    def post_inline_comment(self, repo_full_name: str, pr_number: int, file_path: str, line: int, comment: str):
        pass
