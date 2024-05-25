# Resource Monitor (Монітор ресурсів) #

* Автори: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst та інші учасники спільноти NVDA

Цей додаток надає інформацію про завантаженість процесора, використання
пам’яті та інших ресурсів.

# Гарячі клавіші

All commands support speech on demand mode (NVDA 2024.1 and later).

* NVDA+Shift+E: Надає інформацію про використання оперативної пам’яті,
  середню завантаженість процесора та акумулятор, якщо він є.
* NVDA+Shift+1: Надає інформацію про середню завантаженість процесора і про
  завантаженість кожного ядра.
* NVDA+Shift+2/5: Надає інформацію про зайнятий та повний об'єм як фізичної,
  так і віртуальної пам’яті.
* NVDA+Shift+3: надає інформацію про зайнятий та повний об’єм статичних та
  переносних дисків.
* NVDA+Shift+4: Повідомляє про відсоток акумулятора, статус заряджання, час,
  що залишився (якщо акумулятор не заряджається) і попередження про низький
  та критично низький заряд акумулятора.
* NVDA+Shift+6: називає архітектуру процесора, версію Windows та номер
  пакета оновлень — service pack.
* NVDA+Shift+7: повідомляє час роботи системи від моменту її завантаження.
* NVDA+Shift+8: показує інформацію про бездротове з'єднання, ім'я SSID та
  потужність мережі, або не показує імені, якщо воно відсутнє.

Ці комбінації клавіш можна змінити у діалозі «Жести вводу».

## Примітки про користування

Цей додаток не замінює диспетчера завдань Windows чи інших програм, які
надають інформацію про систему.  Також запам’ятайте:

* Інформацію про ресурси тепер неможливо скопіювати в буфер обміну, якщо
  додаток запущено на захищеному екрані.
* Використання центрального процесора подано для логічних процесорів, а не
  для фізичних ядер. Це важливо для процесорів, які використовують
  Hyper-Threading, де кількість процесорів удвічі перевищує кількість ядер
  процесора. На деяких нових комп'ютерах не всі ядра процесора можуть мати
  увімкнений hyper-threading.
* При інтенсивних діях на диску, таких як копіювання великих файлів, можливі
  затримки з отриманням інформації про використання диска.
* При оголошенні інформації про архітектуру процесора, «x86» і «AMD64»
  відносяться до 32-розрядних і 64-розрядних (x64) процесорів Intel і AMD
  відповідно.
* Цей додаток вимагає Windows 10 чи пізнішу.

Примітка про ліцензування: цей додаток використовує Psutil, проліцензований
ліцензією 3-Clause BSD, яка сумісна з GNU General Public License.

## Version 24.05

* NVDA 2024.1 or later is required.
* NVDA will recognize wireless networks with WPA3 authentication methods
  such as shared authentication of equals (SAE).

## Version 24.04

* Updated psutil dependency to 5.9.8.
* Added support for speech on demand mode so resource information can be
  announced in this mode.

## Version 23.11

* Downgraded psutil dependency to 5.9.4 due to problems with memory usage
  announcements.

## Version 23.10

* Updated psutil dependency to 5.9.5.

## Версія 23.09

* NVDA більше не буде реєструвати повідомлення про помилки запуску в
  системах Windows Server, коли модулі бездротового зв'язку недоступні.

## Версія 23.06

* Виправлено ситуації, коли «Монітор ресурсів» не працював належним чином
  через відсутність бездротових адаптерів.

## Версія 23.05.1

додаток wlanReporter для NVDA тепер є частиною «Монітора ресурсів»!

* Старий спосіб перевірки бездротових з'єднань було замінено на Windows API
  від wlanReporter: https://github.com/kvark128/WlanReporter/ .

	* Після промовляння імені та потужності SSID, NVDA також повідомить вам тип
	  безпеки вашої мережі.
	* Тепер NVDA сповіщатиме вас про підключення та відключення від бездротової
	  мережі.
	* Тепер NVDA повідомлятиме вам, коли бездротове з’єднання буде увімкнено
	  або вимкнено.

## Версія 23.05

