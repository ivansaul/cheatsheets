# Tips and Tricks

## Rename branch

### **Renamed** to `new_name`

  ```bash
  git branch -m <new_name>
  ```

### **Push** and reset

  ```bash
  git push origin -u <new_name>
  ```

### **Delete** remote branch

  ```bash
  git push origin --delete <old>
  ```
  
## Log

Search change by content

```bash
git log -S'<a term in the source>'
```

Show changes over time for specific file

```bash
git log -p <file_name>
```

Print out a cool visualization of your log

```bash
git log --pretty=oneline --graph --decorate --all
```

## Branch

List all branches and their upstreams

```bash
git branch -vv
```

Quickly switch to the previous branch

```bash
git checkout -
```

Get only remote branches

```bash
git branch -r
```

Checkout a single file from another branch

```bash
git checkout <branch> -- <file>
```

## Rewriting history

Rewrite last commit message

```bash
git commit --amend -m "new message"
```

Amend the latest commit without changing the commit message.

```bash
git commit --amend --no-edit
```

See also: [Rewriting history](https://www.atlassian.com/git/tutorials/rewriting-history)

## Git Aliases

```cmd
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

See also: [More Aliases](https://gist.github.com/johnpolacek/69604a1f6861129ef088)
