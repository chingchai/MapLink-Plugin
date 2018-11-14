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
		github				 : 
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
		
		# OpenData_basemap submenu
		#icon_path = self._menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/.....png"))
		self.google_menu = QMenu(u'Google')		
		self.ml_add_submenu(self.google_menu)
		self.google_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_googlemaps.png"))

		self.carto_menu = QMenu(u'Carto')		
		self.ml_add_submenu(self.carto_menu)
		self.carto_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_carto_l.jpg"))

		self.esri_menu = QMenu(u'ESRI')		
		self.ml_add_submenu(self.esri_menu)
		self.esri_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_esri.png"))

		self.stamen_menu = QMenu(u'Stamen')		
		self.ml_add_submenu(self.stamen_menu)
		self.stamen_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_stamen.png"))

		self.osm_menu = QMenu(u'OpenStreetMap')		
		self.ml_add_submenu(self.osm_menu)
		self.osm_menu.setIcon(QIcon(os.path.dirname(__file__) + "/icons/ml_osm.png"))


		##https://mc.bbbike.org/mc/?num=2&mt0=mapnik&mt1=watercolor
		#https://gitlab.com/GIS-projects/Belgium-XYZ-tiles/tree/b538df2c2de0d16937641742f25e4709ca94e42e
		


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
		# ESRI https://gitlab.com/GIS-projects/Belgium-XYZ-tiles/tree/b538df2c2de0d16937641742f25e4709ca94e42e
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


	def unload(self):
		if self.ml_menu != None:
			self.iface.mainWindow().menuBar().removeAction(self.ml_menu.menuAction())
		else:
			self.iface.removePluginMenu("&maplink", self.basemap_menu.menuAction())


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
		service_url = "c.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg" 
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
		service_url ="mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z}" 
		name = "Google Terrain"
		ml_basemap(self.iface,service_url, name)

	def googleterrainhybrid_call(self):
		service_url ="mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}"
		name = "Google Terrain Hybrid"
		ml_basemap(self.iface,service_url, name)


	#########################		
	# Openstreetmap
	#####################

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