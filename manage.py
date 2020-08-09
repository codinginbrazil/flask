from app import manager


if __name__ == "__main__":
    # migrate.init_app(app, db)
    """ manager.run()
        Assuming the above script is stored in a file named manage.py, 
        all the database migration 
        commands can be accessed by running the script
            python manage.py db init
            python manage.py db migrate
            python manage.py db upgrade
        [Doc](https://flask-migrate.readthedocs.io/en/latest/)
        python manage.py db --help
    """
    manager.run()