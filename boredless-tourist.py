destinations = ["Paris, France",
"Shanghai, China",
"Los Angeles, USA",
"São Paulo, Brazil",
"Cairo, Egypt"]

#faraway lands
def get_destination_index(destination):
  destination_index = -1
  for i in range(len(destinations)): 
    if destination == destinations[i]:
      destination_index = i 
      break
  return destination_index
def get_traveler_location(traveler):
  traveler_location = traveler[1]
  traveler_location_index = get_destination_index(traveler_location)
  return traveler_location_index

#interesting places
attractions = [[], [], [], [], []]
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

#best places
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if(interest in attraction_tags):
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#parts of city
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi "
  interests_string += traveler[0] + ", we think you'll like these places around " + traveler[1] + ": "
  for interest in traveler_attractions:
    interests_string += interest + ", "
  return interests_string[:-2]


#test cases
test_traveler = ['Erin Wilkes', 'Mumbai, India', ['historical site', 'art']]
print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Hyderabad, India"))
print(destinations.index("Paris, France"))
print(get_traveler_location(test_traveler))
print(add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']]))
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("Mehrauli, Delhi", ["Qutub Minar", ["monument"]])
print(attractions)
print("\n\n")
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)
smills_france = get_attractions_for_traveler(['Tushar Sachdeva', 'Cairo, Egypt', ['museum']])
print(smills_france)