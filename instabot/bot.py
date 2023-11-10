from instabot import Bot
my_bot = Bot()
my_bot.login(username="patilancha_ladka_ganesh", password="")
my_bot.follow("chetri_sunil11")
my_bot.follow_users(["","",""])
my_bot.unfollow_non_followers()

my_bot.upload_photo("loggo.jpg", caption="pytube | create your own channel")

try:
    my_bot.send_message("hello chetri_sunil11!","chetri_sunil11")
    my_bot.like_user("chetri_sunil11", amount=2)
except Exception:
       print(Exception)

sleep(20)

try:
     user_id = my_bot.get_user_id_from_username("chetri_sunil11")
     media_id = my_bot.get_last_user_medias(user_id, 1)
     my_bot.comment(media_id[0],"very nice")
except Exception:
       print(Exception)

       sleep(20)

following_list = my_bot.get_user_followers("chetri_sunil11")
following_list = my_bot.get_user_following("chetri_sunil11")

for each_follower in followers_list:
    if count > 2:
        continue
    sleep(60)
    print(my_bot.get_username_from_user_id(each_follower))

for count1, each_follow in following_list:
    if count > 2:
       continue
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follow))

my_bot.logout()


