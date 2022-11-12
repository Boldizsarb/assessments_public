


document.getElementById("covidbutton").addEventListener("click", e=>{

    const xhttp = new XMLHttpRequest();

    xhttp.addEventListener("load", response=>{

        document.getElementById("output").innerHTML = response.target.responseText;
    });

    xhttp.open("get", "/covid19"); // page of what the program will render
    xhttp.send(); 

});

// environment button
document.getElementById("environmentbutton").addEventListener("click", e=>{
    
    const xhttp = new XMLHttpRequest();
    xhttp.addEventListener("load", response=>{
        document.getElementById("output").innerHTML = response.target.responseText;
    });
    
    xhttp.open("get", "environmentfaq"); 
    xhttp.send();

});

document.getElementById("generalbutton").addEventListener("click", e=>{
    
    const xhttp = new XMLHttpRequest();
    xhttp.addEventListener("load", response=>{
        document.getElementById("output").innerHTML = response.target.responseText;
    });
    
    xhttp.open("get", "general"); 
    xhttp.send();

});

/////////////

