capitals = {
    "Germany":"Berlin",
    "France":"Paris"
}

travel_log = { #Nesting lists in dictionary
    "France": ["Paris","Lille","Marsylia"],
    "Germany":["Berlin","Hamburg","Drezno"]
    }

travel_log2 = { #nesting dictionary inside dictionary
    "France": {"cities_visited":{"Paris":1,"Lille":"Do odwiedzenia","Marsylia":2}},
    "Germany":{"cities_visited":{"Berlin":3,"Hamburg":2,"Drezno":1}}
}
print(travel_log2)
print(travel_log2["France"])
print(travel_log2["France"]["cities_visited"])

travel_log3 = [ #nesting dictionaries inside list
    {   
        "country":"France",
        "cities_visited":{"Paris":1,"Lille":"Do odwiedzenia","Marsylia":2}
    },
    {   
        "country":"Germany"
        ,"cities_visited":{"Berlin":3,"Hamburg":2,"Drezno":1}
    }
        ]

print(travel_log3)
print(travel_log3[0])