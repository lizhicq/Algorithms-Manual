
## git CRUD file
$git add *
$git commit -m "add all changes"
$git push
$git rm 


## git check log and revert
$git log --pretty=oneline

$git reset --hard 1094a # git revert to a specific version

$git reflog #查看操作记录, 你使用 git reset --hard commitID 把本地开发代码回滚到了一个之前的版本，而且还没有推到远端，怎么才能找回丢失的代码呢？你如果使用 git log 查看提交日志，并不能找回丢弃的那些 commitID。 而 git reflog 却详细的记录了你每个操作的 commitID



## manage branch
$git checkout -b feature_branch # create and check out feature branch
$git status
