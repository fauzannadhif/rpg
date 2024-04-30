# RoomPriceGenie Task

## Setup
- pip install -r requirements.txt
- install rabbitmq (you can use docker)
- cd to data_provider:
    - `python manage.py runserver 7000`
    - `celery -A data_provider worker -l info --pool=solo -Q send_event_topic`
    - `celery -A data_provider beat -l info`
- cd to dashboard_service:
    - `python manage.py runserver 9000`
    - `celery -A dashboard_service worker -l info --pool=solo -Q update_dashboard_topic`
    - `celery -A dashboard_service beat -l info`

## Setup with docker
- run `docker-compose up`

## Swagger
If you have successfully run the server, you can read the api documentation at http://localhost:7000/swagger and http://localhost:9000/swagger

## Data Provider
These are the apis available:
- Get events
`curl --location 'localhost:7000/events/'`
- Create event
`curl --location 'localhost:7000/events/' \
--header 'Content-Type: application/json' \
--data '{
    "hotel_id": 1,
    "timestamp": "2024-04-30T12:37:00Z",
    "rpg_status": 1, 
    "room_id": 1,
    "night_of_stay": "2024-04-30"
}'`

There is a celery task that is run every 1 minute to hit the create event endpoint to populate the data

## Dashboard Service
These are the apis available:
- Get dashboard
`curl --location 'localhost:9000/dashboard?period=month&year=2024&hotel_id=1'`

There is a celery task that is run every 1 minute to hit the get event endpoint to populate the data

