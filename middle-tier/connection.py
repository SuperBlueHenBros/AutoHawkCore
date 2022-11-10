from bizhook import memory

# TODO: move to core.py and delete this file
def connect():
    ### Connection Setup ###
    print("Creating connection...")
    connection = memory.Memory("RAM")
    print("Connection created!")
    return connection
