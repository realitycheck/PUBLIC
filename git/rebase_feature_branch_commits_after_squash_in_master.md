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

Eventually, while doing work in feature_branch2, the feature_branch is squashed to master

Then, to rebase feature_branch2 onto commits from master, do
> git co master
> git pull -r master
> git co feature_branch2
> git rebase --onto master @~4

Where *4* is a number of commits on feature_branch2 to rebase




  
