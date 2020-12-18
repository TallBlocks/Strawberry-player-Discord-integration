###################################################################################################
"""
    Imports
"""
import pyfiglet

from pypresence import Presence # This module will allow us to connect to the Discord's RPC.

from __getInfo__ import getInfo # This will import the getInfo() function from __getInfo__.py
###################################################################################################
"""
    Declaration
"""
token = 'yourToken'

rpc = Presence(token)

connectionClose = 1
###################################################################################################
"""
    EOF
"""
if __name__ == "__main__":
    result = pyfiglet.figlet_format("          TallBlocks's Strawberry DC")

    print (result, "https://TallBlocks.github.io")

    while True: #Starts the loop.
        getInfo() # It calls to the function getInfo in __getInfo__.py.

        from __getInfo__ import artist, album, title #It gets the artist, album and artist variable from __getInfo__.py.

        if artist != 0 and album != 0 and title != 0 and connectionClose == 0: # If the player is playing (so the artist, album and title variables aren't 0) and connection is open it updates the RPC.
            rpc.update(state=str(artist) + " - " + str(album), details=title, large_image="strawberry", small_image="play_icon") # Updates the RPC with the info it got from getInfo().
        
        elif artist != 0 and album != 0 and title != 0 and connectionClose == 1: # If the player is playing (so the artist, album and title variables values aren't 0) but the connection is close it opens again again the connection and updates the RPC.
            connectionClose = 0 # Changes connectionClose variable to 0 beacouse it will open the connection in the next step.
            rpc.connect() # Connecting to Discord's RPC.
            rpc.update(state=str(artist) + " - " + str(album), details=title, large_image="strawberry", small_image="play_icon") # Updates the RPC with the info it got from getInfo().
            
        elif artist == 0 and album == 0 and title == 0 and connectionClose == 0: # If the player isn't playing (so the artist, album and title variables values re 0) and the connection is open it closes it.
            connectionClose = 1 # Changes connectionClose variable to 1 beacouse it will close the connection in the next step.
            rpc.close() # Disconnecting from Discord's RPC.
            
        elif artist == 0 and album == 0 and title == 0 and connectionClose == 1: # If the player isn't playing (so the artist, album and title variables values re 0) and the connection is closed it just pass.
            pass # Nothing to change so it pass.
###################################################################################################