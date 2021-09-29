#!/usr/bin/python
# encoding=utf-8
import urllib2, json, datetime
import cgi, os
import glob
import cgi, os
import cgitb; cgitb.enable()
import shutil
import sys

#from os import listdir
#from os.path import isfile, join

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


www_path = "/var/www/html/"


tab_style = "style='float: left; padding: 10px'"
playlist_item_style = "style='float: left; padding: 5px'"

f = open(www_path + 'templates/header.html', 'r')
print f.read()
f.close()



video_directory = "/Videos"
playlist_directory="/opt/scarepi/Playlists/"
selected_directory = ""
delete_file = ""


print "</head>"
print "<body style='color: #dadadc; background-color: #2f3136; font-family: \"Helvetica Neue\",Helvetica,Arial,sans-serif;'>"
print "<img src='logo.png'style='width:400px'></img><br>"

print "<div " + tab_style + "><a href='index.cgi?tab=Files'>Files</a></div>"
print "<div " + tab_style + "><a href='index.cgi?tab=Upload'>File Upload</a></div>"
print "<div " + tab_style + "><a href='index.cgi?tab=Playlists'>Playlists</a></div>"
print "<div " + tab_style + "><a href='index.cgi?tab=Sound'>Sound</a></div>"
print "<div " + tab_style + "><a href='index.cgi?tab=Playback'>Playback</a></div>"
print "<div style='floating: none'></div>"

form = cgi.FieldStorage()

try:
    use_playlist = form["use_playlist"].value

    f = open("/opt/scarepi/Options/playlist", "w")
    f.write(use_playlist)
    f.close()
    print "<div style='margin-top: 55px'> </div>"
    print "Used Playlist saved"
except Exception, e:
    use_playlist = ""


try:
    playback_mode = form["playback_mode"].value
    f = open("/opt/scarepi/Options/playmode", "w")
    f.write(playback_mode)
    f.close()
    print "<br>"
    print "Playback Mode saved"
except Exception, e:
    playback_mode = ""

try:
    sound_output = form["sound_output"].value
    f = open("/opt/scarepi/Options/sound", "w")
    f.write(sound_output)
    f.close()
    print "<div style='margin-top: 55px'> </div>"
    print "Sound Output Device saved"
except Exception, e:
    sound_output = ""


try:
    html_tab = form["tab"].value
except Exception, e:
    html_tab = ""


try:
    trigger = form["trigger"].value
except Exception, e:
    trigger = ""


if (trigger != ""):
    print "<br><p><br><p>trigger sent"
    try:
        f = open("/opt/scarepi/Trigger/API-Trigger", "w")
        f.write("received")
        f.close()
    except Exception, e:
        print e
    sys.exit()



try:
    delete_playlist = form["delete_playlist"].value
except Exception, e:
    delete_playlist = ""

try:
    add_playlist = form["add_playlist"].value
except Exception, e:
    add_playlist = ""

try:
    delete_file = form["delete_file"].value
except Exception, e:
    delete_file = ""

try:
    add_file = form["add_file"].value
except Exception, e:
    add_file = ""

try:
    fileitem = form['upload_filename']
    upload_filename = form["upload_filename"].value
except Exception, e:
    upload_filename = "none"

try:
    selected_directory = form["dir"].value
except Exception, e:
    selected_directory = video_directory

try:
    selected_playlist = form["playlist"].value
except Exception, e:
    selected_playlist = "Default"

