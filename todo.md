For the backend for this app, the goal is to generate json representations for FE.

As such, the actual data does not have to be stored at all in a model; just use a wrapper to store the time and place it was called.

Have the complete design and DB implementation ready before moving on.

Use a separate `router` for the other implementations and change the link.

Migrations are not committed; do a `python manage.py makemigrations` on stage.