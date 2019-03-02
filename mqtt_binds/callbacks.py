from . import CALLABLE_BACKENDS

def parse_topics(client, userdata, message):
    print('in ON_MESSAGE callback')
    if message.topic in CALLABLE_BACKENDS:
        payload = str(message.payload.decode("utf-8")).strip()
        CALLABLE_BACKENDS[message.topic](payload) #Call a binded function with payload as param

def subscribe_to_listeners(client, userdata, flags, rc):
    print('In ON_CONNECT callback')
    client.connected_flag=True
    topics_to_subscribe = CALLABLE_BACKENDS.keys()
    #tuple(set(CALLABLE_BACKENDS.keys()) | set(LISTENING_BACKENDS.keys()))
    print('Subscribing to:\n%s' % '\n'.join(topics_to_subscribe))
    for topic in topics_to_subscribe:
        client.subscribe(topic)
