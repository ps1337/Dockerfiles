# WHUAT?
This downloads all references in a bibtex file as pdf if shorthands are used. If it doesn't make sense to download a file as pdf (e.g. png) it will try to save it in the native format.

## Building
Run `sudo make build`


## Running
Use `make run` as non-root user and make sure the data folder can be accessed by your user. Be sure to provide the required file(s).

## Why disable chrome sandboxing?!?! :(
Because some kernels still don't allow user namespaces.
