import google.generativeai as genai
import webbrowser
import os
import subprocess
import win32com.client

genai.configure(api_key="AIzaSyDvfxPDMFV1E1-YZaRb9abYqjZeizPTPPU")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def process_user_input(user_input):
    # Check if user wants to open a website
    if user_input.startswith("open "):
        url = user_input[5:]
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' # Path to Chrome executable
        webbrowser.get(chrome_path).open(url)
        return "Opening " + url

    # Check if user wants to search in Chrome
    elif user_input.startswith("!search "):
        query = user_input[8:]
        url = "https://www.google.com/search?q=" + query
        webbrowser.get(chrome_path).open(url)
        return "Searching for " + query + " in Chrome", True

    # Check if user wants to play something on YouTube
    elif user_input.startswith("!play "):
        query = user_input[6:]
        url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
        webbrowser.get(chrome_path).open(url)
        return "Playing " + query + " on YouTube", True

    # Check if user wants to check unread Gmails
    elif user_input == "!gmail":
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        unread_count = len([message for message in inbox.Items if message.UnRead])
        return f"You have {unread_count} unread emails.", False

    # Check if user wants to see all available commands
    elif user_input == "!h":
        return "Available commands:\n" \
               "!open <url>: Open a URL in Chrome\n" \
               "!search <query>: Search the query in Chrome\n" \
               "!play <song/video>: Play a song or video on YouTube\n" \
               "!gmail: Check unread emails\n" \
               "!h: Show all commands\n" \
               "!run <app_name>: Open the specified app in Windows", False

    # Check if user wants to run an application in Windows
    elif user_input.startswith("!run "):
        app_name = user_input[5:]
        try:
            subprocess.Popen(["start", "", app_name], shell=True)
            return "Opening " + app_name, False
        except Exception as e:
            return "Error: " + str(e), False

    # If none of the special commands are used, send the input to the AI model
    else:
        return user_input, True

while True:
    convo = model.start_chat(history=[])

    print("-------------------------------------------------------------------------------")
    print()

    user_input = input("You : ")
    print()

    # Process user input
    processed_input, send_to_model = process_user_input(user_input)

    # If user input is a special command, print the response
    if not send_to_model:
        print("MiuBot : ", processed_input)
    else:
        # Send processed input to the model
        convo.send_message(processed_input)

        # Get model response
        response = convo.last.text

        print("MiuBot : ", response)
        print()
