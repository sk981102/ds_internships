from github import Github
from config import user_name, token, repo_name
import os
# Authenticate yourself
g = Github(user_name, token)

# Find your repository and path of README.md
repo = g.get_user().get_repo(repo_name)
file = repo.get_contents("README.md")

# The new contents of your README.md
print(file.sha)
content = "works"

# Update README.md
repo.update_file("README.md", "commit message", content, file.sha)
os.system("git push")