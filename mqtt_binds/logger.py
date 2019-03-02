import logging

def init_logger(loggername=None, filename=None):
    mqttlogger = logging.getLogger()
    mqttlogger.propagate = False
    mqttlogger.setLevel(logging.DEBUG)

    fmt='%(asctime)s %(message)s'
    datefmt="%Y-%m-%d|%H:%M"

    stream = logging.StreamHandler()
    stream.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    mqttlogger.addHandler(stream)

    
