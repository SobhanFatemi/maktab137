const header = document.getElementById("header");
header.innerText = "My Tasks";

header.style.color = "red"

const item1 = document.getElementById("item1");
item1.innerText = "user dashboard";

const item2 = document.getElementById("item2");
item2.innerText = "admin dashboard";

const item3 = document.getElementById("item3");
let htmlElement = `authentication
        <ul>
            <li id="item4"></li>
            <li id="item5"></li>
            <li id="item6"></li>
        </ul>`

item3.innerHTML = htmlElement

const button = document.getElementById("button");
button.innerText = "add task";

const item7 = document.getElementById("item7");
item7.innerText = "about page";

const item8 = document.getElementById("item8");
item8.innerText = "content page";

item8.style.textDecoration = "line-through"

const item4 = document.getElementById("item4");
item4.innerText = "login";

const item5 = document.getElementById("item5");
item5.innerText = "register";

item5.style.textDecoration = "line-through"

const item6 = document.getElementById("item6");
item6.innerText = "log out";



