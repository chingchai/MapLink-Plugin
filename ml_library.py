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