

from scrapper import get_html, extract_countries_data
from database import  write_on_db, read_data, db_exist
from model import model_exist




URL = "https://www.scrapethissite.com/pages/simple/"
DB_FILE = 'countries.db'
MODEL_FILE = 'area_prediction.pkl'


if not db_exist(DB_FILE):
    print('No Data')
    html_page = get_html(URL)
    countries_data = extract_countries_data(html_page)
    write_on_db(countries_data, DB_FILE)



if not model_exist(MODEL_FILE):

    print('Model need to train')
    data_set = read_data(DB_FILE)
    # train
    # save

# load model
# predict

# load model
# predict
