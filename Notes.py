menu = ("Select option you want: \n[1] Add a note"
        "\n[2] Change note"
        "\n[3] Read note"
        "\n[4] Delete note"
        "\n[0] Exit")
print(menu)
storage = []
while True:
        message = input("Please chose an option:")
        if message == '0':
                break
        elif message == '1':
                while True:
                        new_note = {}
                        note_header = input("Chose your note title:")
                        if note_header == '1':
                                break
                        note = input("Enter your note:")
                        priority = input("Enter priority:")
                        if note_header not in new_note:
                                new_note[note_header] = [note]
                                new_note[note_header].append(priority)
                        else:
                                new_note[note_header].append(note)
                                new_note[note_header].append(priority)

                        storage.append(new_note)
                        message_new = input("Do you want to add another note? Yes/No:")
                        if message_new == 'yes':
                                print(note_header)
                        elif message_new == 'no':
                                break
        elif message == '2':
                print(storage)
                change_note = input("Chose what note you want to change:")
                if change_note not in storage:
                        print("Note can't be found, try something else!")
                        continue
                storage_note = storage[change_note]
                print(storage_note)
                print("Note number:" + str(len(storage_note)))
                note_number = int(input("Chose note number you want to change: "))
                changed_note = input("Enter new note: ")
                storage_note[note_number] = changed_note
                storage[change_note] = storage_note
        elif message == '3':
                print(storage)
        elif message == '4':
                delete_note = input("Chose note you want to delete: ")
                if delete_note in storage:
                        del storage[delete_note]
                        print("You successfully deleted note!")

                else:
                        print("Note doesn't exist!")
