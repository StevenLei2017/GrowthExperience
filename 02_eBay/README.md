## git常用操作

### git合并别人的分支
``` shell
git checkout master
git fetch xchannel
git reset --hard xchannel/master
git log
git push my master --force
git checkout CC-***
git rebase master
```