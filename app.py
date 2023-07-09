from flask import Flask,render_template, request, jsonify
from flask_socketio import SocketIO
from models.dish import Dish
from models import Dish


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)





from models.dish import Dish

# ...

# Route for taking a new order
@app.route('/take_order/<dish_id>')
def take_order(dish_id):
    dish = Dish.get_by_id(dish_id)
    if dish:
        return render_template('order.html', dish_id=dish_id)
    else:
        return 'Dish not found'


# Route for placing an order
@app.route('/place_order', methods=['POST'])
def place_order():
    customer_name = request.form['customer_name']
    dish_id = request.form['dish_id']

    if customer_name.strip() == '':
        return jsonify({'success': False, 'message': 'Please enter a customer name.'})

    # Implement order processing logic here
    # You can save the order to the database, update the order status, etc.

    order_id = 'your_generated_order_id'  # Replace with actual generated order ID
    initial_status = 'received'  # Replace with initial order status

    socketio.emit('order_status_update', {'order_id': order_id, 'status': initial_status}, namespace='/')

    return jsonify({'success': True, 'message': 'Order placed successfully'})
    

# Route for updating the order status
@app.route('/update_order_status', methods=['POST'])
def update_order_status():
    order_id = request.form['order_id']
    status = request.form['status']

    order = Order.get_by_id(order_id)
    if order:
        order.status = status
        order.update()
        socketio.emit('order_status_update', {'order_id': order_id, 'status': status}, namespace='/')
        return jsonify({'success': True, 'message': 'Order status updated successfully'})
         # Emit a WebSocket event for order status update
        socketio.emit('order_status_update', {'order_id': order_id, 'status': status}, namespace='/')
    else:
        return jsonify({'success': False, 'message': 'Order not found'})


# WebSocket event for user input and chatbot response
@socketio.on('user_input', namespace='/')
def handle_user_input(message):
    user_input = message['input']
    chatbot_response = get_chatbot_response(user_input)
    socketio.emit('chatbot_response', {'response': chatbot_response}, namespace='/')


# Route for getting the reviews of a dish
@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    dish_id = request.args.get('dish_id')
    dish = Dish.objects(id=dish_id).first()

    if dish:
        reviews = dish.reviews
        return jsonify({'success': True, 'reviews': reviews})
    else:
        return jsonify({'success': False, 'message': 'Dish not found'})

# WebSocket event for chatbot request
@socketio.on('chatbot_request', namespace='/')
def handle_chatbot_request(message):
    user_input = message['user_input']
    response = get_chatbot_response(user_input)
    socketio.emit('chatbot_response', {'response': response}, namespace='/')

# WebSocket event for order status update
@socketio.on('order_status_update', namespace='/')
def handle_order_status_update(message):
    order_id = message['order_id']
    status = message['status']
    socketio.emit('order_status_update', {'order_id': order_id, 'status': status}, namespace='/')

# Route for adding a review to a dish
@app.route('/add_review', methods=['POST'])
def add_review():
    dish_id = request.form['dish_id']
    review = request.form['review']

    dish = Dish.objects(id=dish_id).first()

    if dish:
        dish.add_review(review)
        dish.save()
        return jsonify({'success': True, 'message': 'Review added successfully'})
    else:
        return jsonify({'success': False, 'message': 'Dish not found'})

if __name__ == '__main__':
    app.run(debug=True)