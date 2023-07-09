from flask import render_template, request, jsonify
from models.dish import Dish
from controllers.dish_controller import add_dish, update_dish, delete_dish

# Route for displaying the menu
@app.route('/')
def menu():
    dishes = Dish.get_all()
    return render_template('menu.html', dishes=dishes)

# Route for adding a new dish
@app.route('/add_dish', methods=['POST'])
def add_dish_route():
    return add_dish()

# Route for taking a new order
@app.route('/take_order/<dish_id>', methods=['GET'])
def take_order_route(dish_id):
    return take_order(dish_id)


# Route for placing an order
@app.route('/place_order', methods=['POST'])
def place_order():
    customer_name = request.form['customer_name']
    dish_id = request.form['dish_id']
    
    # Implement order processing logic here
    # You can save the order to the database, update the order status, etc.
    
    return jsonify({'success': True, 'message': 'Order placed successfully'})

# Route for updating a dish
@app.route('/update_dish', methods=['POST'])
def update_dish_route():
    return update_dish()

# Route for deleting a dish
@app.route('/delete_dish', methods=['POST'])
def delete_dish_route():
    return delete_dish()
