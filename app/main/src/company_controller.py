from flask import jsonify, abort
from flask_restful import Resource

from app.main.src.company_model import Company
from app.main import db


class home(Resource):
    def get(self):
        return 'Ankorstore test 2022 - Jeremy Perthuis'


class CompanyList(Resource):
    def get(self):
        results = db.session.query(Company).all()
        return jsonify({
            'data': [result.serialized for result in results]
        })

class CompanyId(Resource):
    def get(self, company_id):
        res = db.session.query(Company).filter(Company.id == company_id)
        if res is None :
            abort(404, description="Resource not found")
        else :
            return jsonify({
                'data': [result.serialized for result in res]
            })


