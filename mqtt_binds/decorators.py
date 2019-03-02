from . import LISTENING_BACKENDS, CALLABLE_BACKENDS, logging
"""
Decorators
@bind: decorated function will be called, if corresponding topic updates
"""
def bind(topic, mode):
    logging.debug('Decorator over decorator')
    modes_dest_conformity = {
                    'listen' : CALLABLE_BACKENDS,
                    'send_to' : LISTENING_BACKENDS
                    }
    assert mode in modes_dest_conformity.keys(), 'Incorrect param!\nChoose from %s' % modes_dest_conformity.keys()

    def decorator(function):
        logging.debug('The decorator')
        modes_dest_conformity[mode].update({topic : function})
        def wrapper(*args, **kwargs):
            logging.debug('New function')
            if args or kwargs:
                return function(*args, **kwargs)
        return wrapper
    return decorator
