@phildini
You type python, you press enter.  What happens?

The Bash shell.
type: python

(The first thing that the shell does is find the python executable in the path)
We can see the path by typing:
echo $PATH

The shell is looking for an executable.  Wat?
The bash process looks through the $PATH for a file of type executable that matches your request
You can see a description of the file with:
file /bin/python

Upon calling that executable, bash make a copy of itself with:
fork()

That forked process then calls the python binary with:
execute()
(python is now a child of the new bash process)

in the example:
python -v

Bash tokenizes the additional arguments and passes them into the execute() call

The above process is ultimately how *args is created (args[0] always being the name of the called process)


by running:
strace python
We can see all the system calls 


The Python Process on a Unix system essentially does a few things:

Sets file descriptions for
0 std in
1 std out
2 std err

Sets signals for
ctrl c 
pipe
Worth Googling:
An introduction to term ios
