import requests

r = requests.get("https://en.wikipedia.org/wiki/Period_(algebraic_geometry)")
print(r.status_code)
print(r.ok)