from . import HTTPResponse, HTTPRequestParser
import socket
import _thread as thread
import time
from machine import reset


class WebServer:
    """
    HTTP WebServer
    
    Register and serve routes.
    TODO:
       - Handling 1Kb+ long requests
       - Handling HTTP request methods
    """
    
    # Common error responses
    err404 = HTTPResponse(code=404, content="<h1>Not Found</h1><p>Ressources could not be located or doesn't exists</p>")
    err500 = HTTPResponse(code=500, content="<h1>Internal Server Error</h1><p>The server encountered an internal error and was unable to complete your request.</p>")
    
    def __init__(self):
        self.routes_register = {}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('', 80))

    def route(self, name):
        def func_wrapper(func):
            self.routes_register[name] = func
            return func
        return func_wrapper

    def run(self, worker_amount):
        """
        
        """
        self.socket.listen(worker_amount)
        for i in range(worker_amount):
            self.worker(pid=i)

    def worker(self, threaded=True, pid=0):
        """
        A worker takes care of handling HTTP requests forever.
        :param threaded: starts a worker in a seperate thread if True
        :param pid: Worker identifier (preferably unique)        
        """
        
        # This restart the function in another thread
        if threaded:
            thread.start_new_thread(self.worker, (False, pid))
            return
 
        while True:
            # Waiting for client connection
            client, addr = self.socket.accept()
            remote = str(addr[0]) + ":" + str(addr[1])
            
            
            print('[Webserver] <Worker #{}> Got a connection from {}'.format(pid, remote))
            # Receiving a full request. May lead to memory error if request to large
            try:
                buffer = client.recv(1024)
                r = HTTPRequestParser(buffer)
            # Catching empty requests (or too long requests)
            except ValueError:
                print("[WebServer] <Worker #{}> Improperly formatted request : {}".format(pid, buffer))
                client.close()
                continue
            except Exception as err:
                print("[WebServer] <Worker #{}> Exception: {}".format(pid, err))
                client.close()
                continue

            """
            Routing
            """
            
            response = self.err404
            
            # Route matching
            for route in self.routes_register:
                if r.path == route:
                    try:
                        response = self.routes_register[route](r)
                    except:
                        response = self.err500
                    break

            # Sending response to the client and closing it
            try:
                response.feed(client, addr)
            except:
                print("[WebServer] <Worker #{}> Connection error".format(pid))
            else:
                print("[WebServer] <Worker #{}> Ended connection with {}".format(pid, client))

            client.close()
