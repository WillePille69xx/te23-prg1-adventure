import time

adventure = [
    {
        "id": 1,
        "title": "\nThe First Step into Darkness",
        "text": "You stand before a swirling vortex of shadows, its edges flickering like dying embers. The air hums with an eerie resonance, whispering forgotten names. You feel the weight of countless unseen eyes watching you. The creatures in the dark tremble, for they know what you are. Cold. Calculating. Unpredictable. \n\nA choice stands before you: step into the portal and embrace the unknown, or turn away and let curiosity gnaw at your mind forever.",
        "options": [
            {"text": "Step into the portal.", "next_id": 2},
            {"text": "Turn away and leave.", "next_id": 99}
        ]
    },
    {
        "id": 2,
        "title": "\n\nWelcome to the Nightmare",
        "text": "The darkness consumes you, stretching into infinity. Then, suddenly, you land in a realm of twisting corridors, filled with whispers that slither into your ears. Shadows move, but nothing casts them. The scent of decay lingers. \n\nAhead, a doorway pulses with unnatural energy. To your left, a winding staircase vanishes into blackness. To your right, a mirror reflects something that isn’t you. \n\nA faint sound echoes behind you—footsteps? No, more like scraping claws against stone. Something is here, unseen but watching. You can feel its anticipation.",
        "options": [
            {"text": "Enter the doorway.", "next_id": 3},
            {"text": "Ascend the staircase.", "next_id": 4},
            {"text": "Look into the mirror.", "next_id": 5},
            {"text": "Turn around and confront whatever is watching.", "next_id": 6}
        ]
    },
    {
        "id": 3,
        "title": "\nThe Pulsing Doorway",
        "text": "You step through the doorway, and a jolt of energy courses through your body. The walls breathe, shifting as if they are alive. A faint, ghostly figure stands in the center of the room, its face a blur of agony. It raises a trembling hand toward you. Do you listen, attack, or attempt to bypass it?",
        "options": [
            {"text": "Listen to the ghost.", "next_id": 7},
            {"text": "Strike first.", "next_id": 8},
            {"text": "Ignore it and move past.", "next_id": 9}
        ]
    },
    {
        "id": 4,
        "title": "\nThe Endless Ascent",
        "text": "You place a foot on the first step, and the staircase groans beneath you. As you ascend, the darkness thickens, pressing against your skin like damp cloth. The air grows colder, each breath turning to mist. Halfway up, a faint, flickering light appears ahead. A whisper calls your name. Do you continue upward, investigate the whisper, or turn back?",
        "options": [
            {"text": "Continue upward.", "next_id": 10},
            {"text": "Investigate the whisper.", "next_id": 11},
            {"text": "Turn back.", "next_id": 12}
        ]
    },
    {
        "id": 5,
        "title": "\nThe Mirror's Deception",
        "text": "You step closer to the mirror, and your reflection stares back with unsettling stillness. Its eyes, however, are wrong—too sharp, too knowing. Then, it smiles. You do not. A hand reaches from within the glass. Do you accept it, break the mirror, or step away?",
        "options": [
            {"text": "Accept the hand.", "next_id": 13},
            {"text": "Break the mirror.", "next_id": 14},
            {"text": "Step away.", "next_id": 15}
        ]
    },
    {
        "id": 6,
        "title": "\nThe Watcher in the Dark",
        "text": "You spin around, the shadows shifting with you. At first, nothing. Then, the air distorts, revealing a figure—tall, hunched, its skin a writhing mass of darkness. It does not attack. It only watches. A voice, brittle as dead leaves, hisses in your mind: ‘Why have you come?’ Do you answer, attack, or flee?",
        "options": [
            {"text": "Answer the entity.", "next_id": 16},
            {"text": "Attack it.", "next_id": 17},
            {"text": "Flee into the corridors.", "next_id": 18}
        ]
    },
    {
        "id": 7,
        "title": "\nThe Ghost’s Warning",
        "text": "You remain still, watching as the ghost struggles to form words. Its voice is a whisper of wind through cracked stone: ‘She waits… the one with the torn mouth. She will ask… do not answer…’\n\nBefore you can ask anything, the ghost vanishes, leaving behind a small, glowing charm pulsing with energy. You pocket it, feeling its power.\n\nYou hear something approaching from the hall. Do you prepare to fight, hide, or move forward?",
        "options": [
            {"text": "Prepare to fight.", "next_id": 19},
            {"text": "Hide in the shadows.", "next_id": 20},
            {"text": "Run away quickly.", "next_id": 21}
        ],
        "loot": "a small, glowing charm"
    },
    {
        "id": 8,
        "title": "\nFirst Strike",
        "text": "You don’t hesitate. The moment the ghost raises its hand, you lash out. Your fist passes through it, but a wail of agony fills the air. The walls tremble, and the ghost dissipates, leaving behind a faintly glowing blade. It hums with latent energy. Do you take the blade or leave it?",
        "options": [
            {"text": "Take the blade.", "next_id": 22},
            {"text": "Leave it and move forward.", "next_id": 23}
        ]
    },
    {
        "id": 9,
        "title": "\nMoving Past the Dead",
        "text": "You step past the ghost, ignoring its presence. It lets out a rattling sigh and vanishes into the shadows. A chilling sensation lingers on your skin. \n\nSomething glints on the ground where the ghost once stood—a rusted key. Do you pick it up or keep moving?",
        "options": [
            {"text": "Pick up the key.", "next_id": 24},
            {"text": "Ignore it and move on.", "next_id": 25}
        ]
    },
    {
        "id": 10,
        "title": "\nContinue Upward",
        "text": "You press on, ignoring the whispering air and the cold that seems to crawl under your skin. The staircase continues upward, the steps creaking beneath your weight. As you near the top, the light grows brighter, casting eerie shadows on the walls. You reach the top and step into a vast room, its walls covered in strange symbols. In the center, a massive stone statue of a robed figure stands, its eyes glowing faintly. Do you investigate the statue, search the room, or leave it be?",
        "options": [
            {"text": "Investigate the statue.", "next_id": 22},
            {"text": "Search the room.", "next_id": 23},
            {"text": "Leave it be and descend.", "next_id": 24}
        ]
    },
    {
        "id": 11,
        "title": "\nInvestigate the Whisper",
        "text": "The whisper grows louder as you move closer to the source. It is the voice of a woman, speaking words in a language you cannot understand. The closer you get, the more oppressive the air becomes. Suddenly, a hand reaches out from the shadows, grabbing your wrist. You pull back in fear, but the hand holds tight. A figure steps out of the darkness—a tall, gaunt woman with hollow eyes. Do you struggle to escape, speak to her, or fight back?",
        "options": [
            {"text": "Struggle to escape.", "next_id": 25},
            {"text": "Speak to her.", "next_id": 26},
            {"text": "Fight back.", "next_id": 27}
        ]
    },
    {
        "id": 12,
        "title": "\nTurn Back",
        "text": "You decide to turn back, but the staircase behind you has vanished, replaced by an endless void. The darkness presses closer, and the air grows colder still. You hear a soft, mocking laugh from the void. It seems there is no turning back now. Do you move forward into the void, search for another exit, or wait and hope the way opens again?",
        "options": [
            {"text": "Move forward into the void.", "next_id": 28},
            {"text": "Search for another exit.", "next_id": 29},
            {"text": "Wait and hope the way opens again.", "next_id": 30}
        ]
    },
    {
        "id": 13,
        "title": "\nAccept the Hand",
        "text": "You decide to accept the hand reaching out from the mirror. As soon as you touch it, the world around you warps, and you are pulled into the mirror itself. The cold, glassy surface surrounds you as you fall through an endless tunnel of shifting images and faces. Finally, you land on the cold floor of a darkened chamber. A figure stands before you, its face obscured by shadows. Do you approach the figure, speak, or prepare for a fight?",
        "options": [
            {"text": "Approach the figure.", "next_id": 31},
            {"text": "Speak to the figure.", "next_id": 32},
            {"text": "Prepare for a fight.", "next_id": 33}
        ],
    },
    {
        "id": 14,
        "title": "\nBreak the Mirror",
        "text": "You decide to break the mirror. With a sharp crack, the glass shatters, and the room goes dark. A sudden, overwhelming silence fills the space. You hear something shift behind you. The broken pieces of glass begin to move, forming into a jagged shape that lunges at you. Do you fight the shape, or run?",
        "options": [
            {"text": "Fight the shape.", "next_id": 34},
            {"text": "Run.", "next_id": 35}
        ]
    },
    {
        "id": 15,
        "title": "\nStep Away",
        "text": "You decide to step away from the mirror, the hand retracting as soon as you do. The reflection in the mirror morphs into something unrecognizable, its features shifting in unnatural ways. The room begins to hum with energy, and you feel something pulling at you. Do you leave the room, investigate the reflection further, or attempt to touch the mirror again?",
        "options": [
            {"text": "Leave the room.", "next_id": 37},
            {"text": "Investigate the reflection.", "next_id": 38},
            {"text": "Touch the mirror again.", "next_id": 39}
        ],
    },
    {
        "id": 16,
        "title": "\nAnswer the Entity",
        "text": "You decide to answer the entity. The words you speak are swallowed by the air, as if the darkness itself has absorbed them. The figure steps closer, its form shifting as it moves. A low voice responds: ‘Curious, but not wise.’ Suddenly, the shadows around you twist and darken. The entity extends a clawed hand, offering you a choice: power, knowledge, or freedom. Which will you choose?",
        "options": [
            {"text": "Choose power.", "next_id": 40},
            {"text": "Choose knowledge.", "next_id": 41},
            {"text": "Choose freedom.", "next_id": 42}
        ],
    },
    {
        "id": 17,
        "title": "\nAttack the Entity",
        "text": "You choose to attack the entity. You lunge forward, but as your hand reaches for it, the darkness around you seems to fight back. Your body is pulled into the air, suspended by unseen forces. The entity’s voice echoes in your mind: ‘Foolish. You cannot fight the shadows.’ It releases you, and you fall to the ground, disoriented. The creature is gone. Do you rest, search for an exit, or explore the dark corners of the room?",
        "options": [
            {"text": "Rest.", "next_id": 43},
            {"text": "Search for an exit.", "next_id": 44},
            {"text": "Explore the dark corners.", "next_id": 45}
        ],
    },
    {
        "id": 18,
        "title": "\nFlee into the Corridors",
        "text": "You decide to flee into the corridors. The darkness seems to stretch endlessly in every direction. Your footsteps echo in the silence, but the sound soon becomes drowned out by the growing hum of distant voices. Shadows loom at the edge of your vision, always just out of sight. Do you follow the voices, hide in the shadows, or continue running?",
        "options": [
            {"text": "Follow the voices.", "next_id": 46},
            {"text": "Hide in the shadows.", "next_id": 47},
            {"text": "Continue running.", "next_id": 48}
        ],
    },
    {
        "id": 19,
        "title": "\nPrepare to Fight",
        "text": "You brace yourself, drawing upon the charm's energy. The sound of approaching footsteps grows louder. Suddenly, a monstrous creature emerges from the shadows—its form distorted and writhing. It has no face, just a black, gaping void where its head should be. It screeches in a high-pitched, ear-splitting wail as it lunges toward you. You raise your fists, prepared for the battle ahead.",
        "options": [
            {"text": "Attack with the glowing charm.", "next_id": 49},
            {"text": "Lash out with your fists.", "next_id": 50},
            {"text": "Dodge and wait for an opening.", "next_id": 51}
        ]
    },
    {
        "id": 20,
        "title": "\nHide in the Shadows",
        "text": "You slip into the shadows, hoping to evade whatever is coming. The creature moves past you, its formless body scraping against the walls. You hold your breath, heart pounding, as it stops just inches from where you are hidden. The air thickens with dread as the creature sniffs the air. It seems to sense you, but it doesn't move further. Time feels frozen. Will it find you, or will it move on?",
        "options": [
            {"text": "Wait and watch.", "next_id": 52},
            {"text": "Sneak around it and escape.", "next_id": 53},
            {"text": "Attack now while it’s distracted.", "next_id": 54}
        ]
    },
    {
        "id": 21,
        "title": "\nRun Away Quickly",
        "text": "You decide to abandon all thoughts of confrontation and sprint away, your footsteps echoing in the silent corridors. The darkness seems to press in around you, but you push forward. Your chest tightens with fear, yet there’s a strange exhilaration in the flight. You round a corner, only to find yourself facing an even darker hall. Something’s off. The walls seem to pulse with energy. Do you keep running, or stop to investigate?",
        "options": [
            {"text": "Keep running.", "next_id": 55},
            {"text": "Stop and investigate the pulsing walls.", "next_id": 56},
            {"text": "Hide and wait for something to happen.", "next_id": 57}
        ]
    },
    {
        "id": 22,
        "title": "\nInvestigate the Statue",
        "text": "The stone statue looms above you, its eyes glowing faintly. The symbols etched into its base seem to shift as you study them, a cryptic language you can’t decipher. The atmosphere grows heavier as you step closer. Suddenly, the eyes of the statue flicker, and you feel a tug at your mind, as if the statue is trying to communicate. Do you touch the statue, speak to it, or step back?",
        "options": [
            {"text": "Touch the statue.", "next_id": 58},
            {"text": "Speak to the statue.", "next_id": 59},
            {"text": "Step back and search the room.", "next_id": 60}
        ]
    },
    {
        "id": 23,
        "title": "\nSearch the Room",
        "text": "You turn away from the statue, deciding to explore the rest of the room. As you move deeper into the space, your gaze falls on strange markings on the walls—symbols that seem to shift when you aren’t looking directly at them. There’s a chest in the corner, its lock rusted but intact. A faint hum of power emanates from it. Do you open the chest, investigate the markings, or leave the room?",
        "options": [
            {"text": "Open the chest.", "next_id": 61},
            {"text": "Investigate the markings.", "next_id": 62},
            {"text": "Leave the room.", "next_id": 63}
        ]
    },
    {
        "id": 24,
        "title": "\nPick Up the Key",
        "text": "You kneel down and pick up the rusted key. The moment your fingers close around it, the air in the room shifts, growing colder. The key hums with a faint, eerie energy. It feels heavier than it should, as if it has a history you don’t understand. You hear distant whispers, too faint to make out. The key might be important, but you feel the need to move on. Do you leave the area or search for a lock to use it on?",
        "options": [
            {"text": "Search for a lock.", "next_id": 64},
            {"text": "Leave the area.", "next_id": 65},
            {"text": "Inspect the key further.", "next_id": 66}
        ]
    },
    {
        "id": 25,
        "title": "\nIgnore It and Move On",
        "text": "You leave the key behind and press on. The chill of the ghost’s passing lingers, but you shake it off. Ahead, the corridor stretches into darkness, the air thick with a sense of foreboding. A door at the end of the hall beckons. It seems out of place, untouched by the decay around it. Do you approach the door, investigate the walls, or turn back?",
        "options": [
            {"text": "Approach the door.", "next_id": 67},
            {"text": "Investigate the walls.", "next_id": 68},
            {"text": "Turn back.", "next_id": 69}
        ]
    },
    {
        "id": 26,
        "title": "\nSpeak to the Woman",
        "text": "You decide to speak to the gaunt woman. Her hollow eyes meet yours as you ask, ‘What do you want?’ She doesn’t respond immediately but slowly opens her mouth, revealing a gaping void where her teeth should be. A voice, rasping and hollow, emanates from the abyss: ‘I seek your soul… or your servitude.’ Do you offer her your soul, reject her, or ask what she means?",
        "options": [
            {"text": "Offer her your soul.", "next_id": 70},
            {"text": "Reject her.", "next_id": 71},
            {"text": "Ask what she means.", "next_id": 72}
        ]
    },
    {
        "id": 27,
        "title": "\nFight Back",
        "text": "You choose to fight back. With a surge of adrenaline, you lash out at the woman, but her hollow eyes flash, and you feel a sharp pain in your chest as she effortlessly stops your attack. She smiles, and the wound vanishes as quickly as it came. ‘You are weak,’ she whispers. ‘But that can be changed.’ She raises her hand, and shadows coil around you. Do you resist, offer to serve, or try to break free?",
        "options": [
            {"text": "Resist.", "next_id": 73},
            {"text": "Offer to serve.", "next_id": 74},
            {"text": "Try to break free.", "next_id": 75}
        ]
    },
    {
        "id": 28,
        "title": "\nMove Forward into the Void",
        "text": "You step into the void. The world seems to vanish behind you, and you are enveloped by an infinite emptiness. Time loses meaning here, and you feel both lost and liberated. A faint glow appears in the distance, an impossibly far light beckoning you forward. As you draw closer, you hear a voice, soft and gentle: ‘Do you seek the truth, or only escape?’ Do you continue toward the light, ask the voice who it is, or turn away?",
        "options": [
            {"text": "Continue toward the light.", "next_id": 76},
            {"text": "Ask the voice who it is.", "next_id": 77},
            {"text": "Turn away.", "next_id": 78}
        ]
    },
    {
        "id": 29,
        "title": "\nSearch for Another Exit",
        "text": "The void presses in on you, but you refuse to give up. Searching for an exit, you feel the air shift around you, thick with dark energy. Something stirs just ahead. You sense it before you see it—a silhouette moving in the darkness. Do you approach, hide, or continue searching for another exit?",
        "options": [
            {"text": "Approach the silhouette.", "next_id": 79},
            {"text": "Hide.", "next_id": 80},
            {"text": "Continue searching.", "next_id": 81}
        ]
    },
    {
        "id": 30,
        "title": "\nWait and Hope the Way Opens Again",
        "text": "You decide to wait, hoping that the staircase will reappear. The darkness presses in around you, and the air grows colder still. Hours seem to pass, but nothing changes. The mocking laughter from earlier returns, growing louder. It seems the void has no intention of letting you leave. Do you continue waiting, call out for help, or make a desperate attempt to escape?",
        "options": [
            {"text": "Continue waiting.", "next_id": 82},
            {"text": "Call out for help.", "next_id": 83},
            {"text": "Attempt to escape.", "next_id": 84}
        ]
    },
    {
        "id": 31,
        "title": "\nApproach the Figure",
        "text": "You cautiously approach the figure, its features still obscured by shadows. It steps forward, and the dim light reveals a face—twisted and worn, as if time itself has left its mark. It smiles at you, a grin full of malice and pity. The air grows cold as it speaks in a voice that feels like it's clawing at your mind: ‘Do you seek the truth, or do you only wish to be lost in the dark forever?’",
        "options": [
            {"text": "Seek the truth.", "next_id": 34},
            {"text": "Remain silent.", "next_id": 35},
            {"text": "Attack the figure.", "next_id": 36}
        ]
    },
    {
        "id": 32,
        "title": "\nSpeak to the Figure",
        "text": "You decide to speak to the figure, though its presence fills you with unease. ‘Who are you?’ you ask. The figure’s lips twitch into a faint smile before answering: ‘I am the one who awaits. The one who watches those who dare enter this realm. Your choices will define your fate.’ As it speaks, the air thickens, and shadows grow longer. You feel as though you’re being suffocated by its words. Do you ask more questions, leave, or prepare to fight?",
        "options": [
            {"text": "Ask more questions.", "next_id": 37},
            {"text": "Leave the chamber.", "next_id": 38},
            {"text": "Prepare to fight.", "next_id": 39}
        ]
    },
    {
        "id": 33,
        "title": "\nPrepare for a Fight",
        "text": "You gather all your strength and prepare for a fight. The figure seems to anticipate your move, and with a sudden, fluid motion, it reveals a weapon—a blade forged from pure darkness. It lunges at you with inhuman speed. Do you block, counterattack, or dodge?",
        "options": [
            {"text": "Block the attack.", "next_id": 40},
            {"text": "Counterattack with your own weapon.", "next_id": 41},
            {"text": "Dodge and wait for an opening.", "next_id": 42}
        ]
    },
    {
        "id": 34,
        "title": "\nThe Figure's Secret",
        "text": "As you speak the words of truth, the figure’s form begins to shift and flicker. A terrible cry echoes through the chamber, and the shadows retreat, revealing the truth—its true form. It is not just a figure, but a collection of forgotten souls, their faces twisted in eternal torment. ‘You were right to seek the truth,’ the figure says with a voice full of regret. ‘Now you must decide—will you leave this place and forget, or will you take the burden of knowledge with you?’",
        "options": [
            {"text": "Leave and forget.", "next_id": 43},
            {"text": "Take the burden of knowledge.", "next_id": 44}
        ]
    },
    {
        "id": 35,
        "title": "\nSilence",
        "text": "You remain silent, the figure’s gaze piercing you. It seems to ponder your response for a moment before it vanishes into the darkness. The chamber feels emptier now, the weight of its presence gone. The oppressive air lifts, and you are left alone with your thoughts. Do you continue your journey, or search for answers elsewhere?",
        "options": [
            {"text": "Continue your journey.", "next_id": 45},
            {"text": "Search for answers elsewhere.", "next_id": 46}
        ]
    },
    {
        "id": 36,
        "title": "\nAttack the Figure",
        "text": "You lash out at the figure, but it moves with a speed that defies logic. The darkness shifts around it, making it almost impossible to land a blow. You’re caught in its grip, feeling the weight of despair closing in. The figure laughs softly, its voice like ice scraping against stone. ‘Foolish mortal,’ it whispers. ‘You should have known better.’ The darkness wraps around you, pulling you into the void.",
        "options": [
            {"text": "Fight back with all your strength.", "next_id": 47},
            {"text": "Surrender to the darkness.", "next_id": 48}
        ]
    },
    {
        "id": 37,
        "title": "\nAsk More Questions",
        "text": "You press the figure for more answers, but it only responds with cryptic words: ‘The road ahead is not a path, but a choice—a choice to abandon the past or embrace it. What will you become?’ The shadows around you begin to twist into shapes—figures from your past, your mistakes, your regrets. The air becomes thick with memories, both painful and forgotten. Do you confront them, flee, or demand the figure tell you more?",
        "options": [
            {"text": "Confront the figures from your past.", "next_id": 49},
            {"text": "Flee the chamber.", "next_id": 50},
            {"text": "Demand more answers.", "next_id": 51}
        ]
    },
    {
        "id": 38,
        "title": "\nLeave the Chamber",
        "text": "You turn away from the figure, deciding that some answers are better left unknown. As you exit the chamber, the door slams shut behind you. The room feels like a memory, fading with every step you take. You are now in a long, winding corridor, the walls flickering with strange lights. Do you walk down the corridor, investigate the flickering lights, or turn back?",
        "options": [
            {"text": "Walk down the corridor.", "next_id": 52},
            {"text": "Investigate the flickering lights.", "next_id": 53},
            {"text": "Turn back to the chamber.", "next_id": 54}
        ]
    },
    {
        "id": 39,
        "title": "\nPrepare for a Fight",
        "text": "You ready yourself, anticipating the next move. The figure’s blade moves with deadly precision, but you parry its strike and lash out with your own weapon. It steps back, its form shifting, as though it’s made of both light and shadow. The battle rages on, each strike more dangerous than the last. The darkness around you intensifies. Will you break through or succumb to the shadows?",
        "options": [
            {"text": "Break through the shadows.", "next_id": 55},
            {"text": "Counterattack with everything you have.", "next_id": 56},
            {"text": "Retreat and reassess.", "next_id": 57}
        ]
    },
    {
        "id": 40,
        "title": "\nBlock the Attack",
        "text": "You manage to block the figure’s attack with your weapon, the dark blade clashing against your own. A shockwave of dark energy ripples out, but you hold your ground. The figure stumbles back, seemingly unfazed. It stares at you with contempt. ‘Your strength will not save you,’ it whispers. Do you press your advantage, defend, or try to break its grip?",
        "options": [
            {"text": "Press your advantage.", "next_id": 58},
            {"text": "Defend and wait for an opening.", "next_id": 59},
            {"text": "Break its grip and escape.", "next_id": 60}
        ]
    },
    {
        "id": 41,
        "title": "\nCounterattack with Your Weapon",
        "text": "You strike back with all the fury you can muster, your weapon flashing through the air. The figure parries your blow with ease, its own blade cutting through the shadows like a knife through silk. The room shifts, growing darker, the figure’s presence growing stronger. Do you keep fighting, try to escape, or search for something in the room to use against it?",
        "options": [
            {"text": "Keep fighting.", "next_id": 61},
            {"text": "Try to escape.", "next_id": 62},
            {"text": "Search for something to use.", "next_id": 63}
        ]
    },
    {
        "id": 42,
        "title": "\nDodge and Wait for an Opening",
        "text": "You evade the figure’s attack, your body moving with precision. The figure’s blade slices through the air, missing you by inches. The darkness around you grows more oppressive as you wait for an opening. You can sense its next move. Do you strike now, continue dodging, or attempt to break free?",
        "options": [
            {"text": "Strike now.", "next_id": 64},
            {"text": "Continue dodging.", "next_id": 65},
            {"text": "Attempt to break free.", "next_id": 66}
        ]
    },
    {
        "id": 43,
        "title": "\nLeave and Forget",
        "text": "You choose to leave, the knowledge too heavy to carry. As you walk away, the world around you fades, returning to the darkness. The whispers fade, and you are left alone, lost in the void. You are free, but forever changed. The darkness remains, waiting for the next traveler.",
        "options": [
            {"text": "End the journey.", "next_id": 67}
        ]
    },
    {
        "id": 44,
        "title": "\nTake the Burden of Knowledge",
        "text": "With a heavy heart, you take the knowledge the figure offers. The world shifts as you feel the weight of the truth settle upon your shoulders. It is a burden—one that will stay with you forever. But you now see the world as it truly is, with all its darkness and light, and you are ready to face whatever comes next.",
        "options": [
            {"text": "Embrace your fate.", "next_id": 68}
        ]
    },
    {
    "id": 45,
    "title": "\nContinue Your Journey",
    "text": "You press onward, your footsteps echoing in the empty corridor. The shadows seem to watch you, but you remain resolute. Ahead, you notice a strange door, one that glows faintly with an eerie light. It beckons you, as if it holds the answers you seek. Do you open it, investigate the surroundings first, or walk past?",
    "options": [
        {"text": "Open the door.", "next_id": 69},
        {"text": "Investigate the surroundings.", "next_id": 70},
        {"text": "Walk past the door.", "next_id": 71}
    ]
},
{
    "id": 46,
    "title": "\nSearch for Answers Elsewhere",
    "text": "You decide to explore further, searching for other clues or answers. The walls shift, and the ground beneath you begins to hum with a low, rhythmic sound. As you move through the strange halls, you come across an ancient library. The shelves are lined with old tomes, some of which seem to pulse with energy. Do you investigate the books, look for a hidden passage, or leave the library?",
    "options": [
        {"text": "Investigate the books.", "next_id": 72},
        {"text": "Look for a hidden passage.", "next_id": 73},
        {"text": "Leave the library.", "next_id": 74}
    ]
},
{
    "id": 47,
    "title": "\nFight Back with All Your Strength",
    "text": "You fight back with every ounce of strength you have. The figure’s dark blade clashes against yours, sparks flying as the energy from the battle intensifies. The shadows swirl around you both, making it difficult to see. With a final, desperate strike, you land a blow that sends the figure reeling. But its eyes glow with fury as it begins to regenerate. It seems almost impossible to defeat. Do you continue to fight, attempt to escape, or search for a way to weaken it?",
    "options": [
        {"text": "Continue to fight.", "next_id": 75},
        {"text": "Attempt to escape.", "next_id": 76},
        {"text": "Search for a way to weaken it.", "next_id": 77}
    ]
},
{
    "id": 48,
    "title": "\nSurrender to the Darkness",
    "text": "You surrender, letting the darkness consume you. The void envelops your senses, and you feel yourself drifting. The shadows offer no comfort, only cold emptiness. Your body fades into the abyss, your consciousness lost. In this realm, there is no escape, no second chances. It is over.",
    "options": [
        {"text": "End the journey.", "next_id": 78}
    ]
},
{
    "id": 49,
    "title": "\nConfront the Figures from Your Past",
    "text": "You step forward, confronting the shadows that take the shape of figures from your past. The faces are familiar, yet twisted by regret and guilt. As you face them, the memories flood back—both the good and the bad. The figures speak in voices you know well, pleading with you to forgive them, or to understand their choices. Do you forgive them, fight them, or demand answers?",
    "options": [
        {"text": "Forgive them.", "next_id": 79},
        {"text": "Fight them.", "next_id": 80},
        {"text": "Demand answers.", "next_id": 81}
    ]
},
{
    "id": 50,
    "title": "\nFlee the Chamber",
    "text": "You turn and flee, running down the darkened corridor. The figure’s presence looms behind you, but you push forward, ignoring the fear that gnaws at your mind. The flickering lights ahead reveal a doorway, though you’re unsure where it leads. Do you enter the doorway, keep running, or stop to catch your breath?",
    "options": [
        {"text": "Enter the doorway.", "next_id": 82},
        {"text": "Keep running.", "next_id": 83},
        {"text": "Stop and catch your breath.", "next_id": 84}
    ]
},
{
    "id": 51,
    "title": "\nDemand More Answers",
    "text": "You demand more answers from the figure, pressing for clarity in the cryptic words. The figure’s smile fades, replaced by a look of pity. ‘You ask for what cannot be given,’ it says. ‘There are things beyond your comprehension. But perhaps, you can still learn the cost of seeking too much.’ The shadows around you seem to pulse with a strange energy. Do you ask again, leave, or prepare to fight?",
    "options": [
        {"text": "Ask again.", "next_id": 85},
        {"text": "Leave the chamber.", "next_id": 86},
        {"text": "Prepare to fight.", "next_id": 87}
    ]
},
{
    "id": 52,
    "title": "\nWalk Down the Corridor",
    "text": "You take a deep breath and walk down the corridor, your steps slow but steady. The flickering lights ahead cast strange, shifting shadows. As you approach, you realize that the walls themselves seem to pulse with energy. The door at the end of the hallway is adorned with strange symbols. Do you open the door, try to decipher the symbols, or turn back?",
    "options": [
        {"text": "Open the door.", "next_id": 88},
        {"text": "Try to decipher the symbols.", "next_id": 89},
        {"text": "Turn back.", "next_id": 90}
    ]
},
{
    "id": 53,
    "title": "\nInvestigate the Flickering Lights",
    "text": "You move closer to the flickering lights, trying to discern their source. As you touch one, it shatters like glass, releasing a wave of cold air. The fragments swirl around you, forming an eerie pattern on the ground. The ground beneath you begins to tremble. Do you follow the pattern, run away, or investigate further?",
    "options": [
        {"text": "Follow the pattern.", "next_id": 91},
        {"text": "Run away.", "next_id": 92},
        {"text": "Investigate further.", "next_id": 93}
    ]
},
{
    "id": 54,
    "title": "\nTurn Back to the Chamber",
    "text": "You decide to return to the chamber, hoping to find something you missed before. As you step back into the room, the figure is gone, but the shadows still linger. The door to the outside world is now open, but you feel a pull towards the darkness. Do you leave, search for more answers, or face the shadows once more?",
    "options": [
        {"text": "Leave the chamber.", "next_id": 94},
        {"text": "Search for more answers.", "next_id": 95},
        {"text": "Face the shadows.", "next_id": 96}
    ]
},
{
    "id": 55,
    "title": "\nBreak Through the Shadows",
    "text": "You push through the shadows with a fierce resolve, your strength surging as you battle against the oppressive darkness. The figure falters, unable to maintain its form in the face of your determination. You land a decisive blow, shattering its form into a million pieces. The room grows quiet, and the shadows slowly fade. You've won—at least for now.",
    "options": [
        {"text": "Search for a way out.", "next_id": 97},
        {"text": "Rest and recover.", "next_id": 98}
    ]
},
{
    "id": 56,
    "title": "\nCounterattack with Everything You Have",
    "text": "You unleash everything you have, striking with a flurry of blows. The figure stumbles, caught off guard by the intensity of your attack. The blade it wields grows heavier, and its movements slow. But just when it seems like you've gained the upper hand, the shadows around you thicken. It’s not over yet. Do you continue to fight, try to escape, or focus on weakening the shadows?",
    "options": [
        {"text": "Continue to fight.", "next_id": 99},
        {"text": "Try to escape.", "next_id": 100},
        {"text": "Focus on weakening the shadows.", "next_id": 101}
    ]
},
{
    "id": 57,
    "title": "\nRetreat and Reassess",
    "text": "You decide to retreat, pulling back from the figure's relentless onslaught. You take a moment to reassess, the darkness swirling around you as you gather your strength. There’s something about the shadows you’ve yet to understand—perhaps a weakness. Do you continue to fight, attempt to escape, or search for a way to turn the shadows against the figure?",
    "options": [
        {"text": "Continue to fight.", "next_id": 102},
        {"text": "Attempt to escape.", "next_id": 103},
        {"text": "Search for a way to turn the shadows against it.", "next_id": 104}
    ]
}

]

