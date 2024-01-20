$ sudo ln -s /usr/local/lib64/python3.7/lib-dynload/ /usr/local/lib/python3.7/lib-dynload 

is always required when building python with make altinstall


---

Build from source commands:

```
Non-shared:

./configure --enable-optimizations --disable-test-modules

Shared:

./configure  --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib" --disable-test-modules

Then:
make clean
make -j8
```

Tip: Try removing previous build with `make clean` when rebuilding with configure options changed and got errors.

See: https://docs.python.org/3/using/configure.html
