# WeatherCast
Weathercast is a weather forecasting application that utilizes the OpenWeatherMap API to retrieve weather data and present it in a user-friendly manner. The app allows users to select specific latitude and longitude coordinates using a map plugin to obtain weather information for a desired location. Additionally, users have the option to provide their own paid API key to access weather data from OpenWeatherMap.

## Visit the application (Deployed on Vercel)
- [WeatherCast](https://weather-forecast-plum.vercel.app/)

## Screenshots -- 
![image](https://github.com/EGhost98/Weather-Forecast/assets/76267623/cc8b05aa-554d-44f0-a30b-1f7bfe29222b)

![image](https://github.com/EGhost98/Weather-Forecast/assets/76267623/08b86be3-e75e-4498-8683-84a7c11a676c)

## Table of Contents

- [Description](#weathercast)
- [How to Run the Project](#how-to-run-the-project)
- [Tech Stack Used](#tech-stack-used)
- [Project Structure](#project-structure)
- [Models Explanation](#models-explanation)
- [URL Patterns](#url-patterns)
- [Views Explanation](#views-explanation)
- [Custom API Endpoint](#custom-api-endpoint)
- [Tests Explanation](#tests-explanation)
- [Key Takeaways](#key-takeaways)
- [References](#references)

## How to Run the Project
To run the project, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Create a Virtual Python Environment `python -m venv env`.
3. Activate the Virtual Environment (if using Git-Bash) `source env/Scripts/Activate`
4. Navigate to the project directory: `cd Weather-Forecast`
5. Install the dependencies: `pip install -r requirements.txt`
6. Read the .env.example and create a .env file in root diectory (For Your Own OpenWeatherMap [API Key](https://openweathermap.org/api)).
7. Change Databases in Settings.py as required. (local or Your Own Database).
8. Run the migrate command `python manage.py migrate`
9. Run the application: `python manage.py runserver`
10. Access the application in your web browser at: `http://localhost:8000`

Note: Make sure you have Python and Django installed on your system before running the project.
The application runs on the local development server when the script is executed directly.

## Tech Stack Used

- **Python**: Python is a versatile and widely-used programming language known for its simplicity and readability. It serves as the core programming language for the backend development of the project.

- **Django**: Django is a high-level Python web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a robust set of tools and features for building web applications efficiently.

- **Django REST Framework**: Django REST Framework is a powerful toolkit for building RESTful APIs in Django. It simplifies the process of building APIs by providing serializers, authentication, request handling, and other essential functionalities.

- **PostgreSQL**: PostgreSQL is a powerful open-source relational database management system. It is known for its reliability, scalability, and extensive feature set, making it a suitable choice for storing and managing structured data.

- **HTML/CSS**: HTML (Hypertext Markup Language) is the standard markup language used for creating the structure of web pages. CSS (Cascading Style Sheets) is used for styling and visually enhancing the HTML elements.

- **JavaScript**: JavaScript is a versatile programming language that adds interactivity and dynamic functionality to web pages. It is primarily used on the client-side for implementing interactive features and enhancing the user experience.

- **OpenWeatherMap API**: The OpenWeatherMap API is an external service that provides weather data. It offers various endpoints to retrieve weather information based on geographical coordinates, allowing the application to access real-time weather data.

- **Map Plugin**: A Map Plugin (specific plugin name or description can be added) is integrated into the application to allow users to visually select latitude and longitude coordinates on a map. This plugin enhances the user experience by providing an intuitive interface for location selection.

- **Git**: Git is a distributed version control system widely used for tracking changes in code and collaborating with other developers. It allows for efficient branching, merging, and tracking of code changes throughout the development process.

- **Vercel**: Vercel is a cloud platform designed for hosting and deploying web applications. It provides an easy and seamless deployment process, making it convenient to deploy the Weathercast application to the web.

- **Other Libraries and Dependencies**: The project may utilize additional Python libraries and dependencies to enhance specific functionality. For example, the `requests` library may be used for making HTTP requests, `unittest` or `mock` for testing, and other libraries based on the project's requirements.

## Project Structure

The project follows a typical Django project structure:

- **core**: Contains the core files and configurations of the Django application.
  
  - **wsgi.py**: WSGI (Web Server Gateway Interface) configuration file.

  - **settings.py**: Configures the Django application settings, including database connection, installed apps, middleware, static files, templates, and other project-specific configurations.
  
- **/forecast**: The main Django app directory containing the project-specific code.

  - **/migrations**: Directory containing database migration files generated by Django.

  - **/templates**: Directory for HTML templates used to render the views.

  - **/templatetags**: Directory for custom template tags and filters.

  - **admin.py**: Django admin configuration file for registering models.

  - **api_url.py**: File containing utility functions for generating API URLs based on detailing type, API key, latitude, and longitude.

  - **forms.py**: File containing Django forms used for data validation and handling user input.

  - **models.py**: File containing the definition of the `WeatherForecast` model, representing weather forecast data for specific coordinates and detailing types.

  - **tests**: Directory containing test files for unit testing different components of the app.

  - **urls.py**: Django URL configuration file defining the app's URL patterns.

  - **views.py**: File containing the views for handling HTTP requests and rendering templates.

- **manage.py**: This is a command-line utility in Django for managing various aspects of the project, such as running development servers, managing database migrations, and executing administrative tasks.

- **/staticfiles_build**: Directory where static files are collected during the build process.

- **/static**: Directory for static files such as CSS, JavaScript, and images.

- **build_files.sh**: Shell script file used for executing build steps such as installing dependencies, running database migrations, and collecting static files.

- **vercel.json**: Vercel configuration file specifying the build and deployment settings.

- **.env.example**: Example environment variable file containing configuration options such as PostgreSQL database details, OpenWeatherMap API key, and other settings.

- **requirements.txt**: Text file listing the Python dependencies required for the project.

- **README.md**: The file you're currently reading, providing an overview of the project.

## Models Explanation

The `models.py` file contains the definition of the `WeatherForecast` model, which represents weather forecast data for specific coordinates and detailing types.

- **WeatherForecast**: This model represents a weather forecast entry in the database. It has the following fields:

  - `latitude`: A `FloatField` representing the latitude coordinate of the location.
  - `longitude`: A `FloatField` representing the longitude coordinate of the location.
  - `detailing_type`: A `CharField` with choices representing the type of weather forecast detailing (e.g., "current", "daily", "hourly").
  - `weather_data`: A `JSONField` storing the weather data in JSON format.
  - `timestamp`: A `DateTimeField` automatically updated with the timestamp of the last modification.

  - **Meta**: The `Meta` class inside the model contains metadata options for the `WeatherForecast` model. In this case, it specifies `unique_together` to ensure uniqueness of latitude, longitude, and detailing type.

  - `__str__(self)`: This method defines the string representation of the model instance, which returns a formatted string displaying the latitude, longitude, and detailing type.

The `WeatherForecast` model allows storing weather forecast data for different locations and types of detailing. The `weather_data` field is a JSON field that can store various weather-related information retrieved from the OpenWeatherMap API, such as temperature, humidity, and weather conditions.

Note: Make sure to uncomment the database configuration in `settings.py` and run migrations (`python manage.py migrate`) to create the necessary table in the database for the `WeatherForecast` model.

## URL Patterns

The `urls.py` file in the `Forecast` app defines the URL patterns for the application.

- **weather_router**: An instance of `DefaultRouter` from Django REST Framework used for defining the API routes for the `WeatherForecast` model. It registers the `weatherapi` view with the base name "weather".

- **urlpatterns**: This is a list of URL patterns for the `Forecast` app. It includes the following patterns:

  - `path('api/', include(weather_router.urls))`: This pattern includes the API routes generated by the `weather_router` for the `weatherapi` view. The API routes will be prefixed with `/api/`.

  - `path('', views.index, name='index')`: This pattern maps the root URL to the `index` view function from `views.py`. It will be used to render the main index page of the application.

- **handler404**: This line sets the `handler404` to the `error_404` view function from `views.py`. It handles the 404 error page when a requested URL is not found.

The URL patterns defined in `urls.py` determine how incoming requests are mapped to specific views and API endpoints in the `Forecast` app.

## views Explanation

The `views.py` file in the `Forecast` app contains the view functions that handle HTTP requests and render templates.

- **index(request)**: This view function handles both GET and POST requests for the root URL ("/"). When a GET request is received, it renders the "forecast/index.html" template, which represents the main index page of the application. If a POST request is received, it validates the form data submitted, retrieves weather data from the OpenWeatherMap API based on the provided latitude, longitude, and detailing type, and renders the index template with the weather data displayed.

- **class weatherapi(ViewSet)**: This class-based view extends the `ViewSet` class from Django REST Framework and provides the implementation for the API endpoint handling weather data requests.

  - **list(self, request)**: This method handles GET requests to the API endpoint. It retrieves the latitude, longitude, detailing type, and API key from the request query parameters. If the required parameters are missing, it returns a 400 response with an error message. Otherwise, it checks if a weather forecast entry with the given coordinates and detailing type exists in the database and if the data is up-to-date. If so, it returns the weather data from the existing entry. Otherwise, it makes a request to the OpenWeatherMap API, retrieves the weather data, and saves it in a new or existing `WeatherForecast` entry in the database.

- **error_404(request, *args, **kwargs)**: This view function handles the 404 error page. It renders the "404.html" template and returns a 404 status code.

The views defined in `views.py` handle the rendering of templates, processing form data, and interacting with the OpenWeatherMap API to retrieve and store weather data. The `weatherapi` view provides the API endpoint for retrieving weather data based on latitude, longitude, and detailing type.

## Custom API Endpoint

The Weathercast app includes a custom API endpoint (`/api/weather`) that provides weather forecast data based on latitude and longitude coordinates. The endpoint expects the following parameters:

- **lat**: Latitude value (float) representing the location coordinates.
- **lon**: Longitude value (float) representing the location coordinates.
- **detail**: Detailing type (string) specifying the desired weather forecast information.
- **appid** (Optional): API key (string) to access weather data using a custom OpenWeatherMap account.

The API endpoint provides the following output in JSON format:

- **Weather Data**: The forecasted weather information based on the provided latitude, longitude, and detailing type. This includes details such as temperature, humidity, wind speed, and weather conditions.

Developers can utilize the optional `appid` parameter to include their own API key and access premium weather data through their OpenWeatherMap account.

The API endpoint enables seamless integration of weather forecast functionality into external applications by making requests to the specified endpoint with the required parameters.

## Tests Explanation

The `Forecast/tests` directory contains individual test files for different components of the app. Here's an explanation of each file, categorizing them as unit tests or integration tests:

- **test_forms.py** (Unit Tests): This file contains unit tests for the forms in the app. It focuses on validating the behavior of the form classes in isolation. The tests cover scenarios such as validating the form with valid and invalid input data, checking if the form is valid, and verifying that the appropriate validation errors are raised for invalid input.

- **test_models.py** (Unit Tests): This file contains unit tests for the models in the app. It focuses on testing the behavior of the model classes in isolation. The tests cover scenarios such as validating model fields, testing unique constraints, and checking the behavior of the models under different scenarios. These tests ensure the correctness of the model logic and data integrity.

- **test_templates.py** (Unit Tests): This file contains test cases for the templates in the app. It includes tests to ensure that the templates are rendered correctly and that the correct templates are used for different views and responses.

- **test_urls.py** (Unit Tests): This file contains unit tests for the URL configurations in the app. It focuses on testing the URL routing and resolution. The tests verify that the defined URLs resolve correctly to the expected views and API endpoints. These tests ensure that the app's URLs are correctly configured and accessible.

- **test_views.py** (Integration Tests): This file contains integration tests for the views in the app. It focuses on testing the behavior of the views by simulating HTTP requests and checking the responses. The tests cover scenarios such as testing the behavior of the views when handling different types of requests, form submissions, and API responses. These tests ensure the correct functionality and interaction between the views and other components.

Each test file covers specific components of the app and is categorized as either unit tests or integration tests based on its focus. Unit tests isolate specific components for testing, while integration tests test the interaction and integration between different components.

## Key Takeaways

During the development of this project, several special features were implemented to enhance its functionality and user experience. Here are the key takeaways and special features of the Weathercast app:

1. **Weather Forecasting**: The app utilizes the OpenWeatherMap API to fetch weather data based on user-specified latitude and longitude coordinates. It provides real-time weather information, including temperature, humidity, and weather conditions.

2. **Customizable Detailing Type**: Users can choose from various detailing types, such as current weather, 3-hour forecast, hourly forecast, daily forecast, and climatic forecast. This allows users to obtain weather information according to their specific requirements.

3. **API Key Integration**: The app provides an option for users to use their own paid API key from OpenWeatherMap. This enables users to access premium weather data and features by simply providing their API key during the form submission.

4. **Map Integration**: Users can conveniently select latitude and longitude coordinates using an integrated maps plugin. This feature enhances the user experience by simplifying the process of specifying location coordinates.

5. **Caching and Data Expiration**: The app employs a caching mechanism to store weather data locally. It checks the freshness of the data using a timestamp and expires the data after a configurable time interval, ensuring up-to-date weather information.

6. **Unit Testing and Test Coverage**: The project includes a comprehensive set of unit tests and integration tests to validate the functionality of different components, such as forms, models, views, and templates. This ensures reliable and robust code behavior.
   
7. **Download Raw Weather Data**: Users can download the raw JSON data fetched from the OpenWeatherMap API. This feature allows users to access the original weather data and use it for further analysis or processing.

These special features collectively enhance the Weathercast app by providing accurate weather forecasting, customization options, integration with external APIs, and an improved user interface. They contribute to an enhanced user experience and make the app more versatile and reliable.

## References

During the development of this project, the following resources and references were used:

- [Django Documentation](https://docs.djangoproject.com/): Official documentation for the Django web framework, providing detailed information on how to build web applications using Django.

- [Django REST Framework Documentation](https://www.django-rest-framework.org/): Comprehensive documentation for Django REST Framework, a powerful toolkit for building Web APIs in Django.

- [OpenWeatherMap API Documentation](https://openweathermap.org/api): Documentation for the OpenWeatherMap API, which provides access to a wide range of weather data and forecast information.

- [Python Requests Library Documentation](https://docs.python-requests.org/): Official documentation for the Requests library, which is used for making HTTP requests in Python.

- [Unsplash](https://unsplash.com/): A platform for high-quality, royalty-free images. The project utilizes images from Unsplash for visual elements.

- [Stack Overflow](https://stackoverflow.com/): An online community of developers that offers a wealth of knowledge and solutions to programming questions. Various Stack Overflow threads were consulted during the development process.

- [ChatGPT by OpenAI](https://openai.com/): An advanced language model that provides powerful natural language processing capabilities. ChatGPT was utilized to resolve bugs, enhance the frontend, and assist in generating code snippets and explanations.

These resources, including ChatGPT, played a crucial role in the development process, providing valuable guidance, documentation, bug resolution, and enhancements. They contributed to the successful implementation of the Weathercast app and the integration of its various features.
