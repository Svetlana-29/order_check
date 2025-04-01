# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт модуля data, в котором определены заголовок и тела запросов, необходимые для POST-запросов
import data
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body, headers = data.headers)
    track_number = response.json()['track']
    return track_number

# Определение функции get_order для отправки GET-запроса на получение информации о заказе по треку
def get_order(track_number):
    address = configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track_number)
    return requests.get(address)

