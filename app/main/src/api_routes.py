from app.main.src.company_controller import CompanyList, CompanyId, home



class ApiRoutes():
    def __init__(self, api):
        api.add_resource(home, '/')
        api.add_resource(CompanyList, '/api/v1/company')
        api.add_resource(CompanyId, '/api/v1/company/<string:company_id>')

