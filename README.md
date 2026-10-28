# Лабораторная работа №5

![Docker](https://img.shields.io/badge/Docker-29.4.2-2496ED?logo=docker&logoColor=white)
![Compose](https://img.shields.io/badge/Docker%20Compose-5.1.3-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Lab](https://img.shields.io/badge/lab-05-blue)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

## Цель работы

Изучение сборки и запуска Docker-образов, анализа Dockerfile,
изоляции контейнеров с помощью namespaces, ограничения ресурсов через
cgroups, организации контейнерных сетей и запуска многоконтейнерного
приложения с помощью Docker Compose.

## Выполненные действия

- проведён аудит безопасности исходного Dockerfile
- настроен `.dockerignore` и исследован размер контекста сборки
- исходное приложение заменено собственным Python-приложением на Typer
- закреплены версии Python-зависимостей
- исследованы слои single-stage и multi-stage образов
- приложение переведено на запуск от непривилегированного пользователя
- Docker-образ сохранён в TAR-архив и опубликован в Docker Hub
- изучена изоляция процессов, файловой системы и hostname через namespaces
- проверены ограничения памяти и CPU через cgroups
- создана пользовательская Docker-сеть и проверен встроенный DNS
- настроено взаимодействие серверного и клиентского контейнеров
- добавлены healthcheck, повторные запросы и тайм-ауты
- включён параметр безопасности `no-new-privileges`
- доступ к серверу ограничен интерфейсом `127.0.0.1`.

## Структура проекта

- `source/` - кустарное консольное Python-приложение и его Dockerfile
- `server/` - Flask-сервер с HTML, API и healthcheck-маршрутами
- `client/` - клиент для обращения к серверу по внутренней сети docker
- `docker-compose.yml` - здесь находится конфигурация многоконтейнерного приложения
- `DOCKERFILE_AUDIT.md` - результат аудита исходного dockerfile
- `.gitignore`

## Запуск Docker Compose

```bash
docker compose up --build -d
```
Проверка приложения:

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/api/message
```

Остановка и удаление ресурсов:

```bash
docker compose down --remove-orphans
```

## Docker Hub

Собранный образ опубликован в Docker Hub:

<https://hub.docker.com/r/nikmillerson/hello-appsec-world>

Доступные теги:

- `latest`
- `lab05`

Образ приложения запускается от непривилегированного пользователя `app`.

## Вывод

В ходе лабораторной работы были изучены жизненный цикл Docker-образа,
multi-stage сборка, безопасная конфигурация Dockerfile, namespaces,
cgroups, пользовательские сети и Docker Compose. Итоговый стенд проверяет
готовность сервера перед запуском клиента и использует встроенный DNS
Docker для взаимодействия сервисов по имени.
