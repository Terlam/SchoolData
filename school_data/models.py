from school_data import app, db, ma, login_manager

from datetime import datetime

import uuid

from flask_login import UserMixin

# Import for Werkzeug Security 
from werkzeug.security import generate_password_hash, check_password_hash

class School(db.Model):
    rctds = db.Column(db.String(15), unique=True, primary_key = True)
    group_type  = db.Column(db.String(100))
    school_name = db.Column(db.String(100))
    district_name = db.Column(db.String(100))
    city = db.Column(db.String(100), nullable = False)
    county = db.Column(db.String(100), nullable = False)
    school_type = db.Column(db.String(100))
    grades_served = db.Column(db.String(100))
    total_enrollment = db.Column(db.Integer)
    total_enrollment_white = db.Column(db.Float)
    total_enrollment_black = db.Column(db.Float)
    total_enrollment_latinx = db.Column(db.Float)
    total_enrollment_asian = db.Column(db.Float)
    total_enrollment_pacific_island = db.Column(db.Float)
    total_enrollment_indig = db.Column(db.Float)
    total_enrollment_mixed = db.Column(db.Float)
    total_enrollment_low_income = db.Column(db.Float)
    total_enrollment_homeless = db.Column(db.Float)
    mobility_rate = db.Column(db.Float)
    mobility_rate_low_income = db.Column(db.Float)
    truancy_rate = db.Column(db.Float)
    dropout_rate = db.Column(db.Float)
    dropout_rate_low_income = db.Column(db.Float)
    grad_rate = db.Column(db.Float)
    grad_rate_low_income = db.Column(db.Float)
    grad_rate_homeless = db.Column(db.Float)
    class_size_hs = db.Column(db.Float)
    class_size_all = db.Column(db.Float)
    teacher_salary = db.Column(db.Integer)
    admin_salary = db.Column(db.Integer)
    on_track_fresh = db.Column(db.Integer)
    on_track_fresh_p = db.Column(db.Float)
    on_track_fresh_p_low_income = db.Column(db.Float)
    college_enrollment = db.Column(db.Float)
    community_college_enrollment = db.Column(db.Integer)
    commmunity_college_remediation = db.Column(db.Float)
    ap_exam_fresh = db.Column(db.Integer)
    ap_exam_fresh_pass = db.Column(db.Integer)
    ap_exam_soph = db.Column(db.Integer)
    ap_exam_soph_pass = db.Column(db.Integer)
    ap_exam_jr = db.Column(db.Integer)
    ap_exam_jr_pass = db.Column(db.Integer)
    ap_exam_sr = db.Column(db.Integer)
    ap_exam_sr_pass = db.Column(db.Integer)
    crdc_violence = db.Column(db.Integer)
    crdc_violence_p = db.Column(db.Float)
    crdc_dual_credit = db.Column(db.Integer)
    crdc_dual_credit_p = db.Column(db.Float)

    def __init__(self,group_type,school_name,district_name,city,county,school_type,grades_served,total_enrollment,total_enrollment_white,total_enrollment_black,total_enrollment_latinx,total_enrollment_asian,total_enrollment_pacific_island,total_enrollment_indig,total_enrollment_mixed,total_enrollment_low_income,total_enrollment_homeless,mobility_rate,mobility_rate_low_income,truancy_rate,dropout_rate,dropout_rate_low_income,grad_rate,grad_rate_low_income,grad_rate_homeless,class_size_hs,class_size_all,teacher_salary,admin_salary,on_track_fresh,on_track_fresh_p,on_track_fresh_p_low_income,college_enrollment,community_college_enrollment,commmunity_college_remediation,ap_exam_fresh,ap_exam_fresh_pass,ap_exam_soph,ap_exam_soph_pass,ap_exam_jr,ap_exam_jr_pass,ap_exam_sr,ap_exam_sr_pass,crdc_violence,crdc_violence_p,crdc_dual_credit,crdc_dual_credit_p,rctds = rctds):
        self.group_type = group_type 
        self.school_name = school_name 
        self.district_name = district_name 
        self.city = city 
        self.county = county 
        self.school_type = school_type 
        self.grades_served = grades_served 
        self.total_enrollment = total_enrollment 
        self.total_enrollment_white = total_enrollment_white 
        self.total_enrollment_black = total_enrollment_black 
        self.total_enrollment_latinx = total_enrollment_latinx 
        self.total_enrollment_asian = total_enrollment_asian 
        self.total_enrollment_pacific_island = total_enrollment_pacific_island 
        self.total_enrollment_indig = total_enrollment_indig 
        self.total_enrollment_mixed = total_enrollment_mixed 
        self.total_enrollment_low_income = total_enrollment_low_income 
        self.total_enrollment_homeless = total_enrollment_homeless 
        self.mobility_rate = mobility_rate 
        self.mobility_rate_low_income = mobility_rate_low_income 
        self.truancy_rate = truancy_rate 
        self.dropout_rate = dropout_rate 
        self.dropout_rate_low_income = dropout_rate_low_income 
        self.grad_rate = grad_rate 
        self.grad_rate_low_income = grad_rate_low_income 
        self.grad_rate_homeless = grad_rate_homeless 
        self.class_size_hs = class_size_hs 
        self.class_size_all = class_size_all 
        self.teacher_salary = teacher_salary 
        self.admin_salary = admin_salary 
        self.on_track_fresh = on_track_fresh 
        self.on_track_fresh_p = on_track_fresh_p 
        self.on_track_fresh_p_low_income = on_track_fresh_p_low_income 
        self.college_enrollment = college_enrollment 
        self.community_college_enrollment = community_college_enrollment 
        self.commmunity_college_remediation = commmunity_college_remediation 
        self.ap_exam_fresh = ap_exam_fresh 
        self.ap_exam_fresh_pass = ap_exam_fresh_pass 
        self.ap_exam_soph = ap_exam_soph 
        self.ap_exam_soph_pass = ap_exam_soph_pass 
        self.ap_exam_jr = ap_exam_jr 
        self.ap_exam_jr_pass = ap_exam_jr_pass 
        self.ap_exam_sr = ap_exam_sr 
        self.ap_exam_sr_pass = ap_exam_sr_pass 
        self.crdc_violence = crdc_violence 
        self.crdc_violence_p = crdc_violence_p 
        self.crdc_dual_credit = crdc_dual_credit 
        self.crdc_dual_credit_p = crdc_dual_credit_p 
        

