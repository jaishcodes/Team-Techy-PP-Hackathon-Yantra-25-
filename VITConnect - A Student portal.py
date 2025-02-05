import random
import spacy

nlp = spacy.load("en_core_web_sm")

study_resources = {
    "Advances in Web Technologies": [
        "https://www.w3schools.com/html/default.asp",
        "https://www.w3schools.com/css/default.asp",
        "https://www.w3schools.com/js/default.asp",
        "https://www.programiz.com/html"
    ],
    "Blockchain Technologies": [
        "https://www.geeksforgeeks.org/blockchain-technology-introduction/",
        "https://komodoplatform.com/en/academy/bitcoin-script/"
    ],
    "Augmented Reality and Virtual Reality": [
        "https://www.geeksforgeeks.org/basics-augmented-reality/",
        "https://www.geeksforgeeks.org/virtual-reality-vs-augmented-reality-whats-the-difference/"
    ],
    "Foundations of Data Science": [
        "https://www.w3schools.com/datascience/default.asp",
        "https://www.geeksforgeeks.org/data-science/"
    ],
    "Robotics: Machine and Controls": [
        "https://www.geeksforgeeks.org/robotics-introduction/",
        "https://www.geeksforgeeks.org/artificial-intelligence-in-robotics/"
    ],
    "Grundstufe Deutsch": [
        "https://www.leo.org/german-english",
        "https://learngerman.dw.com/en/learn-german/s-9528",
        "https://www.duolingo.com/course/de/en/Learn-German"
    ],
    "Database Management System": [
        "https://www.geeksforgeeks.org/dbms/",
        "https://www.tutorialspoint.com/dbms/index.htm",
        "https://www.javatpoint.com/dbms-tutorial"
    ],
    "Operating System Principals": [
        "https://www.geeksforgeeks.org/operating-systems/",
        "https://www.tutorialspoint.com/operating_system/index.htm",
        "https://dl.acm.org/doi/10.5555/540365"
    ],
    "Programming in Java": [
        "https://www.geeksforgeeks.org/java/",
        "https://www.w3schools.com/java/java_intro.asp",
        "https://www.javatpoint.com/java-tutorial"
    ]
}

