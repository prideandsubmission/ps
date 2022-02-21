


label sim2:
    $ showday = True
    $ goodend_announce = False
    show sit_tight with fade
    "[p] has started to develop feelings for you."
    "Earn his trust and love with 'Talk Options' to him to achieve the 'Good End'. You will receive a 'notification' once you receive it."
    "'Bad End' unlocked. Please choose 'Alteration' if you wish to proceed with that route."
    "'Bad End' will contain 'amputee' (no limbs), 'scat', 'bestiality'. There will be an 'option' to 'skip scat/amputee scenes' in the future, but not currently."
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
        "Good end unlocked. Please choose 'Alteration' to proceed."
        $ goodend_announce = True
    elif food <=50:
        jump askFeed
    elif water <=50:
        jump askWater
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
                        hide screen sit_up_screen
                        if ene <= 0:
                            jump endday2
                        elif water >101:
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_m
                            d "Want some water?"
                            scene darkforest2
                            show m
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m_open_speak
                            p "I-I'm not thirsty."
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            p "..."
                        else:
                            $goodend +=1
                            $ene -= 10
                            $water += 50
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            d "Thirsty yet?"
                            hide m_m
                            show m_m_open_speak
                            p "N-not yet"
                            hide m_m_open_speak
                            show m_m
                            d "You look dehydrated though."
                            scene darkforest2
                            show m
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m_open2
                            p "..."
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            "[d] hands [p] water, [p] hesitate then drinks it"
                            hide m_m
                            show m_m_open_speak
                            p "Thank you"
                            hide m_m_open_speak
                            show m_m_normal
                            "[p] returns the water skin to [d], [d] holds it including [p]'s fingers"
                            scene darkforest2
                            show m
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m_open2
                            p "..."
                            d "Do you still need more?"
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m_open_speak
                            p "N-No. Sorry."
                            hide m_m_open_speak
                            show m_m_normal
                            "[p] retreats his hand and sighs."
                            scene darkforest2
                            show m_close
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m_open_speak
                            p "..."
                            jump simbutton2
                    "Feed":
                        hide screen sit_up_screen
                        if ene <= 0:
                            jump endday2
                        elif food >101:
                            scene darkforest2
                            show m_tire0
                            show m_cockdown
                            show m_shame
                            show m_m
                            d "Want some food?"
                            scene darkforest2
                            show m
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m_open_speak
                            p "..."
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            p "Not now"
                            scene darkforest2
                            show m_close
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            d "Ok"
                        else:
                            $goodend +=1
                            $ene -= 10
                            $food += 50
                            scene darkforest2
                            show m
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            d "Are you hungry?"
                            scene darkforest2
                            show m_tired
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            p "Yes"
                            "[d] gives [p] food. [p] looks at [d] then eats it"
                            scene darkforest2
                            show m_close
                            show m_cockdown
                            show m_shame
                            show m_blush
                            show m_m
                            d "..."
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
                jump alteration

            "Let [p] rest":
                jump endday2