def list_dir(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def list_files(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isfile(os.path.join(a_dir, name))]

def count_files_int(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.islink(os.path.join(a_dir, name))]

def count_files(a_dir):
    files = count_files_int(a_dir)
    counter = 0
    for i in files:
        counter += 1
    return counter

#def list_files(a_dir):
#    files = glob.glob(a_dir + "/*")
#    files2 = [f for f in files if os.path.isfile]

def padd_file(src, dst):
    os.symlink(src, dst)


if (html_tab == "Files"):
    print "<div style='margin-top: 55px'> </div>"

    if (delete_file != ""):
        os.remove(selected_directory + "/" + delete_file)
        print "<div>File " + delete_file + " has been deleted </div>"
        print "<div style='margin-top: 55px'> </div>"


    print "<div "+ playlist_item_style + "> Files in Folder " + selected_directory + ": </div>" + "<div style='clear:both;'> </div>"


    if (str(selected_directory) != str(video_directory)):
        print "<div "+ playlist_item_style + "><i class='fas fa-folder-open'></i> <a href='index.cgi?tab="+html_tab+"&dir=" + os.path.dirname(selected_directory) + "' >..</a>""</div>" + "<div style='clear:both;'> </div>"


    dirs = list_dir(selected_directory)
    for i in dirs:
        print "<div " + playlist_item_style + "><i class='fas fa-folder-open'></i> <a href='index.cgi?tab="+html_tab+"&dir=" + selected_directory + "/" + i + "' >" + i + "</a></div>" + "<div style='clear:both;'> </div>"
        print "<div style='floating: none'></div>"

    files = list_files(selected_directory)
    for i in files:
        print "<div " + playlist_item_style + ">" + i + "</div>" + "<div><a href='index.cgi?tab="+html_tab+"&dir=" + selected_directory + "&delete_file=" + i + "'><img style='height:32px; width: 32px' src='delete.png'></img></a></div>" + "<div style='clear:both;'> </div>"
        print "<div style='floating: none'></div>"



if (html_tab == "Upload"):
    print "<div style='margin-top: 55px'> </div>"
    print "<div "+ playlist_item_style + ">Upload new Files: </div>" +  "<div style='clear:both;'> </div>"


    try:
        if fileitem.filename:
           # strip leading path from file name to avoid
           # directory traversal attacks
           fn = os.path.basename(fileitem.filename)
           open('/Videos/' + fn, 'wb').write(fileitem.file.read())
           message = 'The file "' + fn + '" was uploaded successfully'
           print message
    except Exception, e:
        pass


    print """    <form enctype = "multipart/form-data" action = "index.cgi?tab=Upload" method = "post">
   <p>File: <input type = "file" name = "upload_filename" /></p>
   <p><input type = "submit" value = "Upload" /></p>"""
    print "<br><p><br>"
    print "It is recommended to upload files via Samba/Windows File Sharing<br><p>"
    import socket
    print "Just use '\\\\"+str(socket.gethostbyname(socket.gethostname()))+"\ScarePi'<br>"
    print "Username: scarepi<br>"
    print "Password: scarepi"



if (html_tab == "Playlists"):
    if (add_playlist != ""):
        os.mkdir(playlist_directory + add_playlist)
        print "<div style='margin-top: 55px'> </div>"
        print "<div>Playlist " + add_playlist + " has been created </div>"
        print "<div style='margin-top: 55px'> </div>"
        selected_playlist = add_playlist

    if (delete_playlist != ""):
        print "<div style='margin-top: 55px'> </div>"

        if (selected_playlist == "Default"):
            files = list_files(playlist_directory + selected_playlist)
            for f in files:
                os.remove(playlist_directory + selected_playlist + "/" + f)
            print "<div>Playlist " + selected_playlist + " has been cleared </div>"
            print "<div style='margin-top: 55px'> </div>"
        else:
            shutil.rmtree(playlist_directory + selected_playlist)
            print "<div>Playlist " + selected_playlist + " has been deleted </div>"
            print "<div style='margin-top: 55px'> </div>"
            selected_playlist = "Default"

    if (add_file != ""):
        counter = count_files(playlist_directory + selected_playlist + "/") + 1
        padd_file(selected_directory + "/" + add_file, playlist_directory + selected_playlist + "/" + str(counter))

    print "<div style='margin-top: 55px'> </div>"
    print "<div "+ playlist_item_style + ">Playlists: </div>" +  "</div>"

    print "<div>"

    dirs = list_dir(playlist_directory)
    for i in dirs:
        print "<div style='float: left; padding: 5px'> <a href='index.cgi?tab="+html_tab+"&playlist=" + i + "' >" + i + "</a></div>"
        print "<div style='floating: none'></div>"
    print "</div>"

    print "<div style='clear:both;'> </div>"
    print "<br>"

    print "<form action='index.cgi'  method='get'>"
    print "  <input type='hidden' name='dir' value='" + selected_directory + "'>"
    print "  <input type='hidden' name='tab' value='" + html_tab + "'>"
    print "  <input type='text' name='add_playlist'>"
    print "<br>"
    print "  <button name='add' value='true'>add new playlist</button>"
    print "</form>"


    print "<div style='clear:both;'> </div>"
    print "<div style='margin-top: 55px'> </div>"


    print "<div style=''>"
    print "<div>Files in Playlist</div>"
    files = list_files(playlist_directory + selected_playlist)
    files.sort()
    for i in files:
        print "<div " + playlist_item_style + ">" + os.path.splitext(os.path.basename(i))[0] + " " + os.path.realpath(playlist_directory + selected_playlist + "/" + i) + "</div>" + "<div style='clear:both;'> </div>"
        print "<div style='floating: none'></div>"

    print "<form action='index.cgi?tab=" + html_tab + "&playlist=" + selected_playlist + "&dir=" + selected_directory + "'  method='get'>"
    print "  <input type='hidden' name='playlist' value='" + selected_playlist + "'>"
    print "  <input type='hidden' name='dir' value='" + selected_directory + "'>"
    print "  <input type='hidden' name='tab' value='" + html_tab + "'>"

    print "  <button name='delete_playlist' value='true'>delete this playlist</button>"
    print "</form>"

    print "</div>"


    print "<div style='margin-top: 55px'> </div>"

    print "<div style=''>"
    print "<div>Files in Filesystem</div>"


    if (str(selected_directory) != str(video_directory)):
        print "<div "+ playlist_item_style + "><i class='fas fa-folder-open'></i> <a href='index.cgi?tab="+html_tab+"&playlist=" + selected_playlist + "&dir=" + os.path.dirname(selected_directory) + "' >..</a>""</div>" + "<div style='clear:both;'> </div>"


    dirs = list_dir(selected_directory)
    for i in dirs:
        print "<div " + playlist_item_style + "><i class='fas fa-folder-open'></i>  <a href='index.cgi?tab="+html_tab+"&playlist=" + selected_playlist + "&dir=" + selected_directory + "/" + i + "' >" + i + "</a></div>" + "<div style='clear:both;'> </div>"
        print "<div style='floating: none'></div>"

    files = list_files(selected_directory)

    for i in files:
        print "<div " + playlist_item_style + ">" + i + "</div>" + "<div><a href='index.cgi?tab="+html_tab+"&dir=" + selected_directory + "&playlist=" + selected_playlist + "&add_file=" + i + "'><img style='height:32px; width: 32px' src='add.svg'></img></a></div>" + "<div style='clear:both;'> </div>"
        print "<div style='floating: none'></div>"



    print "</div>"


if (html_tab == "Sound"):
    print "<div style='margin-top: 55px'> </div>"
    print """
<form action=''>
  <label>Sound Output:
    <select name='sound_output' size='1'>"""
    f = open("/opt/scarepi/Options/sound", "r")
    sel_playmode = f.read()
    if ("HDMI" == str(sel_playmode).strip()):
        print "<option selected>HDMI</option>"
    else:
        print "<option>HDMI</option>"

    if ("Jack" == str(sel_playmode).strip()):
        print "<option value='jack 'selected>3,5mm Jack</option>"
    else:
        print "<option value='Jack'>3,5mm Jack</option>"

    if ("Bluetooth" == str(sel_playmode).strip()):
        print "<option selected>Bluetooth</option>"
    else:
        print "<option disabled>Bluetooth</option>"
    print """
    </select>
  </label>
<br><p>
<input type="submit" value="Speichern">
</form>"""

if (html_tab == "Playback"):
    print "<div style='margin-top: 55px'> </div>"
    print """
<form action=''>
  <label>Playback Mode:
    <select name='playback_mode' size='1'>"""
    f = open("/opt/scarepi/Options/playmode", "r")
    sel_playmode = f.read()
    if ("Loop" == str(sel_playmode).strip()):
        print "<option selected>Loop</option>"
    else:
        print "<option>Loop</option>"

    if ("GPIO-Trigger" == str(sel_playmode).strip()):
        print "<option selected>GPIO-Trigger</option>"
    else:
        print "<option>GPIO-Trigger</option>"

    if ("API-Trigger" == str(sel_playmode).strip()):
        print "<option selected>API-Trigger</option>"
    else:
        print "<option>API-Trigger</option>"
    print """
    </select>
  </label>
  <br>
  <label>Selected Playlist:
    <select name='use_playlist' size='1'>"""
    f = open("/opt/scarepi/Options/playlist", "r")
    sel_playlist = f.read()
    dirs = list_dir(playlist_directory)
    for i in dirs:
        if (str(i).strip() == str(sel_playlist).strip()):
            print "<option selected>" + i + "</option>"
        else:
            print "<option>" + i + "</option>"

    print """    </select>
  </label>
<br><p>
<input type="submit" value="Speichern">
</form>"""
