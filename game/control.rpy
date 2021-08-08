####################################################################################################################################################################################### Mind control

label control1:
    hide screen day
    hide screen stat
    scene tie_looka
    "[d] looks at [p]. His eye turns red"
    d "..."
    d "(Not working!)"
    $controlStage = 1
    jump sim
    
label control2:
    hide screen day
    hide screen stat
    scene tie_looka
    "[d] looks at [p]. His eye turns red"
    scene tie
    show m_surprise at s
    show m_blush at s
    show m_shame at s
    show m_m at s
    "[p] feels pain in his head."
    scene tie
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m_open1 at s
    p "..m.."
    scene tie
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_normal at s
    p "(What just happens?)"
    d "(I have reached into his mind but the barrier is too strong. Have to break him more)"
    $controlStage = 2
    jump sim
    
label control3:
    hide screen day
    hide screen stat
    scene tie_looka
    show m at s
    show m_m at s
    "[d] looks at [p]."
    scene tie_looka
    show m_tired at s
    show m_m at s
    "[p] scares. He quickly looks away. [d] chuckles"
    scene tie
    show m_tired at s
    show m_m2 at s
    d "You have start to fear me huh?"
    scene tie_looka
    show m_surprise at s
    show m_blush at s
    show m_m_open2 at s
    p "W-What do you need?"
    hide m_blush
    hide m_m_open2
    show m_blush at s
    show m_m at s
    "[d] smirks. His eyes turn red."
    scene tie
    show m at s
    show m_blush at s
    show m_m_open1 at s
    d "Look at me!"
    scene tie_looka
    show m at s
    show m_m_1 at s
    show m_blush at s
    show m_shame at s
    "[p] looks at [d]. He feels dizzy, like someone penetrate his brain"
    hide m_m_1
    show m_m_sexopen at s
    p "Ngh..."
    scene darkforest
    show m
    show m_cockdown
    show m_shame
    show m_m_normal
    "The vines release [p]"
    hide m_m_normal
    show m_m
    p "..."
    d "What are you doing? On your four and crawl here!"
    scene darkforest
    show m_tired
    show m_cockdown
    show m_shame
    show m_m2
    "[p] feels like his body moves against his will."
    hide m_m2
    show m_m_sexclench1
    p "Mnh..."
    hide m_m_sexclench1
    show m_m_sexclench2
    d "(I cannot stop moving...)"
    scene darkforest with None
    show m
    show m_cockdown
    show m_shame
    show m_m_open1
    "[d] touches his face. [p] feels hot." 
    scene darkforest with None
    show m_tired
    show m_cockdown
    show m_blush
    show m_shame
    show m_m_open_speak
    "[d]'s touch somehow become really pleasant."
    scene fin_touch
    p "Ngh!"
    d "Good boy. If you were to obedient like that from the start, I would have treat you better."
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_open_speak at s
    p "(My head. It hurts!)"
    hide m_m_open_speak
    show m_m_open2 at s
    d "Suck this!"
    scene fin_mouthb
    show m_surprise at s
    show m_blush at s
    show m_shame at s
    show m_m_open1 at s
    p "MNGH!"
    hide m_surprise
    hide m_blush 
    hide m_shame 
    hide m_m_open1 
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m_open1 at s
    "[d]'s thumb thrust in [p]'s throat. It's painful, but feel good at the same time."
    hide m_m_open1
    show m_m_sexopen at s
    p "Ngh..."
    scene darkforest
    show m_close
    show m_cockup
    show m_blush
    show m_shame
    show m_m_open2
    "[d] takes his hand out of [p]'s mouth and moves to his chin."
    scene darkforest with None
    show m_surprise
    show m_cockup
    show m_blush
    show m_shame
    show m_m_open2
    p "?"
    scene darkforest with None
    show m
    show m_cockup
    show m_blush
    show m_shame
    show m_m
    "[d] kisses [p]'s forehead."
    scene darkforest with None
    show m_surprise
    show m_cockup
    show m_blush
    show m_shame
    show m_m2
    p "!"
    scene darkforest with None
    show m_tired
    show m_cockup
    show m_blush
    show m_shame
    show m_m
    p "...."
    scene darkforest with None
    show m_hurt
    show m_cockup
    show m_blush
    show m_shame
    show m_m2
    "He pushes [p] to the ground. Everytime [d] touches him, [p]'s body react in a lewd way."
    scene deepimpact_head
    "[d] grasps [p]'s legs and start to put his dick in." 
    hide m_blush
    hide m_shame
    show m_surprise at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "Mgh!"
    hide m_surprise
    hide m_blush
    hide m_shame
    hide m_m_sexopen
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "...Agh!"
    d "Is it good?"
    hide m_tired
    hide m_blush
    hide m_shame
    hide m_m_sexopen
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m_open1 at s
    p "Ahhh...Ahhh..."
    hide m_m_open1
    show m_m_clench2 at s
    p "Ngh!"
    hide m_m_clench2
    show m_m_sexclench1 at s
    "[p] doesn't react or curse [d]. He lets [d] does whatever he want inside him." 
    hide m_tired
    hide m_blush
    hide m_shame
    hide m_m_sexclench1
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m2 at s
    "[p] know he had no ability to resist what is being done to him. What remains of his will is just a pliable slave."
    hide m_m2
    show m_m_sexclench3 at s
    p "..M...ngh..."
    hide m_hurt
    hide m_blush
    hide m_shame
    hide m_m_sexclench3
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m2 at s
    "[d] slowly enters deeper."
    hide m_m2
    show m_m_sexclench1 at s
    p "...Ngh..."
    hide m_tired
    hide m_blush 
    hide m_shame
    hide m_m_sexclench1
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "...[d]...m..."
    hide m_hurt
    hide m_blush
    hide m_shame
    hide m_m_sexopen
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m2 at s
    "[p] doesn't know what happen to him. Perhaps it was because of the hypnosis. The warmth of [d]'s cock, his movement, his touch, his smell, his voice. Everything arouse [p] at this moment."
    hide m_m2
    show m_m_sexopen at s
    p "..M...n..."
    hide m_m_sexopen 
    show m_m_scream at s 
    p "...Arghhh..."
    hide m_m_scream
    show m_m_open_speak at s
    d "You are so cute."
    hide m_tired
    hide m_blush
    hide m_shame
    hide m_m_open_speak
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "...Ngh....m...aah..."
    hide m_m_sexopen
    show m_m_scream at s
    p "Ahhh...haa....ngh..."
    show m_m2 at s
    d "You twitch a lot [p]. You like my cock inside don't you?"
    hide m_hurt
    hide m_blush
    hide m_shame
    hide m_m_2
    show m_close at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "Ahh...ah..."
    hide m_m_sexopen
    hide m_m_clench
    show m_m_clench at s
    d "Me too.."
    hide m_close
    hide m_blush
    hide m_shame
    hide m_m_clench2
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "N-no I...Ahhh...n...What...did you...ngh...m..."
    hide m_m_sexopen
    show m_m_sexclench1 at s
    "[p] cannot even finish a full sentence in this condition."
    "Ater he gets use to it, [d] slams [p] faster and stronger."
    scene deepimpact_deep
    p "...H...Ngh...aaa...ahhh...."
    p "..N...ngh...no..no don't...ahhh.."
    "[p] cries. It's normal for him to burst into tears while having sex with [d] because it hurts a lot. However, right now, it was tears of shame."
    "They had sex a lot of times already. [d] knows what he likes. [p] feels ashame for enjoying it."
    d "Why are you crying? Is it too good?"
    p "..."
    p "..Ahh...haaa..."
    d "Hey, say something!"
    scene deepimpact_deep
    show m_close at s
    show m_blush at s
    show m_shame at s
    show m_m_1 at s
    p "...Mgh..."
    scene deepimpact_deep_fast
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "P-please [d]. I cannot take it anymore. St-.. mgh!"
    hide m_tired
    hide m_blush 
    hide m_shame 
    hide m_m_sexopen
    show m_close at s
    show m_blush at s
    show m_shame at s
    show m_m2 at s
    d "Ngh... [p], can I cum inside you?"
    hide m_m2
    show m_m_sexopen at s
    p "Ngh...Ahhh...aaa...m..."
    scene deepimpact_deep_fastest
    d "[p]!"
    show m_surprise at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "N-no...Mgh...no...ahh..."
    hide m_surprise
    hide m_blush 
    hide m_shame 
    hide m_m_sexopen
    show m_tired at s
    show m_blush at s
    show m_shame at s
    show m_m_sexopen at s
    p "...Ngh...O-Out...side...[d]..."
    scene deepimpact_deepcum
    "[d] cums inside [p]."
    hide deepimpact_deep
    show deepimpact_deepcum
    show m_hurt at s
    show m_blush at s
    show m_shame at s
    show m_m_sexclench3 at s
    p "Ugh!..."
    hide m_m_sexclench3
    show m_m2 at s
    d "You have to answer faster next time."
    hide m_m2 at s
    show m_m_sexopen at s
    p "Ngh! P-please st-"
    show deepimpact_deep
    "[d] continue to penetrate [p]."
    p "N...mgh!...Take it out...please...I can't-...ahh"
    d "Why? Because I keep on hitting your sensitive spot?"
    p "...Ngh! Ahh...I-I've cum...ahh...please stop."
    d "Liar. Your cock is still really hard here. Does the pleasure too instense for you to handle?"
    p "...[d]...P-please stop..."
    "[d] smirks."
    scene deepimpact_deep_fast
    p "N-no, please. Have you had enough entertainment?"
    p "Is that enough? I'm sorry for what I did to you. I'm begging you. Please let me go! I'm going insane!"
    d "So what? I should stop because of that?"
    scene deepimpact_deep_fastest
    "[d] moves faster"
    p "[d], [d]. Please stop. Have pity on me. Please. I'm really going insane. My mind is breaking apart."
    d "..."
    "[p] sobs. He makes it look like the world had come to an end."
    p "Ahh...hm..."
    p "P-Please stop. Please let me go [d]. I beg you."
    d "..."
    p "P-please [d]. I'll break. Please...Hmmm...ahhh..."
    scene darkforest
    show m_close
    show m_cockup
    show m_shame
    show m_m
    show m_sperm_stomach
    "[d] stops. He seems angry."
    d "What a mood breaker."
    scene darkforest
    show m_tired
    show m_cockup
    show m_shame
    show m_m_open2
    show m_sperm_stomach
    p "I-I'm sorry...Please stop..." #start here
    d "..."
    "[d] facial expression returns to normal."
    d "Since you begging too hard just now, I'll give you a chance."
    p "!"
    d "Drink my piss. If you do this well, I'll not tie you anymore."
    "[p] looks up at [d]. His eyes and cheek look red from all the crying."
    p "W-w- y-...will you really let me go?"
    "[d] smirk."
    p "..."
    "[d] climbs on top of him."
    menu:
        "Peep":
            scene peep_close
            show peep_cry
            "[d] peeps in [p]'s mouth"
            p "Ngmm...mhn..."
            scene peep with None
            show peep_nocry 
            p "...nhh..."
            d "Stop spilling it out!"
            p "Mn...n..."
            scene peep_chew with None
            show peep_cry with None
            "Its hotness and stinkiness makes [p] dizzy. It tastes was horrible. Much worse than when [d] forced him to drink his own piss. Yet, it arouses [p]."
            "It must be because of the hypnosis, that strong crave and attachment for [d] is so abnormal..."
            p "M...h..."
            scene peep_inmouth with vpunch
            p "Ngh..."
            d "Is it hot?"
            p "Mgh...m..."
            d "Drink carefully this time. Don't spill it."
            p "Ngh...M..."
            "[p] was unable to consume that much peep. He dirty himself and [d]."
            d "You are so useless. Cannot even be a proper toilet."
            p "Mnn...ngh...h..."
            p "Ngh...h..."
            "[d]'s cock head was inside [p]'s mouth till the last drop."
        "Smirks and go away":
            "[d] smirks and pulls his trouser on."
            "[p] nervously looks at [d]."  
    scene darkforest
    "[d] moves away from [p]. [p] sits up. He avoids looking at [d] while clumsily wipes his lips."
    p "..."
    p "!"
    show darkforest2
    show kiss_suprised
    "From out of nowhere, [d] kisses [p]." with hpunch
    p "Ngh..."  
    hide kiss_suprised
    show kiss with dissolve
    d "You look so adorable."
    p "N...h..."
    "He kisses [p] more intensively."
    hide kiss
    show kiss_fast
    p "Ngh...m..."
    hide kiss_fast
    show kiss_fast_short
    p "..."
    p "N..."
    "[d] stops."
    hide kiss_fast_short
    p "..."
    d "I'm keeping my words. Pitchy had more important jobs to do anyway."
    p "..."
    "[d] looks at [p] who is still in a daze. He seems lost."
    "[d] slowly moves closer to kiss him again. [p] leans backward, his back touches a tree. When their eyes met, [p] looks away." with vpunch
    d "..."
    p "C-can I really go now?"
    d "Go away? Do you really think I'll let you go?"
    p "..."
    d "But I'll give you a little more freedom."
    "[p] reliefs. Even if he cannot get out, being able to freely move around is clearly much better. He can even find a way to get out."
    d "3 feets."
    p "?"
    d "This tree is the pivot point. From here, you can freely move around 3 feet."
    d "If you move more than that without my permission, don't blame me for your punishment."
    d "You know that even without being tied up, you cannot escape. This whole forest is my eyes and ears. I know each inch you move without looking."
    p "..."
    "[p] becomes depress." 
    "3 feets. What a joke. [d] was just playing around with him." 
    show sit_alt
    "[p] hugs his knees and tucks his head between them, making him as small as possible, to keep himself away from getting noticed by [d]."
    "It was very stupid of him. There is no way [d] lets him go or moving too freely. He will rotten here till the day he dies as [d]'s sex relief toy."
    d "Not being impulsive anymore huh? Your emotion seems to be more stable these days [p]."
    p "..."
    show sit_tight
    "[p] trembles. He hugs his knees tighter, which makes him looks even smaller."
    d "You sure have great mood swings. You look so affectionate just a few minutes ago."
    p "..."
    "[d] can hear tiny sobbing sound coming from [p]. The closer he moves, the more [p] shuts himself and trembles."
    d "..."
    d "Suit yourself!"
    "[d] goes away."
    $controlStage = 3
    jump sim2

