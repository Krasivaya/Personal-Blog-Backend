from . import main
from flask import render_template,redirect,url_for,request
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PitchUploadForm,CommentsForm,UpdateProfile
from .. import db,photos
from ..models import Pitch,Comment,User

#Home view
@main.route('/')
def index():
    pitch = Pitch.get_pitch('Product')
    interview_pitch = Pitch.get_pitch('Interview')
    promotion_pitch = Pitch.get_pitch('Promotion')
    pickup_pitch = Pitch.get_pitch('Pick-up')
    title='Welcome To The Pitch'
    return render_template('index.html',title=title,pitches=pitch,interview_pitch=interview_pitch,promotion_pitch=promotion_pitch,pickup_pitch=pickup_pitch)

#Add pitch view
@main.route('/addpitch',methods = ['GET','POST'])
@login_required
def add_pitch():
    form = PitchUploadForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        category = form.category.data
        new_pitch = Pitch(pitch = pitch,category = category,user = current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Add a pitch'
    return render_template('addpitch.html',title = title,pitchform = form)

#Comment view
@main.route('/pitchdiscussion/<int:pitch_id>/comment',methods=['POST','GET'])
@login_required
def comment(pitch_id):
    current_pitch = Pitch.query.filter_by(id = pitch_id).first()
    if request.method == "POST":
        comment = request.form.get("comment")
        new_comment = Comment(comment = comment,user = current_user,pitch = current_pitch)
        db.session.add(new_comment)
        db.session.commit()
    pitch = Pitch.query.get_or_404(pitch_id)
    comments = Comment.get_comments(pitch_id)
    title = 'Pitch Discussion'
    return render_template('pitchdiscussion.html',title = title,pitch = pitch,comments=comments)

#Profile view
@main.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first()
    userid = user.id
    my_pitches = Pitch.query.filter_by(users_id = userid).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user,my_pitches = my_pitches)

#Update view
@main.route('/user/<username>/update', methods = ['GET','POST'])
@login_required
def profle_update(username):
    user = User.query.filter_by(username = username).first()
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',username = user.username))

    return render_template('profile/update.html',form= form)

#Upload profile view
@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))


