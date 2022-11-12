
/*
document.getElementById('formsearch').addEventListener("submit",e=>{
    e.preventDefault(); // accessibility: if java turned off it wont submit hence it is a backup 
    // ajax request
    let query = document.forms ["formsearch"]["search"].value;
    fetch(`/result/${query}`)
    .then(response => response.text())
    .then(text =>{
        document.getElementById("output").innerHTML = text;
    });
}); */