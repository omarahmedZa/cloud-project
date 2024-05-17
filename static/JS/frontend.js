// JavaScript for modern cart management

// Sample data for shopping cart

/*let shoppingCartItems = [
    { id: 1, name: "Product 1", price: 100, image: "photos/product1.jpg", quantity: 1 },
    { id: 2, name: "Product 2", price: 20, image: "photos/product2.jpg", quantity: 1 },
    { id: 3, name: "Product 3", price: 30, image: "photos/product3.jpg", quantity: 1 }
];*/

var shoppingCartItems 

// Function to display shopping cart items
function displayShoppingCart() {
    const shoppingCartSection = document.getElementById('shopping-cart');
    let html = '<h2>Shopping Cart</h2>';
    html += '<ul>';
    shoppingCartItems.forEach(item => {
        html += `<li>`;
        html += `<div class="item-container">`; // Container for each item
        html += `<div class="item-details">`; // Container for item details (photo and name)
        html += `<div id="image-container" alt="${item.name}" style="width: 100px; height: auto;"></div>`; // Adjust size here
        html += `<span name="name">${item.name}</span>`;
        html += `</div>`; // End of item details container
        html += `<div class="item-actions">`; // Container for item actions (remove, price, counter)
        html += `<span class="price" name="price">$${item.price}</span>`; // Price label
        html += `<button class="remove-btn" onclick="removeItem(${item.id})">Remove</button>`; // Remove button with text
        html += `<div class="quantity-container">`; // Container for quantity buttons
        html += `<button class="quantity-btn" onclick="decrementQuantity(${item.id})">-</button>`;
        html += `<span name="quantity">${item.quantity}</span>`;
        html += `<button class="quantity-btn" onclick="incrementQuantity(${item.id})">+</button>`;
        html += `</div>`; // End of quantity container
        html += `</div>`; // End of item actions container
        html += `</div>`; // End of item container
        html += `</li>`;
    });
    html += '</ul>';
    shoppingCartSection.innerHTML = html;
    document.getElementById('image-container').appendChild(shoppingCartItems.image);
    
    // Adjust positioning of price label
    const priceLabels = document.querySelectorAll('.price');
    priceLabels.forEach(label => {
        label.style.marginRight = '10px';
    });
}

// Function to remove item from shopping cart
function removeItem(id) {
    shoppingCartItems = shoppingCartItems.filter(item => item.id !== id);
    displayShoppingCart();
    removeItemFromCart(id);
}

// Function to increment quantity of an item
function incrementQuantity(id) {
    const itemIndex = shoppingCartItems.findIndex(item => item.id === id);
    if (itemIndex !== -1) {
        shoppingCartItems[itemIndex].quantity++;
        updateTotalPrice();
        displayShoppingCart();
    }
}

// Function to decrement quantity of an item
function decrementQuantity(id) {
    const itemIndex = shoppingCartItems.findIndex(item => item.id === id);
    if (itemIndex !== -1 && shoppingCartItems[itemIndex].quantity > 1) {
        shoppingCartItems[itemIndex].quantity--;
        updateTotalPrice();
        displayShoppingCart();
    }
}
// JavaScript for card details editing

// Function to enable editing of card details
function enableEditing() {
    const cardNameInput = document.getElementById('cardName');
    const cardNumberInput = document.getElementById('cardNumber');
    const expirationInput = document.getElementById('expiration');
    const cvvInput = document.getElementById('cvv');
    const editButton = document.getElementById('editButton');

    cardNameInput.disabled = false;
    cardNumberInput.disabled = false;
    expirationInput.disabled = false;
    cvvInput.disabled = false;

    editButton.textContent = 'Save';
    editButton.removeEventListener('click', enableEditing);
    editButton.addEventListener('click', saveChanges);
}

