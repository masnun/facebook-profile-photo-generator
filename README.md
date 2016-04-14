# Facebook Profile Photo Generator

## Setting Up

It's a Django app. So the installation/setup is trivial if you have deployed Django applications before. 

Install the dependencies from `requirements.txt` file.

    pip install -r requirements.txt

The app by default uses a SQLite Dabase which will be created for you when we run migrations. If you want to use other database engines (eg, mysql) please configure it in `settings.py` file. 

Run the migration:

	python manage.py migrate 
	
This would create the necessary tables for the app. 

We need to update the values for `SOCIAL_AUTH_FACEBOOK_KEY` and `SOCIAL_AUTH_FACEBOOK_SECRET` in `settings.py`. You can get the API Key and the Secret from <a href="https://developers.facebook.com/apps/">Facebook Developers portal</a>.  

Once we have run the migrations and set the API keys, we can run the Django dev server: 

	python manage.py runserver
	

Now visit the url - `http://localhost:8000` to see the app. 