# Run a local copy of the parsl work flow.
import workflow
import parsl

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

r = workflow.run_cat_test().result()
print ("Result from the test is {}".format(r))