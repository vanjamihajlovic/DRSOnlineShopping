from marshmallow import Schema,fields


class UserSchemaUpdate(Schema):
    id=fields.Int(required=True)
    name=fields.Str(required=True)
    surname=fields.Str(required=True)
    address=fields.Str(required=True)
    city=fields.Str(required=True)
    country=fields.Str(required=True)
    phone=fields.Str(required=True)
    email=fields.Str(required=True)
    password=fields.Str(required=True)


class UserSchemaRegister(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True,load_only=True)
    surname=fields.Str(required=True,load_only=True)
    address=fields.Str(required=True,load_only=True)
    city=fields.Str(required=True,load_only=True)
    country=fields.Str(required=True,load_only=True)
    phone=fields.Str(required=True,load_only=True)
    email=fields.Str(required=True,load_only=True)
    password=fields.Str(required=True,load_only=True)


class UserSchemaViewUpdate(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    surname=fields.Str(required=True)
    address=fields.Str(required=True)
    city=fields.Str(required=True)
    country=fields.Str(required=True)
    phone=fields.Str(required=True)
    email=fields.Str(required=True)
    password=fields.Str(required=True)


    
class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    email=fields.Str(required=True)
    password=fields.Str(required=True,load_only=True)
    
    
class ProductSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    image=fields.Str(required=True)
    price=fields.Int(required=True)
    currency=fields.Str(required=True)
    quantity=fields.Int(required=True)
    
class ProductSchemaUpdate(Schema):
    id=fields.Int(required=True)
    name=fields.Str(required=True)
    image=fields.Str(required=True)
    price=fields.Int(required=True)
    currency=fields.Str(required=True)
    quantity=fields.Int(required=True)