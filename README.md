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

To run remotely you'll first need to edit `run_remote.py` and alter the ssh host name and the worker_init command as needed.

# Crashes

The crashes I am seeing are several at the moment.

- if you try to use a hostname of localhost, it just hangs. Looking at the submission scripts it looks like zero length scripts are being written. This might not be a bug. Happy to submit if it is. This would be awesome as it makes it easy to test workflows as if you were running in a remote environment.
- A crash because it can't find the module `workflow`. Crash dump is below.

Crash due to missing module:
```
(parsl_test) -bash-4.2$ python run_remote.py
Traceback (most recent call last):
  File "run_remote.py", line 31, in <module>
    r = workflow.run_cat_test().result()
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/concurrent/futures/_base.py", line 432, in result
    return self.__get_result()
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/concurrent/futures/_base.py", line 384, in __get_result
    raise self._exception
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/site-packages/parsl-0.6.2a1-py3.7.egg/parsl/dataflow/futures.py", line 126, in parent_callback
    res = executor_fu.result()
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/concurrent/futures/_base.py", line 425, in result
    return self.__get_result()
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/concurrent/futures/_base.py", line 384, in __get_result
    raise self._exception
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/site-packages/parsl-0.6.2a1-py3.7.egg/parsl/dataflow/dflow.py", line 257, in handle_exec_update
    res = future.result()
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/concurrent/futures/_base.py", line 425, in result
    return self.__get_result()
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/concurrent/futures/_base.py", line 384, in __get_result
    raise self._exception
  File "/phys/groups/tev/scratch3/users/gwatts/anaconda3/envs/parsl/lib/python3.7/site-packages/ipyparallel-6.2.3-py3.7.egg/ipyparallel/client/asyncresult.py", line 226, in _resolve_result
    raise r
ipyparallel.error.RemoteError: ModuleNotFoundError(No module named 'workflow')
```