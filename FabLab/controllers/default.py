# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
#!/usr/bin/python

#~ ========================== IMPORT  =================================
import datetime, time
import pprint
import re
import sys
import struct

def index():
	if not session.counter:
		session.counter = 1
	else:
		session.counter += 1
	return dict(message="Bienvenu sur l\' Application Novar et Precidot",counter=session.counter);

def first():

    # Questionnaire pour récupérer le nom du fichier à ouvrir 
	form=FORM('Your file:', INPUT(_name='fichier_name', _type='file'), INPUT(_type='submit'))

    # Si on récupère l'information alors : 
	if form.process().accepted:
		#session.fichier_name = form.vars.fichier_name
		response.flash = T('Thanks! The form has been submitted.')
		#Appel de la fonction pour rechercher les composants
		composant_recherche(request.vars.fichier_name)  
	# Si on récupère pas alors Erreur :
	elif form.errors:
		response.flash = T('Please correct the error(s).')
		
	if form.vars.composant is None:
		composant=[]
	else:
		composant=form.vars.composant
		
	return dict(form=form,composant=composant,vars=request.vars)

def composant_recherche(fichier_name) :                    
	#from validators import IS_IN_SET SELECT('yes', 'no', _name='composant', value=fichier_name.value, requires=IS_IN_SET([fichier_name.value])).xml()
	# ouverture du fichier que l'on récupère avec le bouton parcourir
	# On l'appellera fichier_name
	# on lit le fichier afin de trouver les composant qui se situ à la colonne [0]
	
	print("Début programme")
   
   # form=FORM('Your Choose:', SELECT(line,_name='fichier_name',requires=IS_IN_SET([value, 'no'])).xml()
    
	try:
		fichier = open(fichier_name, "r")
		for line in fichier:
			lines = line.strip() 

		p = re.compile('^-composant-(.+)-package-(.+)-X-(.+)-Y-(.*)-rot-(.*)$')

		if "-composant-" in line:
			m = p.match(line)
		if m:
			composant = m.group(1)
		print(composant)
	except IOError:
		print ("Erreur lors de l'ouverture du fichier !")
	except ValueError:
		print ("Erreur lors de la conversion !")

	fichier.close()
	return dict(form=FORM,vars=composant.vars)

def second():
    return dict()
