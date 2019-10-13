#################################################################################################################################################################### Humi
label touch_first:
    "[d] sits near [p]"
    show m_surprise at s
    show m_m_open2 at s
    d "You seem bored."
    show m at s
    show m_m_sexclench1 at s
    p "Go away bastard!"
    "[d] laughs and touches [p]'s cock as a vine touches [p]'s asshole."
    show hand_poke
    p "...m..."
    "[d] pokes it repeatedly as the tip of the vine softly teasing his p-spot."
    p "...n..."
    "It is a really unpleasant feeling. \n[p] can feel the sensation but it isn't intense enough." 
    p "..ngh...s-stop.."
    d "It doesn't seems like you want me to stop. \nYou look so lewd"
    p "...ngh..."
    d "We are serving you slowly and tenderly. Why so tense? Never got someone to gently caress these places before?"
    p "...m...ngh..."
    p "...f-fuck you"
    d "Seriously? Your life must be so miserable."
    p "...ngh..ngh....."
    "[d] touches [p]'s balls as the vine goes deeper, presses his prostate harder."
    show hand_ballclose
    p "...mm...n..ahh.."
    d "Your face tells me you want more. This can't satisfy you."
    p "...m..."
    p "You bastard!"
    show hand_ball
    "[d] and the vine stop."
    hide hand_ball
    hide hand_ballclose
    hide hand_poke
    hide m
    hide m_m_sexclench1
    hide m_m_open2
    show m_m_open1 at s
    p "..!.."
    d "What's with that look? Were you hoping for something else?"
    hide m_m_open1
    show m_m_sexclench2 at s
    show m_shame at s
    p "Fuck you!"
    "[p] was fraught with want. If his hands were not tied he would have tried to jerk off."
    hide m_shame
    show m_blush at s
    show m_shame at s
    hide m_m_sexclench2
    show m_m_sexclench1 at s
    p "(Shit! Fuck! I'll kill you one day [d].)"
    $pride -=1
    $ene -=40
    $food -=5
    $water -=10
    "[p] feels ashame of himself. His pride decreases."
    "[p]'s thirst and hunger increase."
    $touchfirstnone = False
    jump sim

label touch:
    "[d] sits near [p]."
    show m_surprise at s
    show m_m_open2 at s
    show m_blush at s
    p "..."
    d "What happened? You seem scare?"
    hide m_m_open2
    show m_m_1 at s
    show m_shame at s
    p "I-I'm not!"
    "[d] touches [p]'s balls as a vine tease his asshole."
    hide m_shame
    hide m_tired
    show m_tired at s
    show m_m_sexclench1 at s
    show m_shame at s
    show m_blush at s
    p "M!...ngh...Shit!..."
    scene hand_ball
    p "...m..No!...Get away!"
    scene hand_ballclose
    d "You say no, but your expression says otherwise."
    p "..ngh...aaa.."
    d "Relax!"
    scene hand_poke
    p "...m..fuck you..."
    d "..."
    d "Hmp"
    scene hand_balltease
    p "...aaaa...ahhh...haaa..."
    p "...ngh..mm...s-stop it..."
    d "I thought you want more. Isn't that why you try to irritate me while I was being nice?"
    p "...s-stop.."
    "Is it that good?"
    p "...m..."
    "[d] laughs loudly."
    d "Got it prince."
    "[d] and the vines stop."
    scene tie
    show m_close at s
    show m_m_sexopen at s
    show m_blush at s
    show m_shame at s
    p "...haaaa..haaaa.."
    d "You seem desperate. Should I help you jerk off for real?"
    hide m_close
    hide m_m_sexopen 
    hide m_blush 
    hide m_shame 
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_sexclench2 at s
    p "...Bastard! If one day I get you... I'll cut you into thousand pieces. Let you there rotten from lack of blood."
    "[d] pulls [p]'s head"
    show pull_day
    p "...m...ngh..ahhhh.."
    d "For someone who really wants, but is unable to cum, you have a big mouth."
    #blush
    p "I-I'm not!"
    "[p] feels ashamed of himself. His pride decrease."
    "As [p] is exhausted from the pleasure,thirst and hunger increase."
    $touchnone = False
    $water -=40
    $food -=30
    $pride -=2
    $ene -=20
    jump sim
    
label touch_obe:
    "[d] gently touches [p]'s cock."
    show hand_ball
    p "...h..."
    show hand_ballclose
    d "This hard already? Seem like I can earn a lot of money by selling you to a slave market."
    show hand_poke
    p "ahhh...n...m...ahh"   
    p "...m...n-no..."
    d "Even if they they know who you really are, it doesn't matter. You have no power over others anymore."
    p "..ngh.."
    hide hand_poke
    d "Oh wait, with your \"amazing\" reputation, maybe I can even earn more money. Double? Maybe triple?"
    
    p "...m...Don't...don't...say that...n..."
    "[d] smiles wickedly."
    d "I heard you were \"cherished\" by many people in the palace. I will invite them as well. Who knows, they might be interested in purchasing the well-trained slave prince they once served."
    p "...n.."
    d "What do you think [p]? Should I make an auction?"
    show hand_balltease
    p "...m...n-no...ngh...please don't...ngh.."
    "[p]'s cock becomes harder as his face turned completely red."
    p "..m...ngh.." 
    "[d] laughs"
    d "Masochist brat!"
    show m_close at s
    show m_m_sexopen at s
    show m_blush at s
    show m_shame at s
    p "..."
    "[p] feels ashamed of himself. His pride and and psyche decrease."
    "As [p] exaulted from not being able to cum, his thirst and hunger increase."
    $water -=40
    $food -=30
    $mental -=1
    $pride -=2
    $ene -=20
    jump sim