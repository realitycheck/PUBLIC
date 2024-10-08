$ sudo ln -s /usr/local/lib64/python3.7/lib-dynload/ /usr/local/lib/python3.7/lib-dynload 

is always required when building python with make altinstall

---

[Also for --enable-shared shared *.so from /usr/local/lib64 must be copied to /usr/local/lib](https://serverfault.com/questions/71601/compile-python-3-1-1-with-enable-shared)

e.g.
$ sudo ln -s /usr/local/lib64/libpython3.11.so.1.0 /usr/local/lib/libpython3.11.so.1.0

---

Build from source commands:

```
./configure --enable-optimizations --disable-test-modules --enable-shared 

Then:
make clean
make -j8
```

Tip: Try removing previous build with `make clean` when rebuilding with configure options changed and got errors.

See: https://docs.python.org/3/using/configure.html
