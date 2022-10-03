# move_only_roms_from_list
#
# Sposta i giochi in una nuova sottocartella a partire dai nomi dei giochi contenuti in un file 'games.txt'
#
# Per avviarlo posizionarsi nella cartella roms desiderata,
# e nella barra degli indirizzi digitare "cmd" per far comparire
# il prompt dei comandi. Digitare "python " e trascinare questo file.
#
import os
import shutil

# da modificare a seconda dell'estensione dei file
rom_ext = ".chd"
file_path = "games" + ".txt"
fav_dir = os.getcwd().split(os.sep)[-1] + "-moved-v3"

def copy_file(dir_name, ext):
	try:
		os.makedirs("./" + fav_dir + "/" + dir_name)
	except OSError:
		pass
	f = open(file_path, "r")
	for line in f:
		file_to_copy = dir_name + "/" + line.strip() + ext
		if os.path.exists(file_to_copy):
			shutil.copy2(file_to_copy, fav_dir + "/" + dir_name)
		else:
			print("- missing: " + file_to_copy)
	f.close()
	
try:
    os.makedirs("./" + fav_dir)
except OSError:
    pass

def exportMissingGamesList(gamesList):
	with open("missinggames.txt", "w") as fw:
		for game in gamesList:
			fw.write(game + "\n")

# COPIA LE ROMS
print("Moving roms..")
f = open(file_path, "r")
missingGames = []
for line in f:
	file_to_copy = line.strip() + rom_ext
	file_to_copy_cd1 = line.strip() + " (Disc 1).CD1"
	file_to_copy_cd2 = line.strip() + " (Disc 2).CD2"
	file_to_copy_cd3 = line.strip() + " (Disc 3).CD3"
	file_to_copy_cd4 = line.strip() + " (Disc 4).CD4"
	file_to_copy_cd5 = line.strip() + " (Disc 5).CD5"
	file_to_copy_m3u = line.strip() + ".m3u"
	if os.path.exists(file_to_copy):
		shutil.move(file_to_copy, fav_dir)
	elif os.path.exists(file_to_copy_cd1):
		shutil.move(file_to_copy_cd1, fav_dir)
	elif os.path.exists(file_to_copy_cd2):
		shutil.move(file_to_copy_cd2, fav_dir)
	elif os.path.exists(file_to_copy_cd3):
		shutil.move(file_to_copy_cd3, fav_dir)
	elif os.path.exists(file_to_copy_cd4):
		shutil.move(file_to_copy_cd4, fav_dir)
	elif os.path.exists(file_to_copy_cd5):
		shutil.move(file_to_copy_cd5, fav_dir)
	elif os.path.exists(file_to_copy_m3u):
		shutil.move(file_to_copy_m3u, fav_dir)
	else:
		missingGames.append(file_to_copy)
		print(file_to_copy)
f.close()

exportMissingGamesList(sorted(missingGames))

print("End.")