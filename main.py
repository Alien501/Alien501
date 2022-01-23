#Importing needed modules

import os,shutil
from tinytag import TinyTag as tt

def mus_dir(ip_dir):        #Changing current directory to music directory given by user
    os.chdir(ip_dir)
    con = os.listdir()
    return con

def Lrc_create(al_name,old_loc):       #Function to create LRC foder
    files = os.listdir()
    file_new = Music_dir+'\\'+'lrc\\'+al_name
    if al_name not in lrc_added:
        try:
            os.makedirs(file_new)
            shutil.move(old_loc,file_new)
        except:
            shutil.move(old_loc,file_new)
    else:                                     #Handling Unexpected Errors
        try:
            shutil.move(old_loc,file_new)
        except FileNotFoundError:
            os.makedirs(file_new)
            shutil.move(old_loc,file_new)
    lrc_added.append(al_name)                 #Adding added lrc to folder for checking

def file_create(year,al,old_path):                 #Function to sort music files based on year of release
    new_path= Music_dir+'\\'+year+'\\'+al
    year_check = year in year_created
    fol_check = al in songf_created                 #Conditions to check existence
    print(new_path)
    if year_check:
        try:
            if fol_check:
                z = song_dict[al]
                new_path = Music_dir+'\\'+z+'\\'+al
                shutil.move(old_path,new_path)
            else:
                os.makedirs(new_path)
                shutil.move(old_path,new_path)
        except:
            print('Skipped...',old_path)
            return None
    else:
        try:
            os.makedirs(new_path)
            shutil.move(old_path,new_path)
        except:
            print('Skipped...',old_path)
            return None
    year_created.append(year)
    songf_created.append(al)
    if (al not in song_dict):
        song_dict[al] = year
    
Music_dir = input("Enter Your Music Directory: ")
a = mus_dir(Music_dir)
lrc_added = []
songf_created = []
year_created = []
song_dict = {}
for i in a:
    if '.ini' in i:
        continue
    elif '.lrc' in i:
        ol_path = Music_dir+'\\'+i
        file = open(ol_path,encoding='UTF-8')
        con = file.readlines()
        file.close()
        for i in con:
            if 'al:' in i:
                con = i.strip('[al:]')
                con = con[0:len(con)-2]
                new_f =''
                for nm in con:
                    if nm in '\/*?"<>:|':
                        continue
                    else:
                        new_f+=nm
        Lrc_create(new_f,ol_path)
    else:
        song_tag = tt.get(i)
        al_name = song_tag.album
        new_al = ''
        if al_name is None:
            continue
        for nm in al_name:
                    if nm in '\/*?"<>:|':
                        continue
                    else:
                        new_al+=nm
        al_year = song_tag.year
        if al_year == None:
            al_year = 'Unknown'
        old_path = Music_dir+'\\'+i
        file_create(al_year,new_al,i)

print("Successfully Sorted Music Folder....")