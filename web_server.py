from codecs import latin_1_encode
from wsgiref.simple_server import make_server
# using wsgi protocol: a modern way of connecting  web servers to code that runs to provide the services.
# The Web Server Gateway Interface (WSGI) is a specification for simple and universal interface between web servers
#  and web applications or frameworks for the Python programming language


def my_handler(environ, start_response):
    path_info = environ.get("PATH_INFO", None)
    query_string = environ.get("QUERY_STRING", None)
    response_body = "You asked for {0} with query {1}".format(path_info, query_string)
    response_headers = [("Content-Type", "text/plain"),
                        ("Content-Length", str(len(response_body)))]
    start_response("200 OK", response_headers)
    response = latin_1_encode(response_body)[0]
    return [response]


httpd = make_server("127.0.0.1", 8000, my_handler)
httpd.serve_forever()  # starts the server for listening for requests

# Creates a web server on the local machine, listening at port 8000.
# Each incoming html request causes the server to call my_handler which processes the request and
#  returns the appropriate response.
# e.g. Navigate to http://127.0.0.1:8000/catalogue?category=guitars

# The web server will keep running until interrupted (Ctrl+F2).
