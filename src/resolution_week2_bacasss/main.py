import requests
import sys
import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    lyrics_parser = subparsers.add_parser("lyrics", help="Get song lyrisc")
    lyrics_parser.add_argument("artist", type = str, help= "Insert the name of the song's artist")
    lyrics_parser.add_argument("song", type = str, help= "Insett the name of the song")
    group = lyrics_parser.add_mutually_exclusive_group()
    group.add_argument('--preview', action='store_true')
    group.add_argument('--full', action='store_true')

    stat_parser = subparsers.add_parser("stat", help="Get song statistics")
    stat_parser.add_argument("artist", type = str, help= "Insert the name of the song's artist")
    stat_parser.add_argument("song", type = str, help= "Insett the name of the song")

    guess_parser = subparsers.add_parser("guess", help="Guess the next line in the song")

    args = parser.parse_args()

    if args.command == "lyrics":
        req = requests.get(f"https://api.lyrics.ovh/v1/{args.artist}/{args.song}")
        if req.status_code != 200:
            print("API returned with error")
            sys.exit(1)
        api_parsed = req.json()
        lyrics = api_parsed["lyrics"]
        
        if args.preview == True:
            splitlines = lyrics.splitlines()
            print("\n".join(splitlines[:5]))
        else:
            print(lyrics)
        
    elif args.command == "stat":
        req = requests.get(f"https://api.lyrics.ovh/v1/{args.artist}/{args.song}")
        if req.status_code != 200:
            print("API returned with error")
            sys.exit(1)
        api_parsed = req.json()
        lyrics = api_parsed["lyrics"]

        lines = lyrics.splitlines()
        nlines = len(lines)
        words = lyrics.split()
        nwords = len(words)

        print(f"Lines: {nlines}")
        print(f"Words: {nwords}")

    elif args.command == "guess":
        songlist = [("alex warren", "ordinary"), ("alex warren", "fever dream"), ("alex warren", "youll be alright kid"), ("james arthur", "impossible"), ("rosa linn", "snap"), ("zac efron", "rewrite the stars"), ("loren allred", "never enough")]
        randomsong = random.sample(songlist, k = 1)[0]
        (artist, song) = randomsong

        req = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
        if req.status_code != 200:
            print("API returned with error")
            sys.exit(1)
        api_parsed = req.json()
        lyrics = api_parsed["lyrics"]
        splitlines2 = lyrics.splitlines()
        randomline = random.randint(0, len(splitlines2) - 2)

        print("Guess the next line: ")
        print(splitlines2[randomline])
        print(f"Hint: The song is {song}")
        userguess = input("Type your guess: ")

        if userguess == splitlines2[randomline + 1]:
            print("Congrats you got ittt")

        else:
            print("aww u didnt get it, the next line was:")
            print(splitlines2[randomline + 1])



if __name__ == "__main__":
    main()













# req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# if req.status_code != 200:
#     print("API returned with error")
#     sys.exit(1)
# api_parsed = req.json()
# print(f'Ability 1 is {api_parsed["abilities"][0]["ability"]["name"]}')
# print(f'Ability 1 being hidden is {api_parsed["abilities"][0]["is_hidden"]}') 