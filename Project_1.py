"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - Industrial Training Kit (Batch 2026)

Architecture: IPO Model (Input -> Process -> Output)
- Input Loop      : continuous while cycle
- Sanitization    : lowercase + whitespace stripping
- Knowledge Base  : dictionary (O(1) lookup instead of if-elif ladder)
- Fallback        : responses.get(key, default) -> atomic lookup + fallback
- Exit Strategy   : clean break command
"""

# ------------------------------------------------------------------
# PHASE 2: KNOWLEDGE BASE (Dictionary-based intent -> response map)
# ------------------------------------------------------------------
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hey! What can I do for you?",
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great! How about you?",
    "what is your name": "I'm RuleBot, your friendly rule-based AI chatbot.",
    "what can you do": "I can respond to a few predefined commands. Try asking me about myself!",
    "help": "You can say: hello, how are you, what is your name, what can you do, or bye.",
    "bye": "Goodbye! Have a great day.",
    "exit": "Session terminated. See you next time!",
    "quit": "Shutting down. Goodbye!",
}

# Commands that should break the loop (Kill Command)
EXIT_COMMANDS = {"bye", "exit", "quit"}


def get_response(user_input: str) -> str:
    """
    PHASE 3: PROCESS
    Looks up the sanitized input in the knowledge base.
    Uses .get() for a single atomic lookup + fallback operation.
    """
    return responses.get(user_input, "I do not understand. Type 'help' to see what I can do.")


def run_chatbot():
    """
    THE HEARTBEAT: The Infinite Loop
    The organism stays alive until the Kill Command (exit/bye/quit).
    """
    print("RuleBot: Hello! I'm your rule-based AI chatbot. Type 'bye' to exit.\n")

    while True:
        # PHASE 1: INPUT & SANITIZATION
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # KILL COMMAND CHECK
        if clean_input in EXIT_COMMANDS:
            print(f"RuleBot: {get_response(clean_input)}")
            break

        # PROCESS + OUTPUT
        reply = get_response(clean_input)
        print(f"RuleBot: {reply}")


if __name__ == "__main__":
    run_chatbot()