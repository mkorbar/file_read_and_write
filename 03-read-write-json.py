import json

# odpri json datoteko za branje in shrani podatke v all_responses
with open('files/rezultati_ankete.json', 'r') as anketa_handler:
    file_contents = anketa_handler.read()
    all_responses = json.loads(file_contents)

# izpiši število vnosov v seznami all_responses
print(f'There are {len(all_responses)} responses already in the file.')

# za pisanje odpri isto datoteko
with open('files/rezultati_ankete.json', 'w') as anketa_handler:
    # zbiraj rezultate ankete dokler je uporabnik pripravljen odgovarjati
    while True:
        my_name = input("What's your name? ")
        my_age = input("How old are you? ")
        my_gender = input("What's your gender? ")

        # zapiši odgovore uporabnika v dictionary
        users_response = {
            'name': my_name,
            'age': my_age,
            'gender': my_gender,
        }

        # shrani dictionary v seznam
        all_responses.append(users_response)
        if input("Do you wanna answer for another person? [y/n] ").lower() not in ['y', 'yes']:
            break

    # shrani vse podatke ankete nazaj v datoteko
    anketa_handler.write(json.dumps(all_responses, indent=4))
