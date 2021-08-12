import instaloader

mod = instaloader.Instaloader()

user = input("Enter instagram username:")

mod.download_profile(user, profile_pic_only=True)
