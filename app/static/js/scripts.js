const popup = document.getElementById("popup");
const openPopupBtn = document.getElementById("openPopupBtn");
const closePopupBtn = document.getElementById("closePopupBtn");

// open popup
openPopupBtn.addEventListener("click", () => {
  popup.style.display = "block";
});

// click by cross
closePopupBtn.addEventListener("click", () => {
  popup.style.display = "none";
});

// close outside click
window.addEventListener("click", (event) => {
  if (event.target === popup) {
    popup.style.display = "none";
  }
});

function getBasket() {
  let basket = JSON.parse(localStorage.getItem("basket"));
  if (!basket) {
    basket = [];
  }
  return basket;
}

function updateBasket(basket) {
  localStorage.setItem("basket", JSON.stringify(basket));
}

function addToBasket(dishId, title, price, image) {
  const basket = getBasket();
  const existingDish = basket.find((item) => item.id === dishId);

  if (existingDish) {
    existingDish.quantity += 1; // Increase quantity if item exists
    alert(`${title} - ${existingDish.quantity} added to your basket`);
  } else {
    basket.push({
      id: dishId,
      title: title,
      price: price,
      image: image,
      quantity: 1,
    });
    alert(`${title} added to your basket`);
  }

  updateBasket(basket);
  renderBasket();
}

function increaseQuantity(dishId) {
  const basket = getBasket();
  const dish = basket.find((item) => item.id === dishId);

  if (dish) {
    dish.quantity += 1;
    updateBasket(basket);
    renderBasket();
  }
}

function decreaseQuantity(dishId) {
  const basket = getBasket();
  const dish = basket.find((item) => item.id === dishId);

  if (dish && dish.quantity > 1) {
    dish.quantity -= 1;
    updateBasket(basket);
    renderBasket();
  } else if (dish.quantity === 1) {
    removeFromBasket(dishId);
  }
}

function removeFromBasket(dishId) {
  let basket = getBasket();
  basket = basket.filter((item) => item.id !== dishId);
  updateBasket(basket);
  renderBasket();
}

function clearBasket() {
  localStorage.removeItem("basket");
  renderBasket();
}

function renderBasket() {
  const basket = getBasket();
  const basketItems = document.getElementById("basket-items");
  basketItems.innerHTML = "";

  if (basket.length === 0) {
    basketItems.innerHTML = "<li>Your basket is empty.</li>";
  } else {
    basket.forEach((item) => {
      const li = document.createElement("li");
      li.innerHTML = `
            <div class="product">
                <div class="product__left">
                <img
                    src="${item.image}"
                    alt="${item.title}"
                    class="product__img"
                />
                </div>
                <div class="product__rigth">
                <h3 class="product__title">${item.title}</h3>
                <div class="product__buttons">
                    <div class="product__quantity">
                    <button onclick="decreaseQuantity('${item.id}')">-</button>
                    <p>${item.quantity}</p>
                    <button onclick="increaseQuantity('${item.id}')">+</button>
                    </div>
                    <button class="remove__button" onclick="removeFromBasket('${item.id}')">Remove</button>
                </div>
                </div>
            </div>
            `;
      basketItems.appendChild(li);
    });
  }

  const clearBasketButton = document.getElementById("clear-basket");
  if (basket.length > 0) {
    clearBasketButton.style.display = "block";
  } else {
    clearBasketButton.style.display = "none";
  }
}

document.querySelectorAll(".add__to__basket").forEach((button) => {
  button.addEventListener("click", function () {
    const dishId = this.getAttribute("data-dish-id");
    const dishTitle = this.getAttribute("data-dish-title");
    const dishPrice = this.getAttribute("data-dish-price");
    const dishImage = this.getAttribute("data-dish-image");

    addToBasket(dishId, dishTitle, dishPrice, dishImage);
  });
});

document.addEventListener("DOMContentLoaded", renderBasket);

function checkout() {
  const basket = getBasket();
  alert("Proceeding to checkout with " + basket.length + " items.");

  // Отправляем корзину на сервер через POST-запрос
  fetch("/api/checkout/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
    body: JSON.stringify({
      basket: basket,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Order placed successfully!");
        clearBasket();
        window.location.href = "/profile/orders"; // Перенаправляем на страницу заказов
      } else {
        alert("Error placing order: " + data.error);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
