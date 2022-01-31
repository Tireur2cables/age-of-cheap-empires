# # instantiationManager
# from os import getcwd
# from pathlib import Path
# import objects.Entity
# # UTILISER PICKLE POUR LES SAUVEGARDES !!!
# # https://stackoverflow.com/questions/2047814/is-it-possible-to-store-python-class-objects-in-sqlite
# # Utiliser sqlite, pickle, ou bien les 2 ensembles, ou séparément, et pourquoi ?
# import sqlite3
# def createWorldDB(inputName):
# 	inputName += ".db"
# 	worldName = getcwd() + str(Path('/worldConcept/', inputName))

# 	currentDB = None
# 	try:
# 		conn = sqlite3.connect(worldName)
# 		print("DB Version : ", sqlite3.version)
# 	except sqlite3.Error as e:
# 		print(e)
# 	finally:
# 		if conn:
# 			conn.close()


# #createWorldDB()
# #createWorldDB("test")



###############################################
import pickle, json
def pickleSaving(save_name, save_list):
	save_file=save_name+'.pkl'
	data = save_list
	print(f"[Saving]: {type(data)}")
	with open(save_file,'wb') as fileDescriptor:
		pickle.dump(data, fileDescriptor)
		# for i in data:
		# 	for i_i in i:
		# 		print(i_i)
		# 		pickle.dump(i_i, fileDescriptor)
	print(f"[Saving]: Done!")
	pickleLoading(save_name) # A SUPPRIME !!! C'est juste pour teste le loading

def pickleLoading(save_name):
	save_file=save_name+'.pkl'
	print(f"[Loading]: Loading...")
	with open(save_file,'rb') as fileDescriptor:
		test = pickle.load(fileDescriptor)
		print(f"[Loaded]: Loaded {test}")
	print(f"[Loading]: Done!")