# The script of the game goes in this file. /D/PROGRAM/RENPY/renpy-6.99.14-sdk/PriceAndSub

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define p = Character("Prince")
define n = Character("Nine")
define m = Character("Monster")
define k = Character("King Raphael")
define h = Character("A Random Human")
define ri = Character("Rivakh")
define ren = Character("Ren")
default showday = False
default show = False
default firstwater = True # if this is the first time water                  country name:   Rivakh
default firsttime = True # if this is the first time Anal
default firstMos = 0 # BATH Mosquito monsters meeting, =0 at first
default bath_just_enough = False # BATH wrech him enough 
default toyfirst = True # if this is the first time with Sword
default group_baby = False
default group_nobaby = False
default touchfirstnone = True # if this is the first time Tease him
default touchnone = True
default control3first = True
default control4first = True
default slaveannounce = False
default dogtraining = False
default slavemarket = 0
init python:
    showday= False
    day = 1
    def display_day():
        if showday:
            ui.frame(background= "frame.png",xpos= 500, ypos= 50, xsize= 579, ysize= 130, left_padding= 20)
            ui.text("$ %d" %day, xalign= 0.5, yalign= 0.5, xoffset= 2, yoffset= 8)
            config.overlay_functions.append(display_day)
  
transform s:
    zoom 0.8
    ypos 600
    xpos -180
