# Understanding Git & Github

## What is Git?

Git is a distributed version control system that helps developers collaborate on projects of any scale. This allows developers to bring a repo full of code down to their workstations, perform their work items, and then put it back into a central server.

## Commands You'll Need For Today
_\# indicates a comment in bash_

### Check status of changes

```bash
# See list of files changed
git status
```
- The git **status** command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git.

### Upload Your Changes Step 1: Add Files to be Tracked
```bash
# add files by paths
git add [fileName] 
# OR add file interactively one by one
git add -p
# OR add all changed files (what you'll do more often than not)
git add --all 
```
- The git **add** command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit.


### Upload Your Changes Step 2: Save Changes in a Commit
```bash
# Commit changes with a descriptive commit message
git commit -m "commit description"
```
- Changes are not actually recorded after `git add` until you run `git commit`.
- A **commit** captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project—Git will never change them unless you explicitly ask it to.

### Upload Your Changes Step 3: Push Committed Changes to Remote Repository
```bash
# Push changes up to remote repo in whatever branch you are working in
git push

# IF it is your first time pushing, git will show you a message of where to set the push stream
git push --set-upstream origin my-new-feature
```
- The git **push** command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo.

### Get changes from origin/main to current branch

```bash
# origin/main => local main
git pull origin main
```
- The git **pull** command is used to fetch and download content from a remote repository and immediately update the local repository to match that content

# An In-Depth Look at Git

#### So why do we need version control?

Think about a video game where you've gotten to level 16. But to beat the game completely, you have to make it to level 20. Should you only be able to finish the game if you complete flawlessly it in one try? Of course not. With a version control system you can **commit** your code, kind of like a checkpoint in a video game, before you actually push it and merge it into your codebase. With version control, you can also roll back to previous commits if you want to change something you did without having to Ctrl+Z 100 times. This is why you should _commit often_ and with detailed commit messages.

#### Some terms you should understand about version control:

- **Version control** - known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time
- **Repository or "repo"** - Each Git project is called a repository, or “repo” for short. A repo stores all the files and changes made to your project. It’s like a project with memory allowing you to move back and forward in time and observe the ways you have changed and modified your project. Thus, the repo stores data and change information. For developers it can be especially useful as they are learning version control systems to practice how to clone a GitHub repository and know how to delete a repository in GitHub.
  The three big things you do with version control are commit, clone, and branch. When you commit a change, you add your latest changes to your repo and are directing information to be filed. As in life, commitment is a serious responsibility – and is why every commit needs a serious commit message. A commit message explains changes and is the primary way to communicate changes to your development team. When you commit, you push your changes to the repository, and all information heading upstream to your repo is pushed. This push propels information from your local source into the shared repository.
- **Diffs** - Every time you commit there are differences between the project from the last save point to the new one. These changes are called differences, or “diffs” for short. You can compare changes between commits by looking at the diffs.
- **Merge Conflict** - A conflict occurs when two parties change the same file and there's no automatic way to reconcile the changes. You must resolve the change by selecting which change wins.
- **Clone** - When you clone a Git repository, you create a local copy to work on and your version will match the contents of the repository at the time you cloned it. For instance, you can clone a repository on GitHub to your computer where you can compile it from source, modify it, and more.
- **Pull** - If you've been working on a clone project, you may need to catch up with changes others have made by pulling, which changes revisions from the repository to your local copy.
- **Forking** - Another way to copy a repository is called “forking,” and is more like a fork in a tree. Unlike when you clone and make a copy on your computer, forking involves making a new repository, typically on GitHub or whatever hosting site you're using. A fork has all the contents of the original, but you are now the owner of this new repository and you're starting a new development project. You're copying a project when you fork and you're working on a project when you clone.
- **Branch** - Branches let you create alternate versions of your project. When you branch you can work on new features and try new ideas without messing with your main work. Consider this – your main work may have many names and, like a tree trunk, it’s commonly called the “master,” “master branch,” or “baseline.” The trunk or master is where your team keeps its primary project development and if it’s messed with, your team will suffer. Thus, if you plan to work on something that will take a while and may break your build, be sure to branch so you don't interfere with the work of others on your team.
- [**Open Source**](https://opensource.com/resources/what-open-source) - The term open source refers to something people can modify and share because its design is publicly accessible.

There are other distributed version control systems that are widely used, for example Mercurial. Instead of typing `git` before commands, you would use `hg` for this version control system. The three most popular DVCS (Distributed Version Control Systems) are Mercurial, Git, and Bazaar. Here, we will solely focus on Git.


## Creating your own Organizations and Repositories

You can create a repository for each project you start on your personal GitHub account, _but many suggest creating a separate organization_ for projects you plan to collaborate on or make open-source.

#### [QuickStart tutorial for Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)

#### [README Files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

- You can add a README file to your repository to tell other people why your project is useful, what they can do with your project, and how they can use it.
- If a filed titled `README.md` file in your repository's hidden .github, root, or docs directory, GitHub will recognize and automatically surface your README to repository visitors.
- If a repository contains more than one README file, then the file shown is chosen from locations in the following order: the .github directory, then the repository's root directory, and finally the docs directory.

## Understanding Branches & How to Collaborate

#### [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

- Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.
- In order to help your team, make sure you publish your Pull Requests when they're ready with clean code and helpful descriptions```

#### [Merging](https://git-scm.com/docs/git-merge)

Merging is Git's way of putting a forked history back together again. The git merge command lets you take the independent lines of development created by git branch and integrate them into a single branch. Note that all of the commands presented below merge into the current branch.


#### [Merge Conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)

- Merge conflicts happen when you merge branches that have competing commits, and Git needs your help to decide which changes to incorporate in the final merge
- Keep your code loosely coupled and divide work appropriately to try to avoid merge conflicts as much as possible, though they will eventually be inevitable

#### [Rebasing](https://docs.github.com/en/get-started/using-git/about-git-rebase)

The git rebase command allows you to easily change a series of commits, modifying the history of your repository. You can reorder, edit, or squash commits together.
Typically, you would use git rebase to:

- Edit previous commit messages
- Combine multiple commits into one
- Delete or revert commits that are no longer necessary

## Common Commands You Should Know

_For more, check out the [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)_

#### First Time Git users

| **Command**                                          | **Action**                                                                                                              |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `git config -l`                                      | check your Git configuration - returns a list of information about your git configuration including user name and email |
| `git config --global user.name "Genesis"`            | Set up your username                                                                                                    |
| `git config --global user.email "genesis@gmail.com"` | This command lets you setup the user email address you'll use in your commits.                                          |
| `git init`                                           | initialize a git Repo                                                                                                   |

#### Every Day Commands

| **Command**                                                                                           | **Action**                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `git add [file names]`                                                                                | First step in pushing changes. This adds changes in the file listed to be tracked for changes. To add all changes in all files, run `git add .` |
| `git commit -m "message"`                                                                             | Commit your code with a _detailed_ message                                                                                                      |
| [`git push`](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) | Push local changes up to remote git branch                                                                                                      |
| `git checkout -b branch-name`                                                                         | create new branch, branch-name                                                                                                                  |
| `git checkout branch-name`                                                                            | open up the branch branch-name                                                                                                                  |
