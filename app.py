from flask import Flask , render_template , request , url_for , redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Picture(db.Model):
    sno = db.Column(db.Integer , primary_key = True )
    photo_name = db.Column(db.String , nullable = False)
    data = db.Column(db.LargeBinary )
    

    def __repr__(self) -> str:
        return f"{self.sno} - {self.photo_name} - {self.data} "
    

# @app.route('/')
# def Home():
#     return "<h2 > This is the Home Page you need to visit /upload for Upload Form </h2>"

@app.route('/' , methods = ['GET' , 'POST'] )
def upload_image():
    if request.method == 'POST':
       file = request.files['image_upload']
       if file : 
            photo_data = file.read()
            photo_instance = Picture(photo_name = file.filename , data = photo_data )

            db.session.add(photo_instance)
            db.session.commit()

            # return redirect(url_for('/'))
            return "successful"
       
    photos = Picture.query.all()
    return render_template('uploadPage.html' , photos = photos)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    