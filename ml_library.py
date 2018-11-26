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

# LDD Services
def ml_ortho(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=1&crs=EPSG:3857&dpiMode=7&featureCount=10&format=image/png&layers=0&styles&url=http://"+requests.utils.quote(service_url)	
	wms_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not wms_layer.isValid():
  		print("LayerService failed to load!")

# GISTNU Services
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

# GISTDA Services
def ml_gistdaq1(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&url=https://"+requests.utils.quote(service_url)
	service_uri += "?api_key%3D5d7613757d3f478390339f52db26925c&zmax=18&zmin=0"
	gdq1_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not gdq1_layer.isValid():
  		print("LayerService failed to load!")

def ml_gistdaq2(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "type=xyz&url=https://"+requests.utils.quote(service_url)
	service_uri += "?api_key%3D8be4516d85c44bf4826fce62afeddf71&zmax=18&zmin=0"
	gdq2_layer = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not gdq2_layer.isValid():
  		print("LayerService failed to load!")

# Flood Services 2006-2016
def ml_gistdaflood2006(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2006&styles&url=http://"+requests.utils.quote(service_url)
	flood2006 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2006.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2007(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2007&styles&url=http://"+requests.utils.quote(service_url)
	flood2007 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2007.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2008(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2008&styles&url=http://"+requests.utils.quote(service_url)
	flood2008 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2008.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2009(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2009&styles&url=http://"+requests.utils.quote(service_url)
	flood2009 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2009.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2010(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2010&styles&url=http://"+requests.utils.quote(service_url)
	flood2010 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2010.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2011(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2011&styles&url=http://"+requests.utils.quote(service_url)
	flood2011 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2011.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2012(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2012&styles&url=http://"+requests.utils.quote(service_url)
	flood2012 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2012.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2013(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2013&styles&url=http://"+requests.utils.quote(service_url)
	flood2013 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2013.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2014(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2014&styles&url=http://"+requests.utils.quote(service_url)
	flood2014 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2014.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2015(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2015&styles&url=http://"+requests.utils.quote(service_url)
	flood2015 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2015.isValid():
  		print("LayerService failed to load!")

def ml_gistdaflood2016(self, service_url, name):
	import requests
	import qgis.utils	
	service_uri = "contextualWMSLegend=0&crs=EPSG:3857&dpiMode=7&featureCount=10&TILED=true&format=image/png&layers=fram:flood_area_2016&styles&url=http://"+requests.utils.quote(service_url)
	flood2016 = qgis.utils.iface.addRasterLayer(service_uri, name, "wms")
	if not flood2016.isValid():
  		print("LayerService failed to load!")