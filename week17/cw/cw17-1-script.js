const loginForm = document.getElementById("login-form");
const order = document.getElementById("order");
const add = document.getElementById("add");
const sub = document.getElementById("sub");
const sugarAmount= document.getElementById("sugar-amount");
let sugarCount = 0

function addSugar() {
    sugarCount++;
    sugarAmount.innerText = sugarCount;
};

function subSugar() {
    if (sugarCount > 0) {
        sugarCount--;
        sugarAmount.innerText = sugarCount;
    }
};

const LoginFormSubmit = (event)=> {
    event.preventDefault();
    const name = document.getElementById("name").value.trim();
    const type = document.querySelector("input[name='type']:checked").value;
    const size = document.getElementById("size").value;

    if (name === ""){
        alert("لطفا نام خود را وارد کنید!");
        return
    }

    const orderCard = document.createElement("div");
    orderCard.className = "d-flex justify-content-center card mb-2 p-5 w-50 m-auto border rounded gap-3"
    orderCard.innerHTML = `
            <h1 class="text-center">فاکتور خرید</h1>
            <p>نام: ${name}</p> 
            <p>نوشیدنی: ${type}</p>
            <p>اندازه: ${size}</p>
            <p>میزان شکر: ${sugarCount} عدد</p>
    `;

    order.appendChild(orderCard);
    loginForm.reset();
    sugarCount = 0;
    sugarAmount.innerText = sugarCount;
};

loginForm.addEventListener("submit", (event) => LoginFormSubmit(event));
add.addEventListener("click", addSugar)
sub.addEventListener("click", subSugar)