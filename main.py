import requests
from rich import print
from rich.markdown import Markdown

#weather display
def display_current_weather(location):
  #get the real time current temperature and conditions in a location
  api_key = "tfdbcf08d180afdebd50co3aa4ac4389"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}&units=metric"

  response = requests.get(api_url)
  response_data = response.json()
  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']
  print(f"\nThe current temperature in [bold]{location}[/bold] is [bold]{temperature}°C[/bold], [bold]{condition}[/bold].\n")


#itinerary calculation function
def generate_itinerary(origin, destination, duration):
  #generate travel itinerary between 2 places using AI
  print(f"Generating itinerary from {origin} to {destination} for {duration} days.")
  prompt = f"Please generate a travel itinerary from {origin} to {destination}, in {duration} days. This is a road trip. Please keep it short, less than 15 lines. Feel free to use emojis (but not too many).Please estimate a cost for each day in the currency of the country of location. Please give the estimated weather conditions for each day."
  context = "You are well-travelled and a specialist in knowing the best tourist spots around the world to have an amazing road trip."
  api_key = "tfdbcf08d180afdebd50co3aa4ac4389"
  api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"
  response = requests.get(api_url)
  response_data = response.json()
  markdown_data = Markdown(response_data['answer'])
  print(markdown_data)

def credit():
  #adds a final credit
  print("This AI Travel Itinerary Planner was built by [bold orchid]Michelle Hoefer[/bold orchid]. I hope you enjoy your trip.")

def welcome():
  #welcome messgae for users
  print("[bold magenta]Welcome to the AI Travel Itinerary Planner.[/bold magenta]")

welcome()


#user input
origin = input("What city does your trip start from? ").strip().capitalize()
destination = input("What is your final destination? ").strip().capitalize()
duration = input("How many days will your trip last? (Please only enter a number, i.e 5). ").strip()

if origin and destination and duration.isdigit():
  display_current_weather(origin)
  display_current_weather(destination)
  generate_itinerary(origin, destination, duration)
  credit()
else:
  print("Please ensure all fields are filled in correctly.")

