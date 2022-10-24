#importing modules
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from cbs_raw import get_cbs_news
from cbs_config import Config

app = Flask(__name__)
ma = Marshmallow() 
migrate = Migrate()

app.config.from_object(Config)

from cbs_model import db, CbsNews

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

@app.route('/cbs_news')
def cbs_news():
    news_articles = get_cbs_news() 
    data = CbsNews.get_all_news() 
    
    for news in news_articles:
        if news.get('title').lower() not in [info.title.lower() for info in data]:
            row = CbsNews(title = news['title'], link = news['link'], description = news['description'], image = news['image'])
            row.save()
        else:
            continue

    return {'data': [news.serialize() for news in data]}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)