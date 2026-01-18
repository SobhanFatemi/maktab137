import 'bootstrap/dist/css/bootstrap.min.css';

const url = "https://dummyjson.com/users";
const sec = document.getElementById("sec");
const getAvatar = (id) =>
  `https://api.dicebear.com/7.x/bottts/svg?seed=${id}`;

const cardHTMLComponent = (image, firstName, lastName, email, companyName, address) => {
    return `<div class="card text-center bg-dark text-white" style="width: 18rem; height: 25rem;">
                <div class="card-body d-flex flex-column p-0">
                    <img src=${image} class="card-img-top" style="margin: 0 auto; height: 12rem; width: 12rem;" alt="${firstName}">
                    <div class="d-flex border-bottom border-info border-4 mb-3" style="width: 17.9rem"></div>
                    <h4 class="card-text text-center text-info">${firstName} ${lastName}</h5>
                    <p class="card-text mb-0" style="font-size: 14px;">${email}</p>
                    <p class="card-text" style="font-size: 14px;">🏬 ${companyName}</p>
                </div>

                <div class="card-body d-flex flex-column">    
                    <h6 class="text-decoration-underline mb-0" style="font-size: 14px;">Address</h6>   
                    <p class="w-75 m-auto" style="font-size: 14px;">${address.address}, ${address.city}, ${address.state}</p>
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
        data.users.map(user => cardHTMLComponent(
            getAvatar(user.id),
            user.firstName,
            user.lastName,
            user.email,
            user.company.name,
            user.address
        ))

        sec.innerHTML = productCards.join("")
    }

    catch(error){
        console.error(error)
    }
}

fetchURL();