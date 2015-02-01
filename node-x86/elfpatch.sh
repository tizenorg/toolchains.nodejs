#!/bin/bash

patchelf --debug --set-interpreter /emul/ia32-linux/lib/ld-linux.so.2 node
patchelf --debug --set-rpath .:/emul/ia32-linux/lib:/emul/ia32-linux/usr/lib node