* додано можливість виявлення й показу стану підключеної бездротової мережі.

	* Повідомляє ім’я SSID підключеної бездротової мережі.
	* Повідомляє потужність SSID
	* Якщо не знайдено жодного SSID, повідомляє про це.

## Версія 23.02

* Необхідна версія NVDA 2022.4 або новіша.
* Необхідна Windows 10 21H2 (November 2021 Update/build 19044) чи пізніша.

## Версія 23.01

* Необхідна версія NVDA 2022.3 або новіша.
* Вимагається Windows 10, оскільки в січні 2023 року Майкрософт припинила
  підтримку Windows 7, 8 і 8.1.
* Залежність psutil оновлено до 5.9.4.
* NVDA повідомлятиме поточну архітектуру процесора (x86/AMD64/ARM64) як
  частину інформації про версію Windows.
* На одноядерних системах NVDA більше не повідомлятиме про навантаження на
  ядро процесора, оскільки середнє навантаження на процесор збігається з
  навантаженням на ядро.

## Версія 22.03

Версія 22.03  остання стабільна версія, яка підтримує Windows 7 service pack
1, 8 і 8.1.

* Необхідна версія NVDA 2021.3 або новіша.
* Під час спроби встановити додаток на Windows 7, 8 і 8.1 з’являтиметься
  попереджувальне повідомлення.
* Залежність psutil оновлено до versії 5.9.0.

## Версія 22.01

* Необхідна версія NVDA 2021.2 або новіша.

## Версія 21.10

* Через зміни в NVDA, які впливають на цей додаток, потрібна версія NVDA
  2021.1 або новіша.

## Версія 21.08

* Мінімальні вимоги до версії Windows тепер прив’язані до версій NVDA.
* Збірки Windows 20348 і 22000 тепер розпізнаються як Windows Server 2022 і
  Windows 11, відповідно.
* У збірках Insider Preview тепер не використовуватиметься випуск Windows,
  наприклад, «Windows 10». Замість цього NVDA промовлятиме «Windows
  Insider».
* У 64-розрядних системах, архітектура процесора (x64 чи ARM64)
  промовлятиметься як частина інформації про версію Windows.

## Версія 21.04

* Необхідна версія NVDA 2020.4 або новіша.
* Оновлено psutil dependency до versії 5.8.0.
* Якщо двічі натиснути команди додатка для копіювання інформації про ресурс
  у буфер обміну, NVDA оголосить інформацію ресурсу, яка копіюється.

## Версія 21.01

* Оновлено psutil dependency до versії 5.7.3.
* Скорочено повідомлення версії Windows.
* У Windows 8.1 build.revision промовлятиметься як частина повідомлення про
  версію Windows, подібно до Windows 10.

## Версія 20.09

* Час безперервної роботи системи подано у днях, годинах, хвилинах і
  секундах.
* Windows Server Insider Preview build 20201 чи новіша належно розпізнається
  як Server Insider build.

## Версія 20.07

* Windows 10 версії 20H2 належно розпізнається при отриманні інформації про
  версію Windows (NVDA+Shift+6).
* Спрощено повідомлення про версію Windows 10 При натисканні NVDA+Shift+6:
  тепер промовляється Windows 10 РРММ замість Windows 10верРРММ.

## Версія 20.06

* Вирішено багато проблем зі стилем кодування та потенційні помилки за
  допомогою Flake8.

## Версія 20.04

* Оновлено psutil dependency до versії 5.7.0.

## Версія 20.01

* Через розширене використання Python 3 необхідна NVDA версії 2019.3 чи
  новіша.

## Версія 19.11

* Покращене виявлення збірок Windows Insider Preview, особливо для 20H1 та
  пізніших версій.

## Версія 19.07

* Оновлено psutil dependency до versії 5.6.3.
* Внутрішні зміни до команди повідомлення про стан акумулятора.

## Версія 18.12

* Внутрішні зміни для підтримки майбутніх версій NVDA.

## Версія 18.10

