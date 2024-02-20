#dictionary -> a collection of {key:value} pairs. ordered and changable. no dupes allowed

capitals =  {"USA":"Washington",
            "China":"Bejing",
            "Egypt":"Cairo"}

populations =   {"USA":332000000,
                "China":1410000000,
                "Egypt":109000000}

#printing returns {key:value} pairs:
print(capitals)

#to get the values from keys:
#(the get methoods return not print)

capitals.get("Egypt") #outputs: Cairo
capitals.get("India") #outputs: none

#to get population values:
populations.get("USA") #outputs: USA's population
populations.get("India") #outputs: none

#to update the dict:
capitals.update({"Germany":"Berlin"})
capitals.update({"Egypt":"New capital city"})

