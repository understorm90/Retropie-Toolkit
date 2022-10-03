# GAMELIST_MAKER
#
# Crea un file di gamelist.xml a partire dalla lista dei giochi nella cartella corrente.
# Inoltre legge i metadati da una cartella 'desc'
#
# Per avviarlo posizionarsi nella cartella roms desiderata,
# e nella barra degli indirizzi digitare "cmd" per far comparire
# il prompt dei comandi. Digitare "python " e trascinare questo file.
#
# Oltre a leggere le desc, se è presente un file xml, imposta anche il sortname e il releasedate
#

import glob, os
import xml.etree.ElementTree as ET

f = open("gamelist-BETAv3.xml","w+")
f.write("<?xml version=\"1.0\"?>\n")
f.write("<gameList>\n")

#os.chdir("/mydir")
extensions = ["*.chd", "*.m3u"]

for ext in extensions:
	print("1 ** " + str(len(extensions)) + " -------------> " + ext)
	for file in glob.glob(ext):
		filename = os.path.splitext(file)[0]
		print(filename)
		f.write("\t<game id=\"\" source=\"SimoScraper\">\n")
		
		f.write("\t\t<path>./" + file + "</path>\n")

		game_name = filename.split('(')[0].rstrip()
		for s in filename.split('(')[1:]:
			if 'Japan)' in s:
				game_name  = game_name + ' (Japan)'
				print("---> " + s)
			if ',It' in s:
				game_name  = game_name + ' (ITA)'
				print("---> " + s)
			if 'Italy)' in s:
				game_name  = game_name + ' (ITA)'
				print("---> " + s)
			if 'Disc ' in s:
				game_name  = game_name + ' (' + s
				print("---> " + s)
			if 'Patch' in s:
				game_name  = game_name + ' (' + s
				print("---> " + s)
			if 'Translated ' in s:
				game_name  = game_name + ' (' + s
				print("---> " + s)
			if 'Proto)' in s:
				game_name  = game_name + ' (' + s
				print("---> " + s)
			if 'Hack)' in s:
				game_name  = game_name + ' (' + s
				print("---> " + s)
			if 'Homebrew)' in s:
				game_name  = game_name + ' (' + s
				print("---> " + s)

		f.write("\t\t<name>" + game_name  + "</name>\n")

		game_sortname = ""
		game_desc = ""
		game_releasedate = ""
		game_developer = ""
		game_publisher = ""
		game_genre = ""
		game_players = ""
		
		file_path_txt = "desc/" + filename + ".txt"
		if os.path.exists(file_path_txt):
			descfile = open(file_path_txt, "r")
			game_desc = descfile.read()
			descfile.close()

		file_path_xml = "desc/" + filename + ".xml"
		if os.path.exists(file_path_xml):
			root = ET.parse(file_path_xml).getroot()
			for child in root:
				if (child.tag == 'sortname'):
					game_sortname = child.text.strip()
				if (child.tag == 'desc'):
					game_desc = child.text.strip()
				if (child.tag == 'releasedate'):
					game_releasedate = child.text.strip()
				if (child.tag == 'developer'):
					game_developer = child.text.strip()
				if (child.tag == 'publisher'):
					game_publisher = child.text.strip()
				if (child.tag == 'genre'):
					game_genre = child.text.strip()
				if (child.tag == 'players'):
					game_players = child.text.strip()

		if (game_sortname != ""):
			f.write("\t\t<sortname>" + game_sortname + "</sortname>\n")
		f.write("\t\t<desc>" + game_desc + "</desc>\n")
		f.write("\t\t<image>./boxart/" + filename + ".png</image>\n")
		f.write("\t\t<marquee>./wheel/" + filename + ".png</marquee>\n")
		f.write("\t\t<video>./snap/" + filename + ".mp4</video>\n")
		f.write("\t\t<thumbnail></thumbnail>\n")
		f.write("\t\t<rating></rating>\n")
		if (game_releasedate != ""):
			f.write("\t\t<releasedate>" + game_releasedate + "</releasedate>\n")
		f.write("\t\t<developer>" + game_developer + "</developer>\n")
		f.write("\t\t<publisher>" + game_publisher + "</publisher>\n")
		f.write("\t\t<genre>" + game_genre + "</genre>\n")
		f.write("\t\t<players>" + game_players + "</players>\n")
		f.write("\t</game>\n")
f.write("</gameList>\n")
f.close()

