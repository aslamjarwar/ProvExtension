# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:27:36 2021

@author: Aslam
"""

class ProvDocument (PROV):
    def _init_(self, records=None, namespaces=None):
        self._namespaces=namespaces
        self._bundles = dict()
    
    def set_default_namespace(self,uri):
        self._namespaces.set_default_namespace(uri)
        
    def bundle(self,uri):
        self._namespaces.set_default_namespace(uri)
        