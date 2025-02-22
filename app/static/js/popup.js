document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector(".popup__form");
  const popup = document.getElementById("popup");
  const closePopupBtn = document.getElementById("closePopupBtn");
  const phoneInput = document.getElementById("phone");

  phoneInput.addEventListener("input", function (e) {
    let value = e.target.value.replace(/[^\d+]/g, "");
    if (value.startsWith("+380")) {
      value = "+380" + value.slice(4);
    } else if (value.startsWith("380")) {
      value = "+380" + value.slice(3);
    } else if (value.startsWith("0")) {
      value = "+380" + value.slice(1);
    }

    if (value.length > 13) {
      value = value.slice(0, 13);
    }

    if (value.length > 4) {
      value = value.slice(0, 4) + " " + value.slice(4);
    }
    if (value.length > 7) {
      value = value.slice(0, 7) + " " + value.slice(7);
    }
    if (value.length > 11) {
      value = value.slice(0, 11) + " " + value.slice(11);
    }

    e.target.value = value;
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const phoneValue = phoneInput.value.replace(/\s+/g, "");
    const phonePattern = /^\+380\d{9}$/;

    if (!phonePattern.test(phoneValue)) {
      showNotification(
        "error",
        "❌ Please enter a valid Ukrainian phone number in the format +380XXXXXXXXX!"
      );
      return;
    }

    setTimeout(() => {
      showNotification(
        "success",
        "✅ Your table has been booked successfully!"
      );
      popup.style.display = "none";
      form.reset();
    }, 500);
  });

  closePopupBtn.addEventListener("click", function () {
    popup.style.display = "none";
  });

});
