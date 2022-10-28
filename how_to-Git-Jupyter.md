# GITHUB - Standard development cycle

- Before starting with the development you could check whether the upstream repository has been updated with respect to your forked version (that's likely to be the case prior to every lab class). If it had, then merge the changes into your main:

```bash
git checkout main
git fetch upstream
git merge upstream/main
```

- Then synch your development branch (especially in the case your pull request has been recently approved):

```bash
git checkout <BranchName> 	#develop
git fetch upstream <NameSurname> #giada_zuccolo
git merge upstream/<NameSurname> #giada_zuccolo
```

Be careful that the git syntax is inconsistent between fetch and merge. In the former you should use the whitespace to separate the repository and the branch name, in the latter you should use the slash character.

- The idea is that your main always reflects `upstream/main`, i.e. it keeps a local copy of the reference code as a starting point for your developments (i.e. solving the assigned problems). Note that in order to update your repository on GitHub, you need to push the local version to your remote repository.
- You may also need to get the updates from the main, i.e. need to merge the main:

```bash
git merge main
```

- Before starting to edit on the machine that you are using, type the follow command in order to update the directory with the last changes:

```bash
git pull
```

- Now develop some code. Image you create a `<NewFile>`. Add the file to your local repository and stage it for commit (to unstage a file, use `git reset HEAD <NewFile>`)

# JUPYTER NOTEBOOK

To start a new notebook from command line:

```bash
jupyter notebook
```