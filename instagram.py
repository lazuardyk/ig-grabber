import json
import requests
import scrapper
import re
samadengan = "="*25
welcome = samadengan + "Instagram Data Grabber" + samadengan
welcome2 = "by LazuardyK"
print('{:^80}'.format(welcome))
print('{:^80}'.format(welcome2))
print()
usernamenya = input("Username instagram yang ingin di Grab: ")

userurl = "https://instagram.com/{}".format(usernamenya)
content = scrapper.get(userurl)
id = content.find_all('script')
id = re.search(r'"id":"(.*)","is_business_account', str(id)).group(1)
url = "https://i.instagram.com/api/v1/users/{}/info/".format(id)
user_info = json.loads(requests.get(url).text)
profile_username = user_info['user']['username']
profile_name = user_info['user']['full_name']
profile_bio = user_info['user']['biography']
profile_link = user_info['user']['external_url']
profile_post = user_info['user'] ['media_count']
profile_followers = user_info['user']['follower_count']
profile_following = user_info['user']['following_count']
profile_photo_url = user_info['user']['hd_profile_pic_url_info']['url']

print()
print("Hasil:")
print("Username: {}".format(profile_username))
print("Nama: {}".format(profile_name))
print("Bio: {}".format(profile_bio))
print("Link: {}".format(profile_link))
print("Jumlah post: {}".format(profile_post))
print("Jumlah followers: {}".format(profile_followers))
print("Jumlah following: {}".format(profile_following))
print()
x = input("Apakah Anda perlu mengunduh foto profilnya? (ya/tidak): ")
if x == "ya":
    pp = requests.get(profile_photo_url).content
    with open('{}.jpg'.format(profile_username),'wb') as f:
        f.write(pp)
    print("Berhasil mengunduh!")
    input("Tekan apa saja untuk keluar")
else:
    i = input("Silahkan keluar dengan mengetik tombol apapun")
    exit()