label control4_ques:
    $controlStage = 4
    scene sit_alt
    "Early morning, when the sun still have yet move above the tree, [d] comes."
    "He touches [p]'s head while he were sleeping"
    p "Uhm..."
    d "Wake up!"
    show sit_tight
    p "Ugh! N!"
    scene sit_sad
    "[p] slowly opens his eyes. He is not fully awake yet. [d]'s eyes become red."
    p "..."
    p "(This...again...S-Shit. It hurts. I feel like he goes inside my mind...)"
    p "Ngh...m..."
    d "N!"
    d "..."
    "[d]'s eyes turn back to normal. [p] closes his eyes."
    p "Ngh...[d]...I'm sleepy."
    d "..."
    p "!" with hpunch
    "[d] brutaly slaps [p]. [p] knocked down to the ground" with vpunch
    scene control4_slap
    "Not understand what's happen, he consfuses and tries to get up. Too into sleep, [p] is in a very weak state."
    p "Wh-!" 
    scene control4_stomp with vpunch
    "[d] stomps on his head" with hpunch
    p "Hph!"
    p "What are y-"
    p "!"
    "[d] brutally stomps on [p]'s head again" with vpunch
    p "M...Aa..."
    d "You have a very bad sleeping habit [p]. Shouldn't knight need to pay attention to small noises even in sleep?"
    p "N-no, I-I used to..."
    d "So it was because of me huh?"
    scene control4_lickear
    "[d] licks [p]'s ear hole."
    d "You have nothing left but me. Why are you still trying to resisting? Give yourself to me."
    p "Mgh..."
    p "I didn't resist, [d]..."
    d "Yes you are, not physically, but it causes me troubles."
    "[p] heard some noises. The mosquito monsters appeared from the bush. [d] gets away from him."
    scene control4_slap
    p "[d]! [d]!"
    scene darkforest
    show m_surprise
    show m_beaten7 
    show m_m_sexclench1 
    show m_shame
    show m_blush
    show m_cockup
    show thunder at infinite_flash
    "The mosquito attach [p]" with hpunch
    p "AGHHH! AAAAGGGGHHH!"
    d "Hahaha, is it that hard to control your own urine? I can see some stool too."
    p "...W-Why..?"
    "[p] unable to move his mouth and body. He feels so ashamed for the little feeling and trust he have for [d]."
    scene darkforest
    "[d] throws a heavy kick on [p]'s head" with vpunch
    p "Mgh!"
    "He stomps on his head again." with hpunch
    scene control4_stomp
    d "I'm your master, not your ally. I can beat you for no reason whenever I want. That's why!"
    p "F-fu..."
    scene control4_stomp_cries
    "[p] cries."
    d "Cries again? Had you become meek? Or you cannot take it anymore? What a weakling, trying to play tough."
    scene darkforest
    p "Bastard!"
    "Recovered, [p] rushes to [d] but falls. He still paralyzed. [d] laughs." with vpunch
    d "Finished taking your shit first. Don't attack me while poping"
    p "F-Fuck you! I'm not!"
    "[p] rushed to [d], punches him in the face repeatedly. He didn't avoid." with hpunch
    d "..."
    p "You Shithead! Why Are You Treating Me Like This?!?!"
    "[d] kicks [p]. [p] uses both hands to block it. He had to jump backward to neutrolize the kick to not fall." with vpunch
    p "Aaaa!"
    "One of his hand was broken from the kick."
    "[p] rushes to [d] immediately. His punches become stronger and faster. [d] steps backward and avoid the hit as [p] rushes in." with hpunch
    if talk>16:
        d "You have asked me what did I think of your skills. Do you still want to know?"
        p "Fuck you! I don't need it!"
        "[p] continues throwing his punches."
    else:
        d "When we first met, I didn't pay attention, but is this really how you always fight?" 
    "[d] reaches his hand and touches [p]'s forhead with his index finger. [p] steps back then rushes in again and throws heavy punches as [d] avoid them easily" with vpunch
    d "Your reflexness is horrible. You cannot react quickly enough."
    p "FUCK! SHUT UP!" with hpunch
    "He uses more strength and moves faster. Because of that, it also creates a lot of gaps." with vpunch
    "[d] sighs as he avoid [p]'s attacks and looks at him re-position to throws another punch."
    d "So predictable. You don't use your brain at all, do you? Is it just for decoration?"
    p "SHUT UP!!"
    "[p] grows more furious."
    "[d] easily avoid [p]'s attack just by a small and swift movement."
    p "!"
    p "(Crazy bastard! He's not serious at all.)"
    d "No wonder people said you are blood-thrist. That fighting style suits your strengths and weaknesses. I give you one intelligent point for that." 
    p "SHUT YOUR MOUTH UP!!" with hpunch
    "[d] catches the punch and breaks his arm" with vpunch
    p "AGGHHHHHHH!"with hpunch
    p "Haa...haa..."
    d "It breaks just with that strength. Your bones are not good for fighting. Many people and monsters can broke your spine, make you immorbilize forever with just one punch in the back."
    d "Yet, you rushes into battles and makes enemies. Like a morph throwing itself to flames. Just for the sake of recognition by your father."
    p "S-STOP!!"
    "[p] escapes [d] and throws him a kick." with hpunch
    "[d] breaks [p]'s leg." with vpunch
    p "AAAAGGGGHHHH!"
    "[d] throws [p] to the ground" with hpunch
    d "With that many enermies and this type of body plus your reflection speed, do you really think you can be allive after disowned? It feels like your father send you to your own grave huh?"
    d "Is that the reason you look so wild when we meet? Like you can go ahead and murder everyone."
    p "..."
    d "Too bad it just turn out the opposite, but at least you seems sexually satisfy."
    "[p] clenches his teeth and fist."
    d "Use your brain [p], if your father had any planned for you, he wouldn't do nothing and let your reputation ruins so badly." 
    p "S-STOP! JUST SHUT UP!!! What do you even know?!? SHUT THE FUCK UP!!"
    "[p] tries to stands up."
    p "Uhm..N!"
    "[d] smirks"
    d "Do you know what you look like? A stepping stone for your brother. Maybe your father already plan it from the start." 
    p "N-no...Fuck you [d] ...n..."
    d "You like to call your brother his puppet, because your brother listen to him. But you look more like his puppet to me."
    p "Please stop..."
    d "He might have know it too. You were born as an abnormal. A creature that can go against The Flow and unable to in sync with this world. An ill-fated human."
    "[d] bends down and grasps [p]'s broken arm joint."
    p "Uhm..."
    d "It must be hard, living like that. Have you ever feel like you were extemely unlucky, like the world keep on pushing you out no matter how hard you try?"
    p "..."
    d "There are some who pass The Flow threshold too, compare to them, you are nothing. They are either too powerful, or prepare too well, that The Flow cannot touch them. And here you are, cluelessly waiting to be killed."
    "[p] glances at [d]."
    p "!"
    "[p] feels cold. His breath become shorter."
    d "You can feel it right? The death. The Flow told me to kill you as soon as you walk into this forest, but I decide to violate you day after day instead."
    d "Now the time had come. It doesn't need me anymore."
    "[p] sweats and becomes dizzy. Something is squeezing his heart hard."
    p "Ugh...Ahhh..."
    "[p] starting to feel very tired."
    p "Haa...ugh! S-shit! I need The Stone...I will... hmp..."
    "[p]'s glance become softer."
    p "Ghu...a...I beg you [d]. Give me...m...a chance. I don't...n...need anything..."
    p "I...ngh....lied..h...to myself. I didn't look for it..h...for the throne. A-All I really want...n...is just to turn back in time, to fix...uh..."
    "[p] sobs." 
    p "...I beg you [d]...I just want...h...to go back...ah...in time...to fix..."
    "[d] touches [p]'s face."
    p "*sob...*sniff..."
    "[p] tries to hold his tears in. The sound stops. But his tears keep falling out. He had been holding it for a long time, he cannot stop it anymore."
    d "Too bad your little wish will never be fulfill. Only the creations that's in a perfect harmony of The Flow can use The Stone." 
    d "The moment you touch The Stone, either it or you will be destroyed. You are clutching at a straw [p]. You can image going back in time before you die if you want it so badly."
    p "..."
    "[p]'s tearss continue to fall. [d] wipes his tears. [p] feels better. The squeezing started to slow down."
    d "..."
    p "D-Don't. Don't touch me."
    d "I have always tried to help you go through this painlessly, but you didn't let me...And here the dealine comes."
    "[p] clenches his teeth and eat his tears inside."
    p "Fuck you [d]! Why do you need to push me through all of this? Just kill me! Right now!"
    d "..."
    p "Even if this world is pushing me away, am I not a living being? Am I not worthy to be treated like one? My life, it had been nothing but an endless misery..." 
    p "Why do I have to endure your torture and humiliation before being killed? Who give you the right to hurt me and trample on my sanity like this? Does God not need moral?"
    d "No." 
    "[p] clenches his teeth."
    d "But aren't you just doing the same? How many monsters and humans had you torture to death? Aren't they living being too? Aren't they worthy to be treated like one? How many innocent blood you had in your hands?"
    "[p] was shocked. He stays silent."
    "[p] opens his mouth, grasps for air. There was so much pain in his heart from the squeezing. It become stronger and faster every minutes."
    p "Argh...Arghh...Urg..."
    d "..."
    "[d] softly kisses [p] on his eye."
    p "...Aa...n..."
    "[p] feels better after the kiss. Even though his heart is still being squeeze."
    p "(S-Shit. Will this be the last image I see? The last act of kindness I will get?)"
    "[p] closes his eyes. His tears keep on falling."
    p "(Is this the way it end now? My little dream of the three of us having good times like we used to be...My little dream of having someone by my side, love me, and accept me...)"
    p "([d]. You turned my life upside down. My pride, my identity, my believe, my feeling, my sanity...they are all crumble. Is it fun to you?)"
    "Right when [p] open his eyes. [d]'s eyes turn red."
    "Again, [p] feels like his head was penetrated. [p] doesn't understand [d]'s need of fully control his mind before he dies. But at this point, [p] does not care anymore. He can does whatever he wants." 
    "[d] slowly thrusts his hand into [p]'s brain."
    p "Ughh...aaa..."
    "The pain were too much that [p] cannot even scream. [d]'s fingers go on deeper and deeper. With each thrust, [p] feels like thousands of needle attach his brain."
    d "You will enjoy this soon. Your mind will re-arange, and your pain will turns to pleasure." 
    p "Mmm...mngh...m..."
    "[p]'s cock hard on its own and cum. How much [d] want to torture and humiliate him before killing him off?"
    p "Gah...ah...a..."
    "[d]'s other hand grasps [p]'s shoulder hard."
    d "Loosen up!"
    p "(Loosen up?...My mind is blurry. I don't care anymore...Please [d], finish it fast...)"
    "[p] tries to soften himself. The thurst becomes faster and stronger in disregard of [p]'s pain. His muscle keeps on twitching."
    p "N...ahh...aaa..."
    "All 5 fingers of [d] had penetrate to the deepest part of [p]'s brain. [p] feels a flow of energy comming in. It comes faster and heavier each second."
    p "Ngh...aaa...m..."
    "It was even more painful than all the tortures [p] had done. He thinks maybe it was the death that suits him best."
    d "N!"
    "[p] becomes unconscious. His face falls on [d]'s lap."
    d "[p], [p]!"
    d "(He's fine.)"
    p "Ngh!"
    "[d] caress [p]'s head."
    p "Ngh...[d]..."
    "[d] smiles."
    d "It wasn't your father, brother, or anyone else that you call out to in your dream but me. Whatever the reason, I'm glad."
    "[d] moves his hand to [p]'s face."
    p "N..."
    d "When I first met you, you look so sorrowful and confused. Now, you look even more so. You must have loathe me to your heart content." 
    d "But I ..."
    "[d] shakes his head. He tries to be awake but also fallen asleep."
    "He sleeps while sitting upright with [p] lying on his laps." 
    
    "The next morning, [p] wakes up."
    p "(I'm still alive?)"
    "[p] looks at his hands. He seems to have recovered."
    d "You have waken up."
    p "!"
    p "[d]!"
    "[d] smiles."
    d "Don't you feel like this is similar to the day we met, right before I tied you up to teach you obedient and make you satify me?"
    p "You Fucker!"
    "[p] rushes to [d] but stops. He feels lighter than usual. He looks at his hands."
    p "..."
    p "How can this be..."
    d "You have no longer disrubt the flow of this earth, [p]. You will live for as long as I'm still alive."
    p "..."
    "[p] shooks his head."
    p "This cannot be. I cannot live like this..."
    p "...How meek had I become for you to be able to forcefully sharing your power without my acceptant...I rather not being alive to see myself become a monster..."
    d "..."
    "[d] moves closer. When he about to touches [p]'s face, [p] pushes his hand out and pushes him away."
    p "Don't Touch Me You Crazy Bastard!"
    "The ground is moving faster and faster. It forms according to [p]'s will."
    d "..."
    d "You learn fast."
    p "!"
    p "..."
    "[p] creates waves with shatter earth and throws it at [d]. [d] negates then make them crumble."
    "Dust fly everywhere. [p] disspeared."
    d "Good move."
    "[p] runs. He doesn't know where did he runs to. He just run forward."
    p "([d] didn't able to catch me. It seems like he had become weaker. Is it because of the thing he did to me?)"
    p "Water sounds..."
    "He turns and runs to a waterfalls. The demon said to him there is only one river here. The Stone is either top, or down."
    "[p] doesn't know which word of the monster is true. Should he try to get out of this forest, or to find the stone?"
    p "Even if I can get out, he will still find me. If he captured me again,..."
    "[p] remmembered all the time [d] rapes him, as well as some gentle moments." 
    p "No! Stop thinking! I have to find The Stone."

    "[p] heard a foot step."
    p "Who?"
    n "Sir Knight? What happen to you?"
    p "You!"
    "[p] grasp [n]'s shoulder. He askes in a hurry tone."
    p "Where is the stone? Is it upstream or down stream?"
    n "I-It's downstream."
    "[p] looks behind him."
    p "So it's this way."
    n "..."
    p "What if I can't find it?"
    "[p] grasp [n]'s shoulder hard."
    p "Go with me!"
    n "No, I -"
    "[p] carries him and run like flying. [n] points at the middle of the river." with vpunch
    n "It's there!"
    p "I didn't see anything."
    "[p] tries to look, but it just all water."
    p "Guide me, I see nothing."
    n "Right now! Go to the middle of the river."
    "[p] form the ground into a bridge."
    n "That's sir [d]'s power..."
    p "!"
    p "I can see it now. So there was an illusion barrier here. We have to hurry!"
    scene temple 
    "[p] can sense that [d] is really close."
    p "Where Is The Stone?"
    n "Ah! Up there, on the status hands"
    p "!"
    n "!"
    d "What do we have here? A half-ass monster and a demon." with hpunch
    "[d] steps closer to [p] and [n], his footsteps become louder."
    "[p] jumps to the statue hands."
    d "Running away?"
    "A big hand slaps [p] to the ground." with vpunch
    p "Mgh!"
    "[p] forms the ground into a giant hand and attacks [d]. [d] negates it. The hand turns into dust."
    d "!"
    "[p] jumps to the status' hands. [d] destroys the status, [p] falls to the ground." with hpunch
    p "Ugh!"
    "The Stone falls to [d]'s place." with vpunch
    p "..."
    n "Ahh!"
    "A column falls onto [n]. With a swift moment, [p] pushes him away. Both fall to the ground." with hpunch
    p "Kuh!"
    d "I didn't know you were that nice."
    p "..."
    "[p] stands on 1 knee. [d] kicks the stone to [p]."
    p "..."
    d "It just a rock. I put it there 300 years ago, for stupid creatures like you."
    p "..."
    "[p] touches the stone and crush it."
    p "It holds no power. Is The Stone just a lie?"
    d "No. You are closer to it than you think."
    p "..."
    d "How about we make a bet?"
    p "What is it?"
    d "I show you where The Stone is. If you can get it or use it, I'll not touch you anymore. If not, you know what comes next."
    p "Where is the stone?"
    "[d] points toward [n]"
    p "Impossible. What kind of joke is this?"
    d "He should have died a long time ago, in a masscar between human and demon that takes place right here, in this temple." 
    d "The Stone saves him following his mother wish, a newborn child, and I put it inside his body as its will. Hard to believe huh?"
    "[d] eyes turn red. [p] can see the stone inside of [n]."
    p "..."
    "[p] penetrates his hand into [n]'s chest."
    n "Ahhh...no. Sir Knight, p-please..."
    p "Ahhh...Arghhh..."
    d "The energy born from yours and the stone contacting each other will kill [n] first, then you later."
    p "Ahhhh...Arghh...."
    n "S-sir Kni- pleas-..."
    "[p] had pass the outter barrier."
    n "Ahh...Ughhh...ahhh..."
    p "Ahhhh...Arghhh....."
    p "[n]! If you don't want to die. Use its power. Either kill me, [d], or both of us. This is a fair game. I'm not holding back."
    n "N-no. Please stop. I won't. I won't .... ahhhhh..."
    "[p] almost break the inner barrier"
    p "Arghhh...Arghhh..."
    p "(It's your false to not participate in this life and death game. Sorry)"
    "[p] remmembered the time the demon help him to get water, and his worried expression when he turns into a monster." 
    "The demon not once was afraid of him. He offers help and got his life taken away by the one he helped in return"
    "The very first reason [p] wants to become strong was to lesser his father burdern. The second reason was to make his country stronger and everyone lifes better. The third reason was to protect his dad, brother, and people he cares"
    "He doesn't know when or why things turn out this way. His country feared him, his father hated him and his brother pity him. Since when did he drop his humility and kill his opponents mercilessly?"
    "[p] cries. He puts his hand out of Nine's chest"
    n "Ahhh...haa...ahhh..."
    n "ahh..S-sir. Kni-.."
    "[p] punches [n]"
    n "Mgh!"
    p "Go away! If I ever see your face again, I'll kill you!!"
    n "...."
    "[n] runs away"
    "[d] comes closer as [p] crawing on the ground and clenches his fists."
    p "..."
    p "I lost. What do you want to do with me?"
    d "What do you think?"
    p "Stop that already. Didn't you said I'm a birdbrain? How can I know what a genius like you think?"
    jump badend




