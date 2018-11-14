# -*- coding: utf-8 -*-
# --------------------------------------------------------
#    __init__ - MapLink init file
#
#    begin                : 11/11/2018
#    copyright            : 2018 by boonstation
#    email                : ps.gistnu@gmail.com
#    modified script from HCMGIS quachdongthang@gmai.com
# --------------------------------------------------------
def classFactory(iface):
	from .ml_menu import ml_menu
	return ml_menu(iface)

