import vk_api
import time

token=''


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

while True:
  time.sleep(297)
  vk.account.setOnline
