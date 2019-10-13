################################################################################################################################################################################# Free
label free0:
    d "(He is not obedient enough to walk around freely.)"
    d "(But I can let him rest from now till tomorrow.)"
    hide screen day
    hide screen stat
    "[p]'s thirst and hunger increase as day went by."
    scene black with fade
    pause .5
    
    
    $day +=1
    $water -=20
    $food -=10

        
    jump sim

label free1:
    d "Today, I'll let you go for 2 hours."
    p "..."
    "The vines release [p]"
    "[p] go to the trees, searching for the remaining of his cloth."
    d "Monster doesn't care if you are nude or not. Don't have to be embrassing."
    p "..."
    d "When you find your cloth, remember to strip it out before come back here or I'll torn them apart. They are in the way."
    p "You shithole!"
    "After 2 hours, [p] finally find his cloth. He hide them under a tree and return."
    p "..."
    d "Ho, not trying to escape?"
    p "..."
    d "Smart choice."
    p "..."
    "[p] recover as he is not being pet. His pride and psyche increase."
    $firstfree = False
    hide screen day
    hide screen stat
    $day +=1
    $water +=5
    $food +=10

    scene black with fade
    pause .5
    $ene =100
    jump sim
    
label free2:
    d "Release him Pitchy. It's his free time."
    p "..."
    "[p] go to the forest."
    "[p] finds a muddy spot but cannot located a body of water. He digs a hole and wait for the water to flow in."
    p "(The water is heavily contaminated)"
    p "..."
    p "(Whatever. I used to drink worse.)"
    "[p] drinks the water.)"
    "His thirst decrease."
    d "Have a good walk?"
    p "..."
    "[p] ignores [d]"
    show pull_day0008 with vpunch
    "[d] pulls [p]'s hair"
    p "..Arghh!...arg...Stop!"
    d "You are not bright aren't you? The silent game never works with me."
    "[d] releases [p]."
    hide pull_day0008
    p "...m..."
    p "(Fuck this monster!)"
    "[p] recovers as he is not being pet. His pride and psyche increase."
    hide screen day
    hide screen stat
    $day +=1
    $mental +=2
    $pride +=2
    $water +=20
    jump sim
    
label free3:
    d "Go kid, enjoy your free time"
    p "..."
    "[p] walks at the forest"
    p"...."
    p "(I feel so hopeless. Will I really find the river?)"
    "[p] desperately walking forward. He doesn't even bother to find food or water."
    $energy -=30
    hide screen day
    hide screen stat
    $day +=1
    $water -=20
    $food -=10
    jump sim
    
label free4:
    d "Have your free time, unless you want to stay here and have sex with your master."
    p "..."
    "[p] stands up and go deep inside the forest with no goal. His mind is not there."
    "[p] recover as he is not being pet. His pride and psyche increase."
    hide screen day
    hide screen stat
    $day +=1
    $water +=20
    $food +=10
    jump sim