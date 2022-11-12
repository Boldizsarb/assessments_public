

document.getElementById("forma").addEventListener("submit", e=>{
    let input_fname = document.forms["forma"]["fname"].value;
    let input_sname = document.forms["forma"]["sname"].value;
    let input_email = document.forms["forma"]["email"].value;
    let input_phone = document.forms["forma"]["phone"].value;
    let input_query = document.forms ["forma"]["query"].value;

    

    // displaying invalid boxes
    let is_valid = true;
    let ouptut = "";

    if (input_fname.trim()===""){
        ouptut += "First Name is required <br>";
        document.forms["forma"]["fname"].style.backgroundColor = "red";
        is_valid = false
    };
    if (input_sname.trim()=== ""){
        ouptut += "Forename(s) is required<br>";
        document.forms["forma"]["sname"].style.backgroundColor = "red";
        is_valid = false
    };
    if (input_email.trim()=== ""){
        ouptut += "Email is required<br>";
        document.forms["forma"]["email"].style.backgroundColor = "red";
        is_valid = false
    };
    if (input_phone.trim()== ""){
        ouptut += "Phone number is required<br>";
        document.forms["forma"]["phone"].style.backgroundColor = "red";
        is_valid = false
    };
    // in case of wrong phone number, it will display an massage
    let regEx = /((\+44(\s\(0\)\s|\s0\s|\s)?)|0)7\d{3}(\s)?\d{6}/
    
    if (input_phone.match(regEx)){
        ouptut += "Phone number is required<br>";
        document.forms["forma"]["phone"].style.backgorundColor = "red";
        is_valid = true
    }; 
    let result = regEx.test(input_phone)
    if (result == false){
        ouptut += "Enter a valid phone number<br>"
        is_valid = false
    }

    if (input_query.trim() === ""){
        ouptut += "Query is required as well<br>";
        document.forms["forma"]["query"].style.backgroundColor = "red";
        is_valid = false
    }
    // if the query too long or too short it will display a massage. 

    let count = 0
    let split = input_query.split('');
    for (let i = 0; i < split.length; i++) {
        if (split[i]!=""){
            count +=1;
        }
    }
    if (count> 400){
        ouptut += "You exceeded the word limit<br>.";
        is_valid = false
    }
    if (count< 50){
        ouptut += "Explain it a little bit broadher<br>";
        is_valid = false
    }
    // checking the radio button
    let a = document.getElementById("em").checked;
    let b = document.getElementById("wh").checked;
    let c = document.getElementById("vi").checked;
    let d = document.getElementById("sm").checked;
    if(a == false && b == false && c==false && d == false){
        ouptut+= "You need to select a way of communication"
        is_valid = false
    }

    if (is_valid == false){
        e.preventDefault();
        document.getElementById("error").innerHTML = ouptut;
    }


});
