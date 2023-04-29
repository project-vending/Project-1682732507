 
import os

# Define the project directory and subdirectories
PROJECT_DIR = "real_time_social_media_monitoring"
DATA_DIR = os.path.join(PROJECT_DIR, "data")
MODELS_DIR = os.path.join(PROJECT_DIR, "models")
APPS_DIR = os.path.join(PROJECT_DIR, "apps")
DOCS_DIR = os.path.join(PROJECT_DIR, "docs")
LOGS_DIR = os.path.join(PROJECT_DIR, "logs")

# Create the project directory
os.makedirs(PROJECT_DIR)

# Create the data directory and empty files
os.makedirs(DATA_DIR)
open(os.path.join(DATA_DIR, "twitter.csv"), "w").close()
open(os.path.join(DATA_DIR, "facebook.csv"), "w").close()
open(os.path.join(DATA_DIR, "instagram.csv"), "w").close()
open(os.path.join(DATA_DIR, "linkedin.csv"), "w").close()

# Create the models directory and empty files
os.makedirs(MODELS_DIR)
open(os.path.join(MODELS_DIR, "model.pkl"), "wb").close()

# Create the apps directory and empty files
os.makedirs(APPS_DIR)
open(os.path.join(APPS_DIR, "main.py"), "w").close()

# Create the docs directory and empty files
os.makedirs(DOCS_DIR)
open(os.path.join(DOCS_DIR, "README.md"), "w").close()

# Create the logs directory and empty files
os.makedirs(LOGS_DIR)
open(os.path.join(LOGS_DIR, "app.log"), "w").close()