* Код став більш сумісним з Python 3.
* Оновлено psutil dependency до versії 5.4.7.
* Отримуючи об'єм диска та використання пам’яті, NVDA більше не видаватиме
  помилок при використанні комп'ютера або служби з обсягом оперативної
  пам'яті або розміром диска понад петабайт.
* Значення для використання пам'яті та диска відображаються з двома знаками
  після крапки (наприклад, 4.00 ГБ замість 4.0 ГБ).
* Поліпшено виявлення збірок Windows Insider Preview.

## Версія 18.04

Версія 18.04.x остання, яка підтримує Windows 7 без service pack 1.

* Остання версія, яка підтримує Windows Server 2003, Vista і Server 2008.
* Поліпшено виявлення версій Windows 10 і розрізнення між публічними
  випусками та збірками Insider Preview.

## Версія 17.12

* Додано підтримку 64-бітних ARM-процесорів у Windows 10.

## Версія 17.09

Важливо: Версія 17.09.x остання, яка підтримує Windows XP.

* Остання версія, яка запускається на Windows XP.
* Збірки 16278 та пізніших версій Windows 10 розпізнаються як версія
  1709. Незначне оновлення цього додатка буде випущено після випуску
  стабільної збірки версії 1709.

## Версія 17.07.1

* Повторно запроваджено підтримку Windows XP (не працює з версії 17.02).

## Версія 17.05

* Повідомляє час безперервної роботи системи (рахується з часу останнього
  завантаження; NVDA+Shift+7).

## Версія 17.02

* Оновлено psutil dependency до versії 5.0.1.
* Під час перевірки використання диска NVDA більше не відображатиме  помилок
  в деяких системах, де знімний носій не розпізнається належним чином
  (наприклад, якщо картка не вставлена в пристрій читання карток).)

## Версія 16.08

Починаючи з версії 16.08, нові версії додатка називатимуться за роком і
місяцем.

* Тепер різні версії Windows 10 розпізнаються належним чином (наприклад,
  1607 для збірки 14393).
* Версії збірок Windows 10 (після інсталяції сукупних оновлень)
  розпізнаються належним чином (наприклад, 14393.51).
* Якщо ви використовуєте збірки Insider Preview, це буде виявлено.

## Зміни у версії 4.5

* Репозиторій додатка переміщено на GitHub (знайдіть його за адресою
  https://github.com/josephsl/resourcemonitor).
* Належно розпізнається Windows Server 2016.

## Зміни у версії 4.0

* Оновлено psutil dependency до versії 2.2.1.
* Значно поліпшено продуктивність під час отримання інформації про
  завантаженість процесора.
* Додано підтримку розпізнавання Windows 10.
* У Windows 10 також буде промовлятися номер збірки Windows.
* Для перегляду довідки додатка скористайтеся менеджером додатків.

## Зміни у версії 3.1

* Resource Monitor офіційно підтримує Windows 8.1.
* Оновлено переклади.

## Зміни у версії 3.0

* Оновлено psutil dependency до versії 1.2.1.
* Промовляє поточну версію Windows, архітектуру процесора і service pack за
  наявності (NVDA+Shift+6).
* Можливість змінити комбінації клавіш додатка (NVDA 2013.3 чи новіші).
* Можливість копіювати інформацію про окремий ресурс у буфер обміну, двічі
  натискаючи команди ресурсів.

## Зміни у версії 2.4

* Нові мови: китайська (традиційне письмо) та українська.
* Оновлено переклади.

## Зміни у версії 2.3

* Додано болгарську мову інтерфейсу.

## Зміни у версії 2.2

* Додано aragonese, Galatian, арабську, іспанську, італійську, корейську,
  непальську, нідерландську, німецьку, польську, португальську (Бразилія),
  російську, словацьку, словенську, тамільську, турецьку, угорську, фінську,
  французьку, хорватську та японську мови.

## Зміни у версії 2.1

* Оновлено psutil dependency до versії 0.6.1.
* Виправлено велику затримку при отриманні інформації про диски.
* Почищено код.

## Зміни у версії 2.0

* додано підтримку перекладів і коментарів до них.

## Зміни у версії 1.0

* Перший реліз

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor