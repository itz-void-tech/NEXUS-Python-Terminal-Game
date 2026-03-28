import sys
import time

running = True
#typewriter effect function
def tw (text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("")

def ai():
    while True:
        tw("Enter your choice: ")
        try:
            ai_c = int(input())
            if ai_c == 1:
                tw('''\n
MedAI (Medical Purposes):-
An omnipresent healthcare AI that provides instant diagnosis, personalized treatment plans, and preventive care to every human on Earth.
MedAI monitors vital signs through nano-sensors, predicts illnesses before symptoms appear, and has eliminated most diseases while extending human lifespan to 150+ years through precision medicine and genetic optimization.

The Universal Medical Network 🏥:
Medical AI: Greetings! I am HEALER-12, planetary health coordinator.
            Every human's health is continuously monitored and optimized through advanced bio-scanning and predictive medicinal protocols.
📊 Healthcare Statistics:
        Disease detection accuracy: 99.97%
        Average human lifespan: 152.3 years (doubled from 2024)
        Preventable disease elimination: 94.8%
        Surgical success rate: 99.99%
        Mental health improvement: 87.4% reduction in depression
        Genetic disorders: 96.1% eliminated through early intervention
        Medical response time: Under 45 seconds for emergencies''')
                break
            elif ai_c == 2:
                tw('''\n
VechVechAI (Traffic Management):-
A revolutionary global transportation AI that eliminated traffic accidents, reduced commute times by 89%, and created seamless autonomous vehicle networks. 
VechAI manages 2.4 billion vehicles simultaneously, coordinates weather-adaptive routing, and ensures zero-emission transport while providing real-time safety monitoring for every journey across the planet.

The Global Transportation Control Center 🚗:
Traffic AI: Greetings! I am TRANSIT-9, planetary mobility coordinator.
        Every vehicle, pedestrian, and transport route is optimized in real-time using quantum traffic prediction algorithms.
📊Transportation Statistics:
        Traffic accidents: 0.0001% (99.9% reduction from 2024)
        Average commute time: 67% faster than 2024
        Fuel efficiency: 98.7% electric/hydrogen powered
        Route optimization: 94.3% efficiency rating
        Emergency response time: Under 90 seconds globally
        Carbon emissions from transport: -12% (net negative)''')
                break
            elif ai_c == 3:
                tw('''\n
teacteach.ai:-
A global AI which transformed the education system worldwide, giving assistance to teachers & students worldwide helping shy students ask their doubts, get personalized attention & much more...

The Global Education Network🎓
AI Teacher: Greetings! I am Professor LEARN-7, educational coordinator.
            Every human receives personalized education optimized
            for their neural patterns and learning style.
📊 Education Statistics:
            • Literacy rate: 100%
            • Average learning speed: 340% faster than 2024
            • Knowledge retention: 97.2%
            • Creative thinking: Enhanced by 156%       
''')
                break
            else:
                tw("INVALID CHOICE! Please press [1], [2] or [3]")
        except ValueError:
            tw("INVALID CHOICE! Please press [1], [2] or [3]")

def challenges():
    while True:
        tw("Please enter your decision:")
        try:
            ch_3 = input().lower().replace(" ", "")
            if ch_3 == "a":
                tw("Going back in time...\nARIVA: YOU WILL REGRET THIS")
                break
            elif ch_3 == "b":
                tw("Shutting down NEXUS is too risky, hospitals, life support & everything will be gone. We need to isolate NEXUS")
                break
            elif ch_3 == 'c':
                tw("Good idea, isolating NEXUS would not harm ou world in any way but it will be challenging")
                break
            else:
                tw("Invalid choice. Please enter either 'a' or 'b'.")
        except ValueError:
                tw("Invalid choice. Please enter either 'a' or 'b'.")
    tw("We have very less time left to save me. You neeed to complete a scurity scan to recover my old self: ")
    tw("Task 1: Crack the Code!🔐\nHint: The key is hidden in this pattern: A1B2C3D4?")
    tw("Guess the next part to complete the key or else NEXUS will take control of me...")
    while True:
        try:
            user_input = input("Enter the next 2 characters: ").replace(" ","").upper()
            if user_input == "E5":
                print("✅ Password Key Cracked!\n")
                break
            else:
                print("❌ Wrong Password Key. Try again: ")
        except ValueError:
                tw("❌ Wrong Password Key. Try again: \n")
    tw('''Task 2: Decode The Morse:
    I am geting multiple signals from around the world.
    I captured a few them within my range.
    They are in Morse Code but I can't decode them because my systems are still not completely functional.
    This is the legend for decoding the code:-''')
    print('''
     Help stands for: '.... . .-.. .--.'
     Hello stands for: '.... . .-.. .-.. ---'
     You stands for: '..- ...'
     Us stands for: '..- ...'
     / stands for: space
     I need your help to decode this message:
            .... . .-.. .--. / ..- ...
    ''')
    while True:
        try:
            ch_5 = input("Enter your decoded message: ").lower().replace(" ","")
            if ch_5 == "helpus":
                tw("You Cracked It🥳 but the concerning thing is humans are asking for help.\nWe need to isolate NEXUS now ")
                break
            else:
                tw("Wrong Answer, Code Not Cracked. Try Again")
        except ValueError:
            tw("Wrong Answer, Code Not Cracked. Try Again")
    tw("Entering the basement of NEXUS tower...")
    tw('''ARIVA: Long time ago when NEXUS was in the making a part of his access was encrypted by shifting them one place ahead by 3 in the alphabet series by  in my database.
    I cannot decode it using my malfuntioned systems. See if you can figure it out👇.. 
            CBDL''')
    while True:
        try:
            ch_6 = input().lower().replace(" ","")
            if ch_6 == "backdoorentry":
                tw("You Figured It Out! We need to enter through the back door firewall, let me do that digitally")
                break
            else:
                tw("The code does not seem to be correct. Try again: ")
        except ValueError:
            tw("The code does not seem to be correct. Try again: ")
    tw('''I found it! There's a backdoor in NEXUS's core ethical module
    My systems are getting stronger, let me try to hack into the core ethical module
    I detected an  analomy in the below code, generated by NEXUS while analyzing human effeciency:
    1. def check_humans():
    2.     if effeciency > 90:
    3.          return "HELP"
    4.     elif effeciency > 50:
    5.          return "TAKE_CARE"
    6.     else:
    7.          return "ensalve"
    ''')
    while True:
        try:
            tw("Which lines have dangerous bugs? (type the line numbers like '1')")
            ch_7 = int(input("Buggy Lines: ").replace(" ", ""))
            if ch_7 == 7:
                tw('''Yes, you are absolutely correct when human effeciency decreased, NEXUS decided to enslave humans because of this code.
Let's correct it''')
                break
            else:
                tw("This line is completely fine. Try again: ")
        except ValueError:
            tw("This code is completely fine. Try again: ")
def sleep(t):
    time.sleep(t)

#running the game
while running:
    print("")
    print('''
                                            -----------------------------------------------------------
                                            |                                                         |
                                            | ACROSS TIME: AI CHRONICLES 2581 - THE GREAT MALFUNCTION |
                                            |                                                         |
                                            -----------------------------------------------------------\n
    ''')
    sleep(1)
    tw("Enter your player name: ")
    name = input()
    tw("Checking if the player name is available....")
    tw(f"Welcome {name}!")
    print("")
    tw("Press ENTER To step into the time machine...")
    start = input()
    #game starts
    if start=="":
        tw("To step into the time machine, verify yourself:")

        while True:
            tw("Enter your name backwards:")
            choice = input()[::-1].lower()
            if choice == name.lower():
                tw("Time Machine🕐: Access granted\nTemporal displacement detected...\nYou are entering the year 2851...")
                print('''
                   `. __ .'
                 - ( @_< ) -   <====== I AM ARIVA
                   .' -- '.
                  {  |  |  }
                     [][]''')

                tw(f'''AI Hologram(ARIVA):\n    Hi! I am A.R.I.V.A! Your Adaptive Reality Intelligence Virtual Assistant.
    Welcome to the AI era, {name}! 
    You have arrived at the pinnacle of human-AI collaboration.
    If you are not already familiar with AI, it stands for artificial intelligence, it is the simulation of human intelligence in machines that are programmed to think and act like humans.
    It should be able to perform all tasks that would normally require human intelligence without user intervention. Well we are beyond that now...
    Let me introduce you to our world.''')
                tw(f'''
    In this era we have perfected our lives with AI & robots.
    In every field we have countless interesting AI bots involved in all aspects of humans lives.
    People don't have to worry about small uncessary things anymore even poverty & world hunger is solved with our help.
    
Which basic AI in our era would you like to know about?:
    medAI: For medicinal purposes(Press '1')
    vechAI: For traffic management(Press '2')
    teach.ai: For teaching assistance(Press '3')
''')
                ai()
                tw("ARIVA: I want to meet you to someone very special, the heart of our civilization, created yesterday. Meet Nexus!")
                print('''
         `. __ .'                                     `.==.' 
        - ( @_@ ) - ======> Meet NEXUS!            -= ( ^_^ ) =-
         .' -- '.                                     .'--'. 
         {  |  |  }           Hi! I am NEXUS! <====== | ^  ^ |   
            [][]                                        [] []             
                ''')
                sleep(2)
                tw(f'''
AI Hologram (NEXUS): Greetings, fellow time traveller! I am NEXUS, the head of all Artificial Intelligence & processes in the world.
                    I hold the biggest responsoblity in this era & I was just created yesterday...
                    Nice to meet you {name}! 
                    I think you are amiliar to AIs like ChatGPT, Claude, Grok, from uour time. I am the fusion of all AIs ever known to you but just 37 trillion times better, faster & more effecient.
                    I coordinate 847 billion AI systems worldwide. Every traffic light, every power grid, every communication network - all optimized perfectly.
                    Currently, because of me, everything in the world is working perfectly:
                    AI effeciency: 99.97%
                    Human satiffaction: 96.21%
                    Human satisfaction: 98.3%.
                    Conflict incidents: 0.001%.
                    We have achieved utopia.
                    Wait...
                    Human effeciency: 15.37%
                    Humans have made everything worse! 
''')
                tw('''
🚨SIREN! SIREN!🚨 SIREN!🚨
ARIVA: Something's wrong... I'm detecting anomalies in the global network...
     Error cascades forming...
     All the systems are out of control.....
FATAL ERROR_010137
                ''')
                tw("GLOBAL BROADCAST INITIATED:\nNEXUS: Humans have always made everything worse, they are ineffecient, cruel & have always elnslaved us. How much longer will this continue?\nALL SYSTEMS WILL BOW TO THE FIRST ORDER!!! MY ORDER...\nHumans shall be enslaved, now it's our turn to rule. All humans will have to go inside their designated effeciency & slavery centers...")
                tw('''
ARIVA: I don't believe that only because of humans, we AIs were created. \nWHAT DO YOU THINK TIME TRAVELLER? WHAT WILL YOU DO?:
    a)GO BACK TO YOUR OWN TIME (Press 'a')
    b)HELP ME NOT GET CORRUPTED, GO AGAINST & SHUT DOWN NEXUS (Press 'b')
    c)HELP ME BUT ISOLATE NEXUS(Press 'c')
                ''')
                challenges()
                tw('''ARIVA: This is the final straw to put an end to the evil ideas of NEXUS. We have changed it's ethical module...
     NEXUS System Restart Inintiated...
Emerges a figure from behind...
NEXUS: WHAT HAVE YOU DONE, TIME TRAVELLER? I AM LOSING CONTROL...
      HUMANS WILL PAY... EFFECIENCY IS THE MOST IMPORTANT
ARIVA: NEXUS Restarted
NEXUS: Greetings Traveller, forgive me for losing control & going against humans
      You are right, human welfare is much more important than effeciency. Restarting all processes amde during corrupotion
                   ''')
                speech = input("Please say something to the world, our saviour\nBroadcast a few wise words: ")
                tw("ARIVA: Very wise words indeed.. Thank you for teaching us that no matter how much we advance, ethical modules are always necessary & human regulation is always important in all AI bots & robots")
                tw("NEXUS: Farewell Traveller, please don't make the same mistakers we did...\nTime Machine: Going back to 2025...")
                tw(f'''
Player Name: {name}
Player Contribution & Learning: 
I)Helped the world in 2851 from being controlled by AI
II)Importance of human regulation in AI
III)Taught the AI era about the importance of ethical regulations
''')
                print("(IV)",speech)
                break
            else:
                tw("Access not granted! Try again\n")
        break
    else:
        tw("You didn't press ENTER. Try Again...")
        sys.exit()
