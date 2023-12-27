from src.channel import Channel

if __name__ == '__main__':
    wylsacom = Channel('@Wylsacom')
    wylsacom.print_info()
    # получаем значения атрибутов
    print(wylsacom.title)  # wylsacom
    print(wylsacom.video_count)  # 10.5 млн
    print(wylsacom.url)  # https://www.youtube.com/@Wylsacom

    # менять не можем
    wylsacom.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'wylsacom.json' c данными по каналу
    wylsacom.to_json('wylsacom.json')