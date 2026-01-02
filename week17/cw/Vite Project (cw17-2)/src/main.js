import 'bootstrap/dist/css/bootstrap.min.css';

const url = "https://fakestoreapi.com/products";
const sec = document.getElementById("sec");

const cardHTMLComponent = (image, title, rating, rateCount, price) => {
    return `<div class="card d-flex flex-column" style="width: 18rem; height: 32rem;">
                <div class="card-body d-flex flex-column justify-content-start"">
                    <img src=${image} class="d-flex card-img-top m-auto pb-3 border-bottom" style="height: 12rem; width: 12rem;" alt="${title.slice(0,20)}">
                    <h5 class="card-text text-center">${title}</h5>
                </div>

                <div class="card-body d-flex flex-column justify-content-end">
                    <h4 class="card-text border-bottom">${rating}/5 <span class="card-text text-success" style="font-size: 12px;">${rateCount} rates</span></h4>
                    <h4 class="">$${price}</h4>
                    <a href="#" class="btn btn-primary">Order</a>
                </div>
            </div>`;
};
        



const fetchURL = async() => {
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error("Something went wrong!")
            
        const data = await res.json();
        console.log(data);

        const productCards = 
        data.map(product => cardHTMLComponent(
            product.image,
            product.title,
            product.rating.rate,
            product.rating.count,
            product.price
        ))

        sec.innerHTML = productCards.join("")
    }

    catch(error){
        console.error(error)
    }
}

fetchURL();