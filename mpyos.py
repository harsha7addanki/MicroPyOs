import utime
import pickle
import apps as appio

apps = {}


def clear():
    print("\x1B\x5B2J", end="")
    print("\x1B\x5BH", end="")


def bootscreen():
    print(
        r""" 
          __       __  __                                _______              ______    ______  
        |  \     /  \|  \                              |       \            /      \  /      \ 
        | $$\   /  $$ \$$  _______   ______    ______  | $$$$$$$\ __    __ |  $$$$$$\|  $$$$$$\
        | $$$\ /  $$$|  \ /       \ /      \  /      \ | $$__/ $$|  \  |  \| $$  | $$| $$___\$$
        | $$$$\  $$$$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\| $$    $$| $$  | $$| $$  | $$ \$$    \ 
        | $$\$$ $$ $$| $$| $$      | $$   \$$| $$  | $$| $$$$$$$ | $$  | $$| $$  | $$ _\$$$$$$\
        | $$ \$$$| $$| $$| $$_____ | $$      | $$__/ $$| $$      | $$__/ $$| $$__/ $$|  \__| $$
        | $$  \$ | $$| $$ \$$     \| $$       \$$    $$| $$       \$$    $$ \$$    $$ \$$    $$
         \$$      \$$ \$$  \$$$$$$$ \$$        \$$$$$$  \$$       _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                                 |  \__| $$                    
                                                                  \$$    $$                    
                                                                   \$$$$$$
                                        #___                     
        """
    )
    utime.sleep(1)
    clear()
    print(
        r""" 
          __       __  __                                _______              ______    ______  
        |  \     /  \|  \                              |       \            /      \  /      \ 
        | $$\   /  $$ \$$  _______   ______    ______  | $$$$$$$\ __    __ |  $$$$$$\|  $$$$$$\
        | $$$\ /  $$$|  \ /       \ /      \  /      \ | $$__/ $$|  \  |  \| $$  | $$| $$___\$$
        | $$$$\  $$$$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\| $$    $$| $$  | $$| $$  | $$ \$$    \ 
        | $$\$$ $$ $$| $$| $$      | $$   \$$| $$  | $$| $$$$$$$ | $$  | $$| $$  | $$ _\$$$$$$\
        | $$ \$$$| $$| $$| $$_____ | $$      | $$__/ $$| $$      | $$__/ $$| $$__/ $$|  \__| $$
        | $$  \$ | $$| $$ \$$     \| $$       \$$    $$| $$       \$$    $$ \$$    $$ \$$    $$
         \$$      \$$ \$$  \$$$$$$$ \$$        \$$$$$$  \$$       _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                                 |  \__| $$                    
                                                                  \$$    $$                    
                                                                   \$$$$$$
                                        ##__                     
        """
    )
    utime.sleep(1)
    clear()
    print(
        r""" 
          __       __  __                                _______              ______    ______  
        |  \     /  \|  \                              |       \            /      \  /      \ 
        | $$\   /  $$ \$$  _______   ______    ______  | $$$$$$$\ __    __ |  $$$$$$\|  $$$$$$\
        | $$$\ /  $$$|  \ /       \ /      \  /      \ | $$__/ $$|  \  |  \| $$  | $$| $$___\$$
        | $$$$\  $$$$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\| $$    $$| $$  | $$| $$  | $$ \$$    \ 
        | $$\$$ $$ $$| $$| $$      | $$   \$$| $$  | $$| $$$$$$$ | $$  | $$| $$  | $$ _\$$$$$$\
        | $$ \$$$| $$| $$| $$_____ | $$      | $$__/ $$| $$      | $$__/ $$| $$__/ $$|  \__| $$
        | $$  \$ | $$| $$ \$$     \| $$       \$$    $$| $$       \$$    $$ \$$    $$ \$$    $$
         \$$      \$$ \$$  \$$$$$$$ \$$        \$$$$$$  \$$       _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                                 |  \__| $$                    
                                                                  \$$    $$                    
                                                                   \$$$$$$
                                        ###_                    
        """
    )
    utime.sleep(1)
    clear()
    print(
        r""" 
          __       __  __                                _______              ______    ______  
        |  \     /  \|  \                              |       \            /      \  /      \ 
        | $$\   /  $$ \$$  _______   ______    ______  | $$$$$$$\ __    __ |  $$$$$$\|  $$$$$$\
        | $$$\ /  $$$|  \ /       \ /      \  /      \ | $$__/ $$|  \  |  \| $$  | $$| $$___\$$
        | $$$$\  $$$$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\| $$    $$| $$  | $$| $$  | $$ \$$    \ 
        | $$\$$ $$ $$| $$| $$      | $$   \$$| $$  | $$| $$$$$$$ | $$  | $$| $$  | $$ _\$$$$$$\
        | $$ \$$$| $$| $$| $$_____ | $$      | $$__/ $$| $$      | $$__/ $$| $$__/ $$|  \__| $$
        | $$  \$ | $$| $$ \$$     \| $$       \$$    $$| $$       \$$    $$ \$$    $$ \$$    $$
         \$$      \$$ \$$  \$$$$$$$ \$$        \$$$$$$  \$$       _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                                 |  \__| $$                    
                                                                  \$$    $$                    
                                                                   \$$$$$$
                                        ####                     
        """
    )
    utime.sleep(1)
    clear()
    print(
        r""" 
          __       __  __                                _______              ______    ______  
        |  \     /  \|  \                              |       \            /      \  /      \ 
        | $$\   /  $$ \$$  _______   ______    ______  | $$$$$$$\ __    __ |  $$$$$$\|  $$$$$$\
        | $$$\ /  $$$|  \ /       \ /      \  /      \ | $$__/ $$|  \  |  \| $$  | $$| $$___\$$
        | $$$$\  $$$$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\| $$    $$| $$  | $$| $$  | $$ \$$    \ 
        | $$\$$ $$ $$| $$| $$      | $$   \$$| $$  | $$| $$$$$$$ | $$  | $$| $$  | $$ _\$$$$$$\
        | $$ \$$$| $$| $$| $$_____ | $$      | $$__/ $$| $$      | $$__/ $$| $$__/ $$|  \__| $$
        | $$  \$ | $$| $$ \$$     \| $$       \$$    $$| $$       \$$    $$ \$$    $$ \$$    $$
         \$$      \$$ \$$  \$$$$$$$ \$$        \$$$$$$  \$$       _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                                 |  \__| $$                    
                                                                  \$$    $$                    
                                                                   \$$$$$$
                                        FINISHED LOADING MICROPYOS                     
        """
    )
    utime.sleep(1)
    clear()


def osloop():
    print("Here Is An App List From MICRO Py OS:\n")
    with open("apps.pk") as f:
        apps = pickle.load(f)
        for app, i in zip(apps, range(len(apps))):
            print(str(i) +") " + app)
        runapp = input("\nType The Number corresponding to the App To Launch\n>")
    if runapp:
        if runapp not in range(len(apps)):
            print("Invalid Option...")
            utime.sleep(1)
            clear()
            osloop()
        clear()  # Clear Screen
        runapp = apps.values()[int(runapp)] # Get App Name
        exec("appio." + runapp + '({"NOTIMP":"NOTIMP"})') # Run App
    clear()

def mpyos():
    bootscreen()
    osloop()