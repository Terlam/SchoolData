# Import the app variable from the init
from school_data import app,db

# Import specific packages from flask
from flask import jsonify, request, render_template,request, redirect, url_for

# Import Our Form(s)
from school_data.forms import UserForm, LoginForm, PostForm

# Import of Our Model(s) for the Database
from school_data.models import School, school_schema, schools_schema, User, check_password_hash

import jwt
# Import for Flask Login functions - login_required
# login_user, curent_user, logout_user
from flask_login import login_required, login_user, current_user, logout_user
from school_data.token_validation import token_required

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')


#Register Route
@app.route('/users/register', methods = ['GET', 'POST'])
def register():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name,email,password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html', userform = form)

# Login Route
@app.route('/users/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data

    logged_user = User.query.filter(User.email == email).first()
    if logged_user and check_password_hash(logged_user.password, password):
        login_user(logged_user)
        return redirect(url_for('get_key'))
    return render_template('login.html',login_form = form)

# Logout Route
@app.route('/users/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Get API Key Route
@app.route('/getkey', methods = ['GET'])
def get_key():
    token = jwt.encode({'public_id':current_user.id,'email':current_user.email},app.config['SECRET_KEY'])
    user = User.query.filter_by(email = current_user.email).first()
    user.token = token

    db.session.add(user)
    db.session.commit()
    results = token.decode('utf-8')
    return render_template('token.html', token = results)

# Refresh API Key Route
@app.route('/updatekey', methods = ['GET','POST','PUT'])
def refresh_key():
    refresh_key = {'refreshToken': jwt.encode({'public_id':current_user.id, 'email':current_user.email}, app.config['SECRET_KEY'])}
    temp = refresh_key.get('refreshToken')
    actual_token = temp.decode('utf-8')
    return render_template('token_refresh.html', actual_token = actual_token)


# Don't need to Post schools
@app.route('/school/create', methods = ['POST'])
@token_required
def create_school():
    school.rcdts = request.json['rcdts']
    school.group_type = request.json['group_type']
    school.school_name = request.json['school_name']
    school.district_name = request.json['district_name']
    school.city = request.json['city']
    school.county = request.json['county']
    school.school_type = request.json['school_type']
    school.grades_served = request.json['grades_served']
    school.total_enrollment = request.json['total_enrollment']
    school.total_enrollment_white = request.json['total_enrollment_white']
    school.total_enrollment_black = request.json['total_enrollment_black']
    school.total_enrollment_latinx = request.json['total_enrollment_latinx']
    school.total_enrollment_asian = request.json['total_enrollment_asian']
    school.total_enrollment_pacific_island = request.json['total_enrollment_pacific_island']
    school.total_enrollment_indig = request.json['total_enrollment_indig']
    school.total_enrollloment_mixed = request.json['total_enrollloment_mixed']
    school.total_enrollment_low_income = request.json['total_enrollment_low_income']
    school.total_enrollment_homeless = request.json['total_enrollment_homeless']
    school.mobility_rate = request.json['mobility_rate']
    school.mobility_rate_low_income = request.json['mobility_rate_low_income']
    school.truancy_rate = request.json['truancy_rate']
    school.dropout_rate = request.json['dropout_rate']
    school.dropout_rate_low_income = request.json['dropout_rate_low_income']
    school.grad_rate = request.json['grad_rate']
    school.grad_rate_low_income = request.json['grad_rate_low_income']
    school.grad_rate_homeless = request.json['grad_rate_homeless']
    school.class_size_hs = request.json['class_size_hs']
    school.class_size_all = request.json['class_size_all']
    school.teacher_salary = request.json['teacher_salary']
    school.admin_salary = request.json['admin_salary']
    school.on_track_fresh = request.json['on_track_fresh']
    school.on_track_fresh_p = request.json['on_track_fresh_p']
    school.on_track_fresh_p_low_income = request.json['on_track_fresh_p_low_income']
    school.college_enrollment = request.json['college_enrollment']
    school.community_college_enrollment = request.json['community_college_enrollment']
    school.communty_college_remediation = request.json['communty_college_remediation']
    school.ap_exam_fresh = request.json['ap_exam_fresh']
    school.ap_exam_fresh_pass = request.json['ap_exam_fresh_pass']
    school.ap_exam_soph = request.json['ap_exam_soph']
    school.ap_exam_soph_pass = request.json['ap_exam_soph_pass']
    school.ap_exam_jr = request.json['ap_exam_jr']
    school.ap_exam_jr_pass = request.json['ap_exam_jr_pass']
    school.ap_exam_sr = request.json['ap_exam_sr']
    school.ap_exam_sr_pass = request.json['ap_exam_sr_pass']
    school.crdc_violence = request.json['crdc_violence']
    school.crdc_violence_p = request.json['crdc_violence_p']
    school.crdc_dual_credit = request.json['crdc_dual_credit']
    school.crdc_dual_credit_p = request.json['crdc_dual_credit_p']

    school = school(rcdts,group_type,school_name,district_name,city,county,school_type,grades_served,total_enrollment,total_enrollment_white,total_enrollment_black,total_enrollment_latinx,total_enrollment_asian,total_enrollment_pacific_island,total_enrollment_indig,total_enrollloment_mixed,total_enrollment_low_income,total_enrollment_homeless,mobility_rate,mobility_rate_low_income,truancy_rate,dropout_rate,dropout_rate_low_income,grad_rate,grad_rate_low_income,grad_rate_homeless,class_size_hs,class_size_all,teacher_salary,admin_salary,on_track_fresh,on_track_fresh_p,on_track_fresh_p_low_income,college_enrollment,community_college_enrollment,communty_college_remediation,ap_exam_fresh,ap_exam_fresh_pass,ap_exam_soph,ap_exam_soph_pass,ap_exam_jr,ap_exam_jr_pass,ap_exam_sr,ap_exam_sr_pass,crdc_violence,crdc_violence_p,crdc_dual_credit,crdc_dual_credit_p)
    results = school_schema.dump(school)
    return jsonify(results)

# Get School Route
@app.route('/schools', methods = ['GET'])
@token_required
def get_schools(current_user_token):
    schools = School.query.all()
    return jsonify(schools_schema.dump(schools))
    



@app.route('/schools/<id>', methods = ['GET'])
@token_required
def get_school(current_user_token,id):
    school = School.query.get(id)
    results = school_schema.dump(school)
    return jsonify(results)

@app.route('/schools/<id>', methods = ['POST', 'PUT'])
@token_required
def update_school(current_user_token,id):
    school = School.query.get(id)
    
    school.group_type = request.json['group_type']
    school.school_name = request.json['school_name']
    school.district_name = request.json['district_name']
    school.city = request.json['city']
    school.county = request.json['county']
    school.school_type = request.json['school_type']
    school.grades_served = request.json['grades_served']
    school.total_enrollment = request.json['total_enrollment']
    school.total_enrollment_white = request.json['total_enrollment_white']
    school.total_enrollment_black = request.json['total_enrollment_black']
    school.total_enrollment_latinx = request.json['total_enrollment_latinx']
    school.total_enrollment_asian = request.json['total_enrollment_asian']
    school.total_enrollment_pacific_island = request.json['total_enrollment_pacific_island']
    school.total_enrollment_indig = request.json['total_enrollment_indig']
    school.total_enrollloment_mixed = request.json['total_enrollloment_mixed']
    school.total_enrollment_low_income = request.json['total_enrollment_low_income']
    school.total_enrollment_homeless = request.json['total_enrollment_homeless']
    school.mobility_rate = request.json['mobility_rate']
    school.mobility_rate_low_income = request.json['mobility_rate_low_income']
    school.truancy_rate = request.json['truancy_rate']
    school.dropout_rate = request.json['dropout_rate']
    school.dropout_rate_low_income = request.json['dropout_rate_low_income']
    school.grad_rate = request.json['grad_rate']
    school.grad_rate_low_income = request.json['grad_rate_low_income']
    school.grad_rate_homeless = request.json['grad_rate_homeless']
    school.class_size_hs = request.json['class_size_hs']
    school.class_size_all = request.json['class_size_all']
    school.teacher_salary = request.json['teacher_salary']
    school.admin_salary = request.json['admin_salary']
    school.on_track_fresh = request.json['on_track_fresh']
    school.on_track_fresh_p = request.json['on_track_fresh_p']
    school.on_track_fresh_p_low_income = request.json['on_track_fresh_p_low_income']
    school.college_enrollment = request.json['college_enrollment']
    school.community_college_enrollment = request.json['community_college_enrollment']
    school.communty_college_remediation = request.json['communty_college_remediation']
    school.ap_exam_fresh = request.json['ap_exam_fresh']
    school.ap_exam_fresh_pass = request.json['ap_exam_fresh_pass']
    school.ap_exam_soph = request.json['ap_exam_soph']
    school.ap_exam_soph_pass = request.json['ap_exam_soph_pass']
    school.ap_exam_jr = request.json['ap_exam_jr']
    school.ap_exam_jr_pass = request.json['ap_exam_jr_pass']
    school.ap_exam_sr = request.json['ap_exam_sr']
    school.ap_exam_sr_pass = request.json['ap_exam_sr_pass']
    school.crdc_violence = request.json['crdc_violence']
    school.crdc_violence_p = request.json['crdc_violence_p']
    school.crdc_dual_credit = request.json['crdc_dual_credit']
    school.crdc_dual_credit_p = request.json['crdc_dual_credit_p']

    db.session.commit()

    return school_schema.jsonify(school)

# Don't Need to Delete Schools
@app.route('/schools/delete/<id>', methods = ['DELETE'])
@token_required
def delete_schools(current_user_token,id):
    school = School.query.get(rctds)
    db.session.delete(school)
    db.session.commit()
    result = school_schema.dump(school)
    return jsonify(result)