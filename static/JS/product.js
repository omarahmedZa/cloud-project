const cart = {};

document.addEventListener("DOMContentLoaded", function() {
    const productGrid = document.getElementById("product-grid");
    const categoryList = document.getElementById("category-list");
    const cartIcon = document.getElementById("cart-icon");
    


    function displayProducts(products) {
        productGrid.innerHTML = ""; // Clear existing products
        products.forEach(product => {
            const productCard = document.createElement("div");
            productCard.classList.add("product-card");

            const productImage = document.createElement("img");
            productImage.src = product.image;
            productImage.alt = product.name;

            const productName = document.createElement("h2");
            productName.textContent = product.name;


            const productPrice = document.createElement("p");
            productPrice.textContent = `$${product.price.toFixed(2)}`;


            // Cart icon
            const addToCartIcon = document.createElement("button");
            /*addToCartIcon.alt = "Add to Cart";
            addToCartIcon.classList.add("add-to-cart-icon");
            addToCart.name = "Add to Cart";*/
            html = `<button class="cart-icon" onclick="addToCart(${product.id})">Add to Cart</button>`;
            addToCartIcon.innerHTML = html
            

             


            productCard.appendChild(productImage);
            productCard.appendChild(productName);
            productCard.appendChild(productPrice);
            productCard.appendChild(addToCartIcon);

            productGrid.appendChild(productCard);
        });
    }

    function displayCategories() {
        categoryList.innerHTML = ""; // Clear existing categories
        categories.forEach(category => {
            const categoryItem = document.createElement("li");
            const categoryLink = document.createElement("a");
            categoryLink.href = "#"; // Prevent page refresh
            categoryLink.textContent = category.name;
            categoryLink.addEventListener("click", function(e) {
                e.preventDefault();
                displayProducts(category.products); // Show products for this category
            });

            categoryItem.appendChild(categoryLink);
            categoryList.appendChild(categoryItem);
        });
    }

    // Display the first category's products by default
    
    displayProducts(products);
   
});

function addToCart(product) {
    cart["id"] = product;
    console.log("Product added to cart:", cart);
    sendData()
}


function sendData() { 
    $.ajax({ 
        url: "/save_cart_product", 
        type: 'POST',
        data: Object.assign(cart), 
        success: function(response) {
            // Handle the successful response from the server
            console.log("POST request successful");
            console.log("Response:", response);
        },
        error: function(error) { 
            console.log(error); 
        } 
    });
} 