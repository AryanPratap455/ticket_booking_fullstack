from flask import Flask , render_template, request, redirect, flash, session , url_for, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, UserMixin, logout_user, current_user
from werkzeug.utils import redirect, secure_filename
from passlib.hash import sha256_crypt
from datetime import datetime
import os, time

app=Flask(__name__)
app.secret_key = "Aryan_Pratap_@_456456"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ticket_booking.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False


db = SQLAlchemy(app) 
db.init_app(app)

# Initialize CORS after session
CORS(app, resources={r"/*": {'origins':"*"}})

class User(db.Model, UserMixin):
    __tablename__='user'
    user_id=db.Column(db.Integer, primary_key=True)
    user_email=db.Column(db.String(30),nullable=True)
    password=db.Column(db.String(20),nullable=False)
    bookings=db.relationship('Booking', backref='user', lazy='dynamic')
    
    def get_id(self):
        return str(self.user_id)

class Admin(db.Model):
    __tablename__='admin'
    admin_id=db.Column(db.Integer, primary_key=True)
    admin_email=db.Column(db.String(30),nullable=True)
    password=db.Column(db.String(20),nullable=False)
     
class Venue(db.Model):
    venue_id=db.Column(db.Integer, primary_key=True)
    venue_name=db.Column(db.String(20),unique=True, nullable=False)
    place=db.Column(db.String(50),nullable=False)
    location=db.Column(db.String(50), nullable=True)
    capacity=db.Column(db.Integer, nullable=False)
    shows=db.relationship('Show', backref='venue', lazy='dynamic')


class Show(db.Model):
    show_id=db.Column(db.Integer, primary_key=True)
    show_name=db.Column(db.String(20),unique=True, nullable=False)
    tags=db.Column(db.String(50),nullable=False)
    price=db.Column(db.Integer, nullable=False)
    rating=db.Column(db.Integer, nullable=False)
    time=db.Column(db.String, nullable=False)
    venue_id=db.Column(db.Integer, db.ForeignKey('venue.venue_id'))
    bookings=db.relationship('Booking', backref='show', lazy='dynamic')


class Booking(db.Model):
    booking_id=db.Column(db.Integer, primary_key=True) 
    seat=db.Column(db.Integer, nullable=False)
    #remaining_seat=db.Column(db.Integer)
    shows_id=db.Column(db.Integer, db.ForeignKey('show.show_id'))
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'))



'''@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) '''

Dict={}


@app.route('/', methods=['GET', 'POST'])
def Homepage():
    return render_template('home.html')

@app.route('/shark', methods=['GET', 'POST'])
def Shark():
    return('backend data')

@app.route('/venuedata', methods=['GET', 'POST'])
def Venuedata():
    L=[]
    venues=Venue.query.all()
    dataa=[]
    show_data=[]
    for i in venues:
        dataa.append({
            'id':i.venue_id,
            'venue_name':i.venue_name,
            'place':i.place,
            'location':i.location,
            'capacity':i.capacity
        })
    shows=Show.query.all()
    for i in shows:
        show_data.append({
            'show_id':i.show_id,
            'show_name':i.show_name,
            'price':i.price,
            'rating':i.rating,
            'tags':i.tags,
            'time':i.time,
            'venue_id_r':i.venue_id
        })
    L.append(dataa)
    L.append(show_data)
    return L

@app.route('/userhome', methods=['GET'])
def Userhome():
    print(Dict)
    print(Dict["users"])
    l=[]
    venues=Venue.query.all()
    usar=User.query.filter_by(user_email=Dict["users"]).first()
    dataa=[]
    show_data=[]
    #user_data=[{'email':usar.user_email}]
    for i in venues:
        dataa.append({
            'id':i.venue_id,
            'venue_name':i.venue_name,
            'place':i.place,
            'location':i.location,
            'capacity':i.capacity
        })
    shows=Show.query.all()
    for i in shows:
        show_data.append({
            'show_id':i.show_id,
            'show_name':i.show_name,
            'price':i.price,
            'rating':i.rating,
            'tags':i.tags,
            'time':i.time,
            'venue_id_r':i.venue_id
        })
    l.append(dataa)
    l.append(show_data)
    #l.append(user_data)
    return l

@app.route('/createvenue', methods=['POST'])
def create_venue():
    data=request.get_json()
    venue=Venue(venue_name=data.get('name',None), place=data.get('place',None), location=data.get('location',None), capacity=data.get('capacity',None))
    db.session.add(venue)
    db.session.commit()
    return jsonify('venue successfully added')

@app.route('/updatevenue/<id>', methods=['POST'])
def update_venue(id):
    data=request.get_json()
    venu=Venue.query.filter_by(venue_id=id).first()
    venu.venue_name=data.get("name")
    venu.place=data.get("place")
    venu.location=data.get("location")
    venu.capacity=data.get("capacity")
    db.session.commit()
    return jsonify('venue successfully updated')

@app.route('/updateshow/<show_id>', methods=['POST'])
def update_show(show_id):
    data=request.get_json()
    show=Show.query.filter_by(show_id=show_id).first()
    show.show_name=data.get("show_name")
    show.tags=data.get("tags")
    show.price=data.get("price")
    show.time=data.get("time")
    show.rating=data.get("rating")
    db.session.commit()
    return jsonify('Show successfully updated')

@app.route('/createshow', methods=['POST'])
def create_show():
    dataa=request.get_json()
    showw=Show(show_name=dataa.get('show_name',None), price=dataa.get('price',None), tags=dataa.get('tags',None), rating=dataa.get('rating',None), time=dataa.get('time',None), venue_id=dataa.get('venue_id',None))
    db.session.add(showw)
    db.session.commit()
    return jsonify('show successfully added')

