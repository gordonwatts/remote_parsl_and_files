# Run a local copy of the parsl work flow.
from workflow import run_cat_test
import parsl

# Be explicit about loading a threading executor.
# (copied from the tutorial)
from parsl.config import Config
from parsl.executors.ipp import IPyParallelExecutor
from parsl.channels import SSHChannel
from parsl.providers.local.local import LocalProvider
import os

remote_config = Config(
    executors=[
        IPyParallelExecutor(
            label='remote_ipp',
            provider=LocalProvider(
                min_blocks=1,
                init_blocks=1,
                max_blocks=4,
                nodes_per_block=1,
                parallelism=0.5,
                channel=SSHChannel(hostname="localhost"),
                #worker_init='source /phys/groups/tev/scratch3/users/gwatts/anaconda3/etc/profile.d/conda.sh && conda activate parsl',
                worker_init='source /home/gwatts/anaconda3/etc/profile.d/conda.sh && export PYTHONPATH=$PYTHONPATH:{} && conda activate parsl_test'.format(os.getcwd()),
                move_files=False,
            )
        )
    ]
)
parsl.load(remote_config)

# Run this and print out the result
r = run_cat_test()
with open(r.outputs[0].result(), 'r') as f:
    print(f.read())

print ("Result from the test is {}".format(r.result()))