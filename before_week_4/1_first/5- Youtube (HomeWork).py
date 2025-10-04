title: str = "C++ Full Course for free"

youtuber_name: str = "Bro Code"

views: int = 6389322

rounded_views: float = round(views / 1000000, 2)

release_date: str = "2023\\05\\29"

comments_count: int = 7392

rounded_comments_count: float = round(comments_count / 1000, 2)

print("The Youtube title is: ", title)
print("The name of the channel is: ", youtuber_name)
print("The view count of the video is: ", rounded_views, "M")
print("Release date of this video is: ", release_date)
print("The number of comments on this video is: ", rounded_comments_count, "K")