label badend:
    d "Flatering won't help you [p]. A dog shoud know its position."
    "[d] cough."
    p "Hahaha. You seems weaker despite that strong language. I, in the other hand, have become stronger and able to sense that your power is decreasing. It will never come back."
    d "..."
    p "You are so smart huh? Sharing your power to your most hateful enermy and got yourself in this state."
    "[d] eyebrowns furrow."
    p "I'll spread this news out to every creatures in this plannet. I will watch and laugh as you consumed by flame and turn into ashes even if that means I'll experience the same."
    p "The way you look at me makes me sick. Don't ever search for even a shred of empathy from me, you disgusting monster!"
    "[d] smirks." with vpunch
    "He violently kicks [p] to the ground and breaks his arm join." with hpunch
    p "Ugh...Argh!!! FUCKER!!"
    "[d] brutally tramples [p]'s broken join."
    p "ARGH!!"
    p "Uhm...n.."
    d "When you are unhappy, you sure bark and scratch a lot." 
    "[p] looks at [d] and smirks."
    "[d] clenches his fists tight, then stop and relax his muscle."
    d "Now I understand why there are so many people despite you [p]. You are as irritating as hell."
    "[d] brutally tramples [p]'s head." with vpunch
    p "Ugh! N.."
    d "Don't drive me up to a wall. There's a limit of how much I can restrain myself from breaking you completely, brat." 
    p "..."
    "[p] clenches his fist."
    d "Don't worry, I'll still keep you as a plaything even if you wreck to the point of no recovery."
    p "...Bast-"
    "Some noises coming from the ground. There are many thin shadows rising from the flow."
    p "!"
    p "W-what th-!"
    "[p] uses one hand to lifts himself up."
    "Unable to do so, he crawls."
    "[d] smirks. He kicks [p] to their way then crush his stomach with his foot."
    p "Kuk!...Ngh..."
    "[d] sqeezes it. [p] was unable to move an inch."
    p "Ngh...Kuk...L-Let..Me Go [d]!!"
    p "Ugh! Arg...! S-shit!"
    "[p] tries to get out of [d]'s grips but it was too strong. [p] was so frighten that his face become white."
    p "[d]-[d]! Let's go!"
    "[d] steps on [p]'s stomach harder, makes it more painful and difficult for him to move."
    p "Ugh!"
    p "N-No! Stop!! STOOOOOOOOPPPPPPPPP!!!"
    "Big and devasting screams echo through the temple."
    ##---
    scene throne
    "[ri] castle, in a meeting with dozens of dukes, duches, followers and generals."
    h "[k], there's a monster said he knows prince [p] where about. He also want to give you a present. We have our men circle around him."
    ren "A monster? But he knows brother whereabout."
    k "Tell him to get out! If he doesn't comply, kill him!"
    ren "But dad!"
    "There are screams outside the door. [d] walks in with some monsters. They were carrying a cart with a big blanket covered it."
    d "Dear [k], lord of the Holy Land, we know your belove son whereabout."
    k "Guards, kill them!"
    "Guards and the Generals attacks the monsters. But they are no match."
    ren "What did you do to my brother?"
    d "You don't have to worry about that."
    k "..."
    d "Because he is right here!"
    show present_snake
    k "!"
    ren "!"
    "[d] pull [p] out the cover." with hpunch
    p "Mgh! Ngh!"
    "[p] was there, his hands were tied. He was biten and penetrated by venomous snakes."
    ren "Borther!"
    h "Prince [p]!"
    "[p] reacts. The snakes bite him."
    p "UUHHMMMM...UHMMMM..."
    p "Uhmm...uhmp..."
    ren "Brother!"
    "[ren] grasps a lance from a nearby knight and rushes toward [p]."
    p "!"
    "[k] grasps [ren]'s lance and pulls him back. [ren] resists him."
    ren "LET ME GO! He'll die!"
    ren "!" with hpunch
    "[k] slaps [ren]. He falls to the ground." with vpunch
    k "Look! There's a lot of old bites. If those vemon could kill him, he would have die long ago."
    ren "..."
    k "Stay down! Don't do anything!"
    p "..."
    p "!"
    p "Ahh...Ngh..."
    d "You are right. He is now a mixture of human and a more powerful being. These mere venom cannot kill him. It just causes him severely pain and pleasure"
    "[d] kicks the cart. It turned upside down and [p] falls to the ground" with vpunch
    p "Uhh...ahhh..."
    "The snakes get out of [p]. They have had satisfy by releasing their poision, sucking his blood, energy and use his stomach to warm their eggs."
    "They come back to the ground, prepare to hatch."
    show present_push
    "No energy, [p] tries to stand up but falls to the ground. Paralized from the poison, he loses control of himself and peep."
    p "Um..."
    d "Hahaha, look at you. Cannot control your urine in front of this many people."
    "The monster wipes his pee and insert that finger into his mouth"
    show present_feedpee
    d "Suck it!"
    p "Uhm..."
    "[p] sucks [d]'s finger."
    d "Good boy!"
    "Unable to witness this scene, [ren] looks away and closes his eyes."
    ren "..."
    k "..."
    k "What do you want us to do? Creature of the Dark Forest never went outside. If it is because of [p], it is his problems. He is not a human or even a citizen here."
    p "..."
    d "Did you hear that [p]? Your dad chases you out. Isn't that bad? Ater all, you care about his opinion of you so much."
    p "..."
    k "..."
    "[d] holds [p]'s chin and hands. He pushes him forward, facing the king."
    show present_king
    d "Don't you want beg him not chasing you out and accept you?"
    p "..."
    d "Say it, don't be shy."
    p "..."
    d "Huh? Do it passionately."
    p "Y-yes...n...yes..."
    p "...P-please don't chase me out father..."
    "Thinking this might be the last time they can talk like this. [p] bites his lower lip."
    p "I'm sorry for all the fighting and agruments...I never meant it. We had never get along well..." 
    p "...but all I ever wanted was your love and acceptant...just like [ren]...I have always..."
    k "..."
    "[k] looks at [d]."
    k "Please bring him out, together with all your monsters."
    d "Isn't that too cold? He tries so hard to gather his courage."
    k "It is not necessary. He is not a citizen of this country nor human anymore."
    k "He just a disgrace. Living on his knees with no pride nor honour."
    "[p] cries. [d] releases him. [p] falls in a grovel position."
    "He uses one hand covers his tears, tries to not make any sound."
    "[d] bends over, softly pulls his hair back and kisses him."
    p "!"
    p "..."
    d "Good boy..."
    k "..."
    "[p] stops crying. [d] lets go of his lips."
    d "Since you are docile right now. I'll give you a gift."
    p  "..."
    d "Do you want your dad or brother to join you or do you want me to chase them out?"
    p "!"
    d "Don't you think they will understand you better once they are in your position?"
    # shock image, then angry image and
    p "No...no [d]...Please, chase them out..."
    # tired img
    p "..."
    "[p] glances at [d], observes his expression."
    p "...I beg you [d]. Please send them out, to another country..."
    k "..."
    d "You heard that [k], gather everyone, told them you were dethrone. Now, this country is mine. If anyone tries to escape, they will face my friends' wrath."
    k "No! please don't. Monsters of the Dark Forest like you never interested in things like this to begin with. Please don't invole the citizens into your play."
    d "If you do it well, no one will suffer greatly. Else, you will understand what is a country covers by blood means."
    k "..."
    k "I uderstand."
    "[k] looks at [p]."
    d "Do you want to beg me not to hurt him? Or do you want him to die?"
    k "Whatever I said doesn't matter anymore."
    "[d] laughs as the king walks away."
    "The king told the mages to prepare the magical sky screen for the announcement. He has a conversation with [ren]. This is the first time [p] saw [ren] and the king in a heated argument."
    "[ren] looks back at [p] and follows [k]. [p] looks at their blurry figure as they move futher and futher away."
    p "..."
    "[d] puts a collars onto [p]'s neck."
    p "..."
    "He pats his head."
    scene castle_pet
    p "Will you really keep your words this time [d]?"
    "[d] signals the servant to put a bowl of noodle near [p]."
    d "It was meant to your father but since he's gone. How about eat it like a dog?"
    p "..."
    "[p] eats the noodle. It had been long since he ate. His stomach was empty."
    d "Good. I don't want you to be hungry before visiting your citizen as my pet dog and their future king."
    p "!"
    "[d] points to a servant."
    d "This servant seems to like seeing you suffer. I'll let him walk you around and gain citizens affections."
    p "No, please [d]. I was naked and humiliated in front of my own family and everyone here. Isn't it enough? If you push more, I'll go insanse."
    d "What did I told you? As soon as you were about to break, I let you rest. The result? You just hate me more and bite me harder."
    d "You can only blame yourself for barking your master. I won't stop until you completely break and hold onto me."
    "[p] cries. [d] looks away."
    d "Make sure he greets everyone and they know that he's my dog. Also, they have my permission to do whatever they want."
    p "[d]! Please don't treat me like this."
    h "Yes sir!"
    "The servant holds the lease forward."
    h "Move fast!"
    p "[d]. Please let me stay here with you..."
    "[d] pats [p]'s head."
    d "[p]."
    p "..."
    d "Dog shouldn't talk human language."
    p "No, please [d]!"
    "[d] looks at the servant. The servant put a gag inside his mouth"
    p "Umm...n..."
    "The servant pulls the collar."
    h "Move dog!"
    "[p] turns around and pulls back in the opposite direction."
    p "N..M..."
    scene castle_whip
    "The servant whips him!" with hpunch
    p "Ugh!...M..."
    h "I said move! Do you still think you are our prince after all this? You are nothing but troubles since the day you were born. Trash!"
    p "U-uhm...n..."
    scene castle_poop
    "[p] shits himself."
    p "Ngm!"
    h "Gross! You really are trash."
    "[p] looks at [d] as he turns away."
    d "Where is the king's champer?"
    h "T-this way sir!"
    "The servant pull [p]'s collar stronger. They headed toward the castle gate where the citizen concentrate and chat with each other and the guards after hearing [k]'s last speech."
    "Their faces become furious whe they saw [p]."
    "3 days later."
    h "Sir [d], your dog had come back!"
    scene gore_back
    d "..."
    "The servant had to put [p] on a cart. He was in a critical condition." 
    "He was beaten and sratched from head to toe. Blood and sperm everywhere. His hands and legs was chopped off, his tongue is not there anymore." 
    "His eyes were taken away using a clean and neat technique"
    scene gore_back_hand
    p "U-u..a.."
    h "S-sir, you told me they can do whatever they want."
    h "I don't know how he is alive but since he still breath, I bring him back."
    scene gore_back
    d "You did a good job than I expected. And here I thought I have to pick him up from some dumpster."
    p "N..."
    scene gore_back_ass
    p "U-u...a..."
    "[d] calls a servant, they give him a thich stick. He inserts it into [p]'s ass."
    d "At least they keep the most valuable part of your body huh?"
    p "M...m u-..."
    d "I don't get what you are saying. If you can't speak, write it down."
    d "Oh, I forgot. You can't. Hahaha."
    p "Ua,...u-..."
    d "Someone put something in his mouth. It hurts my ears."
    scene gore_back_ass_sock
    p "Ggh..N!"
    p "H! H!"
    "[d] presses a button. The stick generate electric."
    p "NGH! NGH!"
    d "Not as strong as those mosquito. But it's not a bad device."
    p "NGH! N! H!"
    scene gore_back_sock
    p "H...n..."
    d "Throw him into a dog cage! Find a small one that makes he unable to move even an inch!"
    scene gore_cage
    "At night in the pet item storage room, [p] cries. He knows that his hands and legs can regenerate if he did right. But what about his eyes and tongue."
    "The things that he did to others finally comes back and bites him."
    "[p] tries, but he cannot uses the power."
    p "Hmp...ahh...mmm..."
    d "You look like a bitch in heat."
    "[p] heard [d]'s voice."
    p "...m..."
    scene gore_cage_pull with vpunch
    "[d] opens the cage and pull [p]'s hair, drags him out of the cage."
    p "Ugh! U-A..."
    p "H..."
    "[d] lets go of him." with hpunch
    scene gore_pop with vpunch
    p "N...m..."
    d "You."
    "[p]'s fences keeps coming out."
    d "So you have been holding it this hold time huh? That some disgusting stool. I wonder what did they feed you."
    "[p] clenches his whole body, tries to hold his shit in."
    p "U...Ngh..."
    scene gore_pop_pull with vpunch
    "[d] pulls [p]'s head and drags him." with hpunch
    "Hurt and scared, [p] pops even more. He even pisses himself" with vpunch
    p "U-a...n..."
    p "AA...a..."
    d "..."
    "[d] releases his hair and bend down. [p] clenches his teeth. He afraid [d] will hit him."
    "[d] carries him to the pet bath area and put him inside the biggest one."
    p "?"
    "[d] slashes water from the water storage basket to [p]. "
    p "!"
    "He aims directly at [p]'s ass to splash water"
    p "Ngh! U..."
    "At this point, [p] understands that [d] was trying to wash him. He relief." 
    "[d] spreads a few oak tree ashes into the water and takes a pinch of them, scatter his hands to washes [p]'s hair, neck, chest, back, armpit, then his cock and ass."
    scene gore_bath_finger
    p "U-a...ngh!"
    d "Hurt? Since this is a pet item storage room, there's only ashes. If it's too hard, I can get a black soap."
    "[p] shakes"
    d "No? Then what is it? Embrassing?"
    "[p] nodes"
    "[d] thrusts his finger deeper into [p]'s asshole."
    p "Ngh! N..."
    d "What is there to be shy about? There's no place in your body I haven't see. You stool and pee right before my eyes almost everyday."
    "Some tears fallen from [p]'s eyes."
    d "..."
    p "Uh!..Ugh..."
    d "What a pervert. You can even feel it in this situation."
    "[p] cries."
    d "You cried a lot these days [p]. You look cuter."
    "[d] intentionally hits on [p]'s protate again and again."
    p "Umm...Ngh..."
    p "U...a-...Ngh! M!"
    "[p] cums."
    p "Hm..n...ugh..."
    d "You cums just from fingering huh? It likes your sensation was enchance. Is that because you cannot see anymore?"
    p "..."
    "[d] bites Ray’s neck. It’s bleed." 
    p "n..h" 
    d "What you said at the temple still printed in my head Ray. My blood boil every times I saw your face."
    d "How many times had this trouble face make me stop? If you won’t shred even a piece of empathy to me, I’ll do the same."
    d "I will watch as you turn crazy and my embrace is your only salvation. You will wish everyday for my dick to fill your empty hole."
    "[p] cries. [d] kisss him."
    d "Are you hungry?"
    "[p] nods."
    d "Thirsty?"
    "[p] nods."
    d "I bring your meal here."
    "[d] uses a towel to clean [p] and lets him sit on the ground"
    "[d] carries his head and gives him water."
    p "Ugh...uhn..."
    "[d] spoons feed [p]."
    p "...a..u.."
    d "What's wrong? Oh, Seems like your jaw got dislocate. It'll be painful to chew huh?"
    "[p] nods. [d] chews the food and feeds [p] by mouth."
    p "Hmm...hmmm..."
    "[d] kisses [p]."
    p "Umh! Uhm!"
    "The kiss becomes more passionate."
    p "Uhm...Ughm!"
    "[p] kisses [d] back. Even if [d] was the one who did all these terible things, [p] glads that [d] comes and takes care of him."
    "After been through these endless pain and isolation, just [d] appearance alone gives [p] relief, just a small gentle action from him gives [p] enornous gratitude."
    "[d] stops."
    p "!"
    d "Let put you back to the cage."
    p "Ua..u..! Aa.."
    "[d] puts [p] back to the cage and locks it. He puts in some water and food in the dog feeder."
    p "Ua..a...u..."
    d "What's wrong?"
    "[p] shakes his head."
    d "Ah, it'll be painfull for you to eat and drink by yourself since your jaw was dislocate."
    d "I'll comeback tommorow and feed you."
    p "Aa...! Au....u..."
    "[d] continues to lock [p] up in that cage for 3 months. Aside from him, no one was allowed to get in."
    "Isolated, unable to see, move, speak in a silent darkness drives [p] insane to the point [d]'s voice and his carelessness are what he longs for everyday."
    "[p] hears footsteps. He knows that [d] is walking in. The door opened for a few minutes then closed."
    "He was waiting for [d] to step closer and get him out of the cage, but everything was silent."
    p "U...u.."
    "There was no response. [p] waits and waits but there is still no sound. No one was here. Was he hallucinating?"
    p "..."
    "He doesn't know how many days had passed since [d] not coming. Despite the pain, he eats and drinks in the dog feeder to survive."
    "Several days later, he heard footsteps and the sound of the opened door."
    p "A...u..."
    "[d] pulls him out of the dog cage and kisses him."
    p "Uaa...nhm..."
    "He kisses [d] back."
    d "You look more eager than usual. Do you missed me?"
    p "A..ua...a.."
    d "What does that mean?"
    "[p] nods his head and sobs."
    d "You really miss me? How cute!"
    "[p] can hear a sound of cloth smashing each other. The next thing he knows is [d] turns him around and penetrates him."
    p "M...A...Ua...h..."
    d "You feel it more today huh?"
    p "A....aua...."
    d "How does it feel become one with me? Do you like it?"
    p "A...h...ngh...aa..."
    "[p] softly nods multiple times while crying and moaning. [d] smirks."
    d "I like to become one with you too."
    a "U...ngh...n..aa..."
    "[p] cum."
    p  "M...n..."
    "[d] touches [p]'s hair."
    d "After today, it'll took a week until I can get here again."
    p "U..a..."
    d "There was a lot of interesting things to do now I'm in charge of this castle."
    p "A...u..."
    "[p] presses his head into [d]'s chest. [d] careless his head."
    d "Do you want to come with me? I'll let you lie on the throne. I'll sit on your face while your cock and asshole expose to everyone."
    p "U...a...uaa..."
    d "What?"
    "[p] nods."
    d "Hahaha, are you that desparate? You make me want to cry now."
    "[p] presses his face in [d]'s chest harder and kisses it. [d] notices and touches his face."
    d "How about this prince? I will return your body to normal, make you king like you always wanted."
    p "!"
    d "In return, be docile and act cute. Listen and follow my every word, as if I'm your God."
    p "A...a..."
    "[p] nods."
    d "Good boy."
    "[d] stands up, creates an energy sphere and pushes it to [p]. His whole body glows up and returns to normal."
    "[d] coughs. He just gives [p] more of his energy. It goes so smoothly because [p] desperates for it."
    p "A..."
    "[p] looks around with his eyes, holds his throat, touches his arms and legs."
    p "A...haha..."
    "[p] cries. He covers his face with his 2 hands."
    d "Remembered what you promise [p]. Don't go back on your words just because you were healed."
    p "T-.."
    d "Huh?"
    "[p] whole body tremble, his voice cracks up as his tears keep falling down."
    p "T-thank you...[d]."
    "[d] was suprised. This is the first time he really saw that gratitue and happy expression from [p]. It was toward him even though he was the one who causes all of it."
    "Has [p]'s mind finally breaking apart?"
    "[p] grasps [d]'s trouser."
    d "What do you want now?"
    "[p] hugs his leg tight and rubs his head there."
    p "P-please [d], stay like this for a little longer."
    d "..."
    d "I'm not planning to go anywhere..."
    if talk>=18:
        "It reminds [d] of that time when [p] held his hand with a shy expression. [d] was really happy." 
        "He doesn't really remember what makes it turn to this, but he remember the emtiness and dissapoinment he felt, as well as the anger that makes his blood boil."
        d "..."
        "He looks at [p], who still clings onto his leg and cry."
        "He kisses [p]."
        p "..."
        "[p] hugs [d] tight."
        p "Please [d], stay like this with me."
        "[d] hugs [p] back."
        d "I know. I'll stay with you in here until you sick of it."
        p "..."
    "At the throne room, [p] sits on [d] and pleasure him while the meeting taken live using magical sky screen."
    p "Ahhhh...aaa..."
    d "Don't be so passionate, king [p]. You know that your men and citizens are watching right?"
    p "Aaa...Uhm...[d]...[d]..."
    d "Hgh!"
    h "And for the finale situation, the North had been in a huge drought. It's devasting there, king [p]. What do you suggest us to do?"
    p "..Ahh...haaa..."
    p "....A...S-stop the taxes...a...and...ngh...transfer...water there...uhm..."
    d "Hgh!"
    h "King [p], we already thought of that but the water won't be enough..."
    d "We need more money to spent on parties and decorations [p]."
    p "...A...uhm..."
    "[d] observes [p]."
    p "A...r-raise other places' tax...uhm..."
    d "That won't be enough."
    h "K-king [p]..."
    p "Ahh...r-raise other places' tax, and tax the North like usual...uhm..."
    d "That's my belove king. You heard him."
    h "Y-yes your Majesty!"
    p "Ahh...a..."
    "[p] cums."
    p "A..haa..."
    "[d] careless his cheek and glance at his empty face."
    d "Do you despite me for turning you into this?"
    "[p] touches [d]'s hand."
    p "[d]...[d]..."
    d "..."
    p "[d]...my savior...my salvation...my God..."
    d "You completely lost it huh?"
    p "Please [d], don't ever leave me... I'm nothing, I can't do anything without you..."
    p "I love you. Please, don't ever leave me alone."
    "[p] hugs [d] tightly. [d] hugs him back."
    d "Listen [p]. Even if you are too broken that you shatter into pieces, I will never leave you, got it?"
    p "[d]...my God...I love you..."
    d "I love you too, [p], since the day I met you."
    "[p] cries. He hugs [d] tighter. There was no sound comming from him, but [d] can feel a lot of tears falling into his chest." 
    "[p]'s determined and stubborn side had gone, the only things left were is his weak, submissive and dependent side."
    "[d] wipes his tears, and sit in the same position until [p] stops crying and passes out."
    "[d] careless [p]'s sleeping face and kissed his head."
    p "Uhm..."
    d "You finally belong to me now."
    ## At this point Ray doesn’t know what hate and like are anymore

    "End"

    return





    

