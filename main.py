from Backend.github_commits import get_github_commit_history


result = get_github_commit_history(
        repo_url="https://github.com/Tirth9978/NewGit2.0",
        max_commits=20
    )

print(result)