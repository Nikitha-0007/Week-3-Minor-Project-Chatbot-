from reminder import set_reminder
from weather import get_weather
from database import setup_db, log_to_db

def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"The result is: {result}"
    except Exception as e:
        return f"Error in calculation: {e}"

def handle_input(user_input):
    user_input = user_input.lower()
    
    if user_input.startswith("remind"):
        task = user_input[7:]
        response = set_reminder(task)
    
    elif "weather" in user_input:
        response = get_weather()
    
    elif user_input.startswith("calculate"):
        expression = user_input[10:]
        response = calculate(expression)
    
    elif "hello" in user_input:
        response = "Hello! I'm your assistant."
    
    else:
        response = "Sorry, I didn't understand that."
    
    log_to_db(user_input, response)
    return response

if __name__ == "__main__":
    setup_db()
    print("🧠 Virtual Assistant is active. Type 'exit' to quit.")
    while True:
        command = input(">> ")
        if command.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        print(handle_input(command))
