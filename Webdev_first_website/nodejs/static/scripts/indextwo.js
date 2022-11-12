let s_index = [1,1];
let s_id = ["slides1", "slides2"]
showing_slides (1, 0);
showing_slides (1, 1);
            
function nextOne (n, no) {
    showing_slides (s_index[no] += n, no);
}
            
function showing_slides (n, no) {
    let i;
    let x = document.getElementsByClassName(s_id[no]);
        if (n > x.length) {s_index[no] = 1}    
        if (n < 1) {s_index[no] = x.length}
            for (i = 0; i < x.length; i++) {
                 x[i].style.display = "none";  
              }
              x[s_index[no]-1].style.display = "block";  
}


document.getElementById("cookiebut").addEventListener("click",(e)=>{
    document.getElementById("cookieban").style.display = "none"
});


