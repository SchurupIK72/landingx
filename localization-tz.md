# ТЗ: переключатель локализации EN / VI и вьетнамская локализация лендинга PRONET SERVICES

## 1. Цель
Добавить в хедер переключатель языка `EN / VI` и реализовать полную вьетнамскую локализацию текущего лендинга без изменения структуры, дизайна и конверсионной логики страницы.

## 2. Текущее состояние
Сайт сейчас одностраничный, статический, на английском языке.

Структура:
- `header`
- `#hero`
- `#benefits`
- `#services`
- `#trust`
- `#contact`

Технологии:
- чистые `HTML + CSS`
- без библиотек
- без JS-логики локализации

Текущие файлы:
- `index.html`
- `styles.css`

## 3. Объем работ
Нужно:
- добавить в хедер UI-переключатель языка `EN / VI`
- перевести весь пользовательский текст сайта на вьетнамский
- реализовать переключение языков на клиенте без перезагрузки страницы
- обновлять `lang` у тега `<html>`
- сохранять выбранный язык в `localStorage`
- при первом заходе показывать английскую версию по умолчанию

Не нужно:
- менять дизайн-концепцию
- менять структуру секций
- добавлять сторонние i18n-библиотеки
- переводить изображения внутри баннера, так как это графический asset

## 4. Требования к UI переключателя
- Переключатель разместить в хедере справа, рядом с контактными действиями.
- Формат: компактный сегментированный контрол с двумя кнопками `EN` и `VI`.
- Активный язык должен визуально выделяться.
- На mobile переключатель должен корректно переноситься и не ломать layout `topbar`.
- Переключатель должен быть доступным:
- использовать кнопки или radio-like control
- иметь `aria-label="Language switcher"`
- активное состояние должно читаться скринридером

## 5. Функциональные требования
- При клике на `EN` весь интерфейс переключается на английский.
- При клике на `VI` весь интерфейс переключается на вьетнамский.
- Переключение должно менять:
- тексты в хедере
- все заголовки, подзаголовки, списки, кнопки
- подписи в карточках
- служебные тексты и метки
- `document.title`
- `<html lang="en">` / `<html lang="vi">`
- `aria-label`, если он содержит языкозависимый текст
- Номер телефона, email, section id и href-ссылки не менять.
- Выбранный язык хранить в `localStorage` по ключу `site-language`.
- Если в `localStorage` нет значения, использовать `en`.

## 6. Рекомендуемая реализация
- В `index.html`:
- добавить переключатель языка в `header.topbar`
- всем переводимым элементам добавить `data-i18n="key"`
- для атрибутов использовать отдельные ключи, например `data-i18n-aria-label`, `data-i18n-title`
- Добавить небольшой `script` внизу `body` без внешних зависимостей.
- Хранить словарь переводов в объекте вида:

```js
const translations = {
  en: { ... },
  vi: { ... }
};
```

- Функция `setLanguage(lang)` должна:
- обновлять текстовые узлы
- обновлять `document.documentElement.lang`
- обновлять `document.title`
- обновлять активное состояние переключателя
- сохранять язык в `localStorage`

## 7. Словарь переводов: обязательный контент
- `Computer & Laptop Repair`
  `Sua chua may tinh va laptop`

- `Email us`
  `Gui email`

- `Service Center in Nha Trang`
  `Trung tam dich vu tai Nha Trang`

- `Fast Computer & Laptop Repair in Nha Trang`
  `Sua chua may tinh va laptop nhanh tai Nha Trang`

- `Slow laptop, broken PC, virus issues or software problems? PRONET SERVICES restores your device fast, clearly and without hidden costs.`
  `Laptop cham, PC hong, nhiem virus hoac loi phan mem? PRONET SERVICES giup thiet bi cua ban hoat dong tro lai nhanh, ro rang va khong co chi phi an.`

- `Call Now`
  `Goi ngay`

- `Message Us`
  `Nhan tin`

- `Windows setup, virus removal, upgrades, software install, Wi-Fi and printer configuration.`
  `Cai dat Windows, diet virus, nang cap, cai dat phan mem, cau hinh Wi-Fi va may in.`

- `Transparent diagnostics`
  `Chan doan ro rang`

- `Hardware + software support`
  `Ho tro ca phan cung va phan mem`

- `English-friendly communication`
  `Ho tro giao tiep than thien`

- `Why people contact us`
  `Ly do khach hang tim den chung toi`

- `When your device stops, work and daily life stop with it.`
  `Khi thiet bi cua ban dung hoat dong, cong viec va cuoc song hang ngay cung bi gian doan.`

- `We help you avoid downtime, confusion and repeat repairs with a practical service process from the first check to the final fix.`
  `Chung toi giup ban giam thoi gian gian doan, tranh mo ho va han che sua lai nhieu lan bang quy trinh ro rang tu luc kiem tra den khi khac phuc xong.`

- `Clear diagnostics before repair`
  `Kiem tra va chan doan ro rang truoc khi sua`

- `You understand the issue first, then decide on the next step with confidence.`
  `Ban hieu ro van de truoc, sau do moi quyet dinh cach xu ly phu hop.`

