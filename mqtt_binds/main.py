import logging
from . import CALLABLE_BACKENDS, LISTENING_BACKENDS, mqttclient
from callbacks import *
from polling_loop import PollingLoop

class MQTTConnection(object):

    def connect(self, broker_addr, client_name):
        self.client = mqttclient.Client(client_name)
        self._init_callbacks()
        self.client.connect(broker_addr)

    def _init_callbacks(self):
        self.client.on_message = parse_topics
        self.client.on_connect = subscribe_to_listeners

    def start(self, timeout=1.5):
        logging.debug('Started loop')
        self.client.loop_start()
        self.polling_loop = PollingLoop(self.client, timeout)
        self.polling_loop.start()

    def stop(self):
        logging.debug('Stopping')
        self.client.loop_stop()
        if self.polling_loop.is_alive():
            self.polling_loop.stop()



if __name__ == '__main__':
    connection = MQTTConnection('broker.hivemq.com', 'clientId-7VZ0kLFv1V')
    logging.debug(connection.CALLABLE_BACKENDS)