cafeteria_menu = {
    "Monday": {
        "Breakfast": "Poori, Aloo Masala, Semiya, Chutney, Banana Milkshake, Cold Milk, Chocos, Bread, Butter, Jam, Coffee, Tea, Milk, Pea Salad, French toast",
        "Lunch": "Phulka, Chilly Chicken, Dragon Paneer, Thai fried Rice, Dhal Fry, White rice, Sambar, rasam, Wheel Chips, Curd, Sweet",
        "Snacks": "Donut, Sauce, Tea, Coffee, Milk",
        "Dinner": "Dosa, Dal, Sambar, Chutney, Veg Jal Firizhi, Methi Roti, White Rice, Butter Milk, Butter Milk, Cream of Mushroom Soup, Fresh fruits"
    },
        "Tuesday": {
        "Breakfast": "Idly, Vada, Sambar, Veg Kitchadi, Chutney, Fresh Juice, Cold Milk, Corn Flakes, Bread, Butter, Jam, Coffee, Tea, Milk, Pea Salad, Fried Eggs",
        "Lunch": "Phulka, Dal Thadka, Channa Masala, white Rice, Pineapple Rasam, Butter Milk, Bisibilla Baht, Potato chips, Poriyal, Sweet: carrot Halwa",
        "Snacks": "Veg Samosa, Imly Chutney, Jal jeera, Coffee, Milk",
        "Dinner": "Chapathi, Veg & Egg Schewan Fried rice, Dal long Beans Sabzhi, Garlic Sauce, White Rice, Sambar, rasam, Butter Milk, veg Manchow Soup, Hot Badam Milk, Banana "
    },
    "Wednesday": {
        "Breakfast": "Masala Dosa, Sambar, Chutney, Fresh Juice, Cold Milk, Chocos, Bread, Butter, Jam, Coffee, Tea, Milk, Green Salad, Egg Burji ",
        "Lunch": "Phulka, Butter chicken, Shahi Paneer, Arvi Fry, Dal Lasoni, Curd, Fryums, White rice, Sambar, Tomato Rasam, Sweet: Rasagula/Rasmalai",
        "Snacks": "Channa Chat/Masala Chat, Sauce, Tea, Coffee, Milk",
        "Dinner": "Phulka, Dal Maharani, Bindi Jaipuri, Veg Jal Frizhi, White Rice, Sambhar, Rasam, Peas, Pulav, Butter Milk, Corriander Soup, Papaya & Watermelon"
    },
    "Thursday": {
        "Breakfast": "Panner Paratha, Rava Upma, Sambar, Dates Milkshake, Cold MIlk, Cornflakes, Butter, Jam, Coffee, Tea, Milk, Sweet Corn Salad, Egg Fry",
        "Lunch": "Phulka, Baked Egg/Fish Masala, Panner Kofta, White Rice, Sambar, Rasam, Aloo Baigan, Fryums, Dal, Curd, Bread Halwa",
        "Snacks": "Sandwich/Hot Dog, Hot Badam Milk, Tea",
        "Dinner": "Poori, Channa Masala, white rice, Rasam, Jeera rice, Porial, curd, Mixed Veg Soup, Orange"
    },
    "Friday": {
        "Breakfast": "Masala Dosa, Sambar, Chutney, Fresh Juice, Cold Milk, Chocos, Bread, Butter, Jam, Coffee, Tea, Milk, Sprout Salad, Fry Egg",
        "Lunch": "Phulka, Dal, Chicken Tikka/Tandoori, Paneer, Amritsari, White Rice, Sambar, Poondu Rasam, Curd, fryums, Keera Kootu, Gulab Jamun/Makhan Peda",
        "Snacks": "Brownie/Cake, Tea, Coffee, Milk",
        "Dinner": "Phulka, Dum Aloo, White Rice, Sambhar, Rasam, Curd, Pulav, Cream of Tomato Soup, Papaya"
    },
    "Saturday": {
        "Breakfast": "Mixed Veg Paratha, Curd, Kitchadi, Chutney, Fresh Juice, Cold Milk, Chocos, Sambar, Bread, Butter, Jam, Coffee, Tea, Milk, Salad, Egg Burji",
        "Lunch": "Phulka, Dal Makhani, Dingri Muttar, Dahi Varda, Poriyal, Sambar/Karakolambu, White Rice",
        "Snacks": "Masala Vada, Chutney, Masala Tea, Coffee, Milk",
        "Dinner": "Phulka, Dal Fry, Veg & Egg Fried Rice, Baby Corn, Manchurian, Poriyal, Curd, White Rice, Sambar, Rasam, Fresh Garden Pea Soup, Fresh Fruits"
    },
    "Sunday": {
        "Breakfast": "Podi Idly, Paav Bhaji, Sambar, Chutney, Cold Milk, Corn Flakes, Tea, Coffee, Milk, Fresh Juice, Bread, Butter, Jam, Coffee, Tea, Milk, Sprouted Channa, Spanish Omelette",
        "Lunch": "Chicken/Veg Biriyani, Banaras Baigan, Dragon Panneer, Onion Raitha, Phulka, White Rice, Sambar, Tomato Rasam, Papad, Ice Cream",
        "Snacks": "Hot Dog, Dahi Papdi Chat, Jal Jeera, Tea, Coffee, Milk",
        "Dinner": "Phulka, Dal Masala, Butter Peas Masala, White rice, Sambar, Rasam, Aloo Jeera, Curd, Variety Rice, Sweet Corn Soup, Cut Fruits"
    }
}

campus_news = [
    "Yantra week has begun and events are going on in full swing. These are the events ongoing today you can register for them if they interest you,",
    "Yantra: Proctor Proctee Hack",
    "Yantra: DevSOC'25",
    "Yantra: Speed Shifter",
    "Yantra: Techcraft",
    "Yantra: Electro-Hack",
    "Yantra: Getting Started with making IoT projects: Arduino in Action",
    "Yantra: TechTrek 2.0: sustAIn",
    "Yantra: Synapse",
    "Yantra: aiOTopia",
    "Yantra: AI for Sustainable Development Goals in Manufacturing: Transforming Industries for a Greener Future",
    "Yantra: Bid-a-thon",
    "Yantra: Molecular Mayhem",
    "Yantra: Sapient Synthesis",
    "Yantra: Mind Flick"
]

motivational_tips = [
    "Take small steps every day. Progress is progress, no matter how small!",
    "Don't sit down and wait for the opportunities to come. Get up and make them.",
    "Change your life today. Don't gamble on the future; act now without delay.",
    "The most common way people give up their power is by thinking they don't have any.",
    "Your time is limited; don't waste it living someone else's life.",
    "The way to get started is to quit talking and begin doing.",
    "You are never too old to set another goal or to dream a new dream.",
    "Believe you can and you're halfway there.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "You miss 100% of the shots you don't take."
]

