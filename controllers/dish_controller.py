from models.dish import Dish
from flask import jsonify, request

# Controller function for adding a new dish

# Controller function for adding a new dish
def add_dish():
    dish_name = request.form['dish_name']
    price = float(request.form['price'])
    availability = request.form['availability']
    
    if price <= 0:
        return jsonify({'success': False, 'message': 'Please enter a valid price.'})
    
    dish = Dish(dish_name, price, availability)
    dish.save()
    
    return jsonify({'success': True, 'message': 'Dish added successfully'})

# Controller function for updating a dish
def update_dish():
    dish_id = request.form['dish_id']
    dish_name = request.form['dish_name']
    price = request.form['price']
    availability = request.form['availability']
    
    dish = Dish.get_by_id(dish_id)
    if dish:
        dish.dish_name = dish_name
        dish.price = price
        dish.availability = availability
        dish.update()
        return jsonify({'success': True, 'message': 'Dish updated successfully'})
    else:
        return jsonify({'success': False, 'message': 'Dish not found'})

# Controller function for deleting a dish
def delete_dish():
    dish_id = request.form['dish_id']
    
    dish = Dish.get_by_id(dish_id)
    if dish:
        dish.delete()
        return jsonify({'success': True, 'message': 'Dish deleted successfully'})
    else:
        return jsonify({'success': False, 'message': 'Dish not found'})
