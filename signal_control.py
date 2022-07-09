import signal

def signal_handler(signum,frame):
    print("123123",signum,frame)

signal.signal(signal.SIGINT,signal_handler)
signal.pause()