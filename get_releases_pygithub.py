# To be safe, run 'pip install PyGithub' from the cmd line before running this
from github import Github
import github.GitRelease

# Access token from Github account
access_token = "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"
g = Github(access_token, per_page=100) # override default results returned per page to 100

repo_owner_name = "PyGithub/PyGithub"
# repo_owner_name = "kubernetes/kubernetes" # K8s has tons of releases/repos, so a nice test for 500+ releases

repo = g.get_repo(repo_owner_name)

# Tags - these are just the git tags
tags = repo.get_tags()

# Releases - these are the real releases, typically they have a tag associated
releases = repo.get_releases()
print(f'The total releases in {repo_owner_name} is: {releases.totalCount}.')

# You can access a specific release page with the following, or a specific release using the 
page = repo.get_releases()[0]


# Print some tag details
print('\nTags:')
for tag in tags:
    print(f'Name: {tag.name} Commit: {tag.commit}')

# Print some release details, including - Title, Tag Name, Published at, Prerelease
print('\nRelease Details:')
for release in releases.reversed:
    published_at = release.published_at.strftime('%a, %d %b %Y %H:%M:%S')
    print(f'Title: {release.title} Tag Name: {release.tag_name} Published at: {published_at} Prerelease: {release.prerelease}')