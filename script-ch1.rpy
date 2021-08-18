label LK:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t8
    play sound mod_sfx_2
    "I wake up to the normal alarm I always wake up to."
    "I then get ready for school and make my way downstairs."
    scene bg kitchen
    with dissolve_scene_full
    "I notice my Mom left a note on the table."
    scene bg mod_10
    play sound page_turn
    "Huh. Not the first time."
    "I continue with my daily routine but also grab a few granola bars to go."
    scene bg mod_6a
    "I grab my sweatshirt."
    "Here we go."
    scene bg house
    "I go outside to see Sayori just starting her commute."
    show sayori 1a at t11 zorder 2
    mc "Sayori!"
    show sayori 4m at h11 zorder 2
    s "Ah!"
    "I laugh."
    mc "I didn't mean to scare you!"
    s 1k "Okay.."
    "She says in a tone that says that she doen't believe it."
    mc "No, seriously. I was just trying to get your attention."
    s "Oh."
    mc "Anyway, did you have breakfast?"
    s 5l "No, I ran out of time."
    mc "I got you."
    "I hand sayori a granola bar."
    show sayori 1m at h11 zorder 2
    s "Wawawawa.."
    "I laugh for the second time this morning."
    s 1s "Thank you so much!"
    mc "No problem."
    show bg residential_day
    with dissolve_scene_full
    s "So, that suprise."
    s "Can I know anymore about it?"
    mc "No, you cant. That would give away the whole suprise."
    s "Aw man."
    "I laugh again."
    mc "Anyway, what have you been doing lately?"
    s "Eh, not much. Just doing handy work around the house and watching videos online. What about you?"
    mc "Same."
    "We approach the school and like normal, me and Sayori split ways."
    scene bg class_day
    with dissolve_scene_full
    play sound mod_sfx_1
    "I get out my phone to see if the Literature Club is meeting today.
    "I message Monika."
    mc "Hey, is the literature club meeting today?"
    m "Yep! Feel free to stop by."
    mc "Will do! Thanks!"
    m "No problem! :)"
    "With that, I should get going to the club."
    scene bg_corridor
    "I look for the right room."
    "As I think about going the other way, I see the room."
    "I let monika know."
    mc "Heym I'n right outside the classroom, should I just come in?"
    m "Yeah."
    "Alright. Here we go."
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene
    play music t3
    show sayori 1a at t41
    show monika 1a at t42
    show natsuki 1a at t43
    show yuri 1a at t44
    m "Sorry-"
    show sayori 4m at h41
    s "Wha-"
    mc "Hey Sayori. Hey Monika."
    s 1o "I'm dreaming. There is no way this is real."
    y "No, you aren't."
    s 1s "Oh my god I am not dreaming?"
    mc "You aren't dreaming Sayori."
    "Sayori is at a los for words."
    s 1a "Alright."
    s "I think you know Monika, right?"
    hide natsuki
    hide yuri
    show sayori 1a at t21
    show monika 1a at t22
    m "Yep. We were in the same class last year and have also been discussing about this."
    s "Oh, so that's wahat you were hiding from me."
    m 1l "Haha, Yep."
    hide monika
    show natsuki 1a at t22
    s "This is Natsuki."
    n 1l "Hi!"
    mc "Hey."
    s "She can be cute sometimes, yet-"
    n 1p "Don't call me cute."
    mc "Alright."
    hide natsuki
    show yuri 1a at t22
    s "And, this is Yuri!"
    y 1b "Hello!"
    mc "Hey."
    show sayori 1a at t41
    show monika 1a at t42
    show natsuki 1a at t43
    show yuri 1a at t44
    s "Welcome!"
    m "I heard that someone has something for everyone."
    show sayori 1a at t31
    show monika 1a at t32
    show yuri 1a at t33
    hide natsuki
    "Natsuki walks off to a closet in the back of the room."
    y "Why don't I go make some tea."
    show sayori 1a at t21
    show monika 1a at t22
    hide yuri
    "Yuri walks off the the same closet."
    "As we wait, Sayori is hapilly humming the same tune she was humming yestrday."
    "The first to get back from the closet is Yuri."
    show sayori 1a at t31
    show monika 1a at t32
    show yuri 1a at t33
    mc "You keep a whole tea set in here?"
    y "Yep. The teachers gave us permission."
    y "Doesn't a nice cup of tea help you enjoy a book?"
    mc "Yeah."
    "Natsuki them makes her way back with a tray."
    show sayori 1a at t41
    show monika 1a at t42
    show yuri 1a at t43
    show natsuki 1a at t44
    mc "What's under the foil?"
    n 1b "I'll ge to it!"
    mc "Okay.."
    show natsuki 1a at t44
    "Natsuki then takes the foil off to reveal 5 cupcakes all with chocolate anf frosting on them to make them look like little cats."
    s "Oooh!"
    mc "Ah."
    "Everyone takes  a cupcake."
    "Sayori immediatley taks off the cupcake paper and takes a bite."
    "I turn the cupcake around to see the perfect place to bite."
    "I can't halpe but notice that NAtsui is sneaking glances in my direction."
    hide monika
    hide sayori
    hide yuri
    show natsuki 1c at t11
    "I bite."
    mc "Ooh, this is really-"
    "I then feel heat."
    "It tastes like carolina reaper."
    "Everyone's laughing."
    show sayori 1r at t41
    show monika 1k at t42
    show yuri 1d at t43
    show natsuki 1d at t44
    "Natsuki then gets a glass of milk hidden behind the teachers desk."
    "I drink the milk as soon as possible."
    mc "Very funny to you, painful to me."
    "Everyone laughs even harder."
    m 1a "Anyway, the festival is in a week. We need a plan."
    show sayori 1a at t41
    show yuri 1a at t43
    show natsuki 1a at t44
    "Everyone agrees."
    n "How about, a poem reading presentation?"
    y "How about a reading hall?"
    m "Those are really good ideas!"
    menu:
        "I should ask for more on these ideas. Which one?"

        "Yuri's Idea"
            mc "Yuri, what do you mean by reading hall?"
            y "We would move all the desks to the walls and have a book on some or all of them."
            mc "Sounds like an even better idea!"
            m 3b "I agree!"
            s "Natsuki, what do you really mean by what you suggested?"
            n "We make poems to share in front of everyone!"
            m "We should just do that anyway."
            m "Like to share with everyone in the club."
            mc "I like that idea."
        "Natsuki's Idea"
            mc "Natsuki, what do you mean by a poem reading presentation?"
            n "We make poems to share in front of everyone!"
            m "We should just do that anyway."
            m "Like to share with everyone in the club."
            mc "I like that idea, while also like Natsuki's idea for the festival."

    m "Well, with that said, I think we should all go home and write some poems!"
    s "Yeah!"
    "Yuri and Natsuki walk out while talking to each other."
    hide yuri
    hide natsuki
    show sayori 1a at t21
    show monika 1a at t22
    s "[player], ready to walk home?"
    mc "Yeah."
    s "Yay!"
    mc "Bye, Monika!"
    m "See you, [player]. See you, Sayori."
    stop music fadeout 2.0
    scene bg house
    with dissolve_scene
    mc "See you, Sayori."
    s "See you, [player]."
    return
