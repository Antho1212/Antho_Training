import os

def configfile(pathfile:str):
    """Returns the dictionary of the parameters for each folder and the priority for them

    Parameters
    ----------
    pathfile : the path of the config file(str)

    Result
    ------
    dico : dictionary of the parameters for each folder(dict)
    prio : priority of the folders
    """
    fileconfig = open(pathfile, "r")
    dico={}
    prio=[]


    for line in fileconfig.readlines():
        if '---END---' in line:
            fileconfig.close()
            return prio,dico
        elif not line.startswith(" ") and not line.startswith("\n"):
            current_key=line
            str.strip(current_key)
            current_key=current_key[:-1]
            prio.append(current_key)
            dico[current_key]={}
            str.strip(line)
        if '=' in line:
            cond,value = line.split('=')
            str.strip(cond)
            str.strip(value)
            dico[current_key][cond] = value[:-1]

def object_in_dir(path):
    filedict = {'fichier' : [], 'dossier' : []}
    for fh in os.listdir(path):
        if os.path.isfile(fh):
            filedict['fichier'].append(fh)
        else:
            filedict['dossier'].append(fh)
    return filedict

def features (path):
    size = None
    if os.path.isfile(path):
         size = os.path.getsize(path)
         extentions = path.split('.')[1]
         return size, extentions
    
def trier (commentdir, pathfile):



    """
    This function is used to sort files in a directory

    Parameters:
    ----------
    commentdir: is the path of the directory to be sorted

    Note:
    -----
    The function will sort the files in the directory according to the configuration file
    """

    filedict = object_in_dir(commentdir)
    dico,listeexctetion,targetdir = configfile(pathfile)

    for fh in filedict['fichier']:
            size, extentions = features(fh)
            for prio in listeexctetion:
                extentionsverif = dico[prio]['extentions']
                try :
                    sizeverif = dico[prio]['size']
                except KeyError:
                    sizeverif = None
                try :
                    name_countain = dico[prio]['name_countain']
                except KeyError:
                    name_countain = None

                if size == None :
                    if name_countain == None and extentions == extentionsverif:
                        os.rename(commentdir + '/' + fh, targetdir + '/' + fh)
                    elif extentions == extentionsverif and name_countain in fh:
                        os.rename(commentdir + '/' + fh, targetdir + '/' + fh)
                elif name_countain == None and extentions == extentionsverif and size < sizeverif:
                    os.rename(commentdir + '/' + fh, targetdir + '/' + fh)
                elif extentions == extentionsverif and size < sizeverif and name_countain in fh:
                    os.rename(commentdir + '/' + fh, targetdir + '/' + fh)

    for dir in filedict['dossier']:
            path = commentdir + '/' + dir
            trier(path)

    if filedict['fichier'] == [] and filedict['dossier'] == []:
        os.rmdir(commentdir)


trier("C:\\Users\\goffi\\Documents\\Programmation\\python\\mini projet 3\\dossier a trié", "C:\\Users\\goffi\\Documents\\Programmation\\python\\mini projet 3\\config.txt")