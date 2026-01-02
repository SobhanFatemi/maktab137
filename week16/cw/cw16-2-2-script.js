const emoji = document.getElementById("emoji")
const text = document.getElementById("text")

function happyclick() {
    emoji.innerText = "😀";
    text.innerText = "من خوشحالم";
}

function sadclick() {
    emoji.innerText = "🙁";
    text.innerText = "من ناراحتم";
}