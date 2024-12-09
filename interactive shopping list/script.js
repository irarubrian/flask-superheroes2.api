  //DOM functions
  

  const document = window.document;

  const localStorage = {
    getItem: (key) => localStorage[key] || null,
    setItem: (key, value) => {localStorage[key] = value;},
      
    };

  const itemInput = document.getElementById('item-input');
  const addButton = document.getElementById('add-button');
  const clearButton = document.getElementById('clear-button');
  const shoppingLists = document.getElementById('shopping-lists');

  //shoppinglist aray

  let shoppingListItems = JSON.parse(localStorage.getItem(`shoppingList`)) || [];

//render shopping ls

function renderList() {
  shoppingLists.innerHTML = '';
  shoppingListItems.forEach((item , index) => {
    const li = document.createElement(`li`);
    li.className = `list-item ${item.purchased ? `purchased` : ''}`;

    const textSpan = document.createElement(`span`);
    textSpan.textContent = item.name;

    const purchaseButton = document.createElement(`button`);
    purchaseButton.textContent = `purchased`;
    purchaseButton.addEventListener(`click`, () => {
      shoppingListItems[index].purchased = !shoppingListItems[index].purchased;
      saveToLocalStorage();
      renderList();
    });

    const editButton = document.createElement(`button`);
    editButton.textContent = `Edit`;
    editButton.addEventListener(`click`, () => {
      textSpan.contentEdit = !textSpan.contentEdit;
      if(!textSpan.contentEdit) {
        shoppingListItems[index].name = textSpan.textContent.trim();
        saveToLocalStorage();
        renderList();
      }
      });

      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.addEventListener('click', () => {
        shoppingListItems.splice(index, 1);
        saveToLocalStorage();
        renderList();
      });

      li.appendChild(textSpan);
      li.appendChild(purchaseButton);
      li.appendChild(editButton);
      li.appendChild(deleteButton);
      shoppingLists.appendChild(li);

  });

}
// add new item

function  addItem() {
  const itemName = itemInput.value.trim();
  if (itemName) {
    shoppingListItems.push({ name: itemName, purchased: false});
    saveToLocalStorage();
    renderList();
    itemInput.value = '';
    itemInput.value= '';
  }else{
    alert(`item already exist on the shopping-list.`);
  }
}
sss
  // clear the shoppinglist
  function clearlist(){
    shoppingListItems = [];
    saveToLocalStorage();
    renderList();
  }

  //save the list to the local

  function saveToLocalStorage(){
    localStorage.setItem(`shoppingList`, JSON.stringify(shoppingListItems));

  }

  // event listeners

  addButton.addEventListener(`click`, addItem);
  addButton.addEventListener(`click`, clearlist);
  // initial render

  renderList();
