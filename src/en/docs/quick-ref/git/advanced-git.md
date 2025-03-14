# Advanced Git

## Submodules

Create a new submodule within your repository:

```bash
git submodule add <repository_url> <path>
```

Clone a repository and initialize its submodules:

```bash
git clone --recursive <repository_url>
```

Update all the submodules in your repository to the latest commit of their respective branches:

```bash
git submodule update
```

Pull the latest changes from the remote repositories of the submodules and update them in your main repository:

```bash
git submodule update --remote
```

Remove a submodule from your repository:

```bash
git submodule deinit <path>
git rm <path>
git commit -m "Removed submodule"
```

## Cherry-picking

Cherry-picking allows you to apply a specific commit from one branch to another branch.

```bash
git cherry-pick <commit_hash>
```

## Reflog

Display the reflog, showing the history of HEAD and branch movements:

```bash
git reflog
```

Find the hash of the lost commit or branch using the reflog and then checkout to that hash to restore it:

```bash
git checkout <commit_or_branch_hash>
```
