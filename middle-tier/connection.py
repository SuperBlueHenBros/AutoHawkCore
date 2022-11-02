from bizhook import memory

def connect():
    ### Connection Setup ###
    print("Creating connection...")
    connection = memory.Memory("RAM")
    print("Connection created!")
    return connection
