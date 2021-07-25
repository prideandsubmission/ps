

label sim2:
    $ showday = True
    show sit_tight with fade
    "[p] had started to have feeling for you. Earn his trust and love to have vanilla good end. There'll be a notification when you get it." 
    "You can click Brain alteration to go to bad end right away. It'll have gore, scat, bestiality"
    "(Touch [p] to continue.)"
    call screen sit

screen sit:
    imagemap:
        ground "sit_alt"
        hover "sit_sad"
        hotspot (0, 100, 600, 1000) action Function(renpy.transition, dissolve), Call ("simbutton2")

##default tt= Tooltip("[p] feels uncomfortable. Better not touch him")

screen sit_up_screen:
    imagemap:
        ground "sit_up"
        hover "sit_sad_hover"
        hotspot (0, 100, 720, 1000) clicked Jump("clickRay")

label clickRay:
    hide screen sit_up_screen
    scene sit_sad
    if talk >=18:
        show sit-sad-blush with dissolve
    p"..."
    "[p] feels uncomfortable. Better not touch him more."
    jump simbutton2


label simbutton2:
    show screen sit_up_screen with dissolve
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
            "Talk":
                hide screen sit_up_screen
                $goodend +=1
                $talk += 1
                $ene -=5
                if talk <= 2:
                    jump talk1
                elif talk >2 and talk <6:
                    jump talk2 
                elif talk >=6 and talk <8:
                    jump talk3
                elif talk >=8 and talk <10:
                    jump talk4
                elif talk >=10 and talk <12:
                    jump talk5
                elif talk >=12 and talk <14:
                    jump talk6
                elif talk >=14 and talk <16:
                    jump talk7
                elif talk >=16 and talk <18:
                    jump talk8
                elif talk ==18:
                    jump talk9
                else:
                    jump talk7
                
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
            # "Sex":
            #     menu:
            #         "Oral":
            #             if ene <=0:
            #                 jump endday
            #             else:
            #                 $goodend +=1
            #                 #mostly refuse
            #                 "Working on it"
            #         "Anal":
            #             if ene <=0:
            #                 jump endday
            #             else:
            #                 $goodend +=1
            #                 #mostly refuse
            #                 "Working on it"                          
            #         "Group Sex":
            #             # Ray never agrees
            #             jump group2
                        
            #         "Return":
            #             jump simbutton2

            "Alteration":
                jump control4_ques
                
            "Let [p] rest":
                jump endday2
                
   
                
            