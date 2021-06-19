from . import code_string
import json


class HTTPResponse:
    def __init__(self, code=200, content_type="auto", content="Hello world"):
        """
        Response object. can be used to build HTTP responses
        :code: Int ; Status code
        :content_type: Str ; content type
        :content: Str (html/text) or Dict (json/applications)
        """
        self._code = code
        self._content_type = content_type
        self._content = content

    @property
    def code(self):
        """
        Ready to use code header
        """
        return 'HTTP/1.1 {} {}\n'.format(self._code, code_string(self._code))

    @property
    def content_type(self):
        """
        Ready to use content-type header
        """
        if self._content_type == "auto":
            if isinstance(self._content, dict):
                return 'Content-Type: application/json\n'
            else:
                return 'Content-Type: text/html\n'

    @property
    def content(self):
        """
        Ready to use content header
        """
        if isinstance(self._content, dict):
            return json.dumps(self._content)
        else:
            return self._content

    def feed(self, client, addr="Unknown"):
        """
        Sends a response to specified client then close it
        """
        client.send(self.code)
        client.send(self.content_type)
        client.send('Connection: close\n\n')
        client.sendall(self.content)
