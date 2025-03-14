# Getting Started

## Create a Repository

Create a new local repository

```bash
git init [project name]
```

Clone a repository

```bash
git clone git_url
```

Clone a repository into a specified directory

```bash
git clone git_url my_directory
```

## Make a change

Show modified files in working directory, staged for your next commit

```bash
git status
```

Stages the file, ready for commit

```bash
git add [file]
```

Stage all changed files, ready for commit

```bash
git add .
```

Commit all staged files to version history

```bash
git commit -m "commit message"
```

Commit all your tracked files to version history

```bash
git commit -am "commit message"
```

Discard changes in working directory which is not staged

```bash
git restore [file]
```

Unstage a staged file or file which is staged

```bash
git restore --staged [file]
```

Unstage a file, keeping the file changes

```bash
git reset [file]
```

Revert everything to the last commit

```bash
git reset --hard
```

Diff of what is changed but not staged

```bash
git diff
```

Diff of what is staged but not yet committed

```bash
git diff --staged
```

Apply any commits of current branch ahead of specified one

```bash
git rebase [branch]
```

## Configuration

Set the name that will be attached to your commits and tags

```bash
git config --global user.name "name"
```

Set an email address that will be attached to your commits and tags

```bash
git config --global user.email "email"
```

Enable some colorization of Git output

```bash
git config --global color.ui auto
```

Edit the global configuration file in a text editor

```bash
git config --global --edit
```

## Working with Branches

List all local branches

```bash
git branch
```

List all branches, local and remote

```bash
git branch -av
```

Switch to my_branch, and update working directory

```bash
git checkout my_branch
```

Create a new branch called new_branch

```bash
git checkout -b new_branch
```

Delete the branch called my_branch

```bash
git branch -d my_branch
```

Merge branchA into branchB

```bash
git checkout branchB
git merge branchA
```

Tag the current commit

```bash
git tag my_tag
```

## Observe your Repository

Show the commit history for the currently active branch

```bash
git log
```

Show the commits on branchA that are not on branchB

```bash
git log branchB..branchA
```

Show the commits that changed file, even across renames

```bash
git log --follow [file]
```

Show the diff of what is in branchA that is not in branchB

```bash
git diff branchB...branchA
```

Show any object in Git in human-readable format

```bash
git show [SHA]
```

## Synchronize

Fetch down all the branches from that Git remote

```bash
git fetch [alias]
```

Merge a remote branch into your current branch to bring it up to date

```bash
$ git merge [alias]/[branch]
# No fast-forward
$ git merge --no-ff [alias]/[branch]
# Only fast-forward
$ git merge --ff-only [alias]/[branch]
```

Transmit local branch commits to the remote repository branch

```bash
git push [alias] [branch]
```

Fetch and merge any commits from the tracking remote branch

```bash
git pull
```

Merge just one specific commit from another branch to your current branch

```bash
git cherry-pick [commit_id]
```

## Remote

Add a git URL as an alias

```bash
git remote add [alias] [url]
```

Show the names of the remote repositories you've set up

```bash
git remote
```

Show the names and URLs of the remote repositories

```bash
git remote -v
```

Remove a remote repository

```bash
git remote rm [remote repo name]
```

Change the URL of the git repo

```bash
git remote set-url origin [git_url]
```

## Temporary Commits

Save modified and staged changes

```bash
git stash
```

List stack-order of stashed file changes

```bash
git stash list
```

Write working from top of stash stack

```bash
git stash pop
```

Discard the changes from top of stash stack

```bash
git stash drop
```

## Tracking path Changes

Delete the file from project and stage the removal for commit

```bash
git rm [file]
```

Change an existing file path and stage the move

```bash
git mv [existing-path] [new-path]
```

Show all commit logs with indication of any paths that moved

```bash
git log --stat -M
```

## Ignoring Files

```console
/logs/*

# "!" means don't ignore
!logs/.gitkeep

/# Ignore Mac system files
.DS_store

# Ignore node_modules folder
node_modules

# Ignore SASS config files
.sass-cache
```

A `.gitignore` file specifies intentionally untracked files that Git should ignore
