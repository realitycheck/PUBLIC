# HOW-TOs

## Search text in file history

### Find when a string was added or removed in a single file

> git log -S "your_string" --follow -p -- path/to/file.txt

> git log -G "regex_pattern" --follow -p -- path/to/file.txt

### Search all commits and branches for an exact string

> git log -S "your_string" --all -p

### Search every historical revision line-by-line using grep

> git grep "your_string" $(git rev-list --all)
