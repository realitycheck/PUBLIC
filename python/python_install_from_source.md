$ sudo ln -s /usr/local/lib64/python3.7/lib-dynload/ /usr/local/lib/python3.7/lib-dynload 

is always required when building python with make altinstall


---

Build from source commands:

```
./configure --enable-optimizations --enable-shared --disable-test-modules
make -j8
```

Tip: Try removing previous build with `make clean` when rebuilding with configure options changed and got errors.

See: https://docs.python.org/3/using/configure.html
