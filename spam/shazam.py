
import tkinter as tk
import requests

def send_webhook():
    url = url_entry.get()
    message = message_entry.get()
    while True:
        payload = {"content": message}
        requests.post(url, json=payload)

root = tk.Tk()
root.title("Discord Webhook Sender")

url_label = tk.Label(root, text="Discord Webhook URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send Message to Webhook", command=send_webhook)
send_button.pack()

root.mainloop()
