# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:18:50 2021

@author: Aslam
"""
import src.prov.model as prov

document = prov.ProvDocument()
document.set_default_namespace('http://bundle-plus.org/')
document.add_namespace('env','http://bundle-plus.org/')
#document.entity('env:aslam',{"env:type": "government"})
document.entity('e000010')

b1=document.bundle_p('b1',{"env:type": 'government',"env:type1": "value"})
e1=b1.entity('e001',{"env:type": "government"})


#print (b1.parent)
#print (len(b2.listOfBundles))
#for x in range(len(b1.listOfBundles)): 
 #   print(b1.listOfBundles[x])
#print(document.get_provn_p())  
print(document.get_provn()) 