const express = require('express'); // import the express library
const res = require('express/lib/response');
const mysql = require("mysql"); // importing my sql library

const db = mysql.createConnection({ // establishing connection
    host: "localhost",
    user: "root",
    password: "",   // on mac sometimes it is root
    database: "contact"
});
db.connect(error=>{  // connecting to the database
    if (error) throw error; // if there is an error it will throw an error 
    console.log("MySQL has just started.")
});

const app = express(); // express instance

app.set("view engine", "ejs"); // seting up ejs views enginge
app.use(express.static("static"));  // static elements whereabouts
app.use("/static", express.static('./static/'));


app.get("/", (req, res)=>{   // "/" root for the home page
    res.render("index")  // renders the hmtl file onto the page
});

app.get("/contact", (req, res)=>{   
    res.render("contact")  
});

app.get("/stages", (req, res)=>{   
    res.render("stages")  
});


app.get("/puzzle", (req, res)=>{   
    res.render("puzzle")  
});

app.get("/faq", (req, res)=>{   
    res.render("faq")  
});

app.get("/covid19", (req, res)=>{   
    res.render("particles/covid")   // needed a root for this 
});

app.get("/environmentfaq", (req, res)=>{   
    res.render("particles/environment")  
});

app.get("/general", (req, res)=>{   
    res.render("particles/general")  
});


app.listen(3000, ()=>{console.log("Server started!")}); // port number and feedback when it starts


// SQL 
app.use(express.json()); // the received info will be turned into json to be easier to deal with 
app.use(express.urlencoded({extended: true}));

app.post("/contact",(req, res)=>{    // sending data 
    db.query("INSERT INTO contactus(first_name, forename, email, phone, communicaton_way, query) VALUES(?,?,?,?,?,?)", [req.body.fname, req.body.sname, req.body.email, req.body.phone, req.body.radio, req.body.query],(error, results)=>{
        res.render("aftersubmit", {error:error})
        

    }); // against sql injection, and concealing the error massage as a custom massage

});
//////////////////////////////  stages -> my sql 
const db2 = mysql.createConnection({ // establishing connection
    host: "localhost",
    user: "root",
    password: "",   // on mac sometimes it is root
    database: "line_up"
});
db2.connect(error=>{  // connecting to the database
    if (error) throw error; // if there is an error it will throw an error 
    console.log("MySQL 2 has just started.")
});

app.get("/result", (req, res)=>{
    db2.query("SELECT * FROM lineup ", (error, results) =>{
        res.render("stages", {result: results})
        
    }); // it works on the /result root
  
});


