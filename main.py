import requests
from datetime import date
PIXELA_USERNAME = ""
PIXELA_TOKEN = ""
GRAPH_NAME = "graph1"

# Creating a user in PIXELA
pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

# Creating a new graph in PIXELA using requests.post() method
pixela_graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_configuration = {
    "id": GRAPH_NAME,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# response = requests.post(url=pixela_graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

# Creating a pixel in PIXELA using requests.post() method
pixela_graph_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_NAME}"


today = date.today()
today_yyyyMMdd = today.strftime("%Y%m%d")

pixel_configuration = {
    "date": today_yyyyMMdd,
    "quantity": "10.2"
}
# response = requests.post(url=pixela_graph_pixel_endpoint, json=pixel_configuration, headers=headers)
# print(response.text)

# updating a created pixel in PIXELA using the requests.put()
pixela_graph_pixel_upp_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_NAME}/{today_yyyyMMdd}"

pixel_configuration = {
    "quantity": "15.2"
}
response = requests.put(url=pixela_graph_pixel_upp_endpoint, json=pixel_configuration, headers=headers)
print(response.text)

# Deleting a pixel in PIXELA using the requests.delete()
pixela_graph_pixel_del_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_NAME}/{today_yyyyMMdd}"

# response = requests.delete(url=pixela_graph_pixel_del_endpoint,  headers=headers)
# print(response.text)

