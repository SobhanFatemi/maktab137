function increase(btn) {
    let item = btn.parentElement.parentElement.parentElement; 

    let quantity = btn.parentElement.getElementsByClassName('quantity')[0];
    let price = item.getElementsByClassName('price')[0];
    let amount = item.getElementsByClassName('amount')[0];

    let counter = parseInt(quantity.innerText);
    let worth = parseInt(price.innerText);

    counter++;

    let total = counter * worth;

    quantity.innerText = counter;
    amount.innerText = total;

    updateTotal();
}

function decrease(btn) {
    let item = btn.parentElement.parentElement.parentElement;

    let quantity = btn.parentElement.getElementsByClassName('quantity')[0];
    let price = item.getElementsByClassName('price')[0];
    let amount = item.getElementsByClassName('amount')[0];

    let counter = parseInt(quantity.innerText);
    let worth = parseInt(price.innerText);

    if (counter > 0) counter--;

    let total = counter * worth;

    quantity.innerText = counter;
    amount.innerText = total;

    updateTotal();
}

function updateTotal() {
    let allAmounts = document.getElementsByClassName('amount');
    let total = 0;
    for (let i = 0; i < allAmounts.length; i++) {
        total += parseInt(allAmounts[i].innerText);
    }
    document.getElementById('total').innerText = total;
}