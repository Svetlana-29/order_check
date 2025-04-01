# Импорт модуля data, в котором определены заголовок и тела запросов, необходимые для POST-запросов
import data
# Импорт модуля sender_stand_request, содержащего функции для отправки HTTP-запросов к API
import sender_stand_request

# Функция для получения информации о заказе по треку заказа
def check_info(order_body):
    # В переменной get_track вызывается функция создания нового заказа
    get_track = sender_stand_request.post_new_order(order_body)
    # В переменной order_info сохраняется результат запроса на получение информации о заказе
    order_info = sender_stand_request.get_order(get_track)
    
    # Проверяется, что код ответа 200
    assert order_info.status_code == 200

# Тест проверки получения успешного ответа на создание заказа
# data_order_body - данные для создания заказа
def test():
    check_info(data.order_body)