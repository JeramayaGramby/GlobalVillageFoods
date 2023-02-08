import os
import flask
from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.app_context().push()
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_information.db'
db = SQLAlchemy(app)

class HelloWorldModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    email_address = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"HelloWorld(name = {name}, email_address = {email_address}, password = {password})"
    
    '''Run db.create_all ONLY if you have redesigned the underlying database or are running the app for the first time. Otherwise you will overwrite the database'''
db.create_all()


'''This makes sure the correct data is sent on the put request (A request that adds a resource) This handles front-end data input.'''
user_input_data_put_args = reqparse.RequestParser()
user_input_data_put_args.add_argument("name", type=str, help="Your name is required", required=True)
user_input_data_put_args.add_argument("email_address", type=str, help="Your email address is required", required=True)
user_input_data_put_args.add_argument("password", type=str, help="Your password is required", required=True)

user_input_data_update_args = reqparse.RequestParser()
user_input_data_put_args.add_argument("name", type=str, help="Your name is required", required=True)
user_input_data_put_args.add_argument("email_address", type=str, help="Your email address is required")
user_input_data_put_args.add_argument("password", type=str, help="Your password is required")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email_address': fields.String,
    'password': fields.String
}

''' Commands that define what requests do'''
class HelloWorld(Resource):
    @marshal_with(resource_fields)
    def get(self, data_id):
        result = HelloWorldModel.query.filter_by(id=data_id).first()
        if not result:
            abort(404, message="Could not find data with that ID")
        return result
    
    
    @marshal_with(resource_fields)
    def patch(self, data_id):
        args = user_input_data_put_args.parse_args()
        result = HelloWorldModel.query.filter_by(id=data_id).first()
        if not result:
            abort(404, message="Cannot update an entry that does not exist")
        if "name" in args:
            result.name = args['name'] 
        if "email_address" in args:
            result.email_address = args['email_address']
        if "password" in args:
            result.password = args['name']
        
        db.session.add(result)
        db.session.commit()
        return result


    @marshal_with(resource_fields)
    def put(self, data_id):
        args = user_input_data_put_args.parse_args()
        result = HelloWorldModel.query.filter_by(id=data_id).first()
        if result:
            abort(409, message="Data ID was previously used")
        
        complete_data_entry = HelloWorldModel(id=data_id, name=args['name'], email_address = args['email_address'], password = args['password'])
        db.session.add(complete_data_entry)
        db.session.commit()
        return complete_data_entry, 201
    
    @marshal_with(resource_fields)
    def delete(self, data_id):
        del HelloWorldModel[data_id]
        if not data_id:
            abort(409, message="Data ID does not exist")
    
        return '', 204

api.add_resource(HelloWorld, "/working/<int:data_id>")

if __name__ == "__main__":
    app.run(debug=True)