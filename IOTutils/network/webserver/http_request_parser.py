class HTTPRequestParser:
    def __init__(self, r):
        """
        HTTP Request class. All elements callables
        :r: bytes | raw http request
        """
        # Splitting Lines
        r = r.decode()
        r = r.split("\r\n")

        # Getting Method, Path and Protocol from first header
        self.method, self.path, self.protocol = r.pop(0).split()

        try:
            self.raw_params = self.path.split("?")[1]
        except:
            self.raw_params = None

        # Parsing URL parameters
        self.parameters = self.parse_parameters()
        self.path = self.path.split("?")[0]
        # Parsing other headers as Name: Value
        self.headers = self.parse_headers(r)

    def parse_headers(self, header_list):
        """
        :header_list: list, Http request without method/path/protocol, splitted by lines
        :return: Dict ; headers by name: value
        """
        headers = {}
        for header in header_list:
            try:
                # Seperating header strings as name: value
                slices = header.split(": ", 1)
                headers[slices[0]] = slices[1]
            except:
                # Some headers may be improperly formatted. Ignoring them.
                pass
        return headers

    def parse_parameters(self):
        """
        Returns: List of tuples. Key of value may be empty
        """
        formatted_parameters = []

        parameters = self.path.split("?")

        # Checking if parameters are present
        if len(parameters) > 1:
            parameters = parameters[1]
            # Splitting parameters into fragments
            fragments = parameters.split("&")
            # Adding fragments to the returned list
            for frag in fragments:
                key_value = frag.split("=", 1)
                # Parameters doesn't have value
                if len(key_value) == 1:
                    formatted_parameters.append((key_value[0], ''))
                # Parameters has value
                else:
                    formatted_parameters.append((key_value[0], key_value[1]))
        return formatted_parameters

    def params_dict(self):
        return {k: v for k, v in self.parameters}
