
// JavaScript for the Interactive Shopping List

// Get DOM elements
const inputField = document.getElementById("item-input");
const addButton = document.getElementById("add-button");
const clearButton = document.getElementById("clear-button");
const shoppingList = document.getElementById("shopping-list");

// Shopping list array
let items = JSON.parse(localStorage.getItem("shoppingList")) || [];

// Function to render the shopping list
function renderList() {
  shoppingList.innerHTML = "";
  items.forEach((item, index) => {
    const listItem = document.createElement("li");
    listItem.textContent = item.name;
    if (item.purchased) {
      listItem.classList.add("purchased");
    }
    listItem.addEventListener("click", () => togglePurchased(index));
    shoppingList.appendChild(listItem);
  });
}

// Add a new item to the list
addButton.addEventListener("click", () => {
  const newItem = inputField.value.trim();
  if (newItem) {
    items.push({ name: newItem, purchased: false });
    saveToLocalStorage();
    renderList();
    inputField.value = ""; // Clear input field
  }
});

// Mark item as purchased
function togglePurchased(index) {
  items[index].purchased = !items[index].purchased;
  saveToLocalStorage();
  renderList();
}

// Clear the entire list
clearButton.addEventListener("click", () => {
  items = [];
  saveToLocalStorage();
  renderList();
});

// Save the list to local storage
function saveToLocalStorage() {
  localStorage.setItem("shoppingList", JSON.stringify(items));
}

// Initial render on page load
renderList();
