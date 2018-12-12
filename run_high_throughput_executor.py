# Run a the workflow on the high throughput executor
from workflow import run_cat_test
import parsl

# Be explicit about loading a threading executor.
# (copied from the tutorial)
from parsl.config import Config
from parsl.channels import SSHChannel
from parsl.providers.local.local import LocalProvider
from parsl.addresses import address_by_hostname
from parsl.executors import HighThroughputExecutor


import os

remote_config = Config(
    executors=[
        HighThroughputExecutor(
            label='remote_ipp',
            cores_per_worker=2,
            address=address_by_hostname(),
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
if os.path.isfile("all_hellos.txt"):
    os.unlink("all_hellos.txt")
r = run_cat_test()
with open(r.outputs[0].result(), 'r') as f:
    print(f.read())

print ("Result from the test is {}".format(r.result()))