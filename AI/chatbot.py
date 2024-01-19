import pred
import math

adm = [103.78064170954637, 1.4465435114846568]
bot = [103.81639628261368, 1.3150167065491134]
fort = [103.84648706934998, 1.294183080117831]
jur = [103.73183534021483, 1.3344207914846158]


def return_statement(response, location):
    data = location
    location = [data["longitude"], data["latitude"]]
    print(location)
    if (
        "trail" in response.lower()
        or "route" in response.lower()
        and "recommend" in response.lower()
    ):
        return "I recommend Woodlands Waterfront Park trail for you. It is a sceneic route near the Straits of Johor. It is 2km long and takes about 1-2h to complete."
    elif "recommend" in response.lower() and "park" in response.lower():
        return "Sure, I can recommend you a park. What are you looking for in a park (e.g. suitable for children, pets, wheelchair)?"
    elif "children" in response.lower():
        formatted_input = [1, 0, 0]
        return get_park(pred.predict([formatted_input]))
    elif "pet" in response.lower():
        formatted_input = [0, 1, 0]
        return get_park(pred.predict([formatted_input]))
    elif "wheelchair" in response.lower():
        formatted_input = [0, 0, 1]
        return get_park(pred.predict([formatted_input]))
    elif "hello" in response.lower():
        return "Hello, how can I help you today?"
    elif "far" in response.lower():
        return "Then, " + get_park(get_park_cood(location))
    elif "admiralty park" in response.lower() and "place" in response.lower():
        return "Some places you can visit in Admiralty Park are its playgrounds, Shiok Garden Hotpot & BBQ Buffet."
    
    else:
        return "Sorry, I do not understand."


def get_park(answer):
    if int(answer) == 1:
        return "I recommend Admiralty Park. It has many different kinds of slides and faclilities, making it suitable for childrens. It also has wheelchair friendly playgrounds too!"
    elif int(answer) == 2:
        return "I recommend Botanic Gardens. It has many different species of plants and animals, and beautiful secenries to enjoy. Its suitable for pets with many different trails."
    elif int(answer) == 3:
        return "I recommend Fort Canning Park. It offer a variety of arts, heritage and nature experiences to the entire family."
    else:
        return " I recommend Jurong Lake Gardens. It is a large park, comprising Lakeside Garden, Chinese and Japanese Gardens, and Garden Promenade."


def get_park_cood(location):
    min_dist = min(
        math.dist(location, adm),
        math.dist(location, bot),
        math.dist(location, jur),
        math.dist(location, fort),
    )

    if min_dist == math.dist(location, adm):
        return 1
    elif min_dist == math.dist(location, bot):
        return 2
    elif min_dist == math.dist(location, fort):
        return 3
    else:
        return 4