label goodend:
    "[d] touches [p]'s chin and moves it up."
    p "..."
    "[d] kisses [p]"
    p "n!"
    "[d] kisses him harder"
    p "..."
    "[d] stops."
    p "..."
    p "I told you that I started to regret. Yet I almost kill another innocent soul. I'm really deserve whatever you did to me."
    d "..."
    "[d] hugs him."
    d "I know you will not do it."
    p "What do you know about me?"
    d "I know since I first saw you. Underneath that prideful and ruthless mask is a very gentle and vulnerable soul..."
    p "!"
    "[p] cries." 
    "No one had ever describes him that way. He doesn't know if it's true or not, but it hurts."
    p "(My wounds...)"
    d "..."
    "[d] takes a deep breath. He looks tired. He had lost a lot of mana and energy."
    p "Why? Why did you do all of this?" 
    p "I hate you. I hate being alive. Whatever you do, I won't show gratitue."
    d "Have you figure it out yet? The thing I want you to give me?"
    p "..."
    "[p] shooks his head."
    p "No. Do you want to take it now?"
    "[d] smirks."
    d "You are really birdbrained."
    p "..."
    "Somehow, at that moment, [p] doesn't feel humiliated. He just saw the sadness in [d]'s eyes."
    p "..."
    p "One day I'll kill you and all of the things related to you, including this God you keep talking about."
    "[d] smiles."
    d "I'll be waiting."
    p "..."
    "That's unpleasant feeling re-appear again. [p] feels like his body burning. It makes [p] feels unwell." 
    "It was just an unconsious action, [p] looks up at [d]'s face. He is looking at the thing he had always avoid remembering."
    "Now, the blury figure of an unknow man constantly fucking, degrading him, and caring him had become so clear and real."
    "In disregard to [p]'s thought, [d] doesn't have that mean look on him. On the contracy, [p] sees a compassionate and humanely face."
    "[p] wonders if he is in his right mind."
    d "..."
    d "Is there something on my face?"
    "[p] looks away."
    "[d] moves closer and touches [p]'s face."
    d "You feel hot. It's not enough to be a fever but that must be uncomfortable. Have a rest."
    p "..."
    "[p] looks uncomfortable. He sweats, his muscle becomes tenses and his heart races faster."
    p "I-I'm fine. Please don't touch me. I..."
    p "..."
    d "..."
    "[p]'s face becomes all red. [d] releases his hand."
    "After pausing for a moment, [p] glance at [d]."
    "It's not a normal one but a shy glance. Like he wants something but embrassing to say it, he doesn't want [d] to know but his eyes got caught." 
    "Suprise, four eyes look at each other for a few second then [p] looks away."
    p "..."
    "[d] pushes him to the ground and kisses him."
    d "You are hot, and this place is hard. It must be painful to endure."
    "[d]'s words embrassed [p]."
    p "..."
    d "Your endorphins levels went high because of our intense fight just now. It increases your sex drive. This is just human's nature. No need to be shy."
    p "..."
    p "!"
    "[d] holds [p] up, in the spoon position."
    d "I'm not going to serve you forever [p], I don't care if you feel ashamed or not. If you want it, do it yourself."
    p "..."
    p "I-..."
    "[p] closes his eyes and puts [d]'s dick in."
    "[d] moves up while pushing [p]'s hip down."
    p "No! Ahhh! What are y-"
    "[d] smirks."
    p "N...Aaaa..."
    "[p] falls on [d]'s shoulder."
    p "Ngh...n..."
    p "!"
    "[d] puts [p] on a fallen column and thurst his cock in"
    p "Ahh...[d]..This position...Too deep..."
    "[d] smirks"
    d "You like it better right? I'll compensate for all the time we miss."
    p "M...ahh...[d]...please..."
    d "What? What do you want me to do [p]? If you told me to stop, I'll do it."
    p "Ngh...ahhh...uhm..."
    d "Huh?"
    p "Ahh...N-no, please don't stop..."
    p "[d]..d-deeper...s-slower...ahhh"
    d "You like it slow? I will go as slow as the speed your brain functions."
    p "Ahhh...[d]...[d]...ahhh..."
    d "If you are satisfy, tell me. So I can make this obscene hole feel better."
    p "Ahhh...ahhhh...[d]"
    "[d] moves faster."
    d "Uhm...n..."
    p "Ahhh... it's good, it so good..."
    p "uhm...ahhhh...[d]..."
    d "Ngh..."
    "[d] moves even faster."
    p "hmmm...ahhh...[d]...Too fast..."
    p "hmm...[d]..."
    d "Ngh...[p]...Call my name more..."
    p "Ahhh...[d]...[d]... I-I..I can't keep up...please...."
    d "..."
    d "Ngh...."
    p "Ahhh...please slow down...ahhh..."
    "[d] returns to his normal speed."
    p "Ahhh...good...You are great...ahh..."
    p "I-I...you...ngh...ahh...I...haaa..."
    d "..."
    d "I love you [p]..."
    p "..."
    p "ahhh...hmp...ahhh...[d]..."
    # cum
    p "ahh..ahh...[d]"
    "After a while"
    d "You cum a lot [p]. Are you still alive?"
    p "Still conscious..."
    d "Good."
    "[d] reaches his arm and leg to [p]'s body like he hug a pillow."
    d "Warm."
    p "I'll be with you on my free will if that's what you want."
    d "Huh?"
    p "I said I'll be with you on my own free will."
    d "..."
    p "Go together with me to where I want [d]. Give me freedom."
    d "..."
    "[d] smiles."
    d "We can do that while you cotinue to figure out what I really want from you."
    p "..."
    "[p] turns back and hug [d]"
    p "I'm going to sleep."
    d "Tommorow I'll look for some clothes for you, unless you want to travel naked."
    p "!"
    p "W-who would want that."
    "[d] laughs."
    p "An-and you need money to buy cloth. Do you even have that?"
    d "Money, it falls everywhere in this forest, from flee and dead man. It's enough to even buy a legendary weapon."
    p "..."
    p "()"
    "[p] holds [d] tighter"
    "[d] stokes his head and kisses on his forehead"
    d "Goodnight [p]."
    p "..."
    "[p] hugs [d] tighter and closes his eyes."
    p "(The weather's warm today)"
    d "If you are still awake, today is a starry night."
    p "..."
    "[p] looks at the sky of a thousand stars."
    p "It's beautiful."
    d "It is."
    "END"
    return
    

  