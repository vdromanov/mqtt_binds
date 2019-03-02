import paho.mqtt.client as mqttclient
import logging

CALLABLE_BACKENDS = {}
LISTENING_BACKENDS = {}

from main import MQTTConnection
from decorators import *
from logger import *

__version__ = '0.1'

init_logger()
mqtt = MQTTConnection()

"""
TODO: 
    add custom exception hook
    add decorator to handle bounded methods
    parsing values from topic?

"""
