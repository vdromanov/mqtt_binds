import logging
from . import CALLABLE_BACKENDS, LISTENING_BACKENDS, mqttclient
from callbacks import *
from polling_loop import PollingLoop

class MQTTConnection(object):

    def connect(self, broker_addr, client_name):
        self.client = mqttclient.Client(client_name)
        self._init_callbacks()
        self.client.connect(broker_addr)

    """
    def bind(self, topic, mode):
        logging.debug('Decorator over decorator')
        modes_dest_conformity = {
                    'listen' : CALLABLE_BACKENDS,
                    'send_to' : LISTENING_BACKENDS
                    }
        assert mode in modes_dest_conformity.keys(), 'Incorrect param!\nChoose from %s' % modes_dest_conformity.keys()

        def decorator(function):
            logging.debug('The decorator')
            self.client.subscribe(topic)
            modes_dest_conformity[mode].update({topic : getattr(self, function.__name__)})
            return function
        return decorator
    """

    def _init_callbacks(self):
        self.client.on_message = parse_topics
        self.client.on_connect = subscribe_to_listers

    def hardware_loop(self, polling_timeout):
        pass
        #TODO: iterativelly check LISTENING_BACKENDS with polling_timeout. If

    def start(self):
        logging.debug('Started loop')
        self.client.loop_start()
        self.polling_loop = PollingLoop(self.client, timeout=5)
        self.polling_loop.start()

    def stop(self):
        logging.debug('Stopping')
        self.client.loop_stop()
        if self.polling_loop.is_alive():
            self.polling_loop.stop()



if __name__ == '__main__':
    connection = MQTTConnection('broker.hivemq.com', 'clientId-7VZ0kLFv1V')
    logging.debug(connection.CALLABLE_BACKENDS)
