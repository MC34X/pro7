# -*- coding: utf-8 -*-
from .transport import TPersistentHttpClient
from thrift.protocol import TCompactProtocol
from akad import AuthService, TalkService, CallService

class Session:

    def __init__(self, url, headers, path=''):
        self.host = url + path
        self.headers = headers

    def Auth(self, isopen=True):
        self.transport = TPersistentHttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._auth  = AuthService.Client(self.protocol)

        return self._auth

    def Talk(self, isopen=True):
        self.transport = TPersistentHttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._talk  = TalkService.Client(self.protocol)

        return self._talk

    def Call(self, isopen=True):
        self.transport = TPersistentHttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._call  = CallService.Client(self.protocol)

        return self._call