- `Fast turnaround for urgent cases`
  `Xu ly nhanh cho truong hop gap`

- `We focus on getting your working device back as quickly as the repair allows.`
  `Chung toi uu tien tra lai thiet bi hoat dong som nhat co the.`

- `Transparent pricing with no surprise fees`
  `Chi phi minh bach, khong phat sinh bat ngo`

- `Simple communication, clear expectations and no vague repair language.`
  `Trao doi don gian, ky vong ro rang va khong mo ho trong bao gia.`

- `One service point for hardware and software issues`
  `Mot diem dich vu cho ca loi phan cung va phan mem`

- `Bring one problem or several. We handle the full device setup, not just one symptom.`
  `Du ban gap mot van de hay nhieu van de, chung toi deu co the ho tro tong the cho thiet bi.`

- `What we do`
  `Dich vu cua chung toi`

- `Everything your computer needs in one place`
  `Moi thu may tinh cua ban can, trong cung mot noi`

- `Bring your device to our service center and get a practical fix, not a vague promise.`
  `Mang thiet bi den trung tam dich vu va nhan giai phap thuc te, khong chi la loi hua mo ho.`

- `Laptop & PC repair`
  `Sua chua laptop va PC`

- `Windows installation and optimization`
  `Cai dat va toi uu Windows`

- `Virus cleanup and security setup`
  `Diet virus va thiet lap bao mat`

- `Software installation and configuration`
  `Cai dat va cau hinh phan mem`

- `Data backup and basic recovery`
  `Sao luu va khoi phuc du lieu co ban`

- `Wi-Fi and printer setup`
  `Cai dat Wi-Fi va may in`

- `System diagnostics in progress`
  `Dang kiem tra he thong`

- `Hardware`
  `Phan cung`

- `Software`
  `Phan mem`

- `Security`
  `Bao mat`

- `Network`
  `Mang`

- `Repair workflow`
  `Quy trinh xu ly`

- `Check, explain, fix, test`
  `Kiem tra, tu van, sua chua, kiem thu`

- `Trust signals`
  `Ly do de tin tuong`

- `Why clients choose PRONET SERVICES`
  `Vi sao khach hang chon PRONET SERVICES`

- `Built for clarity, practical support and local convenience when your laptop or PC needs attention.`
  `Chung toi tap trung vao su ro rang, ho tro thuc te va su thuan tien tai dia phuong khi laptop hoac PC cua ban gap van de.`

- `Local service center in Nha Trang`
  `Trung tam dich vu tai Nha Trang`

- `Easy to find, easy to contact, easy to bring your device in for direct support.`
  `De tim, de lien he va de mang thiet bi den de duoc ho tro truc tiep.`

- `Direct communication by phone, email and Facebook`
  `Lien he truc tiep qua dien thoai, email va Facebook`

- `Reach us in the channel that feels fastest for your repair or setup request.`
  `Lien he qua kenh thuan tien nhat cho yeu cau sua chua hoac cai dat cua ban.`

- `Friendly support for local and international customers`
  `Ho tro than thien cho khach hang dia phuong va quoc te`

- `Helpful communication without technical confusion or unnecessary complexity.`
  `Trao doi de hieu, khong gay roi boi qua nhieu thuat ngu ky thuat.`

- `Modern troubleshooting for both hardware and software`
  `Chan doan hien dai cho ca phan cung va phan mem`

- `From system errors to physical issues, we look at the whole device experience.`
  `Tu loi he thong den su co phan cung, chung toi danh gia tong the tinh trang thiet bi.`

- `Clear explanation, quick repair, easy communication.`
  `Giai thich ro rang, sua chua nhanh, giao tiep de dang.`

- `Sample customer-style feedback until verified reviews are added.`
  `Noi dung mo phong danh gia khach hang cho den khi co nhan xet xac thuc.`

- `Ready to fix it?`
  `San sang sua chua?`

- `Need your device working again today?`
  `Can thiet bi hoat dong tro lai ngay hom nay?`

- `Call PRONET SERVICES now and get direct help with repair, setup or diagnostics.`
  `Hay goi cho PRONET SERVICES ngay de nhan ho tro truc tiep ve sua chua, cai dat hoac chan doan.`

- `Call +84 389 935 306`
  `Goi +84 389 935 306`

- `Email`
  `Email`

- `Location`
  `Dia diem`

- `Facebook`
  `Facebook`

- `QR contact available on the current brand banner`
  `Ma QR lien he hien co tren banner thuong hieu`

## 8. Технические ограничения
- Без изменения существующих `href`.
- Без дублирования HTML для каждой локали.
- Без серверной логики.
- Все переводы должны храниться централизованно в одном JS-словаре.

## 9. Критерии приемки
- В хедере виден и работает переключатель `EN / VI`.
- Вся страница полностью переключается между английским и вьетнамским.
- После перезагрузки сохраняется выбранный язык.
- На mobile хедер и переключатель не ломают верстку.
- Атрибут `lang` у `<html>` меняется корректно.
- Никакие CTA, ссылки, номера телефона и email не ломаются.
- Не остается английских текстов в режиме `VI`, кроме бренда `PRONET SERVICES`.
