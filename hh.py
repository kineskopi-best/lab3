import serial  # Импорт библиотеки для работы с последовательным портом
import time  # Импорт библиотеки для работы с временем
import serial.tools.list_ports  # Импорт библиотеки для работы с перечислением доступных последовательных портов

speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']  # Список скоростей для последовательного порта
ports = [p.device for p in serial.tools.list_ports.comports()]  # Список доступных портов

port_name = ports[0]  # Выбор первого порта из списка
port_speed = int(speeds[0])  # Использование первой скорости из списка (1200)
port_timeout = 10  # Установка таймаута ожидания ответа

ard = serial.Serial(port_name, port_speed, timeout=port_timeout)  # Открытие соединения с последовательным портом
time.sleep(1)  # Пауза для стабилизации соединения
ard.flushInput()  # Очистка входного буфера порта

msg_str_ = ""  # Инициализация переменной для строки сообщения

try:
    # Чтение данных из порта и декодирование байтов в строку
    msg_bin = ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_str_ = msg_bin.decode()  # Декодирование байтов в строку
    print(len(msg_bin))  # Вывод длины принятого сообщения
except Exception as e:
    print('Error:', e)  # Вывод сообщения об ошибке при возникновении исключения

ard.close()  # Закрытие соединения с портом
time.sleep(1)  # Пауза для завершения передачи данных
print(msg_str_)  # Вывод принятого сообщения
