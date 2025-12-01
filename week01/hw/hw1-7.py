while True:
    user_input = input("To see the youtube information type 'youtube' and for the music type 'music' :  ")

    if user_input == "youtube":

        yt_play: bool = False

        video_title: str = "C++ Full Course for free"

        youtuber_name: str = "Bro Code"

        views: int = 6389322

        rounded_views: float = round(views / 1000000, 2)

        release_date: str = "2023\\05\\29"

        comments_count: int = 7392

        rounded_comments_count: float = round(comments_count / 1000, 2)

        if yt_play == True:
            print("The youtube video is playing now.")
        else:
            print("The youtube video is not playing now.")
        
        print("The Youtube title is: ", video_title)
        print("The name of the channel is: ", youtuber_name)
        print("The view count of the video is: ", rounded_views, "M")
        print("Release date of this video is: ", release_date)
        print("The number of comments on this video is: ", rounded_comments_count, "K")

        while True:
            direction: str = input("To exit type 'quit' or if you want to go to the main menu type 'menu': ")

            if direction == "quit":
                quit: bool = True
                break
            elif direction == "menu":
                quit: bool = False
                break
            else:
                print("Invalid input")
                continue
        if quit == True:
            break
        elif quit == False:
            continue
    

    elif user_input == "music":
        music_play: bool = True

        music_title: str = "Blinding Lights"

        artist_name: str = "The Weeknd"

        views: int = 5020656062

        rounded_views: float = round(views / 1000000000, 2)

        release_date: str = "2019\\11\\29"

        if music_play == True:
            print("The music is playing now.")
        else:
            print("The music is not playing now.")
        
        print(f"The music is: {music_title}")
        print(f"The name of the artist is: {artist_name}")
        print(f"The view count of the music is: ", rounded_views, "B")
        print(f"Release date of this music is: ", release_date)

        ask_lyrics: str = input("Do you want the lyrics? (y/n): ")

        if ask_lyrics == "y":
            print("""[Intro]
        Yeah

        [Verse 1]
        I've been tryna call
        I've been on my own for long enough
        Maybe you can show me how to love, maybe
        I'm goin' through withdrawals
        You don't even have to do too much
        You can turn me on with just a touch, baby

        [Pre-Chorus]
        I look around and
        Sin City's cold and empty (Oh)
        No one's around to judge me (Oh)
        I can't see clearly when you're gone

        [Chorus]
        I said, ooh, I'm blinded by the lights
        No, I can't sleep until I feel your touch
        I said, ooh, I'm drowning in the night
        Oh, when I'm like this, you're the one I trust
        Hey, hey, hey

        [Verse 2]
        I'm running out of time
        'Cause I can see the sun light up the sky
        So I hit the road in overdrive, baby, oh
        See The Weeknd Live
        Get tickets as low as $40

        You might also like
        Open Hearts
        The Weeknd
        The Abyss
        The Weeknd & Lana Del Rey
        Enjoy The Show
        The Weeknd & Future

        [Pre-Chorus]
        The city's cold and empty (Oh)
        No one's around to judge me (Oh)
        I can't see clearly when you're gone

        [Chorus]
        I said, ooh, I'm blinded by the lights
        No, I can't sleep until I feel your touch
        I said, ooh, I'm drowning in the night
        Oh, when I'm like this, you're the one I trust

        [Bridge]
        I'm just calling back to let you know (Back to let you know)
        I could never say it on the phone (Say it on the phone)
        Will never let you go this time (Ooh)

        [Chorus]
        I said, ooh, I'm blinded by the lights
        No, I can't sleep until I feel your touch
        Hey, hey, hey

        [Post-Chorus]
        Hey, hey, hey

        [Outro]
        I said, ooh, I'm blinded by the lights
        No, I can't sleep until I feel your touch""")
        
        while 0 == 0:
            direction: str = input("To exit type 'quit' or if you want to go to the main menu type 'menu': ")

            if direction == "quit":
                quit: bool = True
                break
            elif direction == "menu":
                quit: bool = False
                break
            else:
                print("Invalid input")
                continue
        if quit == True:
            break
        elif quit == False:
            continue
            
    else:
        print("Invalid input")
        continue