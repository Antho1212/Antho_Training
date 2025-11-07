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

    config = {}     # dictionnary for config's parameters
    prio = []       # list to keep the priority of the folders

    for line in fileconfig.readlines():     # reads lines in file
        if '---END---' in line:             # check if it's the end of the configfile
            fileconfig.close()
            return (prio, config)

        elif not line.startswith(" ") and not line.startswith("\n"):               # check if the line start with a character
            line = line.strip()                 # clean the line
            current_key = line                  # keep the name of the folders
            current_key = current_key           # deletes the \n
            prio.append(current_key)
            config[current_key] = {}
        if '=' in line:                         # check if it's a folder's parameter
            line = line.strip()
            cond, value = line.split('=')       # split the line in a key and a value
            if ',' in value:                    # create a list if there is several value in one parameter
                new_value = []
                new_value = value.split(',')
                value = new_value

            config[current_key][cond] = value


def object_in_dir(path):
    """return the folders and file in a directory

    Parameters
    ----------
    path: the path of the directory

    Returns
    -------
    filedict(dict): dictionary of the folders and file in the directory 
    """
    filedict = {'fichier': [], 'dossier': []}       #initilize filedict as a dictionary with 2 list file and folder
    for fh in os.listdir(path):                     #list the current directory  

        if os.path.isfile(path + '\\' + fh):        # check the path, if it's a file add them to the dictionary in the file list
            filedict['fichier'].append(fh)
        elif os.path.isdir(path + '\\' + fh):       #if the path is a folders add them to the dictionary in the folder list
            filedict['dossier'].append(fh)
    return filedict


def features(path):
    """check the path and look if its a file
    if it's a file return the size and the extention of a file
    parameters
    ----------
    path: the path to check

    return
    ------
    size: the size of the file(int)
    extention: the extention of the file(str)
    """
    size = None
    if os.path.isfile(path):
        size = os.path.getsize(path)
        extentions = path.split('.')[1]
        return size, extentions


def sort(commentdir: str, pathconfig: str):
    """
    This function is used to sort all files in a directory

    Parameters:
    ----------
    commentdir: is the path of the directory to be sorted

    Note:
    -----
    The function will sort the files in the directory according to the configuration file
    The function use recursion to treat the subfolders
    """

    filedict = object_in_dir(commentdir)        #call the function object_in_dir for get the file and folder in commentdir
    listdir, config = configfile(pathconfig)    #get parameters of the config file

    for fh in filedict['fichier']:              #realise all the instruction for every file in file dict
        moved = False                           #creation of a flag for avoid to change two times one file
        size, file_ext = features(commentdir + '\\'+fh)         #call the features function for get the size and the extension
        for targetdir in listdir:
            if not moved:                                       
                if not os.path.isdir(targetdir):                #test all the parameters of config file for when they dont are in the dictionnary
                    os.mkdir(targetdir)
                    print(targetdir + ' has been created')
                if 'extension' not in config[targetdir]:        
                    config[targetdir]['extension'] = ""
                if 'min_size' not in config[targetdir]:
                    config[targetdir]['min_size'] = "0"
                if 'name_contains' not in config[targetdir]:
                    config[targetdir]['name_contains'] = ""
                if 'max_size' not in config[targetdir]:
                    config[targetdir]['max_size'] = "0"

                extensionverif = config[targetdir]['extension']         #take all parameters to verify
                
                min_sizeverif = config[targetdir]['min_size']
                min_sizeverif = int(min_sizeverif)

                max_sizeverif = config[targetdir]['max_size']
                max_sizeverif = int(max_sizeverif)

                name_verif = config[targetdir]['name_contains']
                
                if (size <= max_sizeverif) or (max_sizeverif == 0):    #compare parameters of the file with parameters of the config file
                    if (size >= min_sizeverif):
                        if (file_ext in extensionverif) or (extensionverif == ""):
                            if isinstance(name_verif,str):
                                if name_verif in fh:
                                    os.rename(commentdir + '\\' + fh,targetdir + '\\' + fh)     #move the file in the target directory
                                    print (commentdir + '\\' + fh +' moved to '+ targetdir + '\\' + fh)
                                    moved=True
                            else:
                                for name in name_verif:
                                    if (name in fh) and (moved==False):
                                        os.rename(commentdir + '\\' + fh,targetdir + '\\' + fh) #move the file in the target directory
                                        print (commentdir + '\\' + fh +' moved to '+ targetdir + '\\' + fh)
                                        moved=True


    for dir in filedict['dossier']:
        path = commentdir + '\\' + dir
        sort(path,pathconfig)           #recusive fonction if there is folders in the main folder to sort
        os.rmdir(path)                  #remove under directory when they have no more file
        print(path + ' has been removed')

sort("E:\MiniProjet_3", 'A:\infob_1\intro_prog\mp3\config.txt')