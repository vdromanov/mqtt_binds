import paho.mqtt.client as mqttclient
import logging
CALLABLE_BACKENDS = {}
LISTENING_BACKENDS = {}

from main import MQTTConnection
from decorators import *
from logger import *

init_logger()
mqtt = MQTTConnection()

logging.debug('Got instance: %s' % repr(mqtt))
#TODO: add custom exception hook
