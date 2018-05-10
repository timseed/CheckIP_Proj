import socket
import logging
import daiquiri

class CheckService(object):

    def __init__(self, server_name, port=21):
        self.buffer_size=1024
        self.port=port
        self.logger = daiquiri.getLogger(__name__)
        self.logger.info("Looking up" + server_name)
        try:
            self.server_ip=socket.gethostbyname_ex(server_name)
        except Exception as err:
            self.logger.error("Error looking up {}: Err: {}".format(server_name,str(err)))

    def check(self,timeout_in_secs=2):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.logger.debug("Server IP is {}".format(self.server_ip))
            s.settimeout(timeout_in_secs)
            s.connect((self.server_ip[2][0], self.port))
            rv=True
            s.close()

        except TimeoutError:
            rv=False
            pass
        except ConnectionAbortedError:
            rv = False
            pass
        except ConnectionError:
            rv=False
            pass
        except Exception as err:
            rv=False
            self.logger.error("Error {}".format(str(err)))
        return rv