label start:
    scene black
    "Are you a new or old player?"
    $d = "Dietrich"
    $p = "Ray"
    jump control4_ques
    menu:
        "New":
            "Welcome and enjoy the game!"
        "Old":
            "Where do you want to skip to?"
            menu:
                "The sim":
                    $p = renpy.input("Your name is...(press enter to use the default name)", "Ray", length=20)
                    $d = renpy.input("The monster's name is...(press enter to use the default name)", "Dietrick", length=20)
                    $water =30
                    $food =40
                    $ene =100
                    $nothing =1
                    $mental = 90
                    $pride = 90
                    $day = 4
                    $fuckoff =0
                    $clean = 90
                    play music "Angevin.mp3"
                    jump sim
                "End of the sim":
                    $p = renpy.input("Your name is...(press enter to use the default name)", "Ray", length=20)
                    $d = renpy.input("The monster's name is...(press enter to use the default name)", "Dietrick", length=20)
                    $water =90
                    $firstwater = False
                    $food =90
                    $ene =100
                    $nothing =1
                    $mental = 0
                    $pride = 0
                    $day = 50
                    $clean = 40
                    $group_baby = True
                    play music "Angevin.mp3"
                    jump sim
                "No skiping":
                    "Please continue the game."
    
    play music "Thaxted.mp3" fadeout 3.0
    scene cg1

    "Once upon a time, there was a young boy.\nThis youth was far more serious than all the other his age. \nWhatever he does, he always succeeds. \nWhatever he wants, he always gets." 
    "When he enrolled in the army, everyone opposed his decision due to his age, but he was having none of that—he does as he pleases." 
    "After demonstrated his skill, he immediately silenced his opposition. Years later, at the tender age of twenty, he became a general and was known as one of the strongest men alive in Rivakh."
    "He and the king rarely talk to each other. \nAnd if they do, it usually becomes a big fight, resulting in him being thrown out. \nIt is shocking to see, but not surprising that he is the king’s son, the first heir."
    "Unlike his younger half-brother, who is always smiling and loved by everyone, this prince is either feared or hated."
    "Arrogant, stubborn, unpleasant, suspicious, demanding, repulsive, quick-tempered. \nThat’s how everyone describes him... \n..No wonder, despite his capability, the king chose Ren, the younger brother to be the next king."
    
    scene cg2
    "\"You want this dumbass to succeed you because you want a puppet!” the rejected prince shouted angrily, his voice echoing in the throne room"
    "“Don’t you dare speak like that to your future king! Ren can have you executed should he choose so!” the king retorted" 
    "\"Dad, brother, please stop it you two.\" Ren jumps in between them."
    "The room becomes noisy. Some start to laugh.\"SILENCE!\" the prince shouts.\nThe king slaps his face. \"Who gave you that authority? Disrespectful brat!\"" with hpunch
    "The prince glances at the king and slaps him. \nThe king falls to the floor. Soldiers surround the prince." with vpunch
    "\"Good one! From now on, you are not my son anymore. Don’t ever come back to this palace.\" he king points at him."
    "The prince turns and goes out \"One day you will regret this.\"\n ... \nHe takes one last look at the throne room and sees a lot of happy smiles. The prince clenches his fist."
    stop music
    play music "Angevin.mp3" fadeout 3.0
    scene darkforest_night 
    "A few days later, he arrived at the entrance of the Dark Forest, the most fearsome place known to man. \nLegend says this is the place God hid the First Stone with the quote \"This stone will give its owner the power to bend The Flow and destroy the laws of current Universe.\""
    show m_armor at left
    p "Despite being a legend, many rulers have sent troops here to look for it. Even now, there are many that lose their lives here."
    "The prince laughs"
    p "Those useless fools cannot even go deep inside."
    "He entered the forest and immediately encountered many monsters, but he slayed them with little difficulty." 
    p "These monsters are strong, but not as strong as I though. Is this really the most dangerous place in the world?"
    "Suddenly, a small demon appeared in front of him."
    show n at right with dissolve
    p "A demon? In the far depths of the Dark Forest? How could someone as weak as you survive here?"
    $n ="Demon"
    hide n
    show n_smile at right
    n "Human, this is a friendly warning. If you go further, there’s no return."
    p "What I hate most is being told what to do."
    hide n_smile
    show n at right
    n ".... \n Ok"
    "The prince suspected the demon may have information about the First Stone."
    menu:
        "Ask him":
            p "Wait demon!"
            hide n
            show n_smile at right
            n "What?"
            p "Do you know anything about the First Stone?"
            hide n_smile
            show n_smile2 at right
            n "So you are also seeking it."
            p "..."
            hide n_smile2 with dissolve
            show n2 with dissolve
            "The demon whispers to the prince."
            n"In the middle of a giant river lies the Water Temple which holds the first stone..."
            p"Everyone knows that."
            hide n2
            show n_surprise2
            n"You mean all the human authority?"
            p ".."
            hide n_surprise2
            show n_smile2
            n "There is but one big river in this forest. However, you cannot ..."
            p "..."
            "The prince moved past the demon."
            hide n_smile2 with dissolve
            p "\(That's good, I just need to find 1 river.\)"
            "Two hours later, the prince was still nowhere near to finding the First Stone. All he could see were trees and more trees."
            p "I should be getting close to the river."
        "Ignore him":
            
            p "\(I doubt this weak demon knows anything.\)"
            "The prince walks foward."
            p "..."
            menu:
                "Show him the way out":
                    $ show = True
                    "The prince turned back and pointed at where he came from."
                    hide n
                    show n2 at right
                    n "What is it?"
                    p "That’s the way out!"
                    hide n2 with dissolve
                    "The prince made his way further into the forest."
                    "Two hours later, the prince was still nowhere near to finding the First Stone. All he could see were trees and more trees."
                    p "Legend said there is a mysterious temple in the middle of a river here. The First Stone was hid in that place. At this rate, sooner or later, that stone is mine."
                    
                "Nevermind":
                    hide n with dissolve
                    "The prince made his way further into the forest."
                    "Two hours later, the prince was still nowhere near to finding the First Stone. All he could see were trees and more trees."
                    p "Legend said there is a mysterious temple in the middle of a river here. The First Stone was hid in that place. At this rate, sooner or later, that stone is mine."
            
    "Suddenly, there is a girl’s scream. \"HELP! SOMEONE! PLEASE HELP ME!!\""
    menu:
        "Go take a look":
            "The prince follows the scream and sees five monsters fucking a monster girl."
            m "Oh, it’s a human. Human. HUMAN!" with hpunch
            "The monsters attack him. \nThese monsters are stronger than the monsters he faced before. \nBut he is still stronger than them. " with vpunch
            "Monster girl \"Thank you very much!\""
            "The girl suddenly attacks him. He evades and slashes her." with hpunch
            p "Like I couldn’t figure out it would turn out like this."
            m "Retard, you just disrupted my show!"
            p "What now?"
            p "\(Why are there so many monsters here?\)"
            "The prince turns his head to see a normal sized monster. \nHis aura is even weaker than the small demon he just met. \nSo weak that he cannot even feel his presence."
            p "Normally, I don’t beat weaklings, but your tone is annoying for a fly."
            m "Annoying? Me?"
            p "Either run or bow down and beg now if you don’t want to be tortured to death."
            m "Wow, sir, I’m so scared. Can you show mercy on me?"
            "Like lighting, the prince slashes the monster. When the monster falls to the ground, he kicks its wound rapidly and steps on its face." with vpunch
            p "You come at a good time. I'm so irritating right now. Just considered yourself unlucky." with hpunch
            m "Why is that?"
            "The prince stabs the monster’s hand, blood spews out. He laughs." with vpunch
            p "Only a miracle can save you now. But you won't die so soon. Not after I satisfy."
            d "Ouch!"
            p "Beg me more!"
            "The monste smirks."
            d "I didn't know a Royal palace hire a thug for general positions. Had human become that rotten?"
            "[p] was pause for a second, then he laughs."
            p "Ha...Hahaha..."
            "[p] brutally stabs [d]. He would twisted his sword before pulls it out and stabs at other places." with hpunch
            d "M...N..."
            "The monster doesn't move or say anything."
            p "Dammit. Why it still haven't die. It is as if it challenge me."
            "The prince furious."

        "Ignore":
            "The prince continues to drink water. Fifteen minutes later, the screaming still continues."
            m "Argh.. Help!" 
            p "So noisy!" 
            "The prince feels like he is being watched." 
            p"Who’s there?"
            "A monster walks out."
            m "You’re not gonna help her? I thought humans are all about morals." 
            "His voice is full of sarcasm." 
            p "Get out of my sight." 
            "The monster draws close to him. \nThe prince didn’t move. \nThis monster’s aura is even weaker than the small demon."
            m "What makes a human come to this place alone?" 
            p "Go away before I kill you."
            "The monster holds and looks at his sword"
            "This is a good one."         
            p "(since when?)\nThe prince takes his sword back and slashes the monster.\n The monster falls to the ground, covered in blood." with vpunch
            p "Normally, I don’t beat weaklings, but you are annoying"
            m"Me? Annoying?"
            "The monster laughs"
            m"No one’s ever spoken to me like that before."
            p"Either run or bow down and beg now if you don’t want to be beat to death."
            m"Sir, I’ve just being slashed. I cant run or bow down now. Can I beg you instead?"
            "The prince kicks the monster’s wound repeatedly and steps on its face." with hpunch
            p"Even a loser like you making fun of me. Do I look like a joke? Beg me! BEG!" with vpunch
            m"Please let me go!"
            "The prince stabs the monster’s hand, blood spews out. He laughs" with vpunch
            p "More!"
            "He wrenches on the sword." with hpunch
            m "Ouch. Dear human, please let this lowly monster go! It hurts so much!"
            p "Shut up! Stop that sarcastic tone!"
            "The prince beats the monster more brutally!" with vpunch
            
    p "Fuck! You damn monster! YOu think I'm a joke too aren't you?"
    "[p] looks at the monster wounds from head to toe."
    p"Seriously? Do monster always like this? Geting hard while being beaten to death? \nSuch a disgusting race!"       
    m "Haha...You really don't know why it hard like that? It's because..."
    p "What?" 
    "The monster talks so small that [p] cannot hear. He smiles at [p] as if he want [p] to bend over and listen."
    p "..."
    "[p] grasps his sword hard, bends over to hear what the monster had to say."
    "The monster whisper."
    ## Dunno if I should put it here. Spoil too much
    d "I'm hard because...of you. I want to fuck you senselessly till your brain fall out."
    p "!"
    "Too suprise, [p] pauses for a second then stands up and steps backward. The monster stands up. His wounds were healed."
    p "He ... heals himself?"
    p "!" with hpunch
    "The vines in the forest suddenly start moving. They grab ahold of the prince." with vpunch
    hide m_armor
    show vine at left with dissolve 
    "The thought of making you lie on the ground, suffering while being tortured makes me hard."
    p "You sick bastard!"
    hide vine with dissolve
    show vinek at left with flash
    "TThe prince uses his dagger to swiftly cut the vines. He quickly picks up his sword and stabs the monster in a swift motion" with hpunch
    p "Ha!" with vpunch
    "The monster disappeared. The very earth itself rises up to form a hand, slamming down his whole body." with hpunch
    hide vinek
    show m_break2 at left
    p "Urgh!" with vpunch
    "The prince grows furious. \nHe concentrates his power on the tip of his sword and slashes though the hand." with vpunch
    "From behind, the vine attacks him and swaps him tightly. " with hpunch
    hide m_break1
    hide m_break2
    hide m_break3
    show vinebeat at left with flash
    p "Argh!"
    m "You’re not so smart are you?"
    hide vinebeat
    show vinebeatfast at left
    "The vines wrap him tighter." with vpunch
    p "ugh" 
    p "I warn you! Let me go!" 
    m "Beg me." 
    hide vinebeatfast with dissolve
    show vinebreak2 at left with flash
    "The prince creates a barrier to destroy the vines. \n He falls to the ground in exhaustion."
    hide vinebreak2
    show m_break1 at left
    show m_beaten4 at left
    "The monsters kicks his stomach." with hpunch
    hide m_break2
    hide m_break4
    show m_break5 at left
    p "Arggghhh!...Ahhhh!"
    p "uhmmm..."
    "he monster cruelly stomps on it"
    p "Urgh!"
    hide m_break5
    hide m_beaten4
    show trample 
    "Poor thing, you muuussst have been hurt a lot. Let me caress you"
    "The monster presses his foot on the prince’s private area."
    show m_break4:
        zoom 0.8
        ypos 600
        xpos -200
    show m_beaten4:
        zoom 0.8
        ypos 600
        xpos -200
    p "Get your foot off of me you fucking monster!!"
    hide m_break4
    hide m_beaten4
    "The monster stomps on his cock brutally." 
    hide trample
    show trample_a
    hide m_beaten4
    show m_break5:
         zoom 0.8
         ypos 600
         xpos -200
    p "Stop that!"
    hide m_break5
    m "You are so strange. You can do this to me, but I can’t do this to you? It’s unfair you know."
    "He presses harder." 
    hide trample_a
    show trample_b
    p "mmhh..haa..haa\n...\nStop..." 
    m "Shouldn't you ask more nicely?" 
    hide trample_b
    show trample_c
    "He presses harder." 
    p "P-please stop."
    m "More" 
    p"H-have some mercy!" 
    m"For who? For this arrogant dumbass?" 
    p "for th – this… arroga.." 
    "The prince clenches his teeth, swallows the words"
    hide trample_c
    show trample_cum
    "The monster presses even harder" 
    p "ahaahh"
    p "urgh...ahhh"
    m "Wow, what youth! Seems like humans can even cum from pain."
    p "..."
    p "hhh"
    m "What's your name brat?"
    p "..."
    hide trample_cum
    show trample_mouth
    "The monster moves his foot from the prince's cock to his face."
    hide trample_mouth
    show trample_moutha
    p "n.."
    m "Wanna play the silent game? It won't end pretty for you."
    
    hide trample_moutha
    show trample_a
    p "....n....n..ahaaa...haa"
    p "...m...Try...me!"
    "The monster laughs."
    hide trample_a
    show trample_cum
    m "Heh. \nYou even dare to provoke me in this situation? \nI admire your stupidity, sir knight." 
    "Like an explosion, the monster's foot crashes into his head. \nHis helmet was badly damaged." with hpunch
    p "urgh....\n....n..."
    hide trample_cum
    hide m_break1
    hide m_break2
    hide m_break3
    hide m_break4
    show m_break5:
        zoom 0.8
        ypos 600
        xpos -200
        
    p "....F-fuc-k..."
    "The prince tries to get up. \nThe monster tramples his face."
    hide m_break5
    show trample_moutha
    p "Urgh!"
    "The prince struggles."
    m "You are hurting yourself. Your helmet is in the way." with vpunch
    "The monster throws his helmet away."  with hpunch
    p "NO! DON'T!" with flash
    hide trample_moutha
    hide trample_cum
    show m_head_tired at left
    show m_m_sexclench1 at left
    show m_beaten3 at left
    show m_blush at left with flash
    p "..."
    m "Why did you want to keep it? To hide yourself in there?"
    p "Bastard!"
    m "It must be shameful for a knight to get his balls crushed."
    hide m_head_tired
    hide m_m_sexclench1
    hide m_beaten3
    hide m_blush
    show m_head_close at left
    show m_m_clench at left
    show m_beaten3 at left
    show m_shame at left
    p "..."
    "The monster touches his face"
    m "Not a bad face. Looks like an arrogant brat but not bad at all."
    hide m_head_close
    hide m_m_clenth
    hide m_beaten3
    hide m_shame
    show m_head_surprise at left    
    show m_m_sexclench2 at left
    show m_beaten3 at left
    show m_blush at left
    
    p "(Fuck this monster!)\n(Just wait till I get my strength back)"
    m"What is your name kid?" 
    hide m_head_surprise
    hide m_m_sexclench2
    hide  m_blush
    hide m_beaten3
    hide m_m_clench
    show m_head_close at left
    show m_m_clench at left
    show m_beaten3 at left
    p "..."
    "The prince stays silent."
    "The monster pulls his head"
    show pull_armor
    p "arghhh!" 
    m "What is your name?" 
    p"..." 
    hide m_head_close
    hide m_m_clench
    hide m_beaten3
    hide pull_armor
    show pull_armor_hard
    "The monster pulls his hair roughly"
    p "Ahhh..ahh..ahh"
    m "Talk!"
    menu:
        "Say it":
            $p = renpy.input("press enter to use the default name)", "Ray", length=20)
            p "[p]!...[p]!"
            hide pull_armor_hard
            "The monster releases him. [p] falls to the ground."
            show m_head_hurt at left
            m "See? It wasn't that hard."
            m "Hmm... your name sounds familiar, and your sword and armor show you are a high ranking general of the Royal Army. [p], [p]. I’ll find out about that."
        "Stay silent":
            m "You are a stubborn one aren’t you."
            hide pull_armor_hard
            show m_head_hurt at left
            "The monster releases him. The prince falls to the ground."
            m "You see..." 
            show m_head_hurt2 at left
            "The monster kicks him brutally." with vpunch
            p "argh...argh..ahhh"
            hide m_head_hurt2
            m "I’m pretty stubborn too. I can beat you all day and night till you do what I tell you."
            "He pulls the prince's head up."
            show pull_armor_hard
            p "urg...aghh..."
            m "I’ll ask you again, what’s your name?"
            $p = renpy.input("(press enter to use the default name)", "Ray", length=20)
            p "[p]! ..m.ngh.. [p]!"
            hide pull_armor_hard
            hide m_head_hurt
            show m_head_close at left
            show m_beaten6 at left
            show m_shame at left
            show m_m_sexopen at left
            m "[p]. Good boy! See? It wasn’t that hard."    
            m "Hmm... your name sounds familiar. Plus, your sword and armor show you are a high rank general of the Royal Army. [p], [p]. I’ll find out about that."
            
    $d = renpy.input("I'm...(press enter to use the default name)", "Dietrick", length=20)
    d "I'm [d]. The oldest monster in this forest. \nNice to meet you."
    hide m_head_close
    hide m_beaten6
    hide m_shame
    hide m_m_clench
    show m_head_tired at left
    show m_beaten6 at left
    show m_m_sexclench1 at left
    p "..." 
    d "Shouldn’t you say \"Nice to meet you too, [p]?" 
    "The prince clenches his hands and teeth."
    hide m_head_tired
    hide m_beaten6
    hide m_m_sexclench1
    show m_head_close at left
    show m_beaten6 at left
    show m_shame at left
    show m_m_sexclench2 at left
    p "Nice to meet you too."
    "[d] laughs."
    m "You have good manners, [p]."     
    "The monster goes away."
    hide m_head_close
    hide m_beaten6
    hide m_m_sexclentc2
    show m_head_hurt at left
    show m_beaten6 at left
    "[p] tries to get up but he can’t. He was beaten up so badly. \nNever in his life had he been though a shameful situation as this. \nHe wants to cut that monster into a thousand pieces and burn what’s left."
    hide m_head_hurt
    hide m_beaten6
    show m_head_surprise at left
    show m_m_sexclench1 at left
    show m_beaten6 at left
    p "..m..fuck!!"
    n "See, I told you." 
    hide m_head_surprise
    hide m_m_sexclench1
    hide m_beaten6
    show m_head at left
    show m_m at left
    show m_beaten6 at left
    show n_smile at right with dissolve
    "The demon boy appears." 
    if show:
        hide m_surprise
        hide m_m_clench
        hide m_m
        hide m_beaten6
        show m_head_close at left
        show m_m at left 
        show m_beaten6 at left
        p "You...you haven't...get out of here"
        n "Why? This is my home"
        hide m_head_close
        show m_head at left
    "[p] looks away"
    p "You gonna laugh at me now?"
    hide n_smile
    hide m_m_clench
    show n at right
    n "You are not asking for my help?"
    hide m_m
    show m_m_clench at left
    p "Fuck you! Don't joke with me!" 
    "Ray feels thirsty. So thirsty as if he could die. \nThe demon boy throws Ray’s backpack at him." 
    hide n
    show n_smile2 with dissolve:
        xpos 750
    n "It’s yours right? You should stay near to your belongings." 
    hide m_m_clench 
    show m_m at left
    p "..."
    n "Sir, please get out of this forest. Don't look for The Stone anymore. It's for your own good"
    p "..."
    hide n_smile2 with dissolve
    "The demon goes away." 
    hide m_m
    hide m_head
    hide m_beaten6
    show m_head_tired at left
    show m_beaten6 at left
    show m_m at left
    p "..." 
    " [p] uses his head and teeth to open his bag and drink water. A lot of the water spills out."
    hide m_m
    hide m_m_sexopen
    show m_m_sexopen at left
    show m_beaten5 at left
    p "(what a waste!)\n... \n... \n(Did that demon just help me?)." 
    "[p] falls asleep before he realizes it." 
    scene black with fade
    
    scene darkforest with dissolve
    "Morning"
    show m_head_close at left
    show m_m_clench at left
    p "Ugh!" 
    "[p] tries to get up but falls back to the ground. His entire body still trembles in pain. Especially his private part, head, and stomach"
    "Hm..." 
    hide m_head_close
    hide m_m_clench
    show m_head_surprise at left
    show m_m_sexclench1 at left
    p "Bastard!"
    d "You seem well. Better than I thought."
    "[p] glances at him." 
    p "(Why is it still here?)"
    d " Hahaha! Why look at me with those endearing eyes? In love with me?"
    hide m_m_sexclench1
    show m_m_sexclench2 at left
    p "Fucking scumbag!"
    hide m_head_surprise
    hide m_m_sexclench2
    show m_head_close at left
    show m_m at left
    "[p] goes past [d]"
    d "I heard you are a prince."
    hide m_head_close
    hide m_m
    show m_head_surprise at left
    show m_m_clench at left
    p "!"
    hide m_m_clench
    hide m_head_surprise
    show m_head at left
    show m_m_sexclench2 at left
    p "I'm not."
    d "Not anymore?"
    hide m_head
    hide m_m_sexclench2
    show m_head_surprise at left
    show m_m_sexclench1 at left
    p "!"
    hide m_head_surprise
    hide m_m_sexclench1
    show m_head at left
    show m_m_clench at left
    p "(Since when do monsters in the Dark Forest know that much about humans? Too dangerous...)"
    hide m_head
    hide m_m_clench
    show m_head_close at left
    show m_m at left
    "[p] ignores [d] and continues forward."
    hide m_head_close
    hide m_m
    show m_head at left
    show m_m at left
    d "I’m not done talking to you."
    "[p] ignores [d] completely."
    "[d] laughs."
    d "Seems like your dad’s so busy that he did a poor job raising his child."
    hide m_head
    hide m_m
    show m_head_surprise at left
    show m_m_sexclench1 at left
    "[p] turns back, glances at [d]"
    p "!" with vpunch
    hide m_m_sexclench1
    show m_m_clench at left
    p "(Something is moving..)"
    "From underground, dozen of vines wrap around [p]'s legs. He falls to the ground."
    hide m_m_clench
    show m_m_sexclench1 at left
    show m_shame at left
    p "(Shit! What the fuck?!)"
    "[p] uses all his strength to get up. His movements were too slow, the vines squeeze him."
    hide m_head_surprise
    hide m_m_sexclench1
    show vinehead:
        xpos-30
    p "Arghh!"
    d "I can help your dad with teaching you some manners..."
    hide vinehead
    show vinehead_shit2:
        xpos-50
    p "Fuck you!"
    d "...by beating you till you’re on you knees."
    hide vinehead_shit2
    hide m_shame
    show vinehead_blush:
        xpos-50
    p "You shithole!"
    d "..."
    d "Such a naughty boy, he keeps on interrupting me. Make him unable to talk!"
    "The vines squeeze stronger and tighter."
    hide vinehead_blush
    show vinehead:
        xpos-50
    p "Aaaaa! Arghhh!...m..."
    "[d] laughs"
    d "What a nice sound."
    hide vinehead
    show vinehead_shit:
        xpos-50
    p "m....h"
    hide vinehead_shit
    hide m_m_sexclench1
    show vinehead0020:
        xpos-50
    p "(Fuck!)"
    "[p] tries to release his barrier again and destroys the vines"
    d "Hahaha, idiot never learn! Up Pitchy!" with hpunch
    scene sky with dissolve
    hide vinehead
    show vinehead with dissolve:
        xpos-30 
    "The vines shoot up to the sky." with vpunch
    hide vinehead
    show vinehead_shit:
        xpos-50
    p "S-shit!"
    "A giant stone hand carries [d] to the sky."
    hide vinehead_shit
    show vinehead_shit2:
        xpos-50
    p "..."
    p "m...n.."
    d "Loosen him a bit. I want to talk."
    hide vinehead_shit2
    show vinehead_breath:
        xpos-50
    "The vines stop squeezing [p]."
    p "haaa...haaaa"
    p "What do you want?"
    "[d] licks [p]'s ear and whispers."
    hide vinehead_breath
    show vinehead_blush:
        xpos-50
    d "Let's make a deal. \nI'll help you sit on the throne you deserve. \nYou listen to what I say."
    hide vinehead_blush
    show vinehead_blush2:
        xpos-50
    p "In your dreams you lowly monster! Don't make me laugh!"
    d "Hahahahahahaha! Hahahaha!"
    d "If I'm a lowly monster, who are you sir prince?"
    "[d] tears [p]'s clothing off."
    hide vinehead_blush2 with vpunch
    show m_heavybreaksurprise at left
    show m_m_sexclench1 at left
    show m_shame at left
    show m_beaten2 at left
    p "!"
    hide m_m_sexclench1
    show m_m_sexclench2 at left
    d "Remember last night? All of your body trembled under my feet while your mouth kept begging me like a cute puppy."
    hide m_m_sexclench2
    show m_m_sexclench1 at left
    show m_blush at left
    p "I'm not..."
    hide m_blush
    hide m_m_sexclench1
    show m_m_clench at left
    d "Really?"
    "[d] touches [p]'s cock."
    hide m_heavybreaksurprise
    hide m_blush
    hide m_shame
    hide m_beaten2
    hide m_m_sexclench1
    show m_heavybreaktired at left
    show m_blush at left
    show m_m_sexclench2 at left
    show m_beaten2 at left
    p "M!"
    "[d] squeezed it harder."
    hide m_heavybreaktired
    hide m_blush
    hide m_m_sexclench3
    hide m_beaten2
    show m_heavybreakclose at left
    show m_blush at left
    show m_beaten2 at left
    show m_m_sexopen at left
    p "N!"
    d "You really turned me on that time."
    hide m_m_sexopen
    hide m_m_clench
    show m_shame at left
    show m_m_sexclench3 at left
    p "Aa....h"
    "[d] rips off [p]’s remaining clothing, leaving him completely naked." with hpunch
    hide m_m_sexclench2
    hide m_heavybreaksurprise
    hide m_heavybreakclose
    hide m_m_sexclench3
    hide m_shame
    hide m_blush
    hide m_beaten2 with hpunch
    show m_surprise at left
    show m_cockdown at left
    show m_blush at left
    show m_m_sexclench1 at left
    show m_beaten3 at left
    p "W-What are you doing?" with vpunch
    "[d] touches [p]'s stomach."
    hide m_surprise
    hide m_cockdown
    hide m_blush
    hide m_m_sexclench1
    hide m_beaten3
    show m_close at left
    show m_m_sexopen at left
    show m_shame at left
    show m_blush at left
    show m_cockdown at left
    show m_beaten3 at left
    p "H!.."
    d "Say [p], between the two of us, who is at the lower position?"
    "[p] split on [d]'s face"
    hide m_shame
    hide m_close
    hide m_blush
    hide m_cockdown
    hide m_beaten3
    hide m_sexopen
    show m_surprise at left
    show m_m_clench at left
    show m_beaten3 at left
    show m_cockdown at left
    p "Isn't it clear? A lowborn creature like you will always be beneath my ass!"
    "[d] laughs like crazy."
    d "Interesting. You are the first one who has ever said that to me. Even monsters and demons who are much much stronger than you do not dare to say that!"
    d "It's funny. But also annoying."
    "[d] pull [p]'s hair"
    hide m_m_sexclench1
    hide m_surprise
    hide m_beaten3
    hide m_cockdown
    show m at left
    show m_cockup at left
    show m_m_scream at left
    show m_beaten3 at left
    show m_shame at left
    p "Aghhh!...Ah"
    d "Who is lower, masochist brat?!"
    hide m
    hide m_cockup
    hide m_m_scream
    hide m_beaten3
    hide m_shame
    hide m_m_sexopen
    show m_hurt at left
    show m_m_sexopen at left
    show m_beaten3 at left
    show m_cockup at left
    show m_shame at left
    show m_blush at left
    p "Agh...F-Fuck!..Aghhh!...You!...Agh!"
    "[d]'s eyes turn red!"
    hide m_m_sexopen
    hide m_shame
    show m_shame at left
    show m_m_sexclench3 at left
    p "...m...Fuck you!"
    d "..."
    d "(I cannot control his mind. This is rare. If he had a holy soul, it would be easy to understand. But he is completely the opposite...)"
    d "(I see... This guy has a really strong will. Unless I break him completely, I can never completely dominate his body and mind)"
    d "Your luck is really bad you know. \nIf only you could escape my magic by having a holy soul, I would have let you go.\nYours is so corrupted. Only dim light remains. No wonder..."
    hide m_m_sexclench3
    show m_m_sexopen at left
    p "What the fuck you blabbing about?"
    d "Pitchy, our prince is so comfortable that he forgot his owner. Tighten your grip! Play with him however you like."
    "The vines squeeze [p]'s body tightly and pull [p]'s nipples out till it can't stretch anymore."
    hide m_m_sexopen
    hide m_beaten3
    hide m_cockup
    hide m_shame
    show m_nipple at left
    show m_m_sexclench3 at left
    show m_beaten7 at left
    show m_cockup at left
    show m_shame at left
    p "Kuh!...aaahhhh"
    d "Who is lower, brat?"
    hide m_m_sexclench3
    show m_m_sexclench1 at left
    show m_blush at left
    p "...H!...You!"
    "[d] smiles."
    d "Listen kid. Being stubborn with me will never work. I'm actually pretty good at teaching manners to rebellious brats."
    d "Stretch his cock Pitchy."
    hide m_m_sexclench1
    hide m_cockup
    show m_cockvine at left
    show m_m_scream at left
    p "NO! STOP! AGHHHH!"
    d "Annoying!"
    "A vine thrusts in [p]'s throat."
    hide m_m_scream
    show m_m_vine at left
    p "m.....h"
    "[p] tries to stop the vines. It wraps him tighter and fucks his mouth harder."
    show vinecock with dissolve
    p "H..m..! Grghhh! Ggggg..!"
    p "mm...mmm"
    "The vines wrap around [p]'s dick and nipples. Squeezes them like a balloon" with vpunch
    p "mmmm..n..s-!"
    d "You seem to enjoy it. What a perverted prince!"
    "Everyone just kept spreading rumors that you know nothing about having fun. Seems like they don't understand you at all."
    show vinecockfast
    p "mm...nn..f-.."
    d "If you knew this day would come, you wouldn't have had to try so hard all your childhood. \nIn the end, whatever you achieve doesn't matter. You’d still just become my adorable sex toy."
    p "S-s-...! L-... m-.. g..!"
    d "What? You said you're happy to become my sex toy? You are welcome!"
    d "Pitchy, hear that? Give him more pressure. Our prince loves it!"
    hide vinecock
    hide vinecockfast
    show vinecockcum
    p "F-fu-...mm....nngh"
    p "h..hgh...ahhhhhhhh"
    d "Oh wow, our prince came from a plant!"
    hide vinecockcum
    hide m_m_vine
    show m_m_scream at left
    show m_blush at left
    show m_shame at left
    "[p] bites the vine invading his throat. The vine pulls out of his mouth."  with hpunch
    p "Haaa...Haaaa! Let! Me! Go!"
    d "Sure!"
    scene sky with hpunch
    "The vines release [p]. He falls from the sky to the trees. He slips from branch to branch like a ping pong ball. \nHe tries to grasp anything he can but he's falling too fast and his whole body is already badly injured." with vpunch       
    p "h...haah" with vpunch
    scene darkforest
    "[p] falls straight to the ground."
    show m_hurt at left
    show m_beaten3 at left
    show m_sperm at left
    show m_m_sexclench3 at left
    show m_shame at left
    show m_cockdown at left
    p "(Hurt!... My back!)"
    p "m"
    d "Falling from that high and you are not dead yet. What a miracle!"
    p "..."
    hide m_m_sexclench3
    hide m_m_sexclench2
    show m_m_sexclench1 at left
    p"..m.."
    d " That looks suit you"
    d "Nice body! You make my cock hard. It keeps telling me to make you our sex pet."
    show m_blush at left
    p "B-bas..."
    "[d] uses his foot to caress [p]'s cock"
    hide m_m_sexclench1
    show m_m_sexopen at left
    p "mmm..nn..."
    p "(Hurt! Damm this scumbag!)"
    d "It must be hard for you. \nI heard you had never lost, so you are quite full of yourself."
    "[d] gently squeezed it."
    hide m_hurt
    hide m_beaten3
    hide m_sperm
    hide m_shame 
    hide m_cockdown
    hide m_m_sexopen
    hide m_blush
    show m_close at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m_sexclench3 at left
    show m_cockup at left
    p "...m...n..."
    
    d "Understand this; for me, you are just like a small fly."   
    hide m_m_sexclench3
    show m_m_sexclench1 at left 
    p "m...h..."
    hide m_m_sexclench1
    show m_m_sexclench3 at left
    p "haaa...haaaa"
    hide m_m_sexclench3
    show m_m_sexopen at left
    p "h..*cough *cough"
    hide m_m_sexopen
    show m_m at left
    p "*gulp"
    hide m_m
    show m_m_sexclench1 at left
    p "...m..."
    d "You seem so helpless right now. I’m a little touched."
    hide m_m_sexclench1
    show m_m_sexclench2 at left
    p "Fuck you!"
    d "I have a wonderful idea. Prince [p], if you suck my cock, I'll let you relax for now. If not, you will play with Pitchy till you kneel down and beg me to suck it."
    hide m_m_sexclench2
    show m_m_sexclench1 at left
    p "Bastard! In your dreams! I'll cut your cock in half!"
    d "Pitchy!"
    hide m_close
    hide m_beaten3
    hide m_sperm
    hide m_shame 
    hide m_cockup
    hide m_m_sexopen
    hide m_blush
    show m_surprise at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m_sexclench3 at left
    show m_cockup at left
    p "!"
    show vinecocktree with vpunch
    "The vines lift [p]'s up, continue to strecth [p]'s cock and nipple."
    p "...m..."
    d "Have fun brat. I'll let you experience all the fun you missed in the past."
    scene black with fade
    
    "Day 2"
    scene darkforest with dissolve
    show m_nipple
    show m_m_sexclench3
    show m_beaten7
    show m_cockvine
    show m_shame
    show m_m_vine
    p "mm...n...h"
    p "(Fuck! How long do I have to stay here with these disgusting vines! I’ve had enough!)"
    p "...m...n..."
    "[d] appeared out of nowhere"
    d "[p], wanna get out?"
    p "F-...mm..."
    d "Ok! Got it! Stay here and have fun with Pitchy"
    "[d] left."
    p "...M..."
    scene black with fade
    "Day 3"
    scene darkforest_night with dissolve
    show m_nipple at left
    show m_sperm at left
    show m_m_sexclench3 at left
    show m_beaten7 at left
    show m_cockvine at left
    show m_shame at left
    show m_m_vine at left
    p "...ngh...h..."
    d "You seem less lively."
    p "mm...n!"
    d "Wanna get out?"
    "[p] nods."
    "[d] smirks."
    p "..."
    d "Release him Pitchy!"
    "[p] falls to the ground" with vpunch
    hide m_nipple
    hide m_sperm
    hide m_m_sexclench3
    hide m_beaten7
    hide m_cockvine
    hide m_shame
    hide m_m_vine
    show m_tired at left
    show m_sperm at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m_sexopen at left
    show m_cockdown at left
    p "Ha...haaa...haaa..h....m..."
    "[p] closes his eyes."
    hide m_tired 
    hide m_sperm
    hide m_beaten3
    hide m_sperm
    hide m_blush
    hide m_shame
    hide m_m_sexopen
    hide m_cockdown
    show m_close at left
    show m_sperm at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m at left
    show m_cockdown at left
    d "What the fuck? You sleep now?"
    menu:
        "Let him sleep":
            d "Oh well. Have a good rest. I'll play with you later"
            d "Tie him up. Not so tight it wakes him up, but make sure he can't move."
            scene black with fade
            "Day 4"
            scene darkforest with dissolve
            p "...m..."
            show m_close at left
            show m_beaten1 at left
            show m_blush at left
            show m_shame at left
            show m_m at left
            show m_cockdown at left
            "[p] wakes up!"
            hide m_close 
            hide m_beaten1
            hide m_blush 
            hide m_shame 
            hide m_m 
            hide m_cockdown
            show m_tired at left
            show m_m at left
            show m_beaten1 at left
            show m_cockdown at left
            p "How long have I been asleep?"
            hide m_tired at left
            hide m_m at left
            hide m_beaten1 at left
            hide m_cockdown at left
            show m_surprise at left
            show m_m_clench at left
            show m_beaten1 at left
            show m_cockdown at left
            p "!"
            hide m_m_clench
            show m_m_sexclench2 at left
            p "I can't move!"
            "[p] looks around and see the vines wrap him around a tree."
            scene tie_looka with dissolve
            p "Fuck that scumbag!"
            d "What did you say about me?"
            show m_surprise at s
            show m_m_clench at s
            show m_beaten1 at s
            p "!"
            hide m_m_clench
            show m_m_sexclench2 at s
            p "(It's been here all this time?)"
            "(Please click [p] to continue)"
        "Torture him more":
            "[d] kicks [p]"
            d "Wake up brat!"
            hide m_m
            show m_close at left
            show m_beaten1 at left
            show m_blush at left
            show m_shame at left
            show m_m_sexclench2 at left
            show m_cockdown at left
            p "..m.."
            hide m_m_sexclench2
            show m_m_clench at left
            p "..."
            d "Remember what I said. Give me a blowjob now or I'll let Pitchy continue to play with you."
            p "..."
            hide m_close
            hide m_beaten1
            hide m_blush
            hide m_shame
            hide m_m_sexclench2
            hide m_cockdown             
            show m_nipple2 at left
            show m_sperm at left
            show m_beaten7 at left
            show m_cockvine at left
            show m_shame at left
            show m_m_sexclench1 at left
            hide m_cockdown at left
            "The vines wrap [p] tightly."
            hide m_m_sexclench1
            show m_m_scream at left
            pause .5
            hide m_m_scream with dissolve
            show m_m_sexclench3 at left
            p "Argh!"
            "[d] touches [p]'s face"
            d "So?"
            hide m_m_sexclench3
            show m_m_sexopen at left           
            p "Do whatever you want with me bastard! I'll never do anything you say."
            d "Well said!"
            d "Pitchy!"
            hide m_nipple2 
            hide m_sperm 
            hide m_beaten7 
            hide m_cockvine 
            hide m_shame 
            hide m_m_sexclench1 
            hide m_cockdown
            show m_nipple at left
            show m_sperm at left
            show m_beaten7 at left
            show m_cockvine at left
            show m_shame at left
            show m_m_scream at left
            pause 1.0
            hide m_m_scream with dissolve
            show m_m_sexclench3 at left
            p "Argh!" 
            d "I like your spirit! Keep it up [p]!"
            hide m_m_sexclench3
            show m_m_sexclench1 at left
            p "Mother fuck-...m...ngh"
            hide m_m_sexclench1
            show m_m_vine at left
            p "...m...ngh..."
            scene vinecocktree
            show night
            p "...ngh..."
            scene black with dissolve
            "Day 4"
            show vinecocktree
            p "m...n.."
            p "..."
            "[p] is about to die from being unable to breathe."
            d "Release him! Gently! Our helpless princess seems to be one step from Hell’s door"
            "The vines slowly drag [p] to the ground" 
            scene darkforest
            show m_close at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench2 at left
            show m_cockdown at left
            p "...m..."
            "[p] is lying on the ground, cover by sweat. His whole body trembling as he slowly takes deep long breaths."  
            hide m_m_sexclench2
            show m_m_sexopen at left
            p "Haaa haaa"
            "[p] lying there, motionless and completely vulnerable. It seems like he cannot even twitch a muscle."
            "[d] touches [p]'s face"
            d "Has anyone ever told you you look awfully cute when you suffer?"
            hide m_close 
            hide m_sperm
            hide m_beaten1 
            hide m_shame 
            hide m_m_sexclench2
            hide m_cockdown
            show m_tired at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench1 at left
            show m_cockdown at left
            "[p] tries to push [d]'s hand away. But he's too weak."
            hide m_m_sexclench1
            show m_m_sexclench2 at left
            p "Fuck you! I'll slash your tongue in half."            
            d "You are funny. People kept saying the first prince is strong and smart. But all I can see is the opposite. Dumb and pathetic!"
            hide m_tired
            hide m_sperm
            hide m_beaten1
            hide m_shame
            hide m_m_sexclench2
            hide m_cockdown
            show m_surprise at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench1 at left
            show m_cockdown at left
            p "Damn you!"
            "[d] toucks [p]'s face"
            d "But you are indeed a very interesting creature. I have never seen anything that entertaining"
            p "SHUT U-mph"
            "[d] covers [p]'s mouth"
            d "Sht. Consider yourself lucky or unlucky. At least you can have one hell of good life experience here kid."
            "[d] touches [p]'s cock"
            p "Mn"
            d "Tie him there Pitchy!"
            hide m_m_sexopen
            hide m_surprise 
            hide m_sperm 
            hide m_beaten1 
            hide m_shame 
            hide m_m_sexclench1 
            hide m_cockdown 
            show m_tired at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench1 at left
            show m_cockdown at left
            p "F-Fuck!"
            hide m_m_sexclench1
            show m_m_sexclench2 at left
            "(Please click [p] to continue)"

#############################################################################################  Sim start (no proofreading here    
    $water = 20
    $food = 30
    $mental = 90
    $pride = 100
    $ene = 100 #(energy) 
    $day =4
    $fuckoff =0
    $nothing =1
    $clean = 90
    $bath = 0
    jump sim
                      
                    
    return
