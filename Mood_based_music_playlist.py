# Mood-Based Music Playlist Generator

# Define a dictionary with moods and corresponding song recommendations
mood_songs = {
    'happy': ['Happy by Pharrell Williams', 'Can’t Stop the Feeling by Justin Timberlake', 'Uptown Funk by Mark Ronson ft. Bruno Mars'],
    'sad': ['Someone Like You by Adele', 'Fix You by Coldplay', 'Yesterday by The Beatles'],
    'energetic': ['Lose Yourself by Eminem', 'Stronger by Kanye West', 'Eye of the Tiger by Survivor'],
    'relaxed': ['Weightless by Marconi Union', 'Clair de Lune by Debussy', 'Sunset Lover by Petit Biscuit']
}

def display_menu():
    print("\nMood-Based Music Playlist Generator")
    print("Select your current mood from the list:")
    for i, mood in enumerate(mood_songs.keys(), 1):
        print(f"{i}. {mood.capitalize()}")

def get_mood_choice():
    while True:
        try:
            choice = int(input("Enter the number corresponding to your mood: "))
            if 1 <= choice <= len(mood_songs):
                return list(mood_songs.keys())[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_playlist(mood):
    return mood_songs.get(mood, [])

def main():
    display_menu()
    mood = get_mood_choice()
    playlist = generate_playlist(mood)
    
    print(f"\nHere’s a playlist for your '{mood}' mood:")
    for song in playlist:
        print(f"- {song}")

if __name__ == "__main__":
    main()
