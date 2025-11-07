import os
def configfile(pathfile : str):
   """Returns the dictionary of the parameters for each folder and the priority for them

   Parameters
   ----------
   pathfile : the path of the config file(str)

   Result
   ------
   prio : priority of the folders(list)
   dico : dictionary of the parameters for each folder(dict)
   """
   fileconfig = open(pathfile, "r")            #open the config file in mode read
   
   dico={}        #dictionnary for config's parameters
   prio=[]        #list to keep the priority of the folders


   for line in fileconfig.readlines():     #reads lines in file
       if '---END---' in line:             #check if it's the end of the configfile
           fileconfig.close()
           return (prio,dico)
       elif not line.startswith(" ") and not line.startswith("\n"):    #check if the line start with a character 
           line=line.strip()               #clean the line
           current_key=line                #keep the name of the folders 
           current_key=current_key    #deletes the \n
           prio.append(current_key)   #add current key in prio
           dico[current_key]={}
       if '=' in line:                     #check if it's a folder's parameter
           line=line.strip()
           cond,value = line.split('=')           #split the line in a key and a value
           if ',' in value:                #create a list if there is several value in one parameter
               new_value=[]
               new_value=value.split(',')
               value=new_value

           dico[current_key][cond] = value


def object_in_dir(path):
    """return the folders and file in a directory

    Parameters
    ----------
    path: the path of the directory

    Returns
    -------
    filedict(dict): dictionary of the folders and file in the directory 
    """
    filedict = {'file' : [], 'folder' : []} #initilize filedict as a dictionary with 2 list file and folder
    for fh in os.listdir(path):  #list the current directory  
        
        if os.path.isfile(path +'\\'+ fh): # check the path, if it's a file add them to the dictionary in the file list
            filedict['file'].append(fh)
        elif os.path.isdir(path +'\\'+ fh): #if the path is a folders add them to the dictionary in the folder list
            filedict['folder'].append(fh)
    return filedict

def features (path):
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
    if os.path.isfile(path): #check if the path is a file
         size = os.path.getsize(path) #get the size of the file
         extentions = path.split('.')[1] #get the extentions of the file
         return size, extentions
    
def sort(commentdir):
   """
   This function is used to sort all files in a directory

   Parameters:
   ----------
   commentdir: is the path of the directory to be sorted

   Note:
   -----
   The function will sort the files in the directory according to the configuration file
   the function use recursion to treat the subfolders
   """

   filedict = object_in_dir(commentdir) #call the function object_in_dir for get the file and folder in commentdir
   listeexctetion,dico= configfile('A:\infob_1\intro_prog\mp3\config.txt') #get parameters of the config file

   for fh in filedict['file']: #realise all the instruction for every file in file dict
           size, extentions = features(commentdir +'\\'+fh) #call the features function for get the size and the extension
           for prio in listeexctetion:
               targetdir = prio
               extentionsverif = dico[prio]['extension'] #check the extension
               try :
                   min_sizeverif = dico[prio]['min_size'] #check if they are a minimum size
                   min_sizeverif = int(min_sizeverif) #chane it into a integer
               except KeyError: #if not set none
                   min_sizeverif = None
               try :
                   max_sizeverif = dico[prio]['max_size'] #check if they are a maximum size
                   max_sizeverif = int(max_sizeverif) #change it into an integer     
               except KeyError: #if not set none
                   max_sizeverif = None
               try :
                   name_contains = dico[prio]['name_contains'] #check the name
               except KeyError: #if not set none
                   name_contains = None
                   if name_contains == None or name_contains in fh:
                       valid_size = valid_size =  valid_size = min_sizeverif <= size <= max_sizeverif
                       for name in name_contains: #verify if the name is the name attend, the extention is good and if the size is good to
                        if valid_size and extentions == extentionsverif:
                            if not os.path.isdir(targetdir):
                                os.mkdir(targetdir) #create a folder if he not already exist
                            os.rename(commentdir + '\\' + fh, targetdir + '\\' + fh) #move the file in the target folder
                   else: #same conditions but this time we don't check the name
                       if valid_size and extentions == extentionsverif:
                            if not os.path.isdir(targetdir):
                                os.mkdir(targetdir) ##create a folder if he not already exist
                            os.rename(commentdir ) #move the file in the target folder
                       
               
               

   for dir in filedict['folder']: #call the function sort for every folder in filedict
           subdir_path = os.path.join(commentdir, dir) #create the path of the folders for use the sort function
           sort(subdir_path) #call the function

   if not os.listdir(commentdir): #list the directory to sort
       os.rmdir(commentdir) #if he is empty remove it

sort("E:\MiniProjet_3")