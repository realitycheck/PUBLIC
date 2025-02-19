Supposing

```
master
\
 feature_branch
   + commit1
   + commit2
```

Then, after
> git push feature_branch

New branch from first feature branch
> git co -b feature_branch2 (from feature_branch)

Eventually, while doing work in feature_branch2, the feature_branch's PR is squashed to master

Then, to rebase feature_branch2 onto commits from master, do
```
> git co master
> git pull -r master
> git co feature_branch2
> git rebase --onto master @~4
```

Where *4* is the current number of commits in feature_branch2 to rebase




  
