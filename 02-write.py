
# odpremo file handler
# parameter "w" v funkciji open() je za branje obvezen in pomeni, da vsebino datoteke pobrisemo, ko datoteko odpremo
with open("files/sloncki.txt", "w") as file_to_write_handler:

    for num in range(1, 16):
        # z if-elif-else stavki izberemo pravilno sklanjatev za tekst in pripnemo število slončkov
        if num == 1:
            text = str(num) + " majhen slonček se je pozibaval na pajčevini tam pod drevesom in ko je ugotovil " \
                              "da stvar je zanimiva, je poklical še enega slončka"
        elif num == 2:
            text = str(num) + " majhna slončka sta se pozibavala na pajčevini tam pod drevesom in ko sta ugotovila " \
                              "da stvar je zanimiva, sta poklicala še enega slončka"
        elif num < 5:
            text = str(num) + " majhni slončki so se pozibavali na pajčevini tam pod drevesom in ko so ugotovili " \
                              "da stvar je zanimiva, so poklicali še enega slončka"
        else:
            text = str(num) + " majhnih slončkov se je pozibavalo na pajčevini tam pod drevesom in ko so ugotovili " \
                              "da stvar je zanimiva, so poklicali še enega slončka"
        # zapišemo text - eno vrstico v datoteko
        # '\n' dodamo na konec teksta, da naredimo prelom vrstice (\n je znak za 'new line')
        file_to_write_handler.write(text + '\n')

    # še zaključen verz
    text = str(num+1) + " majhnih slončkov se je pozibavalo na pajčevini tam pod drevesom in ko so ugotovili " \
                        "da stvar je zanimiva, se je mreža pretrgala"
    # ki jo zapišemo v file
    file_to_write_handler.write(text)
