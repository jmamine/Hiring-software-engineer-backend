from app import app , scheduler 
from app.routes import task_blueprint
from config import get_config
import os

app.register_blueprint(task_blueprint, url_prefix='/task')
environment = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(get_config(environment))

if __name__ == "__main__":
    scheduler.start()
    port = app.config['PORT']
    app.run(host='0.0.0.0', port=port)
    
