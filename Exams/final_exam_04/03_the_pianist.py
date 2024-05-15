song_number = int(input())
pieces = {}

for x in range(song_number):

    song_data = input().split("|")

    song_title = song_data[0]
    composer = song_data[1]
    key = song_data[2]
    pieces[song_title] = {"composer": composer, "key": key}

while True:

    command = input().split("|")

    if command[0] == "Stop":
        for piece in pieces:
            print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")
        break

    else:
        if command[0] == "Add":
            piece = command[1]
            composer = command[2]
            key = command[3]
            if piece not in pieces:
                pieces[piece] = {"composer": composer,
                                 "key": key}
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")

        elif command[0] == "Remove":
            piece = command[1]
            if piece in pieces.keys():
                pieces.pop(piece)
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        elif command[0] == "ChangeKey":
            piece = command[1]
            new_key = command[2]
            if piece in pieces.keys():
                pieces[piece]["key"] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
