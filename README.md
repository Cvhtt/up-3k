Терминал №1
Запускаем брокер:

python broker.py
Получим:

* Running on http://127.0.0.1:5000
Терминал №2
Отправляем сообщения:

python publisher.py
Терминал №3
Запускаем подписчика:

python subscriber.py


Убиваем брокер:

taskkill /F /PID <pid>

или

kill -9 <pid>


Запускаем снова:

python broker.py

Все сообщения останутся в:

topics/news.log





Load Balancing

Открой два окна:

python subscriber.py
python subscriber.py

Первый получит:

1..5

Второй:

6..10



Restart From Offset

Подписчик прочитал:

1..50

offset автоматически сохранится:

{
"group1": {
"news": 50
}
}

После перезапуска продолжит с 51-го сообщения.





Multiple Groups

Создай второго подписчика:

GROUP = "group2"

Теперь:

group1

и

group2

будут получать одинаковые сообщения независимо друг от друга.
