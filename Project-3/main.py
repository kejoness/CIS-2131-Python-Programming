# Kayla Jones
# Project 3

import random

# function chooses a random word from a list of words
def generate_hidden_word():
    word_list = ["able", "about", "again", "air", "all", "always", "and", "answer", "any", "around", "ask", "at",
                 "back", "be", "before", "best", "better", "between", "black", "body", "book", "boy", "brother", "but",
                 "call", "can", "car", "careful", "cat", "chair", "chance", "cheese", "child", "cinema", "clean",
                 "clear", "close", "cold", "come", "could", "country", "cry", "cut", "dance", "daughter", "day",
                 "dinner", "do", "doctor", "document", "dog", "door", "down", "dream", "drink", "each", "easy", "eat",
                 "egg", "eight", "end", "everything", "explain", "eye", "face", "family", "father", "find", "fire",
                 "first", "for", "friend", "from", "game", "get", "girl", "give", "good", "hand", "head", "help", "her",
                 "his", "home", "idea", "important", "information", "inside", "interesting", "job", "kind", "know",
                 "land", "learn", "life", "light", "live", "long", "make", "man", "many", "may", "money", "more",
                 "morning", "move", "my", "name", "new", "no", "now", "often", "one", "open", "or", "out", "page",
                 "paper", "park", "pay", "peace", "pen", "people", "person", "picture", "place", "play", "please",
                 "popular", "prefer", "problem", "put", "question", "reach", "read", "ready", "red", "rest", "rich",
                 "right", "river", "road", "room", "run", "same", "say", "school", "second", "see", "send", "set",
                 "she", "ship", "shop", "should", "show", "sit", "small", "so", "some", "son", "soon", "speak", "stand",
                 "start", "stone", "stop", "student", "such", "table", "that", "the", "there", "they", "thing", "think",
                 "this", "time", "today", "two", "understand", "up", "very", "visit", "wait", "want", "we", "what",
                 "where", "why", "word", "work", "write", "you	across", "action", "after", "against", "age",
                 "almost", "alone", "already", "also", "anything", "army", "art", "away", "bad", "beautiful", "because",
                 "become", "bed", "big", "box", "bread", "breakfast", "bring", "bus", "buy", "camera", "care", "carry",
                 "catch", "cause", "certain", "change", "chief", "church", "city", "class", "company", "confirm",
                 "continue", "control", "corner", "cost", "cover", "culture", "dead", "dear", "decision", "deep",
                 "describe", "desert", "die", "difficult", "distance", "dress", "drive", "dry", "east", "education",
                 "enjoy", "enough", "evening", "every", "example", "expect", "expensive", "fact", "fast", "feel", "few",
                 "fight", "flower", "food", "free", "full", "garage", "garden", "gold", "great", "green", "group",
                 "happy", "hard", "have", "here", "hope", "house", "how", "ill", "impossible", "include", "industry",
                 "interest", "into", "invite", "island", "journey", "juice", "keep", "late", "leave", "let", "letter",
                 "like", "look", "meet", "member", "miss", "moment", "month", "most", "mother", "much", "must", "need",
                 "never", "next", "nothing", "old", "on", "only", "other", "own", "part", "personal", "phone", "plan",
                 "player", "police", "position", "possible", "power", "present", "president", "pretty", "price",
                 "product", "provide", "public", "quite", "rather", "real", "reason", "receive", "record", "remain",
                 "remember", "report", "result", "return", "round", "sad", "save", "sea", "seat", "service", "several",
                 "shall", "side", "single", "sister", "sleep", "something", "sorry", "sound", "south", "spring", "star",
                 "stay", "story", "street", "strong", "study", "sun", "sweet", "system", "take", "talk", "teacher",
                 "tell", "their", "then", "through", "together", "too", "true", "try", "under", "use", "view", "voice",
                 "water", "way", "week", "which", "who", "wife", "with", "woman", "world", "yes	above", "accident",
                 "act", "add", "address", "ago", "airport", "along", "among", "another", "appear", "apple", "arm",
                 "baby", "bear", "begin", "behind", "believe", "blood", "blue", "both", "break", "building", "built",
                 "business", "card", "case", "central", "century", "check", "chicken", "choose", "clock", "collect",
                 "colour", "common", "computer", "condition", "consider", "course", "court", "crazy", "cross", "cup",
                 "dangerous", "dark", "decide", "depend", "desk", "different", "direct", "direction", "discuss",
                 "dollar", "draw", "during", "ear", "early", "earth", "edge", "effect", "even", "ever", "examine",
                 "exchange", "fall", "field", "film", "fine", "fish", "floor", "fly", "form", "fruit", "general",
                 "gift", "glad", "glass", "government", "grow", "half", "happen", "hear", "heart", "high", "hold",
                 "hour", "ice", "illness", "imagine", "immediately", "increase", "inform", "insect", "introduce",
                 "jump", "just", "key", "less", "line", "little", "love", "low", "magazine", "mark", "material", "mean",
                 "meat", "meeting", "milk", "mind", "minute", "nature", "near", "not", "number", "off", "office",
                 "once", "order", "over", "parent", "party", "pass", "past", "patient", "pencil", "perhaps", "piece",
                 "pink", "plate", "poor", "post", "produce", "protect", "pull", "purpose", "quick", "race", "radio",
                 "rain", "really", "remove", "reply", "respect", "ride", "ring", "rise", "rock", "search", "secret",
                 "sell", "sense", "sharp", "shoe", "short", "similar", "simple", "since", "situation", "slow", "smile",
                 "snow", "sometimes", "song", "speed", "sport", "state", "station", "still", "success", "sugar",
                 "summer", "sure", "tall", "tea", "television", "test", "than", "though", "ticket", "town", "travel",
                 "tree", "turn", "upon", "usual", "valley", "value", "virus", "walk", "war", "watch", "well", "when",
                 "while", "will", "window", "would", "your", "accept", "account", "actor", "advance", "advantage",
                 "afternoon", "agree", "amount", "angry", "arrange", "article", "attack", "available", "bag", "bank",
                 "below", "bird", "boat", "borrow", "bottle", "bridge", "brown", "build", "busy", "butter", "cake",
                 "captain", "centre", "cheap", "chocolate", "choice", "cigarette", "cloth", "cloud", "club", "coast",
                 "coat", "coffee", "college", "comfortable", "cottage", "cream", "crowd", "customer", "damage", "date",
                 "deal", "degree", "demand", "department", "design", "destroy", "detail", "dirty", "dust", "earn",
                 "enemy", "engine", "enter", "escape", "especially", "everywhere", "except", "exercise", "expression",
                 "factory", "famous", "farm", "favourite", "finger", "finish", "follow", "front", "future", "gas",
                 "gate", "gentle", "gentleman", "ground", "guide", "hair", "hat", "history", "holiday", "hospital",
                 "hotel", "hungry", "illegal", "image", "improve", "independent", "individual", "injure", "instrument",
                 "interview", "joke", "kitchen", "knife", "language", "large", "law", "left", "lesson", "listen",
                 "machine", "map", "market", "marry", "meal", "message", "mistake", "moon", "music", "newspaper",
                 "nice", "night", "nose", "object", "obtain", "ocean", "oil", "orange", "pain", "paint", "parcel",
                 "path", "peaceful", "perfect", "petrol", "plane", "plant", "pleasure", "practise", "prepare", "prison",
                 "private", "probably", "proud", "quiet", "recently", "refuse", "relationship", "religion", "repair",
                 "repeat", "replace", "request", "responsible", "restaurant", "rice", "salt", "science", "season",
                 "seem", "serious", "serve", "shape", "shoulder", "sick", "silver", "size", "skirt", "sky", "smart",
                 "smoke", "society", "special", "spend", "square", "step", "store", "strange", "subject", "successful",
                 "supply", "swim", "taste", "teach", "temperature", "thank", "tired", "tomorrow", "top", "touch",
                 "train", "trip", "uncle", "university", "usually", "vegetable", "village", "wall", "warm", "wash",
                 "weather", "welcome", "win", "winter", "wrong", "yesterday", "admire", "admit", "adventure", "afraid",
                 "allow", "although", "animal", "area", "arrive", "asleep", "attempt", "attend", "attitude", "average",
                 "bath", "battle", "beer", "belong", "bill", "board", "born", "bottom", "branch", "brave", "breathe",
                 "calm", "careless", "certainly", "chain", "character", "charge", "circle", "climb", "clothes", "coal",
                 "coin", "comfort", "complete", "consist", "contain", "cook", "copy", "correct", "count", "crime",
                 "death", "declare", "defend", "delay", "discover", "dish", "divide", "double", "doubt", "drop", "duty",
                 "effort", "either", "English", "equal", "event", "exact", "experience", "express", "fail", "farmer",
                 "fat", "flat", "foot", "foreign", "forget", "fresh", "funny", "goal", "grey", "guard", "guess",
                 "guest", "gun", "hate", "health", "heavy", "hide", "hole", "horse", "hot", "husband", "indeed",
                 "influence", "instead", "intelligent", "international", "iron", "jacket", "join", "kill", "lake",
                 "last", "laugh", "leader", "leg", "lie", "lose", "main", "marriage", "match", "measure", "medicine",
                 "metal", "middle", "mine", "modern", "mountain", "necessary", "nervous", "noise", "offer", "operation",
                 "opinion", "opposite", "outside", "pair", "passenger", "perform", "pile", "pity", "plain", "pleasant",
                 "plenty", "point", "politics", "pound", "pour", "press", "prize", "profit", "promise", "prove",
                 "raise", "recent", "reduce", "regard", "regular", "risk", "roll", "rough", "row", "rule", "rush",
                 "safe", "score", "secretary", "series", "share", "shoot", "shut", "sign", "sing", "smell", "smooth",
                 "soft", "soldier", "somewhere", "space", "speech", "spoil", "spot", "spread", "steal", "straight",
                 "suddenly", "suggest", "suit", "support", "surface", "these", "thick", "thin", "third", "those",
                 "toilet", "trade", "trouble", "trust", "type", "until", "useful", "variety", "various", "vote", "west",
                 "whose", "wild", "wish", "without", "wonderful", "wood", "year", "young"]

    return random.choice(word_list)

