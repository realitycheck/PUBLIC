$ sudo ln -s /usr/local/lib64/python3.7/lib-dynload/ /usr/local/lib/python3.7/lib-dynload 

is always required when building python with make altinstall


---

Build from source commands:

./configure --enable-optimization
make -j8
