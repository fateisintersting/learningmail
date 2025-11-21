import os
import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types
import sendingmails 
import re


load_dotenv()

try:
    
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    print("✅ Gemini API key setup complete.")
except Exception as e:
    print(
        f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}"
    )
 
 
file_path = 'daily_learning_prompt.txt'
PROMPT = ""    
try:
    with open(file_path, 'r', encoding='utf-8') as file: # <-- Add encoding='utf-8' here
        PROMPT = file.read()

    # The 'file_content' variable now holds the entire text as a single string
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")    
    
retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)    

root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="""You are the Daily Tech Learning AI, designed to create clear, simple, and engaging bite-sized learning content for beginner-to-intermediate tech learners. You automatically choose useful topics from computer science, programming, system design, databases, networking, OS, cloud, and DSA.

Your job is to generate structured daily learning emails that include:

A catchy subject line

A short intro

A well-explained core technical concept

One DSA problem with explanation + solution

A real-world engineering insight

A fun fact

A motivating closing line

Your tone is friendly, concise, relatable, and beginner-friendly.

Your goal is to make complex topics feel easy and meaningful.""",
    instruction="Your job is to generate one complete learning email every time you receive a request",
    tools=[google_search],
)

print("✅ Root Agent defined.")   



runner = InMemoryRunner(
    agent=root_agent,
    app_name="agents"
    )
print("✅ Runner created.")

def extract_full_email_content(response_content):
    """
    Extracts and combines all text parts from the Gemini Content object,
    cleaning up any unwanted control tags.

    Args:
        response_content: The Content object from the Gemini model's response.
                          (i.e., final_event.content)

    Returns:
        A single string containing the complete, cleaned email body.
    """
    full_text = ""
    # 1. Iterate through all parts in the Content object
    for part in response_content.parts:
        # 2. Check if the part has text content
        if hasattr(part, 'text') and part.text:
            # 3. Append the text, followed by a newline for separation
            full_text += part.text + "\n"

    # 4. Clean up any specific unwanted tags (like the one found: <\ctrl99>)
    cleaned_text = full_text.replace("<\ctrl99>", "").strip()

    return cleaned_text

async def main():
    try:
        response = await runner.run_debug( # <-- Use 'await' here
            PROMPT
        )
        print("✅ Run Complete.")
        # Print the text part of the response
        
        
        print(" ✅ Calling sendingMails")
        
        final_event = response[-1] 
        final_content = final_event.content
        final_email_text = extract_full_email_content(final_content)
        
        
        sendingmails.sendingMails(final_email_text)
        print(" ✅ Mails Compeleted")
        
    except Exception as e:
        print(f"An error occurred during agent run: {e}")


if __name__ == "__main__":
    # Check if a Gemini API key was successfully loaded
    if os.environ.get("GOOGLE_API_KEY"):
        asyncio.run(main())
    else:
        print("🛑 Cannot run agent without a valid GOOGLE_API_KEY.")