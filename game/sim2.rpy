


label sim2:
    $ showday = True
    $ goodend_announce = False
    show sit_tight with fade
    "[p] had started to have feeling for you. Earn his trust and love to have vanilla good end. There'll be a notification when you get it." 
    "You can click Brain alteration to go to bad end right away. It'll have gore, scat, bestiality"
    "(Touch [p] to continue.)"
    call screen sit

screen sit:
    imagemap:
        ground "sit_alt"
        hover "sit_sad"
        hotspot (0, 100, 550, 1000) action Function(renpy.transition, dissolve), Call ("simbutton2")
##default tt= Tooltip("[p] feels uncomfortable. Better not touch him")

screen sit_up_screen:
    imagemap:
        ground "sit_up"
        hover "sit_sad_hover"
        hotspot (0, 100, 500, 1000) clicked Jump("clickRay")

    text ("Day %d" %day): 
        xpos 5
        ypos 20
        font "Benegraphic.ttf"

    text ("Energy: %d" % ene): 
        xpos 10
        ypos 100 

    text ("Water: %d" % water): 
        xpos 10
        ypos 150
     
    text ("Food: %d" % food): 
        xpos 10
        ypos 200 
       
    text ("Pride: %d" % pride): 
        xpos 10
        ypos 250 
       
    text ("Mental: %d" % mental): 
        xpos 10
        ypos 300 
    
    text ("Cleaniness: %d" % clean): 
        xpos 10
        ypos 350 

label clickRay:
    hide screen sit_up_screen
    scene sit_sad
    if talk >=18:
        show sit-sad-blush with dissolve
    p"..."
    "[p] feels uncomfortable. Better not touch him more."
    jump simbutton2

label simbutton2:
    show screen sit_up_screen
    if ene <=0:
        jump endday2
    elif goodend_announce==False and talk >=20:
        "Good end unlocked."
        $ goodend_announce = True
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
                            jump endday2
                        elif water >120:
                            d "Want some water?"
                            p "I-I'm not thirsty."
                        elif water <= 50:
                            p "[d]"
                            d "What?"
                            p "..."
                            p "Can I have some water?"
                            "[d] gives [p] some."
                            p "T-thanks"
                            $water += 50
                        else:
                            $goodend +=1
                            $ene -= 10
                            $water += 50
                            "Working on it"
                            jump simbutton2
                    "Feed":
                        if ene <= 0:
                            jump endday2 
                        elif food >120:
                            d "Want some water?"
                            p "I-I'm not thirsty."
                        elif food <= 50:
                            p "[d]"
                            d "What?"
                            p "..."
                            p "Can I have some water?"
                            "[d] gives [p] some."
                            p "T-thanks"
                            $food += 50
                        else:
                            $goodend +=1
                            $ene -= 10
                            $food += 50
                            "Working on it"
                            jump simbutton2
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
                
   
                
            