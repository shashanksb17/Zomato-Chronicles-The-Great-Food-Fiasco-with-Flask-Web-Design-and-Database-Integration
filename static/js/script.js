// script.js
function editDish(dishId) {
    // Handle edit dish functionality (implementation depends on your design)
    // You can show a modal or redirect to an edit page
  }
  
  function deleteDish(dishId) {
    // Handle delete dish functionality (implementation depends on your design)
    // You can show a confirmation dialog and make an AJAX request to delete the dish
  }

  
function updateOrderStatus(orderId, status) {
    // Handle updating the order status
    // Implementation depends on your design (e.g., make an AJAX request to update the status)
  }

// Function to show the reviews modal
function showReviews(dishId) {
    var modal = document.getElementById('reviewsModal');
    var closeBtn = modal.getElementsByClassName('close')[0];
    var reviewsContainer = modal.getElementById('reviewsContainer');
  
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_reviews?dish_id=' + dishId, true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        reviewsContainer.innerHTML = '';
        if (response.success) {
          response.reviews.forEach(function (review) {
            reviewsContainer.innerHTML += '<p>' + review + '</p>';
          });
        } else {
          reviewsContainer.innerHTML = '<p>No reviews available.</p>';
        }
        modal.style.display = 'block';
      }
    };
    xhr.send();
  
    closeBtn.onclick = function () {
      modal.style.display = 'none';
    };
  
    window.onclick = function (event) {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    };
  }
  
  // Handle form submission for updating order status
  document.getElementById('orderStatusForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
    var form = event.target;
    var formData = new FormData(form);
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/update_order_status', true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        alert(response.message);
        if (response.success) {
          form.reset();
        }
      }
    };
    xhr.send(formData);
  });
  
  // Handle form submission for adding a new dish
  document.getElementById('addDishForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
    var form = event.target;
    var formData = new FormData(form);
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/add_dish', true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        alert(response.message);
        if (response.success) {
          form.reset();
        }
      }
    };
    xhr.send(formData);
  });


// Handle form submission for taking an order
document.getElementById('orderForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
    var form = event.target;
    var formData = new FormData(form);
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/place_order', true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        alert(response.message);
        if (response.success) {
          form.reset();
        }
      }
    };
    xhr.send(formData);
  });

// script.js
function editDish(dishId) {
    // Handle edit dish functionality
    // Implementation depends on your design (e.g., show a modal or redirect to an edit page)
  }
  
  function deleteDish(dishId) {
    // Handle delete dish functionality
    // Implementation depends on your design (e.g., show a confirmation dialog and make an AJAX request to delete the dish)
  }
  
  function takeOrder(dishId) {
    // Handle taking an order
    // Implementation depends on your design (e.g., show a form to input customer details and selected dish)
  }
  
  