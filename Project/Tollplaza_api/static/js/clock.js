
function startTime() {
	var monthno = new Array("01","02","03","04","05","06","07","08","09","10","11","12");
    var today = new Date();
    var day = today.get
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    "Date/Time" + ":"+ " " + today.getDate() + "/" +monthno[today.getMonth()] + "/" + today.getFullYear()+ " " + "["+ h + ":" + m + ":" + s +"]";
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}
 
function myFunction() {
    window.print();
}

function isFutureDate(idate){
	
    var today = new Date().getTime(),
        idate = idate.split("/");
    
    idate = new Date(idate[2], idate[1] - 1, idate[0]).getTime();
    return (today - idate) < 0 ? true : false;
}
function checkDate(dat){
    //alert(dat)
    var idate = document.getElementById(dat),
        resultDiv = document.getElementById("datewarn"),
        dateReg = /(0[1-9]|[12][0-9]|3[01])[\/](0[1-9]|1[012])[\/]201[4-9]|20[2-9][0-9]/;
    
	
	
    if(dateReg.test(idate.value)){
        if(isFutureDate(idate.value)){
            
           idate.style.background = "#99ff99";
        } else {
            
            idate.style.background = "#ff4d4d";
        }
    } else {
        
        idate.style.background = "#ff4d4d";
    }
}

