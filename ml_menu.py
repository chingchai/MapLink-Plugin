#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
                      MapLink QGIS plugin
 Generates ****************************************************************.
                            -------------------
        begin                : 2018-11-11
        License              : MIT License
        email                : ps.gistnu@gmail.com
		github				 : https://github.com/chingchai/MapLink-Plugin
 ***************************************************************************/
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from .ml_library import *
# ---------------------------------------------

class ml_menu:
	def __init__(self, iface):
		self.iface = iface
		self.ml_menu = None

	def ml_add_submenu(self, submenu):
		if self.ml_menu != None:
			self.ml_menu.addMenu(submenu)
		else:
			self.iface.addPluginToMenu("&maplink", submenu.menuAction())


	def initGui(self):
		# Uncomment the following two lines to have ml accessible from a top-level menu
	

		self.ml_menu = QMenu(QCoreApplication.translate("maplink", "MapLink"))
		self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.ml_menu)
		
		#########################		
		# Menu Map
		#####################

		#icon_path = self._menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/.....png"))
		self.google_menu = QMenu(u'Google')		
		self.ml_add_submenu(self.google_menu)
		self.google_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png"))

		#Menu Carto
		self.carto_menu = QMenu(u'Carto')		
		self.ml_add_submenu(self.carto_menu)
		self.carto_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_carto_l.jpg"))

		#Menu ESRI
		self.esri_menu = QMenu(u'ESRI')		
		self.ml_add_submenu(self.esri_menu)
		self.esri_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png"))

		#Menu Stamen
		self.stamen_menu = QMenu(u'Stamen')		
		self.ml_add_submenu(self.stamen_menu)
		self.stamen_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png"))

		#Menu OpenStreetMap
		self.osm_menu = QMenu(u'OpenStreetMap')		
		self.ml_add_submenu(self.osm_menu)
		self.osm_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png"))


		#Menu Wikimedia 
		self.wikimap_menu = QMenu(u'Wikimedia')	
		self.ml_add_submenu(self.wikimap_menu)
		self.wikimap_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_wk.png"))


		#OpenWeatherMap 
		self.owm_menu = QMenu(u'OpenWeatherMap')	
		self.ml_add_submenu(self.owm_menu)
		self.owm_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_owm.jpg"))


		#Menu Bing Map
		self.bingmap_menu = QMenu(u'Bing Map')	
		self.ml_add_submenu(self.bingmap_menu)
		self.bingmap_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_bing.png"))


		#Menu Overlay LDD
		self.ldd_menu = QMenu(u'LDD Ortho')	
		self.ml_add_submenu(self.ldd_menu)
		self.ldd_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ldd.png"))
		
		#Menu GISTNU
		self.gs_menu = QMenu(u'GISTNU WMS')	
		self.ml_add_submenu(self.gs_menu)
		self.gs_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_gs.png"))

		#Menu ThunderForest Map
		self.tfm_menu = QMenu(u'ThunderForest Map')	
		self.ml_add_submenu(self.tfm_menu)
		self.tfm_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png"))

		#Menu GISTDA 
		self.gd_menu = QMenu(u'GISTDA WMS')	
		self.ml_add_submenu(self.gd_menu)
		self.gd_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png"))

		#########################		
		# Icon Map
		#####################


		#########################		
		# GISTDA
		#####################

		#GISTDA Thaichote
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdbm_action = QAction(icon, u'GISTDA Thaichote ', self.iface.mainWindow())
		self.gdbm_action.triggered.connect(self.gdbm_call)		
		self.gd_menu.addAction(self.gdbm_action)

		#GISTDA Planet Map Q1 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdpnq1_action = QAction(icon, u'GISTDA Planet Map Q1 ', self.iface.mainWindow())
		self.gdpnq1_action.triggered.connect(self.gdpnq1_call)		
		self.gd_menu.addAction(self.gdpnq1_action)

		#GISTDA Planet Map Q2
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdpnq2_action = QAction(icon, u'GISTDA Planet Map Q2', self.iface.mainWindow())
		self.gdpnq2_action.triggered.connect(self.gdpnq2_call)		
		self.gd_menu.addAction(self.gdpnq2_action)

		#GISTDA Flood Map 2006
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2006_action = QAction(icon, u'GISTDA Flood 2006', self.iface.mainWindow())
		self.gdfld2006_action.triggered.connect(self.gdfld2006_call)		
		self.gd_menu.addAction(self.gdfld2006_action)

		#GISTDA Flood Map 2007
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2007_action = QAction(icon, u'GISTDA Flood 2007', self.iface.mainWindow())
		self.gdfld2007_action.triggered.connect(self.gdfld2007_call)		
		self.gd_menu.addAction(self.gdfld2007_action)

		#GISTDA Flood Map 2008
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2008_action = QAction(icon, u'GISTDA Flood 2008', self.iface.mainWindow())
		self.gdfld2008_action.triggered.connect(self.gdfld2008_call)		
		self.gd_menu.addAction(self.gdfld2008_action)

		#GISTDA Flood Map 2009
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2009_action = QAction(icon, u'GISTDA Flood 2009', self.iface.mainWindow())
		self.gdfld2009_action.triggered.connect(self.gdfld2009_call)		
		self.gd_menu.addAction(self.gdfld2009_action)

		#GISTDA Flood Map 2010
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2010_action = QAction(icon, u'GISTDA Flood 2010', self.iface.mainWindow())
		self.gdfld2010_action.triggered.connect(self.gdfld2010_call)		
		self.gd_menu.addAction(self.gdfld2010_action)

		#GISTDA Flood Map 2011
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2011_action = QAction(icon, u'GISTDA Flood 2011', self.iface.mainWindow())
		self.gdfld2011_action.triggered.connect(self.gdfld2011_call)		
		self.gd_menu.addAction(self.gdfld2011_action)

		#GISTDA Flood Map 2012
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2012_action = QAction(icon, u'GISTDA Flood 2012', self.iface.mainWindow())
		self.gdfld2012_action.triggered.connect(self.gdfld2012_call)		
		self.gd_menu.addAction(self.gdfld2012_action)

		#GISTDA Flood Map 2013
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2013_action = QAction(icon, u'GISTDA Flood 2013', self.iface.mainWindow())
		self.gdfld2013_action.triggered.connect(self.gdfld2013_call)		
		self.gd_menu.addAction(self.gdfld2013_action)

		#GISTDA Flood Map 2014
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2014_action = QAction(icon, u'GISTDA Flood 2014', self.iface.mainWindow())
		self.gdfld2014_action.triggered.connect(self.gdfld2014_call)		
		self.gd_menu.addAction(self.gdfld2014_action)

		#GISTDA Flood Map 2015
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2015_action = QAction(icon, u'GISTDA Flood 2015', self.iface.mainWindow())
		self.gdfld2015_action.triggered.connect(self.gdfld2015_call)		
		self.gd_menu.addAction(self.gdfld2015_action)

		#GISTDA Flood Map 2016
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_gd.png")
		self.gdfld2016_action = QAction(icon, u'GISTDA Flood 2016', self.iface.mainWindow())
		self.gdfld2016_action.triggered.connect(self.gdfld2016_call)		
		self.gd_menu.addAction(self.gdfld2016_action)

		#########################		
		# Thunderforest Map
		#####################

		#ThunderForest Map OpenCycleMap 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmocc_action = QAction(icon, u'ThunderForest Map OpenCycle', self.iface.mainWindow())
		self.tfmocc_action.triggered.connect(self.tfmocc_call)		
		self.tfm_menu.addAction(self.tfmocc_action)

		#ThunderForest Map Transport
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmtst_action = QAction(icon, u'ThunderForest Map Transport', self.iface.mainWindow())
		self.tfmtst_action.triggered.connect(self.tfmtst_call)		
		self.tfm_menu.addAction(self.tfmtst_action)

		#ThunderForest Map Landscape
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmlsc_action = QAction(icon, u'ThunderForest Map Landscape', self.iface.mainWindow())
		self.tfmlsc_action.triggered.connect(self.tfmlsc_call)		
		self.tfm_menu.addAction(self.tfmlsc_action)

		#ThunderForest Map Outdoors
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmods_action = QAction(icon, u'ThunderForest Map Outdoors', self.iface.mainWindow())
		self.tfmods_action.triggered.connect(self.tfmods_call)		
		self.tfm_menu.addAction(self.tfmods_action)

		#ThunderForest Map Transport Dark
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmtsd_action = QAction(icon, u'ThunderForest Map Transport Dark', self.iface.mainWindow())
		self.tfmtsd_action.triggered.connect(self.tfmtsd_call)		
		self.tfm_menu.addAction(self.tfmtsd_action)

		#ThunderForest Map Spinal 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmspn_action = QAction(icon, u'ThunderForest Map Spinal', self.iface.mainWindow())
		self.tfmspn_action.triggered.connect(self.tfmspn_call)		
		self.tfm_menu.addAction(self.tfmspn_action)

		#ThunderForest Map Pioneer
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmpio_action = QAction(icon, u'ThunderForest Map Pioneer', self.iface.mainWindow())
		self.tfmpio_action.triggered.connect(self.tfmpio_call)		
		self.tfm_menu.addAction(self.tfmpio_action)

		#ThunderForest Map Mobile Atlas
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmmat_action = QAction(icon, u'ThunderForest Map Mobile Atlas', self.iface.mainWindow())
		self.tfmmat_action.triggered.connect(self.tfmmat_call)		
		self.tfm_menu.addAction(self.tfmmat_action)

		#ThunderForest Map Neighbourhood
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_tfm.png")
		self.tfmnbh_action = QAction(icon, u'ThunderForest Map Neighbourhood', self.iface.mainWindow())
		self.tfmnbh_action.triggered.connect(self.tfmnbh_call)		
		self.tfm_menu.addAction(self.tfmnbh_action)


		#########################		
		# OpenWeatherMap
		#####################

		#OpenWeatherMap Temperature
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_owm.jpg")
		self.owmtem_action = QAction(icon, u'OpenWeatherMap Temperature', self.iface.mainWindow())
		self.owmtem_action.triggered.connect(self.owmtem_call)		
		self.owm_menu.addAction(self.owmtem_action)

		#OpenWeatherMap Clouds
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_owm.jpg")
		self.owmcl_action = QAction(icon, u'OpenWeatherMap Clouds', self.iface.mainWindow())
		self.owmcl_action.triggered.connect(self.owmcl_call)		
		self.owm_menu.addAction(self.owmcl_action)

		#OpenWeatherMap Wind Speed
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_owm.jpg")
		self.owmws_action = QAction(icon, u'OpenWeatherMap Wind Speed', self.iface.mainWindow())
		self.owmws_action.triggered.connect(self.owmws_call)		
		self.owm_menu.addAction(self.owmws_action)


		#########################		
		# Bing Map
		#####################

		#Bing VirtualEarth
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_bing.png")
		self.bingve_action = QAction(icon, u'Bing VirtualEarth', self.iface.mainWindow())
		self.bingve_action.triggered.connect(self.bingve_call)		
		self.bingmap_menu.addAction(self.bingve_action)

		#########################		
		# Wikimedia Map
		#####################

		#Wikimedia Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_wk.png")
		self.wikimap_action = QAction(icon, u'Wikimedia Map', self.iface.mainWindow())
		self.wikimap_action.triggered.connect(self.wikimap_call)		
		self.wikimap_menu.addAction(self.wikimap_action)

		#Wikimedia Hike Bike Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_wk.png")
		self.wikihbm_action = QAction(icon, u'Wikimedia Hike Bike Map', self.iface.mainWindow())
		self.wikihbm_action.triggered.connect(self.wikihbm_call)		
		self.wikimap_menu.addAction(self.wikihbm_action)



		#########################		
		# LDD WMS
		#####################

		#LDD WMS
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_ortho.png")
		self.lddortho_action = QAction(icon, u'LDD Ortho', self.iface.mainWindow())
		self.lddortho_action.triggered.connect(self.lddortho_call)		
		self.ldd_menu.addAction(self.lddortho_action)


		#########################		
		# GeoServer GISTNU
		#####################


		#GeoServer GISTNU WMS Province
		icon = QIcon(os.path.dirname(__file__) + "/icons/server_map.png")
		self.prov_action = QAction(icon, u'ขอบเขตจังหวัด', self.iface.mainWindow())
		self.prov_action.triggered.connect(self.prov_call)		
		self.gs_menu.addAction(self.prov_action)
		
		#GeoServer GISTNU WMS Amphoe
		icon = QIcon(os.path.dirname(__file__) + "/icons/server_map.png")
		self.amp_action = QAction(icon, u'ขอบเขตอำเภอ', self.iface.mainWindow())
		self.amp_action.triggered.connect(self.amp_call)		
		self.gs_menu.addAction(self.amp_action)	
		
		#GeoServer GISTNU WMS Tambon
		icon = QIcon(os.path.dirname(__file__) + "/icons/server_map.png")
		self.tambon_action = QAction(icon, u'ขอบเขตตำบล', self.iface.mainWindow())
		self.tambon_action.triggered.connect(self.tambon_call)		
		self.gs_menu.addAction(self.tambon_action)	

		#Carto Antique
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_carto_l.jpg")
		self.cartoantique_action = QAction(icon, u'Carto Antique', self.iface.mainWindow())
		self.cartoantique_action.triggered.connect(self.cartoantique_call)		
		self.carto_menu.addAction(self.cartoantique_action)

		#Carto Dark
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_carto_l.jpg")
		self.cartodark_action = QAction(icon, u'Carto Dark', self.iface.mainWindow())
		self.cartodark_action.triggered.connect(self.cartodark_call)		
		self.carto_menu.addAction(self.cartodark_action)

		#Carto Eco
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_carto_l.jpg")
		self.cartoeco_action = QAction(icon, u'Carto Eco', self.iface.mainWindow())
		self.cartoeco_action.triggered.connect(self.cartoeco_call)		
		self.carto_menu.addAction(self.cartoeco_action)

		#Carto Light
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_carto_l.jpg")
		self.cartolight_action = QAction(icon, u'Carto Light', self.iface.mainWindow())
		self.cartolight_action.triggered.connect(self.cartolight_call)		
		self.carto_menu.addAction(self.cartolight_action)

		#########################		
		# ESRI 
		#####################
		#Esri Boundaries and Places 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esriboundary_action = QAction(icon, u'Esri Boundaries and Places', self.iface.mainWindow())
		self.esriboundary_action.triggered.connect(self.esriboundary_call)		
		self.esri_menu.addAction(self.esriboundary_action)

		#Esri Dark Gray 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esridarkgray_action = QAction(icon, u'Esri Dark Gray', self.iface.mainWindow())
		self.esridarkgray_action.triggered.connect(self.esridarkgray_call)		
		self.esri_menu.addAction(self.esridarkgray_action)

		#Esri DeLorme World Base Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esridelorme_action = QAction(icon, u'ESri DeLorme', self.iface.mainWindow())
		self.esridelorme_action.triggered.connect(self.esridelorme_call)		
		self.esri_menu.addAction(self.esridelorme_action)

		#Esri Imagery 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esriimagery_action = QAction(icon, u'Esri Imagery', self.iface.mainWindow())
		self.esriimagery_action.triggered.connect(self.esriimagery_call)		
		self.esri_menu.addAction(self.esriimagery_action)
	
		#Esri Light Gray 
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esrilightgray_action = QAction(icon, u'Esri Light Gray', self.iface.mainWindow())
		self.esrilightgray_action.triggered.connect(self.esrilightgray_call)		
		self.esri_menu.addAction(self.esrilightgray_action)

		#Esri National Geographic World Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esrinational_action = QAction(icon, u'Esri National Geographic', self.iface.mainWindow())
		self.esrinational_action.triggered.connect(self.esrinational_call)		
		self.esri_menu.addAction(self.esrinational_action)

		#Esri Ocean Basemap
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esriocean_action = QAction(icon, u'Esri Ocean', self.iface.mainWindow())
		self.esriocean_action.triggered.connect(self.esriocean_call)		
		self.esri_menu.addAction(self.esriocean_action)

		#Esri Physical Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esriphysical_action = QAction(icon, u'Esri Physical', self.iface.mainWindow())
		self.esriphysical_action.triggered.connect(self.esriphysical_call)		
		self.esri_menu.addAction(self.esriphysical_action)

		#Esri Shaded Relief
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esrishaded_action = QAction(icon, u'Esri Shaded Relief', self.iface.mainWindow())
		self.esrishaded_action.triggered.connect(self.esrishaded_call)		
		self.esri_menu.addAction(self.esrishaded_action)

		#Esri Street Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esristreet_action = QAction(icon, u'Esri Street', self.iface.mainWindow())
		self.esristreet_action.triggered.connect(self.esristreet_call)		
		self.esri_menu.addAction(self.esristreet_action)

		#Esri Terrain Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esriterrain_action = QAction(icon, u'Esri Terrain', self.iface.mainWindow())
		self.esriterrain_action.triggered.connect(self.esriterrain_call)		
		self.esri_menu.addAction(self.esriterrain_action)
		
		#Esri World Topo Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esritopo_action = QAction(icon, u'Esri Topographic', self.iface.mainWindow())
		self.esritopo_action.triggered.connect(self.esritopo_call)		
		self.esri_menu.addAction(self.esritopo_action)

		#Esri World Transportation
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png")
		self.esritransport_action = QAction(icon, u'Esri Transport', self.iface.mainWindow())
		self.esritransport_action.triggered.connect(self.esritransport_call)		
		self.esri_menu.addAction(self.esritransport_action)

		
		#############
		#Google Maps
		#############

		#Google Maps
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png")
		self.googlemaps_action = QAction(icon, u'Google Maps', self.iface.mainWindow())
		self.googlemaps_action.triggered.connect(self.googlemaps_call)		
		self.google_menu.addAction(self.googlemaps_action)
		
				
		#Google Terrain
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png")
		self.ml_googleterrain_action = QAction(icon, u'Google Terrain', self.iface.mainWindow())
		self.ml_googleterrain_action.triggered.connect(self.googleterrain_call)		
		self.google_menu.addAction(self.ml_googleterrain_action)

		#Google Terrain Hybrid
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png")
		self.ml_googleterrainhybrid_action = QAction(icon, u'Google Terrain Hybrid', self.iface.mainWindow())
		self.ml_googleterrainhybrid_action.triggered.connect(self.googleterrainhybrid_call)		
		self.google_menu.addAction(self.ml_googleterrainhybrid_action)

		#Google Satellite
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png")
		self.googlesatellite_action = QAction(icon, u'Google Satellite', self.iface.mainWindow())
		self.googlesatellite_action.triggered.connect(self.googlesatellite_call)		
		self.google_menu.addAction(self.googlesatellite_action)

		#Google Satellite Hybrid
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png")
		self.ml_googlesatellitehybrid_action = QAction(icon, u'Google Satellite Hybrid', self.iface.mainWindow())
		self.ml_googlesatellitehybrid_action.triggered.connect(self.googlesatellitehybrid_call)		
		self.google_menu.addAction(self.ml_googlesatellitehybrid_action)
		
		
		#############
		#Stamen
		#############

	
		
		#Stamen Toner
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamentoner_action = QAction(icon, u'Stamen Toner', self.iface.mainWindow())
		self.stamentoner_action.triggered.connect(self.stamentoner_call)		
		self.stamen_menu.addAction(self.stamentoner_action)

		# Stamen Toner Background
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamentonerbkg_action = QAction(icon, u'Stamen Toner Background', self.iface.mainWindow())
		self.stamentonerbkg_action.triggered.connect(self.stamentonerbkg_call)		
		self.stamen_menu.addAction(self.stamentonerbkg_action)

		# Stamen Toner Hybrid
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamentonerhybrid_action = QAction(icon, u'Stamen Toner Hybrid', self.iface.mainWindow())
		self.stamentonerhybrid_action.triggered.connect(self.stamentonerhybrid_call)		
		self.stamen_menu.addAction(self.stamentonerhybrid_action)

		# Stamen Toner Lite
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamentonerlite_action = QAction(icon, u'Stamen Toner Lite', self.iface.mainWindow())
		self.stamentonerlite_action.triggered.connect(self.stamentonerlite_call)		
		self.stamen_menu.addAction(self.stamentonerlite_action)
		
		# Stamen Terrain
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamenterrain_action = QAction(icon, u'Stamen Terrain', self.iface.mainWindow())
		self.stamenterrain_action.triggered.connect(self.stamenterrain_call)		
		self.stamen_menu.addAction(self.stamenterrain_action)

		# Stamen Terrain Background
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamenterrainbkg_action = QAction(icon, u'Stamen Terrain Background', self.iface.mainWindow())
		self.stamenterrainbkg_action.triggered.connect(self.stamenterrainbkg_call)		
		self.stamen_menu.addAction(self.stamenterrainbkg_action)

		
		# Stamen Watercolor
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png")
		self.stamenwatercolor_action = QAction(icon, u'Stamen Watercolor', self.iface.mainWindow())
		self.stamenwatercolor_action.triggered.connect(self.stamenwatercolor_call)		
		self.stamen_menu.addAction(self.stamenwatercolor_action)
			

		#############
		#OpenStreetMap 
		#############


		# OpenStreetMap Mapnik
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmapmnk_action = QAction(icon, u'OpenStreetMap Mapnik', self.iface.mainWindow())
		self.openstreetmapmnk_action.triggered.connect(self.openstreetmapmnk_call)		
		self.osm_menu.addAction(self.openstreetmapmnk_action)

		# OpenStreetMap BlackAndWhite
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmapbaw_action = QAction(icon, u'OpenStreetMap BlackAndWhite', self.iface.mainWindow())
		self.openstreetmapbaw_action.triggered.connect(self.openstreetmapbaw_call)		
		self.osm_menu.addAction(self.openstreetmapbaw_action)

		# OpenStreetMap France
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmapfnc_action = QAction(icon, u'OpenStreetMap France', self.iface.mainWindow())
		self.openstreetmapfnc_action.triggered.connect(self.openstreetmapfnc_call)		
		self.osm_menu.addAction(self.openstreetmapfnc_action)

		# OpenStreetMap DE
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmapde_action = QAction(icon, u'OpenStreetMap DE', self.iface.mainWindow())
		self.openstreetmapde_action.triggered.connect(self.openstreetmapde_call)		
		self.osm_menu.addAction(self.openstreetmapde_action)

		# OpenStreetMap CH
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmapch_action = QAction(icon, u'OpenStreetMap CH', self.iface.mainWindow())
		self.openstreetmapch_action.triggered.connect(self.openstreetmapch_call)		
		self.osm_menu.addAction(self.openstreetmapch_action)

		# OpenStreetMap HOT
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmaphot_action = QAction(icon, u'OpenStreetMap HOT', self.iface.mainWindow())
		self.openstreetmaphot_action.triggered.connect(self.openstreetmaphot_call)		
		self.osm_menu.addAction(self.openstreetmaphot_action)

		# OpenStreetMap Topo
		icon = QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png")
		self.openstreetmaptp_action = QAction(icon, u'OpenStreetMap Topo', self.iface.mainWindow())
		self.openstreetmaptp_action.triggered.connect(self.openstreetmaptp_call)		
		self.osm_menu.addAction(self.openstreetmaptp_action)

	def unload(self):
		if self.ml_menu != None:
			self.iface.mainWindow().menuBar().removeAction(self.ml_menu.menuAction())
		else:
			self.iface.removePluginMenu("&maplink", self.basemap_menu.menuAction())

	#########################		
	# Connected Tiles BaseMap
	#####################
	
	
	#########################		
	# Carto
	#####################
	
	def cartolight_call(self):
		service_url ="a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png" 
		name = "Carto Light"
		ml_basemap(self.iface,service_url, name)
		
	def cartodark_call(self):
		service_url ="a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png" 
		name = "Carto Dark"
		ml_basemap(self.iface,service_url, name)
	
	def cartoantique_call(self):
		service_url ="cartocdn_a.global.ssl.fastly.net/base-antique/{z}/{x}/{y}.png" 
		name = "Carto Antique"
		ml_basemap(self.iface,service_url, name)

	def cartoeco_call(self):
		service_url ="cartocdn_a.global.ssl.fastly.net/base-eco/{z}/{x}/{y}.png" 
		name = "Carto Eco"
		ml_basemap(self.iface,service_url, name)
	
	#########################		
	# ESRI
	#####################
	def esridelorme_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri DeLorme"
		ml_basemap(self.iface,service_url, name)
	
	def esrinational_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri National Geographic"
		ml_basemap(self.iface,service_url, name)
	
	def esriocean_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Ocean_Basemap/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Ocean"
		ml_basemap(self.iface,service_url, name)

	def esriboundary_call(self):
		service_url ="server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Boundaries and Places"
		ml_basemap(self.iface,service_url, name)
	
	def esridarkgray_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Dark Gray"
		ml_basemap(self.iface,service_url, name)

	def esrilightgray_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Light Gray"
		ml_basemap(self.iface,service_url, name)

	def esriimagery_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Imagery"
		ml_basemap(self.iface,service_url, name)

	def esriphysical_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Physical"
		ml_basemap(self.iface,service_url, name)
	
	def esristreet_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Street"
		ml_basemap(self.iface,service_url, name)
	
	def esriterrain_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Terrain"
		ml_basemap(self.iface,service_url, name)

	def esritopo_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Topographic"
		ml_basemap(self.iface,service_url, name)
	
	def esritransport_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Transport"
		ml_basemap(self.iface,service_url, name)

	def esrishaded_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Shaded Relief"
		ml_basemap(self.iface,service_url, name)

	#########################		
	# Stamen
	#####################
			
	def stamenwatercolor_call(self):
		service_url = "a.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg" 
		name = "Stamen Watercolor"
		ml_basemap(self.iface,service_url, name)
	
	def stamentoner_call(self):
		service_url ="a.tile.stamen.com/toner/{z}/{x}/{y}.png"
		name = "Stamen Toner"
		ml_basemap(self.iface,service_url, name)
	
	def stamentonerbkg_call(self):
		service_url ="a.tile.stamen.com/toner-background/{z}/{x}/{y}.png"
		name = "Stamen Toner Background"
		ml_basemap(self.iface,service_url, name)

	def stamentonerhybrid_call(self):
		service_url ="a.tile.stamen.com/toner-hybrid/{z}/{x}/{y}.png"
		name = "Stamen Toner Hybrid"
		ml_basemap(self.iface,service_url, name)

	def stamentonerlite_call(self):
		service_url ="a.tile.stamen.com/toner-lite/{z}/{x}/{y}.png"
		name = "Stamen Toner Lite"
		ml_basemap(self.iface,service_url, name)

	
	def stamenterrain_call(self):
		service_url ="a.tile.stamen.com/terrain/{z}/{x}/{y}.png" 
		name = "Stamen Terrain"
		ml_basemap(self.iface,service_url, name)
	
	def stamenterrainbkg_call(self):
		service_url ="a.tile.stamen.com/terrain-background/{z}/{x}/{y}.png" 
		name = "Stamen Terrain Background"
		ml_basemap(self.iface,service_url, name)
	
	##############
	# Google
	############
	def googlemaps_call(self):
		service_url ="mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
		name = "Google Maps"
		ml_basemap(self.iface,service_url, name)


	def googlesatellite_call(self):
		service_url ="mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}" 
		name = "Google Satellite"
		ml_basemap(self.iface,service_url, name)
	

	def googlesatellitehybrid_call(self):
		service_url ="mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}"
		name = "Google Satellite Hybrid"
		ml_basemap(self.iface,service_url, name)
	

	def googleterrain_call(self):
		service_url ="mt0.google.com/vt/lyrs=t&hl=en&x={x}&y={y}&z={z}" 
		name = "Google Terrain"
		ml_basemap(self.iface,service_url, name)

	def googleterrainhybrid_call(self):
		service_url ="mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}"
		name = "Google Terrain Hybrid"
		ml_basemap(self.iface,service_url, name)


	#########################		
	# Openstreetmap
	#########################

	def openstreetmapmnk_call(self):
		service_url ="tile.openstreetmap.org/{z}/{x}/{y}.png"
		name = "OpenStreetMap Mapnik"
		ml_basemap(self.iface,service_url, name)

	def openstreetmapbaw_call(self):
		service_url ="tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png"
		name = "Openstreetmap BlackAndWhite"
		ml_basemap(self.iface,service_url, name)

	def openstreetmapde_call(self):
		service_url ="tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png"
		name = "Openstreetmap DE"
		ml_basemap(self.iface,service_url, name)

	def openstreetmapch_call(self):
		service_url ="tile.osm.ch/switzerland/{z}/{x}/{y}.png"
		name = "Openstreetmap CH"
		ml_basemap(self.iface,service_url, name)

	def openstreetmapfnc_call(self):
		service_url ="tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png"
		name = "Openstreetmap France"
		ml_basemap(self.iface,service_url, name)

	def openstreetmaphot_call(self):
		service_url ="tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"
		name = "Openstreetmap HOT"
		ml_basemap(self.iface,service_url, name)

	def openstreetmaptp_call(self):
		service_url ="c.tile.opentopomap.org/{z}/{x}/{y}.png"
		name = "Openstreetmap Topo"
		ml_basemap(self.iface,service_url, name)

	#########################		
	# LDD Map
	#########################
	def lddortho_call(self):
		service_url ="eis.ldd.go.th/ArcGIS/services/LDD_RASTER_WM_CACHE/MapServer/WMSServer" 
		name = "LDD Ortho"
		ml_ortho(self.iface,service_url, name)


	#########################		
	# GeoServer GISTNU
	#####################
	
	# GISTNU Province
	def prov_call(self):
		service_url ="www3.cgistln.nu.ac.th/geoserver/wms/"
		name = "ขอบเขตจังหวัด"
		ml_overlay_prov(self.iface,service_url, name)

	# GISTNU Tambon
	def tambon_call(self):
		service_url ="www3.cgistln.nu.ac.th/geoserver/wms/"
		name = "ขอบเขตตำบล"
		ml_overlay_tam(self.iface,service_url, name)

	# GISTNU Amphoe
	def amp_call(self):
		service_url ="www3.cgistln.nu.ac.th/geoserver/wms/"
		name = "ขอบเขตอำเภอ"
		ml_overlay_amp(self.iface,service_url, name)


	#########################		
	# Wikimedia Map
	#########################

	#Wikimedia Map
	def wikimap_call(self):
		service_url ="maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png"
		name = "Wikimedia Map"
		ml_basemap(self.iface,service_url, name)

	#Wikimedia Hike Bike Map
	def wikihbm_call(self):
		service_url ="tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png"
		name = "Wikimedia Hike Bike Map"
		ml_basemap(self.iface,service_url, name)


	#########################		
	# OpenWeatherMap
	#########################

	#OpenWeatherMap Temperature
	def owmtem_call(self):
		service_url ="tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png"
		name = "OpenWeatherMap Temperature"
		ml_basemapapi(self.iface,service_url, name)

	#OpenWeatherMap Clouds
	def owmcl_call(self):
		service_url ="tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png"
		name = "OpenWeatherMap Clouds"
		ml_basemapapi(self.iface,service_url, name)

	#OpenWeatherMap Wind Speed
	def owmws_call(self):
		service_url ="tile.openweathermap.org/map/wind_new/{z}/{x}/{y}.png"
		name = "OpenWeatherMap Wind Speed"
		ml_basemapapi(self.iface,service_url, name)


	#########################		
	# Bing Map
	#####################

	#Bing VirtualEarth
	def bingve_call(self):
		service_url ="ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg"
		name = "Bing VirtualEarth"
		ml_bingmap(self.iface,service_url, name)
	

	#########################		
	# Thunderforest Map
	#####################

	#Thunderforest Map OpenCycle
	def tfmocc_call(self):
		service_url ="b.tile.thunderforest.com/cycle/{z}/{x}/{y}.png"
		name = "Thunderforest Map OpenCycle"
		ml_tfmmap_b(self.iface,service_url, name)

	#Thunderforest Map Transport
	def tfmtst_call(self):
		service_url ="a.tile.thunderforest.com/transport/{z}/{x}/{y}.png"
		name = "Thunderforest Map Transport"
		ml_tfmmap_a(self.iface,service_url, name)

	#Thunderforest Map Landscape
	def tfmlsc_call(self):
		service_url ="a.tile.thunderforest.com/landscape/{z}/{x}/{y}.png"
		name = "Thunderforest Map Landscape"
		ml_tfmmap_a(self.iface,service_url, name)

	#Thunderforest Map Outdoors
	def tfmods_call(self):
		service_url ="a.tile.thunderforest.com/outdoors/{z}/{x}/{y}.png"
		name = "Thunderforest Map Transport"
		ml_tfmmap_a(self.iface,service_url, name)

	#Thunderforest Map Transport Dark
	def tfmtsd_call(self):
		service_url ="b.tile.thunderforest.com/transport-dark/{z}/{x}/{y}.png"
		name = "Thunderforest Transport Dark"
		ml_tfmmap_b(self.iface,service_url, name)

	#Thunderforest Map Spinal
	def tfmspn_call(self):
		service_url ="b.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png"
		name = "Thunderforest Spinal"
		ml_tfmmap_b(self.iface,service_url, name)

	#Thunderforest Map Pioneer
	def tfmpio_call(self):
		service_url ="a.tile.thunderforest.com/pioneer/{z}/{x}/{y}.png"
		name = "Thunderforest Pioneer"
		ml_tfmmap_a(self.iface,service_url, name)

	#Thunderforest Map Mobile Atlas
	def tfmmat_call(self):
		service_url ="a.tile.thunderforest.com/mobile-atlas/{z}/{x}/{y}.png"
		name = "Thunderforest Mobile Atlas"
		ml_tfmmap_a(self.iface,service_url, name)

	#Thunderforest Map Neighbourhood
	def tfmnbh_call(self):
		service_url ="b.tile.thunderforest.com/neighbourhood/{z}/{x}/{y}.png"
		name = "Thunderforest Neighbourhood"
		ml_tfmmap_b(self.iface,service_url, name)


	#########################		
	# GISTDA
	#####################

	#GISTDA Thaichote
	def gdbm_call(self):
		service_url ="go-tiles1.gistda.or.th/mapproxy/wmts/thaichote/GLOBAL_WEBMERCATOR/{z}/{x}/{y}.png"
		name = "GISTDA Thaichote"
		ml_basemap(self.iface,service_url, name)

	#GISTDA Planet Map Q1
	def gdpnq1_call(self):
		service_url ="tiles.planet.com/basemaps/v1/planet-tiles/thailand_2018q1_mosaic/gmap/{z}/{x}/{y}.png"
		name = "GISTDA Planet Map Q1"
		ml_gistdaq1(self.iface,service_url, name)
		
	#GISTDA Planet Map Q2
	def gdpnq2_call(self):
		service_url ="tiles.planet.com/basemaps/v1/planet-tiles/thailand_2018q2_mosaic/gmap/{z}/{x}/{y}.png"
		name = "GISTDA Planet Map Q2"
		ml_gistdaq2(self.iface,service_url, name)	

	#GISTDA Flood Map 2006
	def gdfld2006_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2006"
		ml_gistdaflood2006(self.iface,service_url, name)	

	#GISTDA Flood Map 2007
	def gdfld2007_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2007"
		ml_gistdaflood2007(self.iface,service_url, name)

	#GISTDA Flood Map 2008
	def gdfld2008_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2008"
		ml_gistdaflood2008(self.iface,service_url, name)

	#GISTDA Flood Map 2009
	def gdfld2009_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2009"
		ml_gistdaflood2009(self.iface,service_url, name)

	#GISTDA Flood Map 2010
	def gdfld2010_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2010"
		ml_gistdaflood2010(self.iface,service_url, name)

	#GISTDA Flood Map 2011
	def gdfld2011_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2011"
		ml_gistdaflood2011(self.iface,service_url, name)

	#GISTDA Flood Map 2012
	def gdfld2012_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2012"
		ml_gistdaflood2012(self.iface,service_url, name)

	#GISTDA Flood Map 2013
	def gdfld2013_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2013"
		ml_gistdaflood2013(self.iface,service_url, name)

	#GISTDA Flood Map 2014
	def gdfld2014_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2014"
		ml_gistdaflood2014(self.iface,service_url, name)

	#GISTDA Flood Map 2015
	def gdfld2015_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2015"
		ml_gistdaflood2015(self.iface,service_url, name)

	#GISTDA Flood Map 2016
	def gdfld2016_call(self):
		service_url ="ecoplant.gistda.or.th/rest/gis/wms/"
		name = "GISTDA Flood 2016"
		ml_gistdaflood2016(self.iface,service_url, name)