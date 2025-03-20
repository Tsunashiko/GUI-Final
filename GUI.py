"""GUI script that can look up IP against VirusTotals API."""

# Modules
import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TV_API_KEY")
BASE_URL = os.getenv("TV_LINK")


# Functions
def on_click():
    entry = my_str_var.get()
    headers = {"accept": "application/json", "x-apikey": f"{API_KEY}"}
    response = requests.get(f"{BASE_URL}/{entry}", headers=headers)
    data = response.json()
    label3_text = data["data"]["attributes"]["last_analysis_stats"]
    label3.config(text=f"{label3_text}")


# Window
root = tk.Tk()
root.title("IP Reputation")
root.geometry("480x150")
# Allows entry str to pass into function
my_str_var = tk.StringVar()
# Starter text for label3
label3_text = "IP Information here"


# widgets
label = tk.Label(
    root,
    text="IP Reputation Checker",
    font=("Times New Roman", 20)
).pack()

label2 = tk.Label(
    root,
    text="Please Copy/paste an IP and click the Button to get a report from "
         "VirusTotal API",
    font=("Arial", 10),
).pack()

entry = tk.Entry(
    root,
    textvariable=my_str_var,
    width=50,
    borderwidth=3
).pack()

button_check = tk.Button(
    root,
    text="Check Reputation",
    width=20,
    height=1,
    bg="green",
    command=on_click,
).pack(pady=5)

label3 = tk.Label(
    root,
    text=f"{label3_text}"
)
# .pack() split - non-split causes .config() issues for on_click()
label3.pack()

# Main event loop
root.mainloop()
