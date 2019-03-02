from . import LISTENING_BACKENDS
from threading import Thread, Event
import time
import logging

class PollingLoop(Thread):
    loop_status = Event()

    def __init__(self, client, name='polling_loop', timeout=0):
        super(PollingLoop, self).__init__()
        self.name = name
        self.timeout = timeout
        self.client = client

    def start(self):
        self.loop_status.set()
        super(PollingLoop, self).start()

    def stop(self):
        self.loop_status.clear()
        self.join()

    def run(self):
        while self.loop_status.is_set():
            for topic, func in LISTENING_BACKENDS.iteritems():
                value = repr(func())
                self.client.publish(topic=topic, payload=value)
                logging.debug('%s has published %s to %s' % (func.__name__, value, topic))
                time.sleep(self.timeout)

