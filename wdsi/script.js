// Function to handle "Buy Now" button click event
function handleBuyNowClick(event) {
    // Create a modal container
    const modalContainer = document.createElement('div');
    modalContainer.classList.add('modal-container');

    // Create modal content
    const modalContent = document.createElement('div');
    modalContent.classList.add('modal-content');

    // Modal title
    const modalTitle = document.createElement('h2');
    modalTitle.textContent = 'How much do you want to buy?';

    // Quantity input
    const quantityInput = document.createElement('input');
    quantityInput.setAttribute('type', 'number');
    quantityInput.setAttribute('placeholder', 'Enter quantity');
    quantityInput.classList.add('quantity-input');

    // Confirm button
    const confirmButton = document.createElement('button');
    confirmButton.textContent = 'Confirm';
    confirmButton.classList.add('confirm-button');

    // Append modal content to modal container
    modalContent.appendChild(modalTitle);
    modalContent.appendChild(quantityInput);
    modalContent.appendChild(confirmButton);
    modalContainer.appendChild(modalContent);

    // Append modal container to body
    document.body.appendChild(modalContainer);

    // Add event listener for confirm button
    confirmButton.addEventListener('click', () => {
        const quantity = quantityInput.value;
        console.log(`You want to buy ${quantity} items.`);
        closeModal();
    });

    // Function to close the modal
    function closeModal() {
        document.body.removeChild(modalContainer);
    }
}

// Get all "Buy Now" buttons and attach click event listener
const buyNowButtons = document.querySelectorAll('.buy-now-btn');
buyNowButtons.forEach(button => {
    button.addEventListener('click', handleBuyNowClick);
});
