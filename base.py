#https://imagine.gsfc.nasa.gov/educators/programs/cosmictimes/downloads/newsletters/2006NL_HomeEd.pdf


import requests

durl = str(input("provide url : "))
req =requests.get(durl)
print(req.headers)
print(req.url)
filename= req.url[durl.rfind('/')+1:]
with open(filename,'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
            