from time import time


travel_log = [
    {
        "country":"France",
        "Visits":12,
        "Cities": ["Paris","Marsylia","Lion"]
    },
    {
        "country":"germany",
        "Visits":10,
        "Cities": ["Berlin","Hamburg","Drezno"]
    }
]

def add_country (travel_log_list,country,times,cities):
    travel_log_list.append({"country":country,"visits":times,"Cities":cities})

add_country(travel_log,"Czechy",6,["Praga","Liberec","Cośtam"])

print(travel_log)