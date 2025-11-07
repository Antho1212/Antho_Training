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

configfile("C:\\Users\\goffi\\Documents\\Programmation\\python\\mini projet 3\\configfile")