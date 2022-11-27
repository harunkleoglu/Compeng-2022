$(".version-control").load("Data.txt .version-control");

function startTime() {

    const today = new Date();
    
    let hour = today.getHours();
    let min = today.getMinutes();
    let sec = today.getSeconds();
    
    min = checkTime(min);
    sec = checkTime(sec);

    document.getElementById('dateText').innerHTML = '<h4>' + hour + ":" + min + ":" + sec + '</h4>';
    setTimeout(startTime, 1000);

}

function checkTime(i) {

    if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
    return i;

}