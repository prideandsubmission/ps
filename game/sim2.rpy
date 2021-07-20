
label sim2:
    $ showday = True
    show sit_tight with fade
    "(Touch [p] to continue.)"
    call screen sit

screen sit:
    imagemap:
        ground "sit_alt"
        hover "sit_sad"
        hotspot (0, 100, 600, 1000) action Function(renpy.transition, dissolve), Call ("simbutton2")

default tt= Tooltip("[p] feels uncomfortable.")

screen sit_up:
    imagemap:
        ground "sit_up"
        hover "sit_sad_hover"
        hotspot (0, 100, 720, 1000) clicked Jump("clickRay")

label clickRay:
    hide screen sit_up
    scene sit_sad
    p"..."
    "[p] feels uncomfortable."
    jump simbutton2
    
label simbutton2:
    show screen sit_up
    show screen day
    show screen stat

    if ene <=0:
        jump endday
    elif water<=0 or food <=0:
        jump faint
    elif clean<=0:
        jump bath
    else:
        menu:
            "Water and Feed":
                menu:
                    "Water":
                        if ene <= 0:
                            jump endday
                        else:
                            $goodend +=1
                            "Working on it"
                    "Feed":
                        if ene <= 0:
                            jump endday
                        else:
                            $goodend +=1
                            "Working on it"
                    "Return":
                        jump simbutton2
            "Humiliation":
                menu:
                    "Tease":
                        if ene <=0:
                            jump endday
                        else:                           
                            #jump touch_obe
                            "Working on it"
        
                    "Toy":
                        if ene <=0:
                            jump endday
                        else:
                            #jump toy_thurst
                            "Working on it"
                    "Dog Sex" if dogtraining:
                        jump dogtraining
                        #jump simbutton2
                        "Working on it"
                    "Return":
                        jump simbutton2   
            "Sex":
                menu:
                    "Oral":
                        if ene <=0:
                            jump endday
                        else:
                            $goodend +=1
                            #jump cock_obe
                            "Working on it"
                    "Anal":
                        if ene <=0:
                            jump endday
                        else:
                            $goodend +=1
                            #jump ass_obe 
                            "Working on it"                          
                    "Group Sex":
                        jump group2
                        
                    "Return":
                        jump simbutton2

            "Brain alteration":
                    jump control4_ques
                
            "Let [p] rest":
                jump endday
            "Sleep with [p]":
                $goodend +=1
                "Working on it"
                
   
                
            