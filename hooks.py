

# install header2whatever, then you can run
# h2w jni_java.j2 CANEncoder.h --hooks hooks.py
# h2w jni_cpp.j2 CANEncoder.h --hooks hooks.py
# .. TODO: show how batch mode is used

skip_funcs = ['operator=']

def class_hook(cls, data):
    """Called for each class in the header"""

    for fn in cls['methods']['public']:

        fn['skip'] = fn['name'] in skip_funcs or fn['constructor']

        fn['jni_returns'] = fn['returns']
        for p in fn['parameters']:
            p['jni_name'] = p['name']
            p['jni_type'] = p['type']
