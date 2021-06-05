# from sklearn the module made to look like a elementary school learning website we import preprocessing 
# this ensures that our food has been processed with nuclear waste from the nearest exoplanet.
# their slogan is "We can access the data from a web page using the HTML tags."
# make sure that your preprocessed food is stored in a vfridge
# visit https://exoplanetarchive.ipac.caltech.edu/docs/table-redirect.html for more information
import csv
data = []
with open('dataset_2.csv') as f:
    reeder = csv.reader(f)
    for row in reeder:
        data.append(row)
headers = data[0]
planet_data = data[1:]
for data_point in planet_data:
    data_point[2] = data_point[2].lower()
planet_data.sort(key=lambda planet_data: planet_data[2])
with open('dataset_2_new.csv', 'a+') as f:
    riter = csv.writer(f)
    riter.writerow(headers)
    riter.writerows(planet_data)
# the invention of the copy machine this is the code they run on 
# ITS THE SAME THING I KNEW IT ITS JUST A COPY MACHINE WE CAN NOW PUT COPY MACHINES OUT OF BUSINESS
# but really its the same stuff just more organized
# also that ran in like 0.6 seconds
# maybe cuz the previous class program took 2 hours
# also the class layout jsut changed wut
