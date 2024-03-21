# The game starts here.
label start:   
    stop music fadeout 0.5

    S "This is a work of fiction. Names, characters, events and incidents are the products of the authors imagination. 
    Any resemblance to actual persons, living or dead, or actual events is purely coincidental."

    menu :
        "Do you agree with the term of this game"
        "I do agree":
            N 'Very well, then let me introduce you to the character you need to know for now' 
            jump part_1
        "I don't agree":
            N "Very well, this means I can't let you take part in this game"
    return

# TODO finish the first part of the story 
label part_1:

    play music "audio/oji.mp3"
    show Past_Kat
    N 'First, Kat Age: 17 (at this time) Birthday: March 21st origens'
    hide Past_Kat
   
    show Past_Kai
    N 'second Kai Age: 15 (At this time)' 
    hide Past_Kai

    N "let's go back to the past before the uprising of a new prince in the small town of Port Cinibar"

    scene port_cinabar_kat_house 
    show Past_Kat at smidge_left
    show Past_Kai at smide_right
    pk "Hey Kai, question for you?"
    pk2 "Yeah what's  on your mind Kat?"
    pk "Where do you think we will end up in I don't know say two years\nwhen we can leave this hole and go to vermilion"
    pk2 "Wait did we agree to leave cinabar to go to the other port"
    pk "yeah you, me and him"
    pk2 "what ever happend to him any way it just like one day he was just gone missing"
    pk "you think know where the hell he is kai I know i have some insane powers but not that one"
    pk2 "so about leaving cinibar how about we just leave this place tonight"
    pk "what about your parents they already think im a bad infuence"
    pk2 "just cause you got hurt by him and now have to turn to smokes just to forgot does not mean your a bad infuence to me"
    pk "do you forget how old i am kai im 17 you think i can up and leave what about the life i wanted "
    

    

