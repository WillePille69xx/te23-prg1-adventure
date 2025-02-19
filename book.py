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
        "text": "You decide to break the mirror. With a sharp crack, the glass shatters, and the room goes dark. A sudden, overwhelming silence fills the space. You hear something shift behind you. The broken pieces of glass begin to move, forming into a jagged shape that lunges at you. Do you fight the shape, run, or use the charm you found earlier?",
        "options": [
            {"text": "Fight the shape.", "next_id": 34},
            {"text": "Run.", "next_id": 35},
            {"text": "Use the charm.", "next_id": 36}
        ],
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
    }
]

