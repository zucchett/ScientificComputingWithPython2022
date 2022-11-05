def sleepy(msg, sleep=1.0):
    """Delays a while before answering."""
    import time
    time.sleep(sleep)
    print(msg)

sleepy("Hello", 1.5)