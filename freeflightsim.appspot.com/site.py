# -*- coding: utf-8 -*-

"""
### Site Configuration ###

Copy the file 
site.skel.py 
to 
site.py

Then modify the vars below


"""
site = {

	'app_id': 'freeflightsim', 

	# admin email. Note this MUST be one of the developer accounts
	'email.admin':  'dev@freeflightsim.org',

	# general incoming email
	'email.inbox':  'dev@freeflightsim.org',

	# Name of the site
	'name':         'FreeFlightSim.org',

	# title at the top
	'title':        "FreeFlightSim with FlightGear - Fly like a pro with open source",


	#'tm':         = "<span class='tm'>Crosshands</span>" #&#0174;
	

	# Set this variable if using a CDN for the javascript lids and css
	# ie the ext libs, reset css etc (standard stuff)
	##'CDN':          '',
	'CDN':          'http://ffs-cache.appspot.com',

	## Default maps vars.. soon in Database
	'DEFAULT_LAT':  '51.796812149158164',
	'DEFAULT_LNG':  '-4.083539843559265',

	'CENTER_LAT':   '51.793826178175635',
	'CENTER_LNG':   '-4.080600142478943',

	'nani': 'FOO',
	'nav': [
		{'path': '/', 'text': 'Home'},
		{'path': '/features', 'text': 'Features'},
		{'path': '/screenshots', 'text': 'Screen Shots'},
		{'path': '/faq', 'text': 'Faq'},
		{'path': '/terrain', 'text': 'Terrain'},
		{'path': '/aircraft', 'text': 'Aircraft'},
		{'path': '/about', 'text': 'About'},
	] 

}