@app.route('/deletevenue/<id>')
def delete_venue(id):
    vend=Venue.query.filter_by(venue_id=id).first()
    db.session.delete(vend)
    db.session.commit()
    return jsonify('venue deleted...')

@app.route('/deleteshow/<show_id>')
def delete_show(show_id):
    show=Show.query.filter_by(show_id=show_id).first()
    db.session.delete(show)
    db.session.commit()
    return jsonify('Show deleted successfully...')

@app.route('/seat_remain/<show_id>')
def Seat_remain(show_id):
    print(show_id)
    shov=Show.query.filter_by(show_id=show_id).first()
    item=Booking.query.filter_by(shows_id=show_id).all()
    cap=shov.venue.capacity
    sum=0
    for i in item:
        sum=sum+int(i.seat)
    available_seat=int(cap)-sum
    return jsonify({'available_seat':int(available_seat)})
    

@app.route('/bookshow/<show_id>', methods=['POST', 'GET'])
def book_show(show_id):
    print(show_id)
    print(Dict["users"])
    show=Show.query.filter_by(show_id=show_id).first()
    z=User.query.filter_by(user_email=Dict["users"]).first()
    if request.method=='POST':
        data=request.get_json()
        booking_data=Booking(seat=data.get('seat_c',None),shows_id=show_id,user_id=z.user_id)
        db.session.add(booking_data)
        db.session.commit()
        return jsonify({ 'conclusion':'booking successful'})
    return jsonify('no action done till now')

@app.route('/booking', methods=['GET', 'POST'])
def user_booked_page():
    book_data=[]
    z=User.query.filter_by(user_email=Dict["users"]).first()
    books=Booking.query.all()
    for i in books:
        if i.user_id==z.user_id:
            book_data.append(
                {'shows_name':i.show.show_name,
                'rating':i.show.rating,
                'time':i.show.time,
                'venue_name':i.show.venue.venue_name
                }
            )
    return book_data

@app.route('/search', methods=['POST', 'GET'])
def Search():
    s_data=request.get_json()
    #output=Show.query.filter_by(show_name=s_data.get('search',None)).all()
    show_output=Show.query.filter(
        (Show.show_name.like('%'+ s_data.get('search',None) + '%')) |
        (Show.tags.like('%'+ s_data.get('search',None) + '%'))
        ).all()

    venue_output=Venue.query.filter(
        (Venue.venue_name.like('%' + s_data.get('search', None) + '%')) |
        (Venue.place.like('%' + s_data.get('search', None) + '%')) |
        (Venue.location.like('%' + s_data.get('search', None) + '%')) 
    ).all()

    if request.method=='POST':
        if show_output:
            show_list = [{'show_name': show.show_name, 'tags': show.tags} for show in show_output]
            return jsonify({'status':'Data is present','val':show_list})
        if venue_output:
            venue_list = [{'venue_name': venue.venue_name, 'place': venue.place, 'location':venue.location} for venue in venue_output]
            return jsonify({'status':'Data is present','val':venue_list})
        return jsonify({'status':'Data is not present'})
    if request.method=='GET':
        return jsonify({'val':output})


@app.route('/registeradmin', methods=['POST'])
def adminregister():
    a_data=request.get_json()
    enc_pas=sha256_crypt.encrypt(a_data.get('password',None))
    dataa=Admin(admin_email=a_data.get('email',None),password=enc_pas)
    db.session.add(dataa)
    db.session.commit()
    return jsonify('Admin registration has successfully done !')

@app.route('/registeruser', methods=['POST'])
def userregister():
    u_data=request.get_json()
    enc_pas=sha256_crypt.encrypt(u_data.get('password',None))
    dataa=User(user_email=u_data.get('email',None),password=enc_pas)
    db.session.add(dataa)
    db.session.commit()
    return jsonify('User registration has successfully done !')

@app.route('/loginadmin',methods=['POST'])
def adminlogin():
    AL_data=request.get_json()
    email=AL_data.get("email")
    password=AL_data.get("password") 
    admin=Admin.query.filter_by(admin_email=email).first()
    #session['admin_email']=email
    if admin is None:
        return jsonify('User does not exist !!')
    if admin and sha256_crypt.verify(password,admin.password):
        return jsonify({'status':'success','message':'successfully logged in'})
    return jsonify('Invalid password')

@app.route('/logoutadmin')
def adminlogout():
    admin_emails = session.get('admin_email')
    if admin_emails is not None:
        #print(session['admin_email'])
        #session.pop('admin_email', None)
        return jsonify("admin is logged out")
    else:
        return jsonify("No active session. User is not logged in.")


@app.route('/loginuser', methods=['POST'])
def userlogin():
    UL_data = request.get_json()
    email = UL_data.get("email")
    password = UL_data.get("password") 
    cur_user = User.query.filter_by(user_email=email).first()  
    if cur_user is None:
        return jsonify('User does not exist !!')
    if cur_user and sha256_crypt.verify(password,cur_user.password):
        Dict['users']=email
        print(Dict['users'])
        print(Dict)
        return jsonify({'status': 'success', 'message': 'successfully logged in'})
    return jsonify('Invalid password')

@app.route('/logoutuser')
def userlogout():
    if 'users' in Dict:
        Dict.pop('users', None)
    return jsonify({'message': 'logged out successfully'})

@app.route('/trigger_celery_job')
def trigger_celery_job():
    a=add_together.delay(4,9)
    return jsonify({
        'Task ID':a.id,
        'Task State':a.state,
        'Task Result':a.result
    })


if __name__ =="__main__":
    app.run(debug=True)      

