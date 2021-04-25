# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    with fade

    stop music fadeout 2.0
    # need to figure why this thing is freezing the game
    #python:
    #    try: renpy.file("../characters/aoba.chr")
    #    except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    menu:
        "From the Beginning":
            window hide
            pause 1
        "Simon joins Ainu!":
            window hide
            jump ep1
        "Family":
            window hide
            jump ep2
        "Coffee":
            window hide
            jump ep3

    scene black

    with fade

    "..."

    "This is..."

    "This is how Ainu! begins"

    "It all started with one story..."

    "Once upon a time..."

    pause 1

    # Let's spice some beats
    play music "audio/bgm/M01.opus"

    scene aoba watering plants

    with fade

    "It all started with me, watering the plants in the garden."

    # These display lines of dialogue.

    voice "voice/aoba/1.ogg"
    aoba "Today is a good day!"

    voice "voice/aoba/2.ogg"
    aoba "So, I'll make my plants fresh for a day~"

    scene aoba and apple plants

    apple "Mom! I\'m going to plants some seeds!"

    voice "voice/aoba/3.ogg"
    aoba "OK son, so I can give those seeds some water too"

    scene aoba aoffy and apple

    with irisin 

    aoffy "I hope I can catch some fishes, so we don't have to buy fish"

    aoffy "I can do this...!"

    aoffy "*pls fish*"

    scene aaaa

    with dissolve

    "And Akinya, qt just play with the cat"

    "Isn't it that cute?"

    scene whole family

    with dissolve

    "And Jerry, he's just watching us inside the house"

    "He doesn't want to go outside"

    stop music fadeout 3.0

    scene aoba and apple fucked up

    with Shake((0, 0, 0, 0), 3.0, dist=15)

    "..."

    play music "audio/PERSUIT(Miles).mp3"

    scene aa giant tree

    with zoomout

    apple "!!!"

    voice "voice/aoba/4.ogg"
    aoba "WHAT THE HELL?!"

    voice "voice/aoba/5.ogg"
    aoba "APPLE!!! TELL ME WHERE YOU GOT THAT SEED"

    scene aa nice tree

    with dissolve

    apple "I... I don't really know mom"

    apple "I think I just found it in--"

    voice "voice/aoba/6.ogg"
    aoba "OK WHATEVER YOU SAY"

    voice "voice/aoba/7.ogg"
    aoba "BUT DAMN BOI, THAT TREE LOOKIN' THICC"

    apple "..."

    voice "voice/aoba/8.ogg"
    aoba "LET'S CLIMB IT!"

    apple "Wait... what? why?"

    voice "voice/aoba/9.ogg"
    aoba "I always read Jack and the Beanstalk ya know"

    apple "(Why does she always mention that... It's not even a bean...)"

    apple "Okay mom, whatever you say..."

    voice "voice/aoba/10.ogg"
    aoba "get on my back!"

    voice "voice/aoba/11.ogg"
    aoba "come on now!"

    stop music fadeout 1.75

    play music "audio/bgm/M12.opus" fadein 1.75

    scene aa climb 

    with wipeup

    "And then Aoba and Apple went to climb the tree together to see what's on the top"

    "(How does Aoba do that?!)"

    apple "Wow mom, how are you so strong"

    voice "voice/aoba/12.ogg"
    aoba "You'll never know"

    voice "voice/aoba/13.ogg"
    aoba "I've done so many things since you were still a little kid"

    apple "(I shouldn't come with her in the first place... oh god)"

    voice "voice/aoba/14.ogg"
    aoba "Almost there!"

    apple "Mom.. Are you not scared of heights?"

    voice "voice/aoba/15.ogg"
    aoba "No? Why?"

    apple "I don't want to die young mom"

    voice "voice/aoba/16.ogg"
    aoba "Just don't look down you'll be fine!"

    play music "audio/bgm/M13.opus" fadein 1.75

    scene aa heaven

    with wipeup

    voice "voice/aoba/17.ogg"
    aoba "..."

    apple "..."

    voice "voice/aoba/18.ogg"
    aoba "What..."

    voice "voice/aoba/19.ogg"
    aoba "I..."

    voice "voice/aoba/20.ogg"
    aoba "How is this possible?!"

    apple "..."

    voice "voice/aoba/21.ogg"
    aoba "So all of the stories... ARE REAL?!"

    voice "voice/aoba/22.ogg"
    aoba "WE HAVE TO GO INSIDE THAT, NOW!"

    apple "huh?"

    voice "voice/aoba/23.ogg"
    aoba "COME WITH ME!"

    apple "but... we shouldn't get in random--"

    voice "voice/aoba/24.ogg"
    aoba "NOW!"

    apple "ok ok mom!"

    stop music fadeout 2.0

    scene aa enter

    with dissolve

    voice "voice/aoba/25.ogg"
    aoba "..."

    apple "..."

    voice "voice/aoba/26.ogg"
    aoba "Stay close!"

    apple "Okay mom... Please careful..."

    voice "voice/aoba/27.ogg"
    aoba "Woah...!"

    apple "...!"

    play music "audio/bgm/M04.opus" fadein 1.75

    scene aa god

    with dissolve

    angel "I... am..."

    angel "The Angel!"

    angel "Since you're are here..."

    angel "I... will grant you a wish"

    angel "Choose... Your wish... Wisely..."

    scene aa thinking

    with dissolve

    voice "voice/aoba/28.ogg"
    aoba ":thinking:"

    apple "..."

    apple "(I wonder...)"

    apple "(Why Akinya is always playing with cat)"

    apple "(mmmm... maybe... I should get a cat...?)"

    scene aa raise

    with dissolve

    stop music fadeout 2.0

    apple "Angel! I want to have a cat!"

    scene aa angel

    with dissolve

    angel "Good choice... Young man..."

    angel "Here it is... Your cat."

    play music "audio/Noisy People.mp3" fadein 1.8

    scene aa cat

    with dissolve

    "*mrowwwwwww*"

    voice "voice/aoba/29.ogg"
    aoba "What the fuck"

    voice "voice/aoba/30.ogg"
    aoba "You can have anything... But you"

    voice "voice/aoba/31.ogg"
    aoba "ASK FOR A CAT?!"

    apple "I just want to know why Akinya loves his cat"

    apple "That's all!"

    voice "voice/aoba/32.ogg"
    aoba "(sigh)"

    scene aa noticed

    with dissolve

    angel "What about you? Good sir."

    voice "voice/aoba/33.ogg"
    aoba "...!"

    voice "voice/aoba/34.ogg"
    aoba "I can ask for... A wish?"

    scene aa angel

    with dissolve

    angel "Of course, you can!"

    angel "Because this young man... Already granted his wish..."

    angel "So why don't you have one?"

    stop music fadeout 2.25

    voice "voice/aoba/35.ogg"
    aoba "..."

    scene what do you wish for

    with dissolve

    angel "What do you wish for?"

    scene aoba stare

    with dissolve

    voice "voice/aoba/36.ogg"
    aoba "..."

    voice "voice/aoba/37.ogg"
    aoba "I..."

    voice "voice/aoba/38.ogg"
    aoba "I want..."

    voice "voice/aoba/39.ogg"
    aoba "I want to have a proper AntiCheat on my osu! server!"

    scene aa angel

    angel "..."

    voice "voice/aoba/40.ogg"
    aoba "..."

    scene angel lmao

    with dissolve

    play music "audio/Interesting People.mp3" fadein 1.75

    angel "OK"

    angel "(what a dumb wish lmao)"

    stop music fadeout 1.75

    scene angel ac

    with dissolve

    angel "Here it is... The AntiCheat"

    voice "voice/aoba/41.ogg"
    aoba "Th- Thank you... sir."

    scene aa ppy

    with dissolve

    play music "audio/Noisy People.mp3" fadein 1.8

    voice "voice/aoba/42.ogg"
    aoba "YAAH!! YEAH! HAHA"

    apple "What the fuck"

    voice "voice/aoba/43.ogg"
    aoba "Hey guys, peppy here"

    angel "Now, you two got your wish granted."

    angel "gtfo of here"

    "*snaps*"

    stop music fadeout 3.0

    with Shake((0, 0, 0, 0), 3.0, dist=15)

    "..."

    scene aa ffa

    with wipedown

    voice "voice/aoba/110.ogg"
    "AAAAAAHHHHHHHHHHHHH"

    scene aoffy fish

    with wipedown

    play music "audio/bgm/M12.opus" fadein 1.8

    aoffy "I hope I get big fish this time!"


    voice "voice/aoba/110.ogg"
    "AAAAAAHHHHHHHHHHHHH!!!"

    stop music fadeout 3.0

    scene aoffy fish huh

    with dissolve

    aoffy "..."

    scene aoffy fish wtf

    play music "audio/Interesting People.mp3" fadein 1.75

    with hpunch

    aoffy "!!!"

    aoffy "What the fuck!?"

    scene aaa get up

    with irisin

    voice "voice/aoba/44.ogg"
    aoba "..."

    apple "..."

    aoffy "..."

    "..."

    aoffy "HOW?"

    scene aoffy wtf

    with dissolve

    aoffy "WHERE THE HELL DID YOU COME FROM?"

    voice "voice/aoba/45.ogg"
    aoba "I..."

    scene apple ok retard

    with vpunch

    apple "My mom!"

    voice "voice/aoba/46.ogg"
    aoba "..."

    scene aoffy ok retard

    with dissolve

    aoffy "..."

    aoffy "ok retard"

    scene aaa get up

    with dissolve

    voice "voice/aoba/47.ogg"
    aoba "It's quite a long story... let's talk inside"

    scene meanwhile

    with dissolve

    pause 1

    play music "audio/Trial(AA).mp3" fadein 1.4

    scene aaa kitchen

    with fade

    apple "... and then we fell from the sky!"

    aoffy "Wow... Apple, that sounds like hella bullshit..."

    voice "voice/aoba/48.ogg"
    aoba "This is the truth son, we both spoke to an angel"

    scene aa flex

    with dissolve

    voice "voice/aoba/49.ogg"
    aoba "The Angel actually gave us what we wished for!"

    voice "voice/aoba/50.ogg"
    aoba "I got an anticheat and..."

    apple "Ya! and I got this awesome cat!"

    scene aoffy big brain

    with dissolve

    aoffy "Uh... well..."

    aoffy "I mean... this story isn't believable at all!"

    aoffy "Apple, you know that you can just find a stray cat out in the street easily"

    aoffy "and mom, I know that you can develop an anti-cheat with ease"

    scene aa unamused

    with dissolve

    stop music fadeout 1.666

    apple "B- But..."

    play music "audio/bgm/M09.opus" fadein 1.8

    voice "voice/aoba/51.ogg"
    aoba "It's okay..."

    voice "voice/aoba/52.ogg"
    aoba "You don't have to believe us."

    voice "voice/aoba/53.ogg"
    aoba "I gotta get back to coding"

    scene aoba lbye

    with dissolve

    apple "..."

    aoffy "..."

    scene aoba im back

    with dissolve

    voice "voice/aoba/54.ogg"
    aoba "..."

    scene aoba hi pc

    with dissolve

    voice "voice/aoba/55.ogg"
    aoba "This is me..."

    voice "voice/aoba/56.ogg"
    aoba "I am..."

    voice "voice/aoba/57.ogg"
    aoba "Aoba..."

    scene aoba anti hq

    with dissolve

    "After 10 years of development..."

    "I couldn't find the perfect anti-cheat against the HQ"

    "But today..."

    "is the day..."

    "Where I use what god gave me..."

    "an opportunity..."

    "a way to change my osu! career..."

    "Forever..."

    stop music fadeout 2.0

    scene end

    with dissolve

    pause 3

    ".:. End."

    # This ends the game.

    stop music fadeout 2.0

    scene black

    with fade

    return

label ch0_kill:
    "..."
    "..."
    "W-What..."
    "..."
    "This..."
    "What is this...?"
    "Oh no..."
    "No..."
    "This can't be it."
    "This can't be all there is."
    "What is this?"
    "What am I?"
    "Make it stop!"
    "PLEASE MAKE IT STOP!"
    $ delete_character("aoba")
    $ delete_character("akinya")
    $ delete_character("aoffy")
    $ delete_character("apple")
    $ delete_character("angel")
    $ delete_character("simon")
    $ delete_character("jerry")
    $ delete_character("cashier")
    $ renpy.quit()
    return