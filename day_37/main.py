import requests
import webbrowser
from datetime import datetime
from tkinter import *

pixela_url = "https://pixe.la/v1/users"
pixela_username = ""
pixela_token = ""
pixela_graph_id = ""

auth_header = {
    "X-USER-TOKEN": pixela_token,
}

# Creating user

#
# create_user_params = {
#     "token": pixela_token,
#     "username": pixela_username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# create_user_request = requests.post(url=pixela_url, json=create_user_params)
# create_user_request.raise_for_status()

# Creating graph

# create_graph_url = f"{pixela_url}/{pixela_username}/graphs"
#
# create_graph_params = {
#     "id": pixela_graph_id,
#     "name": "programming_graph",
#     "unit": "hour",
#     "type": "float",
#     "color": "ajisai",
#     "timezone": "Poland",
# }
# create_graph_request = requests.post(url=create_graph_url, headers=auth_header, json=create_graph_params)
# create_graph_request.raise_for_status()

# Post value to the graph

post_pixel_url = f"{pixela_url}/{pixela_username}/graphs/{pixela_graph_id}"


def add_pixel():
    quantity = quantity_text.get("1.0", 'end-1c')
    date = date_text.get("1.0", 'end-1c')
    post_pixel_params = {
        "date": date,
        "quantity": quantity
    }
    request = requests.post(url=post_pixel_url, headers=auth_header, json=post_pixel_params)
    request.raise_for_status()


# Get the graph
def open_graph():
    get_graph_url = f"{pixela_url}/{pixela_username}/graphs/{pixela_graph_id}.html"
    webbrowser.open(get_graph_url, new=0, autoraise=True)


# -------------- UI ------------- #

window = Tk()
window.title("Habit Tracker")
window.config(bg='white', padx=20, pady=20)

# Text
quantity_text = Text(height=5, width=30)
quantity_text.focus()
quantity_text.insert(END, "Add units")
quantity_text.grid(row=1, column=0)

date_text = Text(height=5, width=30)
date_text.focus()
date_text.insert(END, datetime.now().strftime("%Y%m%d"))
date_text.grid(row=0, column=0)

add_button = Button(text="Add pixel", command=add_pixel)
add_button.grid(row=0, column=1)

get_graph_button = Button(text="Get programming graph", command=open_graph)
get_graph_button.grid(row=1, column=1)

window.mainloop()
