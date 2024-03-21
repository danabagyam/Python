country = {
    "id" : 1,
    "country_name" : "India",
    "code" : "+91",
    "State" : ["Kerala", "Tamil nadu", "karnataka", "Andhra Pradesh", "Delhi"],
     "City" : [{
         "id": 1,
         "name" : "chennai"
     },
     {
         "id": 2,
         "name": "Trivandrum"
     },
     {
         "id": 3,
         "name" : "Bangalore"
     },{
         "id": 4,
         "name" : "Chittod"
     },{
         "id": 5,
         "name" : "Delhi"
     }]
     
}

Name = "Danabagyam"
Number = "666666666"

print("My name is",Name,"and I'm from",country["City"][0]["name"],",",country["State"][1],",",country["country_name"],",", "and my mobile number is +91", Number)