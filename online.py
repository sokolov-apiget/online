import vk_api

token=''


vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

While True:
  time.sleep(297)
  vk.account.setOnline
