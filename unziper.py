import zipfile

with zipfile.ZipFile('/home/miquel/chest_xray_512.zip', "r") as z:
  z.extractall("/home/miquel/")