// Function to save changes made to card details
function saveChanges() {
    const cardNameInput = document.getElementById('cardName');
    const cardNumberInput = document.getElementById('cardNumber');
    const expirationInput = document.getElementById('expiration');
    const cvvInput = document.getElementById('cvv');
    const editButton = document.getElementById('editButton');

    const cardName = cardNameInput.value;
    const cardNumber = cardNumberInput.value;
    const expiration = expirationInput.value;
    const cvv = cvvInput.value;

    // Here you can handle saving the changes (e.g., sending data to a server)

    cardNameInput.disabled = true;
    cardNumberInput.disabled = true;
    expirationInput.disabled = true;
    cvvInput.disabled = true;

    editButton.textContent = 'Edit';
    editButton.removeEventListener('click', saveChanges);
    editButton.addEventListener('click', enableEditing);
}

// Function to calculate total price
function calculateTotalPrice(items) {
    let totalPrice = 0;
    items.forEach(item => {
        totalPrice += item.price * item.quantity;
    });
    return totalPrice.toFixed(2); // Round to 2 decimal places
}

// Function to create and append the checkout button inside the Card Details container
function createCheckoutButton(totalPrice) {
    // Create button element
    const button = document.createElement("button");
    button.setAttribute("id", "checkoutButton");
    button.classList.add("checkout-btn");

    // Create span element for total price
    const totalPriceSpan = document.createElement("span");
    totalPriceSpan.classList.add("total-price");
    totalPriceSpan.textContent = `$${totalPrice}`;

    // Create span element for checkout label
    const checkoutLabelSpan = document.createElement("span");
    checkoutLabelSpan.classList.add("checkout-label");
    checkoutLabelSpan.textContent = "Checkout ";

    // Create icon element for checkout arrow
    const arrowIcon = document.createElement("i");
    arrowIcon.classList.add("fas", "fa-long-arrow-alt-right");

    // Append arrow icon to checkout label span
    checkoutLabelSpan.appendChild(arrowIcon);

    // Append total price span and checkout label span to button
    button.appendChild(totalPriceSpan);
    button.appendChild(checkoutLabelSpan);

    // Get the Card Details container
    const cardDetailsContainer = document.querySelector(".card-details");

    // Append button to the Card Details container
    cardDetailsContainer.appendChild(button);
}

// Function to create and append the line separator
function createLineSeparator() {
    const lineSeparator = document.createElement("div");
    lineSeparator.classList.add("line-separator");

    // Get the Card Details container
    const cardDetailsContainer = document.querySelector(".card-details");

    // Append line separator to the Card Details container
    cardDetailsContainer.appendChild(lineSeparator);
}


// Function to calculate total price
function calculateTotalPrice(items) {
    let totalPrice = 0;
    items.forEach(item => {
        totalPrice += item.price * item.quantity;
    });
    return totalPrice.toFixed(2); // Round to 2 decimal places
}

// Function to update total price
function updateTotalPrice() {
    const totalPriceSpan = document.querySelector(".total-price");
    const totalPrice = calculateTotalPrice(shoppingCartItems);
    totalPriceSpan.textContent = `$${totalPrice}`;
}

// Function to remove an item from the shopping cart
function removeItemFromCart(itemId) {
    shoppingCartItems = shoppingCartItems.filter(item => item.id !== itemId);
    updateTotalPrice(); // Update total price after item removal
}

fetch('/')
    .then(response => response.json())
    .then(data => {
        // Process the received data
        shoppingCartItems = document.getElementById('product-list');
        data.forEach(product => {
            const li = document.createElement('li');
            var img = new Image();
    
            img.src = "data:image/jpg;base64," + product.image;
            li.textContent = `id: ${product.id}, name: ${product.name}, price: $${product.price}, image: $${img}, quantity: $${product.quantity}`;
            shoppingCartItems.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching product data:', error));


var img = new Image();

img.src = "data:image/jpg;base64," + shoppingCartItems.image;
print(shoppingCartItems.image)
shoppingCartItems.image = img
const totalPrice = calculateTotalPrice(shoppingCartItems);

// Call function to create and append the line separator
createLineSeparator();


// Calculate total price


// Call function to create and append the checkout button with the total price
createCheckoutButton(totalPrice);

// Attach event listener to the edit button
document.getElementById('editButton').addEventListener('click', enableEditing);


// Call functions to display data
displayShoppingCart();

console.log(data);



