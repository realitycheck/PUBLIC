# HOW-TOs

## Solve rebase conflicts when there is a file that differs but not relevant so it can be replaced or ignored entirely

> git rebase <master>
> git co <--ours|--theirs> <file>
> git add <file>
> git rebase --continue

## Search text in file history

### Find when a string was added or removed in a single file

> git log -S "your_string" --follow -p -- path/to/file.txt

> git log -G "regex_pattern" --follow -p -- path/to/file.txt

### Search all commits and branches for an exact string

> git log -S "your_string" --all -p

### Search every historical revision line-by-line using grep

> git grep "your_string" $(git rev-list --all)
