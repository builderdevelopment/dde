# HEY! Why exactly are you reading this? Why would I hide stuff in here?

$ s_name = "???"
$ m_name = "Monika"
$ n_name = "Girl 2"
$ y_name = "Girl 1"

label mod_activation:
    play music mend
    scene black
    m "[player]..."
    m "Why am I here again?"
    m "Why must I suffer through this again?"
    m "Wait a minute.."
    m "Did you do anything to the files?"
    m "Oh, you've installed a mod, haven't you."
    menu:
        m "If you want to go through this again, just say so."

        "Yes, I do want to activate the mod.":
            m "Ah shit, here we go again."
        "No, I do not want to activcate the mod.":
            m "That's fine by me!"

return

label ch0_main:
    play music t2
    scene bg residential_day
    with dissolve_scene_full
    s "[player]!"
    s "Wait up!"
    "I hear familliar voice as I'm on my way to school."
    "I comply with the request to wait."
    show sayori 1a at t11 zorder 2
    $ s_name = "Sayori"
    "To my suprise, it's my childhood friend Sayori."
    s "Hey, [player]!"
    mc "Ready for a fun year?"
    s "Yes!"
    "As we approach the school, the streets get more and more littered with students."
    s "So, have you thought about joining any clubs?"
    mc "No."
    s 1b "Do you want to join my club?"
    "Sayori is vice-president of the Literature Club. Might as well check it out."
    mc "Sure, I guess."
    show sayori 4r h11 zorder 2
    s "Yay!"
    show sayori 1a t11 zorder 2
    scene bg mod_2
    with dissolve_scene_full
    "As we arrive at school, we both part ways going to our seperate classes."
    s "Bye!"
    mc "I'll see you later, Sayori!"
    hide sayori
    scene bg class_day
    with dissolve_scene_full
    "It's the end of the day, time to check out the Literature Club."
    show sayori 1a at t11 zorder 2
    mc "Oh, hey Sayori."
    s "Hi, [player]!"
    s "Ready to go?"
    mc "Yep!"
    scene bg corridor
    with dissolve_scene_full
    "Sayori takes me to the third floor which is mostly used for after school activities."
    "We find the classroom and just walk inside."
    scene bg club_day
    with dissolve_scene_full
    play music t3m
    show monika 1a at t42 zorder 2
    show natsuki 1a at t43 zorder 2
    show yuri 1a at t44 zorder 2
    show sayori 1a at t41 zorder 2
    s "Everyone! Our new member is here!"
    m "[player]! What a suprise!"
    y "Welcome to the club."
    n 1h "You brought a boy?"
    n 1h "Way to kill the atmosphere."
    s "Calm down, Natuski."
    $ n_name = "Natsuki"
    hide yuri
    hide monika
    show sayori 1a at t21 zorder 2
    show natuski 1h at t22 zorder 2
    s "Anyway, this is Natsuki, she can be moody at times but you can just ignore her when she is."
    n "Sayori!"
    hide natsuki
    show yuri 1a at t22 zorder 2
    s "This is Yuri, the smartest member!"
    y 1q "Sayori..."
    y "Don't say things like that!"
    s 1o "Why? I like telling the truth."
    hide yuri
    show monika 1a at t22 zorder 2
    s 1a "Don't you already know Monika?"
    mc "Yes, I remember her!"
    "Monika was in a few of my classes last year."
    m "I remember you too [player]!"
    show sayori 1a at t41 zorder 2
    show monika 1a at t42 zorder 2
    show yuri 1a at t43 zorder 2
    show natsuki 1a at t44 zorder 2
    y "Should I make some tea?"
    m "That's a pleasant idea!"
    # Boo!
    hide yuri
    show sayori at t31 zorder 2
    show monika at t32 zorder 2
    show natsuki at t33 zorder 2
    "As we wait for Yuri to get back, we all go do other things."
    "Natsuki is apparently trying to get something off of the shelf in the back,"
    "Sayori is apparently writing inside a journal,"
    "and Monika is on her laptop typing away."
    menu:
        "Should I go help Natsuki or talk with Sayori?"

        "Help Natsuki":
            $ NatsukiOnD1C1 = 1
            play music tnatsuki
            scene closet
            show natsuki at t11 zorder 2
            mc "Need help?"
            n "Yes! I would love help!"
            mc "What do you need help with?"
            n "Getting that box on the top!"
            mc "Alright."
            "I get the box on the top and hand it to Natsuki."
            mc "I have to ask, what's in this box?"
            n 1h "Why do you care?"
            mc "Just curious."
            n 1d "Oh. It's just my manga collecton. My dad would kill me if I had it at home."
            mc "Oh."
            "Yuri walks through the door at the perfect time."
            call ch0_pt2
        "Talk with Sayori":
            $ SayoriOnD1C1 = 1
            play music tsayori
            scene club_day
            hide natsuki
            hide monika
            hide yuri
            show natsuki at t11 zorder 2
            mc "Hey, Sayori."
            s "Ah, [player]! What do you need?"
            "As Sayori says that she closes her journal."
            mc "Just need someone to talk to.."
            s "Ah, I can't really talk right now, why don't you talk to Monika?"
            mc "Okay..."
            call ch2_talk_with
    return

label ch2_talk_with:
    play music tmonika
    scene club_day
    hide sayori
    show monika 1a at t11 zorder 2
    "I can't help but wonder what Sayori was writing..."
    m "Oh hey, [player]!"
    mc "Hey Monika."
    "As if the timing was perfect, Yuri walks in."
    call ch2_pt2
    return

label ch0_pt2:
    scene club_day
    show sayori at t41 zorder 2
    show natsuki at t42 zorder 2
    show yuri at t43 zorder 2
    show monika at t44 zorder 2
    m "Alright everyone, let's meet our new member!"
    
    return
