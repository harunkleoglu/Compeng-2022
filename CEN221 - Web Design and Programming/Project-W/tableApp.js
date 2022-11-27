$(document).ready(function () {
    $("#bugs").load("Data.txt .table")
    // Add Element to Table
    $("#submitbtn").click(function () {
        const firstname = document.getElementById("firstname").value;
        const lastname = document.getElementById("lastname").value;
        const email = document.getElementById("mail").value;

        const tag = document.createElement("tr");
        tag.className = ""

        const tdcount = document.createElement("td");

        const tdfirst = document.createElement("td");
        tdfirst.innerHTML = firstname;
        const tdlast = document.createElement("td");
        tdlast.innerHTML = lastname;
        const tdmail = document.createElement("td");
        tdmail.innerHTML = email;
        const tdbutton = document.createElement("td");
        tdbutton.className = "text-center"

        const deletebtn = document.createElement("button");
        deletebtn.innerHTML = '<span class="material-symbols-outlined" style="color: white; padding-top: 5px; height: 5px; width: 40px"> delete </span>'
        deletebtn.className = "deleteBtn btn bg-danger btn-sm"
        if (document.getElementById("firstname").value != "" && document.getElementById("lastname").value != "" && document.getElementById("mail").value != "") {
            tag.appendChild(tdfirst);
            tag.appendChild(tdlast);
            tag.appendChild(tdmail);
            tdbutton.appendChild(deletebtn);
            tag.appendChild(tdbutton);
        }
        else{
            if(document.getElementById("firstname").value == ""){
                $("#firstname").animate({fontSize: '+=4px'},300);
                $("#firstname").animate({fontSize: '-=4px'},300);
            }
            if(document.getElementById("lastname").value == ""){
                $("#lastname").animate({fontSize: '+=4px'},300);
                $("#lastname").animate({fontSize: '-=4px'},300);
            }
            if(document.getElementById("mail").value == ""){
                $("#mail").animate({fontSize: '+=4px'},300);
                $("#mail").animate({fontSize: '-=4px'},300);
            }
        }

        elementlist.appendChild(tag);
        // Delete Element from Table
        $(".deleteBtn").click(function () {
            $(this).parent().parent().remove();
        });
    });


});