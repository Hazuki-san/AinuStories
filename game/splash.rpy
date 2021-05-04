label language_chooser: 
    scene black 
    menu: 
        "English":
            $ renpy.change_language(None) 
        "ภาษาไทย":
            $ renpy.change_language("thai")
        "Polski":
            $ renpy.change_language("polish")
        "Indo":
            $ renpy.change_language("indo")
        "{font=Mali.ttf}{size=48} {/size}{/font}{font=Neucha.ttf}{size=30}Русский{/size}{/font}":
            $ renpy.change_language("russian")
    $ renpy.utter_restart() #alternatively, use "return" if you don't want to go to the main menu.

label splashscreen:
    #python:
    #    import ctypes
    #    import os
    #    aoba_dead = None
    #    everyone_dead = None
    #    try: renpy.file("../characters/aoba.chr")
    #    except: aoba_dead = True
    #    if aoba_dead:
    #        if len(os.listdir(config.basedir + "/characters/")) == 0:
    #            everyone_dead = True
    #        else:
    #            ctypes.windll.user32.MessageBoxW(0, "aoba.chr not found! Exiting the game...", "Ainu Stories", 0x10)
    #           os._exit(0)
    #
    #scene black
    #
    #if everyone_dead:
    #    show black
    #    play music "audio/bgm/s_kill_early.ogg"
    #    $ renpy.pause(1.0)
    #    show endDDLC with Dissolve(0.75)
    #    $ renpy.pause(3.0)
    #    scene white
    #    show expression "images/z.png":
    #        yalign -0.05
    #        xalign 0.25
    #        dizzy(1.0, 4.0, subpixel=False)
    #    show white as w2:
    #        choice:
    #            ease 0.25 alpha 0.1
    #        choice:
    #            ease 0.25 alpha 0.125
    #        choice:
    #            ease 0.25 alpha 0.15
    #        choice:
    #            ease 0.25 alpha 0.175
    #        choice:
    #            ease 0.25 alpha 0.2
    #        choice:
    #            ease 0.25 alpha 0.225
    #        choice:
    #            ease 0.25 alpha 0.25
    #        choice:
    #            ease 0.25 alpha 0.275
    #        choice:
    #            ease 0.25 alpha 0.3
    #        pass
    #        choice:
    #            pass
    #        choice:
    #            0.25
    #        choice:
    #            0.5
    #        choice:
    #            0.75
    #        repeat
    #    show noise:
    #        alpha 0.1
    #    with Dissolve(1.0)
    #    #show text "{color=#000000}Now everyone can be happy.{/color}" with dissolve
    #    show expression Text("{color=#000000}Now everyone can be happy.{/color}") with dissolve:
    #        xalign 0.8
    #        yalign 0.5
    #        alpha 0.0
    #        600
    #        linear 60 alpha 0.5
    #    pause
    #    $ renpy.quit()
    

    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        jump language_chooser

    show text (_("{color=#ffffff}This story is completely FULL OF NONSENSE, you should take some paracetamol before playing this game.{/color}")) with dissolve
    $ renpy.pause(2)

    hide text with dissolve
    
    $ renpy.pause(2)
    
    show text (_("{color=#ffffff}Aoba Suzukaze Presents\na story and art by: Aoffy{/color}")) with dissolve ## fix
    $ renpy.pause(2)
    
    with dissolve
    with Pause(1.0)

    hide text
    with dissolve
   
    return