label ep3:
    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('854617207304224808', callbacks=callbacks, log=False)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Playing EP3',
                'state': 'Coffee',
                'large_image_key': 'coffee',
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        
    scene black

    with fade

    $ renpy.pause(1, hard=True)

    scene ep3_1 with fade

    play sound "audio/beep.mp3" loop

    "*beep* *beep* *beep*"

    stop sound

    play sound "audio/click.mp3"

    scene ep3_e_1 with dissolve

    "*click*"

    scene ep3_2 with dissolve

    play sound "audio/blanket.mp3"

    aoba "..."

    scene ep3_3 with dissolve

    apple "Good morning, mom!"

    aoba "Good morning, apple..."

    scene ep3_4 with dissolve

    aoba "...?"

    aoba "Hey... today is odd... Where is Simon?"

    scene ep3_5 with dissolve

    aoffy "Simon? He disappeared..."

    scene ep3_6 with dissolve

    aoffy "Guess he doesn't want to stay here after all..."

    aoba "...!" with vpunch

    scene white with dissolve

    "..."

    "No..."

    "Simon is gone... what do I do..."

    "I need to find him home, something bad might happen!"

    play music "audio/bgm/M03.opus"

    scene ep3_7 with dissolve

    aoba "SIMON!!"

    scene ep3_8 with dissolve

    aoba "Simon?"

    scene ep3_9 with dissolve

    aoba "Simon? Come out already..."

    scene ep3_10 with blinds

    aoba "Siiimonn?"

    unknown "what the fuck?"

    unknown "who are you?"

    unknown "and why are you in my house??"

    scene ep3_11 with dissolve

    aoba "..."

    aoba "(No wait... he shouldn't be here... the fuck am I doing?)"

    $ quick_menu = False

    window hide

    $ renpy.pause(0, hard=True)
    scene white with dissolve

    $ renpy.pause(0, hard=True)
    scene ep3_12 with pushdown

    $ renpy.pause(1, hard=True)

    scene ep3_13 with Dissolve(0.175)

    $ renpy.pause(1, hard=True)

    scene ep3_14 with pushup

    $ renpy.pause(1, hard=True)

    scene ep3_15 with PushMove(0.25, "pushup")

    $ renpy.pause(0, hard=True)
    show expression Text(_("{size=64}{color=#000000}Have you seen Simon?{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 0.025
            alpha 0.0
            0.5
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    stop music fadeout 1.25

    $ renpy.pause(0, hard=True)
    scene white with dissolve
    $ renpy.pause(0, hard=True)
    window show
    $ quick_menu = True

    "..."

    scene ep3_16 with dissolve

    aoba "Ah well... He's really gone..."

    aoba "now I don't have to worry about food shortage ever again..."

    scene ep3_17 with dissolve

    aoba "Oh-"

    window hide

    play sound "audio/shit.mp3"
    show ep3_18 with Shake((5, 5, 5, 0), 1.25, dist=30)

    $ renpy.pause(0.65, hard=True)

    play music "audio/latest.ogg"

    scene ep3_19 with dissolve

    apple "Mom??"

    aoffy "Aoba-san??"

    aoba "..."

    scene ep3_20 with dissolve

    apple "Mom...?!"

    aoffy "What the actual f--"

    scene ep3_21 with dissolve

    aoffy "Uhh... Please calm down here..."

    aoffy "What's going on here?"

    scene ep3_22 with vpunch

    aoba "NOT ONLY THAT WE RAN OUT OF FOOD" with vpunch

    aoba "NOW WE RAN OUT OF COFFEE AS WELL" with vpunch

    scene ep3_23 with dissolve

    aoffy "Oh right..."

    aoffy "but uhmmm... Coffee?"

    scene ep3_24 with vpunch

    aoba "You just don't get it Aoffy" with vpunch

    aoba "I absolutely need my morning coffee!!!" with vpunch

    aoffy "Uh... o- okay...?"

    scene ep3_25 with vpunch

    aoba "I'll buy some immediately!!" with vpunch

    play sound "audio/splash.ogg"
    scene ep3_26 with hpunch

    "..."

    play sound "audio/lvlup.ogg"
    scene ep3_27 with vpunch

    $ renpy.pause(0.65, hard=True)

    angel "yo wtf?"

    $ quick_menu = False

    stop music fadeout 0.5
    play music "audio/UFO.ogg" fadein 0.5

    window hide

    $ renpy.pause(0, hard=True)
    scene ep3_28 with dissolve
    $ renpy.pause(2.56, hard=True)

    play sound "audio/explode1.ogg"
    $ renpy.pause(0, hard=True)
    scene ep3_29 with dissolve
    $ renpy.pause(0, hard=True)

    $ renpy.pause(1.65, hard=True)

    stop music

    play sound "audio/aaaaaaaaaaaaaa.mp3"
    $ renpy.pause(0, hard=True)
    scene ep3_30 with Shake((5, 5, 5, 0), 5, dist=30)
    $ renpy.pause(0, hard=True)

    $ renpy.pause(0, hard=True)
    scene ep3_31 with dissolve
    $ renpy.pause(1, hard=True)

    $ quick_menu = True

    scene ep3_32 with dissolve

    apple "wtf is going on Aoffy?!?"

    aoffy "I don't know anymore, apple..."

    stop sound fadeout 1.75

    scene ep3_33 with Fade(1.25, 0.75, 0.75)

    aoba "*huff* *huff*"

    scene ep3_34 with dissolve

    aoba "...!"

    scene ep3_35 with dissolve

    aoba "..."

    scene ep3_36 with dissolve

    aoba "(Simon... would he be alright...?)"

    scene ep3_37 with Dissolve(1.5)

    $ renpy.pause(1.5, hard=True)

    scene ep3_38 with Fade(1.25, 0.75, 0.75)

    play music "audio/bgm/M06.opus" fadein 1.5
    aoba "Finally in Tesco~!"

    scene ep3_39 with dissolve

    aoba "Okay, let's see... Coffee..."

    scene ep3_40 with vpunch
    stop music fadeout 1.25

    aoba "WHAT!!"

    aoba "HOW COULD THIS HAPPEN!!"

    scene ep3_41 with dissolve

    aoba "Excuse me...?"

    aoba "When will you restock the coffee, Aisle?"

    scene ep3_42 with dissolve
    play music "audio/bgm/M08.opus"
    
    simon "Oh hey, Aoba!"

    aoba "What the?! SIMON!?" with vpunch

    scene ep3_43 with dissolve

    aoba "Holup- You work here?"

    simon "Yeah, I've got bills I've gotta pay"

    scene ep3_44 with dissolve

    aoba "You live in my house..."

    simon "I would feel bad if I'm being such a freeloader tho..."

    simon "So... I figured I should get a a job..."

    scene ep3_45 with dissolve

    aoba "Oh, that's nice!"

    simon "Yeah... Thanks for taking me in, feeding me and stuff like that..."

    scene ep3_46 with dissolve

    simon "Anyways, how can I help?"

    aoba "...!" with vpunch

    scene ep3_47 with vpunch

    aoba "Please tell me if you have coffee!!" with vpunch

    simon "What?"

    simon "Coffee?"

    scene ep3_48 with dissolve

    simon "no."

    aoba "SHIT!" with vpunch

    scene ep3_49 with vpunch

    simon "Don't worry, Aoba!"

    simon "If you want coffee, I'll get you the best of the best!"

    stop music fadeout 2
    scene ep3_50 with vpunch

    simon "I'm taking you to Brazil!"

    scene ep3_51 with dissolve

    aoba "wut?"

    $ renpy.pause(1.25, hard=True)

    scene meanwhile

    stop music fadeout 1.5

    with dissolve

    $ renpy.pause(1.25, hard=True)

    scene ep3_52 with dissolve

    play music "audio/over and over.ogg" fadein 1.25

    play sound "audio/less.mp3"
    simon "less go" with vpunch

    aoba "W- wait...! Whose motorboat is this?!"

    $ renpy.pause(1.25, hard=True)

    scene ep3_53

    with dissolve

    $ renpy.pause(1.25, hard=True)

    stop music fadeout 1.5

    scene ep3_54 with Fade(2.0, 0.75, 2.0)

    aoba "zZz"

    scene ep3_55 with dissolve

    simon "Hey, Aoba!"

    aoba "...?"

    scene ep3_56 with dissolve

    aoba "Huh...?"

    scene ep3_57 with dissolve

    play music "audio/ng_d_1_32.mp3" fadein 2.5

    simon "We got a problem..."

    aoba "..."

    play sound "audio/shit.mp3"
    show ep3_58 with Shake((5, 5, 5, 0), 1.25, dist=30)

    scene ep3_59 with dissolve

    aoba "WE'RE DOOMED"

    scene ep3_60 with dissolve

    simon "Hello, is anyone on shores?"

    simon "...uhh... help-"

    stop music

    $ quick_menu = False

    window hide

    play sound "audio/splash.ogg"
    show ep3_61 with Shake((5, 5, 5, 0), 1.25, dist=30)

    play music "audio/underwater.ogg"
    scene ep3_62 with dissolve

    $ renpy.pause(2, hard=True)

    scene ep3_63 with dissolve

    $ renpy.pause(0.95, hard=True)

    scene ep3_64 with dissolve

    $ renpy.pause(0.75, hard=True)

    scene ep3_65 with dissolve

    $ renpy.pause(2, hard=True)

    stop music fadeout 1.25

    play sound "audio/beach.ogg" fadein 4.5 loop
    $ renpy.pause(5, hard=True)

    scene ep3_66 with Dissolve(1.25)
    $ renpy.pause(0, hard=True)
    scene ep3_65 with Dissolve(1.25)
    $ renpy.pause(0, hard=True)
    scene ep3_66 with Dissolve(1.25)
    $ renpy.pause(0, hard=True)
    scene ep3_67 with Dissolve(1.25)

    show expression Text(_("{size=64}{color=#FFFFFF}...{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.5
            linear 0.5 alpha 1

    $ renpy.pause(3, hard=True)
    scene ep3_68 with Dissolve(2.5)

    show expression Text(_("{size=64}{color=#FFFFFF}Ehhh...?{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.5
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_69 with Dissolve(2.5)

    show expression Text(_("{size=64}{color=#FFFFFF}Where... am I...?{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_70 with dissolve

    $ renpy.pause(4.5, hard=True)

    scene ep3_71 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}Goddamnit... All this shit just for coffee...?{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_72 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}Simon! There you are!{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_73 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}Come on, Let's go home already!{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_74 with dissolve

    play music "audio/bgm/M20.opus" fadein 2.0

    show expression Text(_("{size=64}{color=#FFFFFF}Aoba-san...{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_75 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}The ocean sure beautiful, isn't it?{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_76 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}...{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(3.5, hard=True)

    scene ep3_77 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}...Simon-kun...{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_78 with dissolve

    show expression Text(_("{size=64}{color=#FFFFFF}You know that we don't have enough budget for this... right?{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 1.0
            yoffset -20
            alpha 0.0
            0.25
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    stop music
    stop sound
    $ quick_menu = True

    scene ep3_79

    simon "a-"

    scene ep3_80 with dissolve

    aoba "..."

    scene ep3_81 with vpunch

    aoba "SIMON!! YOU BETTER TAKE ME HOME! RIGHT NOW!" with hpunch

    simon "Ahh~ Aoba~ Calm downnnn... nyaa~~" with hpunch

    scene ep3_82 with vpunch

    simon "Don't worry, Aoba!"

    simon "I'm a pro minecraft player!"

    simon "I will get us outta here!"

    play music "audio/speedrun.mp3"
    scene ep3_83 with vpunch

    "*crushed tree sound here*"

    scene ep3_e_2 with vpunch

    scene ep3_e_3 with vpunch

    scene ep3_e_4 with vpunch

    scene ep3_84 with vpunch

    aoba "wtf..."

    scene ep3_85 with vpunch

    $ renpy.pause(0.25, hard=True)

    scene ep3_86 with vpunch

    simon "annddd... DONE!"

    stop music fadeout 0.75

    scene ep3_87 with dissolve

    aoba "Okay, let's go then..."

    scene ep3_88 with dissolve

    simon "Wait! Aoba!" with vpunch

    simon "We're here for coffee, remember?" with vpunch

    scene ep3_89 with dissolve

    simon "besides... it's not a good idea to go right now!"

    scene ep3_90 with dissolve

    aoba "Huh?"

    play music "audio/ng_d_1_37.mp3"

    scene ep3_91 with Shake((5, 5, 5, 0), 7.5, dist=30)

    scene ep3_92 with dissolve

    aoba "Well... shit, you're right..."

    stop music fadeout 1.5

    scene ep3_93 with Fade(2.0, 0.75, 2.0)

    play sound "audio/campfire.ogg" loop
    $ renpy.pause(4.5, hard=True)

    scene ep3_94 with dissolve

    simon "Ah! A shooting star!"

    scene ep3_95 with dissolve

    simon "..."

    aoba "..."

    scene ep3_96 with dissolve

    simon "Aren't you gonna wish for anything?"

    aoba "No... Feeling hopeless right now..."

    scene ep3_97 with dissolve

    play audio "audio/badumtss.mp3"
    simon "Don't you mean... \"Hoap-less\""

    aoba "NO!"

    "(Fun fact: Aoba's Minecraft Username is Hoap)"

    scene ep3_98 with dissolve

    aoba "I don't know how you're in the mood to make stupid jokes right now..."

    aoba "Aren't you worried at all?"

    scene ep3_99 with dissolve

    simon "..."

    scene ep3_100 with dissolve

    simon "Well... honestly..."

    simon "Yeah... I'm just trying to be positive..."

    simon "Just believing that we'll be alright..."

    scene ep3_101 with dissolve

    aoba "..."

    scene ep3_102 with dissolve

    aoba "Right... sorry..."

    scene ep3_103 with dissolve

    simon "Don't stress it, Aoba!"

    simon "We'll figure out what to do in the morning!"

    scene ep3_104 with dissolve

    simon "Welp! Good night!"

    scene ep3_105 with dissolve

    simon "zZz"

    aoba "..."

    scene ep3_106 with dissolve

    aoba "..."

    scene ep3_107 with dissolve

    aoba "zZz"

    scene ep3_108 with dissolve
    stop sound fadeout 3.0
    scene ep3_109 with Dissolve(5.0)

    play sound "audio/sisgug.mp3" fadein 3.727 loop    
    $ renpy.pause(4.5, hard=True)

    scene ep3_110 with dissolve

    aoba "Oof... I have't eat anything since yesterday morning..."

    aoba "My stomach hurts..."

    aoba "Gah... and my back... sleeping on sand made it hurts..."

    aoba "This is bad... I feel so horrible right now..."

    simon "OKAY! LET'S GATHER SOME FOOD THEN!" with vpunch

    stop sound fadeout 2
    play music "audio/ng_d_1_13.mp3" fadein 2
    scene ep3_111 with dissolve

    simon "GATHERING MONTAGE!!!" with vpunch

    $ quick_menu = False

    window hide

    scene ep3_112 with dissolve

    $ renpy.pause(0.75, hard=True)

    scene ep3_113 with vpunch

    $ renpy.pause(1.75, hard=True)

    scene ep3_114 with dissolve

    $ renpy.pause(2, hard=True)

    scene ep3_115 with dissolve

    $ renpy.pause(0.65, hard=True)

    scene ep3_116 with vpunch

    $ renpy.pause(1.727, hard=True)

    scene ep3_117 with hpunch

    $ renpy.pause(3, hard=True)

    scene ep3_118 with pushright

    $ renpy.pause(1, hard=True)

    scene ep3_119 with dissolve

    $ renpy.pause(1, hard=True)

    scene ep3_120 with vpunch

    $ renpy.pause(1, hard=True)

    scene ep3_121 with wipeleft

    $ renpy.pause(2, hard=True)

    scene ep3_122 with wipeleft

    $ renpy.pause(2, hard=True)

    scene ep3_123 with wipeleft

    stop music fadeout 2
    $ renpy.pause(2, hard=True)

    play music "audio/ng_cs_0_21.ogg"
    scene ep3_124 with slidedown
    $ quick_menu = True

    aoba "God damn, isn't there anything edible around here?"

    scene ep3_125 with vpunch

    $ renpy.pause(1, hard=True)

    scene ep3_126 with dissolve

    simon "There!"

    aoba "Hmm?"

    scene ep3_127 with vpunch

    simon "A banana tree!"

    stop music fadeout 1
    play music "audio/honk gong.mp3" fadein 1
    scene ep3_128 with vpunch

    aoba "Leave it to me, Simon!"

    aoba "I know Muay Thai!"

    simon "Yoooooo! Way to go, Aoba!"

    scene ep3_129 with vpunch

    show expression Text(_("{size=64}{color=#000000}This is truely Thai-Denmark moment.{/color}{/size}")) with dissolve:
            xalign 0.5
            yalign 0.025
            alpha 0.0
            0.5
            linear 0.5 alpha 1

    $ renpy.pause(2.5, hard=True)

    scene ep3_130

    play sound "audio/punch.ogg"
    aoba "Ora!" with hpunch

    simon "Yooo! That's a classic move right there!"

    show ep3_130_extra with Dissolve(2.5)

    "(This is Bua-Kao famous move, if you didn't know)"

    stop music fadeout 3

    play music "audio/ng_d_2_27.mp3" fadein 4
    scene ep3_131 with dissolve

    aoba "Now we have bananas to eat for days!"

    stop music
    play sound "audio/punch.ogg"
    scene ep3_132 with vpunch

    aoba "!?"

    simon "?"

    scene ep3_133 with dissolve

    "..."

    aoba "Hmm..? That doesn't look like a banana-"

    play sound "audio/shit.mp3"
    show ep3_134 with Shake((5, 5, 5, 0), 1.25, dist=30)

    play music "audio/ng_d_2_28.mp3" fadein 1.2
    scene ep3_135 with vpunch

    aoba "RUN FOR YOUR LIFE!!!" with vpunch

    scene ep3_136 with hpunch

    aoba "Ah--"

    play sound "audio/bush.ogg"
    scene ep3_137 with vpunch

    $ renpy.pause(2, hard=True)

    show ep3_138 with dissolve

    $ renpy.pause(1.25, hard=True)

    scene ep3_139 with dissolve

    stop music fadeout 1.75
    $ renpy.pause(2, hard=True)

    scene ep3_140 with hpunch

    $ renpy.pause(0.54321, hard=True)

    scene ep3_141 with dissolve

    simon "Woah there! Aoba, you okay?"

    aoba "Y-yeah... I'm okay..."

    scene ep3_142 with dissolve

    "...!"

    scene ep3_143 with vpunch

    simon "Yooo, isn't that a coffee plant?!"

    aoba "Yeah! You're right!"

    $ renpy.pause(1.25, hard=True)

    scene ep3_144

    with dissolve

    #play music "audio/ng_d_2_08.mp3" fadein 1.25
    play sound "audio/campfire.ogg" loop
    $ renpy.pause(1.25, hard=True)

    scene ep3_145 with dissolve

    $ renpy.pause(1.5, hard=True)

    scene ep3_146 with dissolve

    simon "So... how was it?"

    aoba "Ahh~ it's so great..."

    scene ep3_147 with dissolve

    simon "See? Brazilian coffee is the best!"

    show ep3_147_extra with Dissolve(2.5)

    $ renpy.pause(2.5, hard=True)

    scene ep3_148 with dissolve

    aoba "..."

    scene ep3_149 with dissolve

    aoba "Wait..."

    scene ep3_150 with dissolve

    aoba "We shouldn't drink coffee at this hour..."

    simon "..."

    scene ep3_151 with dissolve

    simon "Ah welp... guess we won't be sleeping tonight..."

    scene ep3_152 with dissolve

    simon "But hey! our advanture is coming to an end..." with vpunch

    simon "We got the coffee... now we just need to get back home!"

    scene ep3_153 with dissolve

    aoba "Yep..."

    scene ep3_154 with vpunch

    simon "You know what?"

    scene ep3_155 with dissolve

    simon "Drinking hot coffee, sitting by campfire near the beach..."

    simon "I'm feeling really cozy right now!"

    simon "We should sing something!"

    scene ep3_156 with dissolve

    aoba "Oh, alright"

    scene ep3_157 with dissolve

    simon "We should totally sing \"Glass Beach\"..."

    simon "This is a beach episode after all!"

    aoba "Fine by me!"

    scene ep3_158 with dissolve

    simon "~ can we forget about the places that we should be ~"

    scene ep3_159 with dissolve

    "~ we don't have to go home today ~"

    scene ep3_160 with dissolve

    "~ i'll sleep on a million couches ~"

    scene ep3_161 with dissolve

    "~ if we have to, to keep us both safe. ~"

    scene ep3_162 with dissolve

    $ renpy.pause(2.3, hard=True)

    scene ep3_163 with dissolve

    $ renpy.pause(2.3, hard=True)

    scene ep3_164 with dissolve
    $ renpy.pause(5, hard=True)
    stop sound fadeout 3.0
    scene ep3_165 with Dissolve(5.0)

    play sound "audio/sisgug.mp3" fadein 3.727 loop    
    $ renpy.pause(4.5, hard=True)

    scene ep3_166 with dissolve

    simon "..."

    aoba "..."

    scene ep3_167 with vpunch

    simon "the coast is clear!"

    aoba "alrighty! let's go!"

    scene ep3_168 with vpunch

    $ renpy.pause(0.727, hard=True)

    scene ep3_169 with dissolve

    $ renpy.pause(3, hard=True)

    scene ep3_170 with dissolve
    scene ep3_171 with Dissolve(5.0)

    $ renpy.pause(5, hard=True)

    stop sound fadeout 2.0
    stop music fadeout 2.0

    scene black with Dissolve(3.0)

    return
