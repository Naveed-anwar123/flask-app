from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        
        return {'message':'Store is not found'},404


    def post(self , name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message':'Store with  the name {} Already there'.format(name)}, 400

        store = StoreModel(name)    
        store.save_to_db()
        return store.json()

        
    def delete(self,name):

        store = StoreModel.find_by_name(name)
        if store is None:
            return {'message':'Store Does not exists'}, 400

        store.delete_from_db()
        return {'message':'Store Deleted '}
        


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()] }
