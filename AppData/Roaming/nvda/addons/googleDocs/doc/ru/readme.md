# Поддержка  Google Документов для NVDA

Это дополнение улучшает совместимость с сервисом  Google Документы. Оно работает в режиме просмотра, заставляя команды Быстрой навигации и команды навигации курсором работать правильно. Например, если вы используете Google Документы без этого дополнения, то нажатие `H` приведёт вас к следующему заголовку, но только среди тех заголовков, которые видны на экране. Данное дополнение исправляет это поведение, и команда `H` теперь переводит вас ко всем заголовкам в документе.

## Установка

Для правильной работы этого дополнения нам необходимо в сервисе Google Документы включить режим  чтения с экрана и режим Брайля. Для этого:
* Убедитесь, что сочитание клавиш быстрого запуска NVDA по умолчанию либо не назначено, либо назначено не на комбинацию клавиш "Control+Alt+N". Для этого отредактируйте свойства вашего ярлыка NVDA на рабочем столе. Это требование взято из документации сервиса  Google документы.
* Откройте любой Google документ.
* Нажмите `Control+Alt+Z`, пока не услышите фразу "Поддержка  чтения экрана включена".
* Нажмите `Control+Alt+H`, пока не услышите фразу "поддержка  Брайля Включена ".
* Нажмите `NVDA+Space`, чтобы перейти в режим просмотра, если вы находитесь в режиме форм.

## Требования

Поддерживаемые браузеры:

* Google Chrome
* Mozilla Firefox

На данный момент это дополнение требует, чтобы на вашем компьютере была установлена раскладка клавиатуры "Английский_США". Это необходимо, потому что дополнение должно распознавать нажатия клавиш  в сервисе Google Документы, а оно делает это только в раскладке "Английский_США". Если раскладка клавиатуры "Английский_США" не будет найдена, произойдёт сбой. Pull-запросы на исправление этого поведения приветствуются.

## Поддерживаемые команды

Глобальные команды:

* `NVDA+Alt+G` - переключение доступности Google Документы\ (позволяет временно отключить функциональность этого дополнения)

Команды Быстрой навигации (их аналоги `Shift+` опущено для краткости):

* `H` - следующий заголовок
* `1..6` - следующий заголовок с 1 по 6 уровень
* `K` - следующая ссылка
* `L` - следующий список
* ``I`` - следующий элемент списка
* `G` - следующий графический элемент
* `T` - следующая таблица

Команды навигации:

* ``Клавиши-стрелки`
* `Control+Клавиши-стрелки`
* `Начало`, `Конец`
* `Control+Начало`, `Control+Конец`
`Страница Вверх`, `Страница Вниз`

## Известные проблемы

* Это дополнение требует, чтобы на компьютере была установлен раскладка клавиатуры`"Английский_США".
* Это дополнение преобразует команды NVDA в жесты сервиса Google Документы . Поэтому их поведение не может быть настроено.
* Например, повторное нажатие `H` приведёт к переходу в начало документа. Это неудобно для пользователей NVDA, но такова стандартная конфигурация  сервиса Google Документы, и, к сожалению, её нельзя изменить.
* Команды выделения, такие как` Shift+клавиши-стрелки ' в настоящее время не поддерживаются. Пожалуйста, для выделения переключитесь в режим просмотра.