class SchoolSchema(ma.Schema):
    class Meta:
        #Fields to show on 
        fields = ['rctds', 'group_type', 'school_name', 'district_name', 'city', 'county', 'school_type', 'grades_served', 'total_enrollment', 'total_enrollment_white', 'total_enrollment_black', 'total_enrollment_latinx', 'total_enrollment_asian', 'total_enrollment_pacific_island', 'total_enrollment_indig', 'total_enrollment_mixed', 'total_enrollment_low_income', 'total_enrollment_homeless', 'mobility_rate', 'mobility_rate_low_income', 'truancy_rate', 'dropout_rate', 'dropout_rate_low_income', 'grad_rate', 'grad_rate_low_income', 'grad_rate_homeless', 'class_size_hs', 'class_size_all', 'teacher_salary', 'admin_salary', 'on_track_fresh', 'on_track_fresh_p', 'on_track_fresh_p_low_income', 'college_enrollment', 'community_college_enrollment', 'commmunity_college_remediation', 'ap_exam_fresh', 'ap_exam_fresh_pass', 'ap_exam_soph', 'ap_exam_soph_pass', 'ap_exam_jr', 'ap_exam_jr_pass', 'ap_exam_sr', 'ap_exam_sr_pass', 'crdc_violence', 'crdc_violence_p', 'crdc_dual_credit', 'crdc_dual_credit_p']

school_schema = SchoolSchema()
schools_schema = SchoolSchema(many = True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Column(db.String(200), primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    token = db.Column(db.String(400), default = 'No Token Created')
    token_refreshed = db.Column(db.Boolean, default = False)
    date_refreshed = db.Column(db.DateTime)

    def __init__(self,name,email,password,id = id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
   
    def __repr__(self):
        return f'{self.name} has been created successfully'

# Creation of the Post Model
# The Post model will have an 
# id, title, content, date_created
# user_id
# class Post(db.Model):
#     id = db.Column(db.String(200), primary_key = True)
#     title = db.Column(db.String(100))
#     content = db.Column(db.String(300))
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
#     user_id = db.Column(db.String(200), db.ForeignKey('user.id'), nullable = False)

#     def __init__(self,title,content,user_id):
#         self.title = title
#         self.content=content
#         self.user_id = user_id

#     def __repr__(self):
#         return f'The title of the post is {self.title} \n and the content is {self.content}'
