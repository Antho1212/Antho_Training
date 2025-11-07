import os

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
def trier ():
    commentdir = os.getcwd()
    filedict = object_in_dir(commentdir)
    dico = configfile()
    listeexctetion = dico['prioriter']
    for fh in filedict['fichier']:
        size, extentions = features(fh)
        for prio in listeexctetion:
            extentionsverif = dico[prio]['extentions']
            sizeverif = dico[prio]['size']
            name_countain = dico[prio]['name_countain']
            pathdestination = dico[prio]['path']
            if size == None :
                if name_countain == None and extentions == extentionsverif:
                    os.rename(commentdir + '/' + fh, pathdestination + '/' + fh)
                elif extentions == extentionsverif and name_countain in fh:
                    os.rename(commentdir + '/' + fh, pathdestination + '/' + fh)
            elif name_countain == None and extentions == extentionsverif and size < sizeverif:
                os.rename(commentdir + '/' + fh, pathdestination + '/' + fh)
            elif extentions == extentionsverif and size < sizeverif and name_countain in fh:
                os.rename(commentdir + '/' + fh, pathdestination + '/' + fh)