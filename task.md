## Практическое задание

Доработать сервис распознающий номерной знак с картинки:

### Этап 1

Сделать хендлер, который принимает на вход ID картинки (формат API нужно придумать самостоятельно).

По пришедшему ID нужно скачать картинку со стороннего сервиса.

После скачивания, нужно распознать номер картинки и отдать ответ в формате JSON

### Этап 2

Потребители нашего сервиса хотят отправлять нам сразу несколько ID в одном запросе.

Нужно создать новый хендлер, выполняющий то же самое, только сразу с несколькими картинками (формат API нужно придумать самостоятельно).

Требования к реализации:

- Сервис должен учитывать, что при скачивании картинки могут возникнуть проблемы. В таких случаях нужно отдавать понятный ответ с ошибкой.
- Желательно написать сервис так, чтобы в нем не было дублирования кода.
- Сервис должен запускаться с помощью docker run.
 