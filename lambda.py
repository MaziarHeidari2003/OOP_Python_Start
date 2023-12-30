people = [
  {'name':'Harry','house':'Gryffindor'},
  {'name':'Ron','house':'Gryffindor'},
  {'name':'Draco','house':'Slytherin'}
]

people.sort(key=lambda person : person['name'])
for person in people:
  print(person['name'])