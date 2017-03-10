import requests

# To get the latest position of ISS
resp = requests.get("http://api.open-notify.org/iss-now.json")  # returns data as json

print(resp.status_code)
# print the contents of the response(the data that server returned)
print(resp.content, "\n")


# The ISS pass endpoint returns when the ISS will next pass over a given location
parameters = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
# response = requests.get("http://api.open-notify.org/iss-now.json?lat=40.71&lon=-74")
print(response.content)

# get the response data as a python object.
data = response.json()
print(type(data))
print(data)

# the server doesn't just send a status code and the data when it generates a response,
# but metadata containing information on how the data was generated and how to decode it.
# This is stored in the response headers.

# headers will be shown as a dictionary. Within it, content-type is the most important key for now,
# it tells the format of the response and how to decode it.
print(response.headers)

# get the content type from the dictionary
print(response.headers["content-type"], "\n")


# To find the no of people in space
response_no = requests.get("http://api.open-notify.org/astros.json")
data = response_no.json()
print(data["number"])
print(data)