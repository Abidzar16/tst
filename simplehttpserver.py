#!/usr/bin/env python
# coding: utf-8

# In[16]:


import http.server
import socketserver


# In[21]:


port = 9876 # masukan nilai port-nya


# In[22]:


handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), handler) as httpd:
    print("serving at port", port)
    httpd.serve_forever()


# In[ ]:




