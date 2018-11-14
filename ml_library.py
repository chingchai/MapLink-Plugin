#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------
#    ml_library - base tiles xyz library
# --------------------------------------------------------

import io
import re
import sys
import time
import locale
import random
import os.path
import operator
import tempfile
import xml.etree.ElementTree

from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.gui import QgsMessageBar


#--------------------------------------------------------
#    Add basemap tiles xyz
# --------------------------------------------------------

def ml_basemap(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&zmin=0&zmax=22&url=http://"+requests.utils.quote(service_url)	
	tms_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not tms_layer.isValid():
  		print("LayerService failed to load!")

#--------------------------------------------------------
#    Add Overlay WMS Service
# --------------------------------------------------------

def ml_ortho(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=1&crs=EPSG:3857&dpiMode=7&featureCount=10&format=image/png&layers=0&styles&url=http://"+requests.utils.quote(service_url)	
	wms_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not wms_layer.isValid():
  		print("LayerService failed to load!")

def ml_overlay(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=1&crs=EPSG:4326&dpiMode=7&format=image/png&layers=gistdata:province&styles=&url=http://"+requests.utils.quote(service_url)
	gs_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not gs_layer.isValid():
  		print("LayerService failed to load!")

#service_uri = "contextualWMSLegend=1&crs=EPSG:4326&dpiMode=7&format=image/png&layers=gistdata:amphoe&styles=&url=http://"+requests.utils.quote(service_url)
#service_uri = "contextualWMSLegend=1&crs=EPSG:4326&dpiMode=7&format=image/png&layers=gistdata:tambon&styles=&url=http://"+requests.utils.quote(service_url)