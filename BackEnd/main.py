from flask import request, jsonify
from config import db, app
from models import Contact

# CRUD


@app.route("/contacts", methods=["GET", "OPTIONS", "POST"])
def handle_contacts():
    if request.method == "OPTIONS":
        response = jsonify({"message": "opted"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

        return response, 204
    
    if request.method == "POST":
        first_name = request.json.get("firstName")
        last_name = request.json.get("lastName")
        email = request.json.get("email")
        
        if not first_name or not last_name or not email:
            return jsonify(
                {"message": "error, contact needs first name, last name and email"},
                400,
                        )
        
        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        try:
            db.session.add(new_contact)
            db.session.commit()
        except Exception as e:
            return jsonify(
                {"message": str(e )},
                400,
                )
            
        return jsonify({"message": "User created!"}, 201 )
    
    if request.method == "GET":
        contacts = Contact.query.all()
        json_contacts = list(map(lambda x: x.to_json(), contacts))
        return jsonify({"contacts": json_contacts})
    

@app.route("/contacts/<int:user_id>", methods=["PATCH, DELETE"])
def alter_user(user_id):
    if request.method == "DELETE":
        contact = Contact.query.get(user_id)
    
        if not contact:
            return jsonify(
                {
                    "message": "error, no matching id found"
                }, 
                400
            )
        

        db.session.delete(contact)
        db.session.commit()

        return jsonify({"message": "Deleted contact!"}, 201)
    
    if request.method == "PATCH":
        contact = Contact.query.get(user_id) 
    
        if not contact:
            return jsonify(
                {
                    "message": "error, no matching contact found"
                }, 
                404
            )
        
        data = request.json
        contact.first_name = data.get("firstName", contact.first_name)
        contact.last_name = data.get("lastName", contact.last_name)
        contact.email = data.get("email", contact.email)
        
        db.session.commit() 
        
        return jsonify({"message": "Updated contact!"}, 201)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