riviera_info = {
    "main_event": {
        "dates": "February 20 to March 24, 2025",
        "description": "A 4-day international sports and cultural carnival with participation from over 40,000 students from 125+ colleges",
        "venue": "VIT Vellore Campus"
    },
    "expo": {
        "name": "Riviera Expo 1.0",
        "date": "February 6, 2025",
        "description": "Pre-event showcase and exhibition"
    },
    "events": [
        "Sports competitions",
        "Cultural events",
        "Concerts",
        "Dramatic performances",
        "Literary events",
        "Musical performances",
        "Dance competitions",
        "Informal events",
        "Stunt show"
    ]
}

def get_riviera_info(query):
    query = query.lower()
    if any(word in query.lower() for word in ["how many", "participants", "participate"]):
        if "college" in query:
            return f"Riviera sees participation from {riviera_info['main_event']['participation']['colleges']} colleges across the globe"
        else:
            return f"Riviera has participation of {riviera_info['main_event']['participation']['total_students']} students from {riviera_info['main_event']['participation']['colleges']} colleges"

def process_query(query):
    doc = nlp(query.lower())
    
    if any(word in query.lower() for word in ["lunch", "menu", "food", "cafeteria"]):
        return get_cafeteria_menu()
    
    elif any(word in query.lower() for word in ["resources", "study", "learn", "subject"]):
        return get_study_resources()
    
    elif any(word in query.lower() for word in ["news", "campus", "events", "happening"]):
        return get_campus_news()
    
    elif any(word in query.lower() for word in ["motivate", "inspiration", "tip", "advice"]):
        return get_motivational_tip()
    
    elif any(word in query.lower() for word in ["schedule", "timetable", "class"]):
        return get_class_schedule()
    
    elif any(word in query.lower() for word in ["weather", "temperature", "forecast"]):
        return get_weather_info()
    
    elif any(word in query.lower() for word in ["faculty", "professor", "teacher"]):
        return get_faculty_info()
    
    else:
        return "I'm sorry, I don't have information about that. Can you please ask about lunch menu, study resources, campus news, motivational tips, class schedules, weather, or faculty information?"

def get_cafeteria_menu():
    day = input("Which day do you want the menu for? ").capitalize()
    
    if day in cafeteria_menu:
        return f"Cafeteria Menu for {day}: {cafeteria_menu[day]}"
    else:
        return "Invalid day selected."

def get_study_resources():
    subjects = list(study_resources.keys())
    return f"Available subjects: {', '.join(subjects)}"

def get_campus_news():
    return "\n".join([f"- {news}" for news in campus_news])

def get_motivational_tip():
    return random.choice(motivational_tips)

def get_class_schedule():
    return "Your class schedule for today: [Class schedule would be displayed here]"

def get_weather_info():
    return "Today's weather: Sunny with a high of 25°C (77°F)"

def get_faculty_info():
    return "Faculty information: [Faculty details would be displayed here]"

def display_menu():
    print("\nWelcome to the Student Assistant! How can I help you today?")
    print("1. Get Study Resources")
    print("2. View Campus News")
    print("3. View Cafeteria Menu")
    print("4. Get Motivational Tip")
    print("5. Ask a Question")
    print("6. Exit")

while True:
    display_menu()
    
    choice = input("Choose an option (1-6): ")
    
    if choice == '1':
        print("\nSelect a subject:")
        subjects = list(study_resources.keys())
        
        for i, subject in enumerate(subjects, start=1):
            print(f"{i}. {subject}")
        
        subject_choice = int(input("Enter the number of the subject: ")) - 1
        
        if 0 <= subject_choice < len(subjects):
            selected_subject = subjects[subject_choice]
            links = study_resources[selected_subject]
            print(f"\nResources for {selected_subject}:")
            for link in links:
                print(link)
        else:
            print("Invalid selection.")
    
    elif choice == '2':
        print("\nCampus News:")
        print(get_campus_news())
    
    elif choice == '3':
        print(get_cafeteria_menu())
    
    elif choice == '4':
        print(f"\nMotivational Tip: {get_motivational_tip()}")
    
    elif choice == '5':
        query = input("What would you like to know? ")
        response = process_query(query)
        print(response)
    
    elif choice == '6':
        print("\nGoodbye! Have a great day!")
        break
    
    else:
        print("\nInvalid option. Please try again.")