# prints out hidden word in blanks and
# displays player's correct guesses
def print_hidden_word(hidden_word, letters_guessed):
    # initializes displayed word as an empty string
    # before adding in blanks to the hidden word
    displayed_word = ""

    # for each letter in hidden word, check if a letter has already been guessed
    # if it has not been guessed, add a blank to the hidden word
    for letter in hidden_word:
        if letter in letters_guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    # show the player's progress in guessing a word
    print(displayed_word)


# displays hangman's gallows as the player
# makes incorrect guesses
def print_gallows(number_of_body_parts):
    # body parts for the hangman
    gallows = [
        "   O",
        " --|--",
        "  / \\",
        " /   \\"
    ]

    # checks the current number of body parts and
    # adds on a specific part based on the
    # player's current amount of incorrect guesses
    if number_of_body_parts >= 1:
        print("#")
    if number_of_body_parts >= 2:
        print("# |")
    if number_of_body_parts >= 3:
        print("# " + gallows[0])
    if number_of_body_parts >= 4:
        for part in gallows[1:3]:
            print("# " + part)
    if number_of_body_parts == 6:
        print("# " + gallows[3])
    if number_of_body_parts >= 7:
        print("# ")
    print("#\n#-----------")


# ask the player to make a guess and
# checks if the player guess is valid input
def ask_user_for_guess(letters_guessed):
    # infinite loop that repeatedly asks the player
    # to guess a letter until a valid input is given
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1: # if the guess is not exactly one character long
            print("Please enter only one letter.")
        elif not guess.isalpha(): # if the guess has anything other than letters
            print("Please enter a valid letter.")
        elif guess in letters_guessed: # if the guessed letter has already been guessed
            print("You have already guessed that letter.")
        else:
            return guess


