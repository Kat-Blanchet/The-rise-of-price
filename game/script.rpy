# The game starts here.
label splashscreen:
    scene black
    pause(0.5)
    scene splashy with dissolve
    pause(4)  #length of above movie
    scene black with dissolve
    return


label start:   
    stop music fadeout 0.5

    show text "This is a work of fiction. Names, characters, events and incidents are the products of the authors imagination. Any resemblance to actual persons, living or dead, or actual events is purely coincidental."
    with Pause(5)
    hide text


    menu :
        "Do you agree with the term of this game"
        "I do agree":
            show text 'Very well, then let me introduce you to the character you need to know for now' 
            with Pause(5)
            jump part_1
        "I don't agree":
            show text "Very well, this means I can't let you take part in this game"
            with Pause(5)
    return

# TODO finish the first part of the story 
label part_1:


    play music "audio/oji.mp3" fadein 0.6
    scene expression "gui/game_menu.png"
    show Past_Kat
    N 'First, there is Kat a 17 years old male at the time with a very dark past keeps to him self'
    hide Past_Kat
    show Past_Kai
    N 'Next theres Kai 15 year of age at this time but is a shy and young individual that looks up to kat since a young age ' 
    hide Past_Kai

    N "let's go to where this story all started to the small town of Port Cinnabar"

    scene port_cinabar_kat_house 
    show Past_Kat at smidge_left
    show Past_Kai at smide_right
    

    

