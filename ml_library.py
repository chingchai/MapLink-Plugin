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
from urllib.parse import quote

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


def ml_basemapapi(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&zmin=0&zmax=24&url=http://"+requests.utils.quote(service_url)
	service_uri += "?APPID=282ba1192254376a27ec79893cb2b1d5"
	api_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not api_layer.isValid():
  		print("LayerService failed to load!")

def ml_bingmap(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&zmin=0&zmax=24&url=http://"+requests.utils.quote(service_url)
	service_uri += "?g=1"
	bing_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not bing_layer.isValid():
  		print("LayerService failed to load!")

def ml_tfmmap_a(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&zmin=0&zmax=24&url=http://"+requests.utils.quote(service_url)
	service_uri += "?apikey=7c352c8ff1244dd8b732e349e0b0fe8d"
	tfma_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not tfma_layer.isValid():
  		print("LayerService failed to load!")

def ml_tfmmap_b(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&zmin=0&zmax=24&url=http://"+requests.utils.quote(service_url)
	service_uri += "?apikey=7c352c8ff1244dd8b732e349e0b0fe8d"
	tfmb_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not tfmb_layer.isValid():
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

def ml_overlay_prov(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=1&crs=EPSG:4326&dpiMode=7&format=image/png&layers=gistdata:province&styles=&url=http://"+requests.utils.quote(service_url)
	gs_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not gs_layer.isValid():
  		print("LayerService failed to load!")


def ml_overlay_tam(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=1&crs=EPSG:4326&dpiMode=7&format=image/png&layers=gistdata:tambon&styles=&url=http://"+requests.utils.quote(service_url)
	gs_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not gs_layer.isValid():
  		print("LayerService failed to load!")


def ml_overlay_amp(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=1&crs=EPSG:4326&dpiMode=7&format=image/png&layers=gistdata:amphoe&styles=&url=http://"+requests.utils.quote(service_url)
	gs_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not gs_layer.isValid():
  		print("LayerService failed to load!")