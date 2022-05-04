#### **Structure**

* `app/main.py`: Main app file and docker entrypoint. This defines the FastAPI logic;
* `app/model.py`: Utility file that defines the model's logic;
* `app/static/`: Contains the icons and CSS files
* `app/templates/`: Contains the `index.html` template file that will be modified at run time with the dialog HTML using jinja
* `Dockerfile`: Defines the steps needed to install all required libraries, and run the FastAPI app (`app.main.py`).
* `test/test_app.ipynb`: Testing notebook file

#### **How to run?**
1. Clone the repository to your local machine
2. Build the docker container `docker build . -t chatbot`
3. Run the container `docker run -p 8000:8000 chatbot`
4. Type http://0.0.0.0:8000/ in your favorite browser to interact with the app
