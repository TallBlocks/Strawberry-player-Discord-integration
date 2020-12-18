###################################################################################################
"""
    Imports
"""
from mpris2 import Player
from dbusdecorator import DbusAttr, DbusInterface, DbusMethod
###################################################################################################
"""
    Functions
"""
def getInfo():
    player = Player(dbus_interface_info={'dbus_uri': 'org.mpris.MediaPlayer2.strawberry'}) # This will tell mpris2 module wich music player it have to take the info from.

    """
        I haven't found an easier way to split the strings it returns from dbus call. As it doesnt work with arguments as i spected i had to use .rsplit() to be able to split the info.

        x and y variables are just 2 variables to help me to split the words.
    """

    x = 0
    y = 0

    Metadata = str(player.Metadata) # It gets the metadata from dbus, its like typing qdbus org.mpris.MediaPlayer2.strawberry /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Metadata in the terminal.

    #print(Metadata) if you want to see how it shows the metadata and why i couldn't do it in any other way.
    
    if Metadata != str('{}'): # When no song is playing it returns {} so if Metadata isnt "{}" it means that any song is playing.
        
        splited_metadata = Metadata.rsplit(", ") # It splits the metadata.

        for line in splited_metadata:
            x = x+1
            if x == 9:
                y = 0
                album_metadata = line
                album_metadata2 = album_metadata.rsplit("'")
                for line in album_metadata2:
                    y = y+1
                    if y == 4:
                        global album
                        album = line
            if x == 14:
                y = 0
                artist_metadata = line
                artist_metadata2 = artist_metadata.rsplit("'")
                for line in artist_metadata2:
                    y = y+1
                    if y == 4:
                        global artist
                        artist = line
            h = line.find("xesam:title")
            if h != -1:
            

                uwu = line.split(":")
                XD = uwu[2]
                AAAA = XD.split("(")

                jej = AAAA[1]
                
                global title
                title = jej[1:-1]

    else: #If no song is playing we have to return it.
        title = 0
        album = 0
        artist = 0