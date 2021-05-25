# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:33:42 2021

@author: Aslam
"""


class MultiDict:
    def __init__(self):
        self.dict = {}

    def __setitem__(self, key, value):
        try:
            self.dict[key].append(value)
            print('*********',key, value)
        except KeyError:
            self.dict[key] = [value]

    def __getitem__(self, key):
        return self.dict[key]
    
    def items(self,key):
        return self.__getitem__(key)

multiDict=   MultiDict()

class ProvBundle(object):
    _bundles=dict()
    _bundleRecords=list()
    def __init__(self, records=None, identifier=None, namespaces=None, attributes_env=None,parent_identifier=None):
        self._records=list()
        self._records=identifier
        self._identifier=identifier
        self._attributes_env=attributes_env
        self._parent_identifer=parent_identifier
    
    def parentChild(self,parent,child):
        multiDict[parent]=child
        #return multiDict    
    @property
    def identifier (self):
        return self._identifier
    @property
    def env_attributes (self):
        return self._attributes_env
    @property
    def b_parent_id(self):
        return self._parent_identifer
    
    @property
    def bundles(self):
        """
        Returns bundles contained in the document

        :return: Iterable of :py:class:`ProvBundle`.
        """
        return self._bundles.values()
    # Miscellaneous functions
    def is_document(self):
        """
        `True` if the object is a document, `False` otherwise.

        :return: bool
        """
        return False
    
    def bundle_p(self, identifier, other_attributes=None,parent=None):
        self._parent_identifer=self.b_parent_id  
        #if (self._parent_identifer is None):
         #   self._parent_identifer='root' 
        #x=self._bundles['b1']
        #print(x.identifier)
        b=ProvBundle(identifier=identifier, attributes_env=other_attributes,parent_identifier=parent)
        self._bundles[identifier]=b
        self._bundleRecords.append(b)
        self.parentChild(parent,identifier)
        return b
    
    def print_prov(self):
        #print ("oo")
        line=[]
        if self.is_document():
            line.extend(bundle.print_prov() for bundle in self.bundles)
        print (line)
        return line

class ProvDocument(ProvBundle):
    def __init__(self, records=None, namespaces=None):
        self._namespace=namespaces
        
        ProvBundle.__init__(
            self, records=None, identifier=None, namespaces=namespaces, attributes_env=None,parent_identifier=None
        )
        
    def set_default_namespace(self,uri):
        self._namespace=uri
        return self._namespace
        
    def bundle(self, identifier, other_attributes=None):
        b=ProvBundle(identifier=identifier, attributes_env=other_attributes,parent_identifier='root')
        self._bundles[identifier]=b
        self._bundleRecords.append(b)
        
        return b
    
    def is_document(self):
        """
        `True` if the object is a document, `False` otherwise.

        :return: bool
        """
        return True
  
    
document=ProvDocument()
# =============================================================================
document.set_default_namespace('http://bundle-plus.org/')
b1=document.bundle('b1', {'prov:type':'yy'})
b2=b1.bundle_p('b2',parent=b1.identifier)
b3=document.bundle('b3', {'prov:type':'b33333'})
b4=b1.bundle_p('b4',parent=b1.identifier)
# b5=b4.bundle_p('b5',parent=b4.identifier)
# for b in document._bundleRecords:
#     print("Identifier {0} Environment Attributes {1} parent_id {2}".format(b.identifier,b.env_attributes,b.b_parent_id))
# 
# #print (multiDict.__getitem__(b1.identifier))
# 
# print (len(multiDict.items(b1.identifier)))
# print (multiDict.__sizeof__())
# for x in multiDict.items(b1.identifier):
#     print (x)
# 
# # Append multiple value to a key in dictionary
# def add_values_in_dict(sample_dict, key, list_of_values):
#     """Append multiple values to a key in the given dictionary"""
#     if key not in sample_dict:
#         sample_dict[key] = list()
#     sample_dict[key].extend(list_of_values)
#     return sample_dict
# 
# # Append multiple values for existing key 'at'
# word_freq={}
# word_freq = add_values_in_dict(word_freq, 'at', [20, 21, 'b1'])
# word_freq = add_values_in_dict(word_freq, 'b1', [20, 21, 22,23])
# print(len(word_freq.get('b1')))
# =============================================================================
document.print_prov()
