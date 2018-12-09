# Run a local copy of the parsl work flow.
#import workflow
from workflow import run_cat_test
import parsl
import os

# Be explicit about loading a threading executor.
# (copied from the tutorial)
from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor

local_config = Config(
    executors=[
        ThreadPoolExecutor(
            max_threads=8,
            label='local_threads'
        )
    ]
)
parsl.load(local_config)

# Run this and print out the result
if os.path.isfile("all_hellos.txt"):
    os.unlink("all_hellos.txt")
r = run_cat_test()
with open(r.outputs[0].result(), 'r') as f:
    print(f.read())

print ("Result from the test is {}".format(r.result()))