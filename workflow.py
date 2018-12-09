import parsl
from parsl.app.app import python_app, bash_app

# Start with the cat from the tutorial
# Will concatenate all of its inputs into a single output file.
@bash_app
def cat(inputs=[], outputs=[]):
    return 'cat %s > %s' %(" ".join(inputs), outputs[0])

# Write out a small text files
def write_test_text_file (fName, text):
    with open(fName, 'w') as f:
        f.write(text)
        f.close()

# Write out a file async
@python_app
def write_file(txt, outputs=[]):
    write_test_text_file(outputs[0], txt)
    return 0

# String together the apps, return a future
def run_cat_test():
    files = [write_file('hi{}'.format(i), outputs=['/tmp/hello{}.txt'.format(i)]).outputs[0] for i in range(0,3)]
    return cat(inputs=files, outputs=['all_hellos.txt'])
