# remote_parsl_and_files
Can we access parsl written files correctly?

# Running the test

To run the test first create a parl environment. You can see the actual commands that were use to
do this in the `.vscode/tasks.json` file.

    conda create -y --name parsl_test python=3.7
    cd /tmp
    git clone https://github.com/Parsl/parsl
    cd parsl
    python setup.py install

To run the test locally threaded you can do:

    python run_local.py

It should print out `hi1hi2hi3`.

To run remotely you'll first need to edit `run_remote.py` and alter the ssh host name and the worker_init command as needed. It should
run on localhost just fine, though the startup and config scripts will have to be fixed in the file.

# Crashes

1. When the run_remote.py is run, it creates an all_files.txt as its final
   output. Unfotunately, it is created in the user's home directory, not in the directory from where you are running. What i thought should have happened:
   - The file should have been automatically written in the local directory.
     Because that is where the source script is being run, or, 
   - The DataFuture returned should have had the full path in it so even though   it was written somewhere else, it would have been tracked properly (e.g. h   how did the existance of that file get checked?).

```
Traceback (most recent call last):
  File "run_remote.py", line 35, in <module>
    with open(r.outputs[0].result(), 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: all_hellos.txt
The terminal process terminated with exit code: 1
```
