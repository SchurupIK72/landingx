# ТЗ: добавить блок дополнительных услуг из визитки PRONET SERVICES

## 1. Цель
Расширить лендинг PRONET SERVICES новым блоком дополнительных услуг, чтобы показать, что компания оказывает не только ремонт и настройку компьютеров, но и digital/IT-услуги для бизнеса: performance, support, AI и automation.

## 2. Основа для контента
Пункты, считанные с визитки:

`Performance & Stability`
- `Website Speed Check`
  `don't lose customers because of a slow site`
- `Bug Finding & Fixing`
  `we find and fix errors before your users do`
- `Monthly IT Support`
  `reliable help to keep your business running`
- `Load & Stress Testing`
  `make sure your site survives peak sales`

`AI & Automation`
- `AI Business Tools`
  `use chatgpt and ai to work faster and smarter`
- `Custom AI Automation`
  `automate your daily tasks with ai power`
- `App & API Integration`
  `connect all your tools into one smart system`
- `Smart Booking & Orders`
  `automated systems that handle clients 24/7`

## 3. Продуктовая логика
- Основной оффер лендинга не менять: сайт по-прежнему в первую очередь продает ремонт и настройку компьютеров/ноутбуков.
- Новый блок подается как `Additional Services` / `Business Tech Services`.
- Это кросс-сейл блок: он расширяет доверие и средний чек, но не перетягивает фокус с основной услуги.
- CTA внутри блока не нужен отдельный агрессивный; достаточно кнопки или текстовой ссылки к финальному `#contact`.

## 4. Изменение структуры страницы
Добавить новый отдельный блок между текущими секциями:
- после `#services`
- перед `#trust`

Новый section:
- `id="extras"`
- тип блока: двухколоночный grid
- слева категория `Performance & Stability`
- справа категория `AI & Automation`

Итоговая структура станет:
- `#hero`
- `#benefits`
- `#services`
- `#extras`
- `#trust`
- `#contact`

## 5. Контент блока
Заголовок секции:
- EN: `Additional Services for Business Growth`
- VI: `Dịch vụ bổ sung cho tăng trưởng doanh nghiệp`

Подзаголовок:
- EN: `Beyond repair and setup, PRONET SERVICES helps improve website performance, automate routine work and connect the tools your business depends on.`
- VI: `Ngoài sửa chữa và cài đặt, PRONET SERVICES còn hỗ trợ tối ưu hiệu suất website, tự động hóa công việc hằng ngày và kết nối các công cụ doanh nghiệp đang sử dụng.`

Колонка 1:
- EN category: `Performance & Stability`
- VI category: `Hiệu suất & ổn định`

Карточки:
- `Website Speed Check`
  EN desc: `Don't lose customers because of a slow site.`
  VI desc: `Đừng mất khách hàng chỉ vì website tải chậm.`

- `Bug Finding & Fixing`
  EN desc: `We find and fix errors before your users do.`
  VI desc: `Chúng tôi tìm và sửa lỗi trước khi người dùng của bạn gặp phải.`

- `Monthly IT Support`
  EN desc: `Reliable help to keep your business running.`
  VI desc: `Hỗ trợ định kỳ để doanh nghiệp của bạn vận hành ổn định.`

- `Load & Stress Testing`
  EN desc: `Make sure your site survives peak sales.`
  VI desc: `Đảm bảo website vẫn ổn định khi lưu lượng truy cập tăng cao.`

Колонка 2:
- EN category: `AI & Automation`
- VI category: `AI & tự động hóa`

Карточки:
- `AI Business Tools`
  EN desc: `Use ChatGPT and AI to work faster and smarter.`
  VI desc: `Ứng dụng ChatGPT và AI để làm việc nhanh hơn và thông minh hơn.`

- `Custom AI Automation`
  EN desc: `Automate your daily tasks with AI power.`
  VI desc: `Tự động hóa các tác vụ hằng ngày bằng giải pháp AI phù hợp.`

- `App & API Integration`
  EN desc: `Connect all your tools into one smart system.`
  VI desc: `Kết nối các công cụ của bạn thành một hệ thống thông minh.`

- `Smart Booking & Orders`
  EN desc: `Automated systems that handle clients 24/7.`
  VI desc: `Hệ thống tự động tiếp nhận đặt lịch và đơn hàng 24/7.`

Нижняя строка блока:
- EN: `Need one of these solutions? Contact PRONET SERVICES for a direct consultation.`
- VI: `Cần một trong các giải pháp này? Liên hệ PRONET SERVICES để được tư vấn trực tiếp.`

## 6. UI/UX требования
- Визуально блок должен быть в том же tech-premium стиле, что и остальной лендинг.
- Использовать 2 крупные category cards, внутри каждой по 4 service cards или compact rows.
- На desktop:
- 2 колонки по категориям
- внутри каждой 4 элемента
- На mobile:
- одна колонка
- сначала `Performance & Stability`, затем `AI & Automation`
- Не перегружать блок тяжелой графикой.
- Можно использовать фоновые glow-акценты, сетку, тонкие рамки и glassmorphism, как в существующих секциях.
- Важный акцент: блок должен выглядеть как допуслуги, а не как новый главный оффер.

## 7. Требования к локализации
Так как сайт уже поддерживает EN/VI:
- все новые тексты должны быть добавлены в существующий JS-словарь `translations.en` и `translations.vi`
- все новые элементы должны быть размечены через `data-i18n`
- при переключении языка блок должен полностью переключаться без перезагрузки
- если будут `aria-label`, их тоже локализовать

Новые ключи перевода рекомендовано назвать:
- `extrasEyebrow`
- `extrasTitle`
- `extrasLead`
- `extrasCategory1`
- `extrasCategory2`
- `extrasService1Title` ... `extrasService8Title`
- `extrasService1Text` ... `extrasService8Text`
- `extrasFooter`

## 8. Технические изменения
В `index.html`:
- добавить новый section `#extras`
- вставить его между `#services` и `#trust`
- разметить все новые тексты через `data-i18n`

В `styles.css`:
- добавить стили для секции допуслуг
- добавить responsive grid для 2 категорий
- поддержать мобильное отображение без ломки общей вертикальной ритмики

Во встроенном JS словаре в `index.html`:
- добавить все EN/VI ключи для нового блока

## 9. Критерии приемки
- На странице появился новый блок `#extras`
- Все 8 услуг с визитки отображаются без пропусков
- Блок визуально соответствует текущему дизайну сайта
- На мобильных устройствах блок читается и не ломает layout
- EN/VI локализация работает для всех новых заголовков и описаний
- Основной фокус сайта на ремонте компьютеров сохраняется, а допуслуги воспринимаются как расширение сервиса