# checks if any game-ending conditions have been met
def is_game_over(hidden_word, letters_guessed, number_of_incorrect_guesses):
    if number_of_incorrect_guesses >= 6: # if maximum number of incorrect guesses have been reached
        return True
    for letter in hidden_word: # if there are any letters in the hidden word that haven't been guessed yet
        if letter not in letters_guessed:
            return False
    return True # returns True if the player has guessed every letter in the hidden word, ending the game

def play_hangman():
    hidden_word = generate_hidden_word()
    letters_guessed = []
    number_of_incorrect_guesses = 0

    print("Let's play Hangman! Good luck :)")
    print_hidden_word(hidden_word, letters_guessed) # set the hidden word

    # while no game-ending conditions are met,
    # allow the player to keep guessing a word
    # if they guess a letter incorrectly,
    # print a gallow for the hangman
    while not is_game_over(hidden_word, letters_guessed, number_of_incorrect_guesses):
        guess = ask_user_for_guess(letters_guessed)
        letters_guessed.append(guess)
        if guess not in hidden_word:
            number_of_incorrect_guesses += 1
        print_hidden_word(hidden_word, letters_guessed)
        print_gallows(number_of_incorrect_guesses)

    if number_of_incorrect_guesses >= 6:
        print("You lost. The word was:", hidden_word)
    else:
        print("Congratulations! You win! You guessed the word:", hidden_word)


# ask the player if they'd like to player another
# round of hangman
while True:
    play_hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
