'''code to fetch data from the database and display on the webpage mainly depends on how the data is saved and in what format'''


''' we can save data into database in string format or in the form of objects using ORMs'''

''' if we use list we can simply use database query to fethc data and can easily display it on the webpage '''

''' here i am using second method which is an object oriented method, as it is more suitable as per the requirements of the assesment'''


class Property:
  def __init__(self, name, prop_type, bedroom, bathroom):
    self.name = name
    self.prop_type = prop_type
    self.bedroom = bedroom
    self.bathroom = bathroom
    self.amenities = []

  def info(self):
    print("\nProperty Info: (Name: " + self.name + ", Type: " + self.prop_type + ", No. of Bedroom: " + str(self.bedroom) + ", No. of Bathroom: " + str(self.bathroom) + ")\n")

  def print_amenities(self):
  	print("Amenities:")
  	print(self.amenities)
  	print("\n")



p1 = Property("Birch Lodge 16, Newton Stewart", "residential", 2, 1)
p1.amenities = ["Kitchen", "Wifi", "Free parking on premises", "TV", "Patio or balcony", "Hair dryer", "Refrigerator", "Microwave", "Long-term stays allowed"]

p2 = Property("Lovely loft on the beautiful North Norfolk Coast", "guest house", 1, 1)
p2.amenities = ["Wifi", "Free parking on premises", "TV", "Hair dryer", "Microwave"]



p1.info()
p1.print_amenities()

p2.info()
p2.print_amenities()




''' we can save these objects in the database and to dispaly the data on the webpage we can fetch the data in variable by running database queries. To send this data to front-end (webpage) we can use different methods depending on the framework or backend language but the most common method is by creating API and sending the data/data-variable in json response.'''

''' after getting data in the front-end (webpage) in json data-type, javascript can be used to display that data on the webpage. Different libraries are there in javascript to fetch json response and display it on the webpage. React framework can be used to make frontend or simple ajax can be used to handle and display the data ''' 