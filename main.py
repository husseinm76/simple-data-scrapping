

from scrapper import get_html, extract_countries_data
from database import  write_on_db, read_data, db_exist
from model import model_exist, train_model, save_model, load_model




URL = "https://www.scrapethissite.com/pages/simple/"
DB_FILE = 'countries.db'
MODEL_FILE = 'area_prediction.pkl'


if not db_exist(DB_FILE):
    print('! No Database Exists: Next Step-> Scrape Data and Create db')
    html_page = get_html(URL)
    countries_data = extract_countries_data(html_page)
    write_on_db(countries_data, DB_FILE)



if not model_exist(MODEL_FILE):

    print('! No Model Exists: Next Step-> Train a Model')
    rows = read_data(DB_FILE)
    model = train_model(rows)
    save_model(model, MODEL_FILE)


model = load_model(MODEL_FILE)
# predict
