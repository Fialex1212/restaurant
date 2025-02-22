function showNotification(type, message, duration = 5000) {
  const container = document.querySelector(".notification-container");
  if (!container) return;

  const notification = document.createElement("li");
  notification.classList.add("notification-item", type);

  notification.innerHTML = `
    <div class="notification-content">
      <div class="notification-icon">
        ${getIcon(type)}
      </div>
      <div class="notification-text">${message}</div>
    </div>
    <div class="notification-icon notification-close">
      <svg aria-hidden="true" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18 17.94 6M18 18 6.06 6"></path>
      </svg>
    </div>
    <div class="notification-progress-bar"></div>
  `;

  container.appendChild(notification);

  notification.querySelector(".notification-close").addEventListener("click", () => {
    notification.remove();
  });

  setTimeout(() => {
    notification.remove();
  }, duration);
}

function getIcon(type) {
  const icons = {
    success: `<svg aria-hidden="true" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.5 11.5 11 14l4-4m6 2a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>`,
    info: `<svg aria-hidden="true" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 11h2v5m-2 0h4m-2.592-8.5h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>`,
    warning: `<svg aria-hidden="true" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>`,
    error: `<svg aria-hidden="true" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>`
  };
  return icons[type] || "";
}


document.querySelector("#success-btn").addEventListener("click", () => {
  showNotification("success", "Everything went perfectly!");
});

document.querySelector("#error-btn").addEventListener("click", () => {
  showNotification("error", "Something went wrong!");
});
