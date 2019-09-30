#!/usr/bin/env python
# coding: utf-8

# In[5]:


from http.server import HTTPServer,SimpleHTTPRequestHandler
from socketserver import BaseServer
import ssl


# In[ ]:


port = 1443

httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='cacert.pem', keyfile='privkey.pem', server_side=True)
httpd.serve_forever()

