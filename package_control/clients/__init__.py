from .bitbucket_client import BitBucketClient
from .github_client import GitHubClient
from .gitlab_client import GitLabClient


CLIENTS = [
    BitBucketClient,
    GitHubClient,
    GitLabClient
]
