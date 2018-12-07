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

@python_app
def run_cat_test():
    # Write the files out
    write_test_text_file ('/tmp/hello1.txt', 'hi1')
    write_test_text_file ('/tmp/hello2.txt', 'hi2')
    write_test_text_file ('/tmp/hello3.txt', 'hi3')

    # Make sure we don't have an output file.
    import os
    if os.path.isfile('all_hellos.txt'):
        os.unlink('all_hellos.txt')

    concat = cat(inputs=['/tmp/hello1.txt','/tmp/hello2.txt','/tmp/hello3.txt'],
             outputs=['all_hellos.txt'])

    # Open the concatenated file
    with open(concat.outputs[0].result(), 'r') as f:
        print(f.read())

    return 0
