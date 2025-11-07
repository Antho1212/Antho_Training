import os


def configfile(pathfile: str):
    """Returns the dictionary of the parameters for each folder and the priority for them

    Parameters
    ----------
    pathfile : the path of the config file(str)

    Result
    ------
    prio : priority of the folders(list)
    config : dictionary of the parameters for each folder(dict)
    """
    fileconfig = open(pathfile, "r")  # open the config file in mode read

    config = {}  # dictionnary for config's parameters
    prio = []  # list to keep the priority of the folders

    for line in fileconfig.readlines():  # reads lines in file
        if '---END---' in line:  # check if it's the end of the configfile
            fileconfig.close()
            return (prio, config)
        # check if the line start with a character
        elif not line.startswith(" ") and not line.startswith("\n"):
            line = line.strip()  # clean the line
            current_key = line  # keep the name of the folders
            current_key = current_key  # deletes the \n
            prio.append(current_key)
            config[current_key] = {}
        if '=' in line:  # check if it's a folder's parameter
            line = line.strip()
            # split the line in a key and a value
            cond, value = line.split('=')
            if ',' in value:  # create a list if there is several value in one parameter
                new_value = []
                new_value = value.split(',')
                value = new_value

            config[current_key][cond] = value


def object_in_dir(path):
    filedict = {'fichier': [], 'dossier': []}
    for fh in os.listdir(path):

        if os.path.isfile(path + '\\' + fh):
            filedict['fichier'].append(fh)
        elif os.path.isdir(path + '\\' + fh):
            filedict['dossier'].append(fh)
    return filedict


def features(path):
    size = None
    if os.path.isfile(path):
        size = os.path.getsize(path)
        extentions = path.split('.')[1]
        return size, extentions


def trier(commentdir: str, pathconfig: str):
    """
    This function is used to sort all files in a directory

    Parameters:
    ----------
    commentdir: is the path of the directory to be sorted

    Note:
    -----
    The function will sort the files in the directory according to the configuration file
    """

    filedict = object_in_dir(commentdir)
    listdir, config = configfile(pathconfig)

    for fh in filedict['fichier']:
        moved = False
        size, file_ext = features(commentdir + '\\'+fh)
        for targetdir in listdir:
            if not moved:
                if not os.path.isdir(targetdir):
                    os.mkdir(targetdir)
                if 'extension' not in config[targetdir]:
                    config[targetdir]['extension'] = ""
                if 'min_size' not in config[targetdir]:
                    config[targetdir]['min_size'] = "0"
                if 'name_contains' not in config[targetdir]:
                    config[targetdir]['name_contains'] = ""
                if 'max_size' not in config[targetdir]:
                    config[targetdir]['max_size'] = "0"

                extensionverif = config[targetdir]['extension']
                
                min_sizeverif = config[targetdir]['min_size']
                min_sizeverif = int(min_sizeverif)

                max_sizeverif = config[targetdir]['max_size']
                max_sizeverif = int(max_sizeverif)

                name_verif = config[targetdir]['name_contains']
                
                if (size <= max_sizeverif) or (max_sizeverif == 0):
                    if (size >= min_sizeverif):
                        if (file_ext in extensionverif) or (extensionverif == ""):
                            if isinstance(name_verif,str):
                                if name_verif in fh:
                                    os.rename(commentdir + '\\' + fh,targetdir + '\\' + fh)
                                    moved=True
                            else:
                                for name in name_verif:
                                    if (name in fh) and (moved==False):
                                        os.rename(commentdir + '\\' + fh,targetdir + '\\' + fh)
                                        moved=True


    for dir in filedict['dossier']:
        path = commentdir + '\\' + dir
        trier(path,pathconfig)
        os.rmdir(path)

trier("E:\MiniProjet_3", 'A:\infob_1\intro_prog\mp3\config.txt')