label ep2:
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
                'details': 'Playing EP2',
                'state': 'Family',
                'large_image_key': 'the_crew',
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        
    scene black

    with fade

    pause 1

    scene black

    play sound "audio/help.ogg" loop

    voice "voice/aoba/103.ogg"
    aoba "..."

    stop sound

    play sound "audio/undelet.ogg"

    "*click*"

    voice "voice/aoba/104.ogg"
    aoba "Oh... It's morning already...?"

    voice "voice/aoba/105.ogg"
    aoba "Guess I'm going to get some coffee then"

    play music "audio/bgm/M07.opus" fadein 1.5

    scene ep3 aoba wake

    with fade

    voice "voice/aoba/106.ogg"
    aoba "Wow, this morning... I'm so dizzy here..."

    voice "voice/aoba/107.ogg"
    aoba "Need... coffee..."

    scene ep3 aoba no word with dissolve

    stop music fadeout 1.5

    voice "voice/aoba/108.ogg"
    aoba "..."

    scene ep3 aoba stare with dissolve

    simon "..."

    voice "voice/aoba/109.ogg"
    aoba "..."

    scene ep2 world is going to explode

    with dissolve

    "..."


    voice "voice/aoba/110.ogg"
    "AAAAAAAAAAAAAHHHHHHHHHHHH" with Shake((5, 5, 5, 0), 1.5, dist=30)

    play music "audio/latest.ogg" fadein 1.5

    scene ep3 aoba why man with dissolve

    voice "voice/aoba/111.ogg"
    aoba "WHAT THE FUCK SIMON?!"

    voice "voice/aoba/112.ogg"
    aoba "WHY ARE YOU EATING RAW FOOD FROM THE FRIDGE!?!"

    scene ep3 simon idk man with dissolve

    simon "Man... I don't know how to cook"

    simon "so I eat it raw..."

    voice "voice/aoba/113.ogg"
    aoba "*sigh*"

    scene ep3 aoba smh with dissolve

    voice "voice/aoba/114.ogg"
    aoba "Seriously... You're gonna get sick"

    voice "voice/aoba/115.ogg"
    aoba "Why don't you learn how to cook?"

    scene ep3 simon nani with vpunch

    simon "...!"

    scene ep3 simon ayee with hpunch

    simon "COOKING?!"

    simon "HELL YEAH! I\'M GOING TO BE THE CHEF OF THE HOUSE"

    scene ep3 teh pan with vpunch

    simon "I ALWAYS WANTED TO BE CHEF"

    simon "I SAW THE CHEF COOK BEFORE NOW WATCH ME!"

    scene ep3 this is epic with vpunch

    simon "*fwoosh*"

    voice "voice/aoba/116.ogg"
    aoba "...!" with vpunch

    scene ep3 aoba how with vpunch

    voice "voice/aoba/117.ogg"
    aoba "WHAT THE FUCKKKKKKKK IS THISSSSSSSSS" with vpunch

    voice "voice/aoba/118.ogg"
    aoba "WHY ARE YOU DUMPING EVERYTHING IN THERE?!!" with vpunch

    voice "voice/aoba/119.ogg"
    aoba "AND IS THAT MOTHERFUCKIN {color=#add8e6}{b}ICE{/b}{/color}!?" with Shake((30, 30, 30, 30), 1.75, dist=50)

    scene ep3 simon slam with vpunch

    simon "DONE!"

    simon "BON APPETIT!"

    scene ep3 help us pls

    with dissolve

    voice "voice/aoba/120.ogg"
    aoba "(dear god...)"

    voice "voice/aoba/121.ogg"
    aoba "(you better not feed this to my kids)"

    scene ep3 angel punish simon

    simon "I\'m glad that I made my first dish"

    simon "I\'m going to taste first!"

    scene ep3 simon dont know what is going to happen next with vpunch

    simon "*nom*"

    scene black

    stop music fadeout 0.75


    "..."

    scene ep3 f for simon

    with vpunch

    pause 0.75

    voice "voice/aoba/122.ogg"
    aoba "SIMON!!"

    scene black with dissolve

    pause 1.25

    scene ep3 hospital with fade

    "{color=#add8e6}Hospital{/color}"

    scene ep3 emergency with dissolve

    "..."

    play music "audio/bro this is so sad.ogg"

    scene ep3 simon off with dissolve

    simon "..."

    voice "voice/aoba/123.ogg"
    aoba "..."

    scene ep3 aoba well fucked with dissolve

    voice "voice/aoba/124.ogg"
    aoba "...bon appetit, eh?"

    voice "voice/aoba/125.ogg"
    aoba "You shouldn't have done like that in the first place... Simon."

    voice "voice/aoba/126.ogg"
    aoba "You know that you are actually homeless... and don't know how to cook"

    voice "voice/aoba/127.ogg"
    aoba "but don't worry, when you're better... We'll actually help you"

    voice "voice/aoba/128.ogg"
    aoba "with this..."

    scene ep3 simon ok im sorry with dissolve

    simon "Well... I guess you're right"

    simon "Don't worry... I'll recover soon"

    voice "voice/aoba/129.ogg"
    aoba "Get well soon..."

    scene a week later

    stop music fadeout 1.25

    with dissolve

    pause 1

    scene black with dissolve

    pause 0.75

    play music "audio/over and over.ogg" fadein 1.4

    scene ep3 aoba ranger with hpunch

    voice "voice/aoba/130.ogg"
    aoba "ok, Simon..."

    voice "voice/aoba/131.ogg"
    aoba "We will teach you how to cook so we don't keep losing our ingredients..."

    simon "(wtf is with that pose...!?)"

    voice "voice/aoba/132.ogg"
    aoba "anyway... enough talk! LET'S GET HIM TO COOKING KIDS!"

    scene ep3 how to cook wit aoba one

    with irisin

    "*chop* *chop*"

    aoffy "Can you add more salt, Apple?"

    apple "Yeah, here you go!"

    aoffy "Thanks, Apple"

    simon "(Wow... does cooking actually need many people like this...?)"

    scene ep3 how to cook wit aoba two

    with blinds

    voice "voice/aoba/133.ogg"
    aoba "Now you just put everything in here"

    simon "Okay, there..."

    scene ep3 aoba tips

    with dissolve

    voice "voice/aoba/134.ogg"
    aoba "A big pot of soup is probably the easiest for you to make..."

    voice "voice/aoba/135.ogg"
    aoba "Since you like to toss many stuff in the frying pan like last time."

    voice "voice/aoba/136.ogg"
    aoba "Just be considerate about what you use in soup"

    voice "voice/aoba/137.ogg"
    aoba "and then make sure those ingredients bring out each other's flavor"

    simon "...!"

    scene ep3 teh soup with vpunch

    voice "voice/aoba/138.ogg"
    aoba "BON APPETIT!"

    scene ep3 we going to eat now with vpunch

    voice "voice/aoba/139.ogg"
    aoba "Alright everybody! Let's dig in!"

    Character("Apple & Aoffy", color="#9acd32") "Thanks for the food!"

    simon "..."

    scene ep3 simon eh with dissolve

    voice "voice/aoba/140.ogg"
    aoba "*nom* *nom*"

    aoffy "*nom* *nom*"

    apple "*nom* *nom*"

    stop music fadeout 1.25

    simon "..."

    scene ep3 simon oh with dissolve

    simon "(...well everybody is eating them...)"

    simon "here's goes nothing..."

    scene ep3 the moment of the truth with dissolve

    simon "aaaaa...."

    scene ep3 tattatatatatatatatatata with dissolve

    "*nom*"

    simon "..."

    scene ep3 mmmmm aaa roi with dissolve

    simon "...!"

    scene ep3 aoba roast with vpunch

    voice "voice/aoba/141.ogg"
    aoba "Hey! How was it?"

    voice "voice/aoba/142.ogg"
    aoba "Is this way better than your cooking"

    voice "voice/aoba/143.ogg"
    aoba "lol, just kidding alright"

    simon "..."

    scene ep3 simon cri with dissolve

    simon "T- Thank you..."

    voice "voice/aoba/144.ogg"
    aoba "Huh...?"

    scene ep3 bowl of tears with dissolve

    simon "Thank you..."

    simon "Really..."

    simon "for everything..."

    scene ep3 aoba no word again with dissolve

    voice "voice/aoba/145.ogg"
    aoba "..."

    scene ep3 no problem with dissolve

    voice "voice/aoba/146.ogg"
    aoba "No problem...!" with vpunch

    scene ep3 end

    with dissolve

    pause 3

    ".:. End."

    # This ends the game.

    stop sound fadeout 2.0
    stop music fadeout 2.0

    scene black with Dissolve(3.0)

    return
