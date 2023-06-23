# long hash: 94cd6ca67c801c8b41f0b103be0b19906b411d00
git log -1 --format=%H

# short hash: 9411d00
git rev-parse --short HEAD  

# nearest tag, commit number, short commit hash: 1.0.0-1123-g9411d00
git describe --tags --always 
