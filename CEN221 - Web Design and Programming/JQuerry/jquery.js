$(document).ready(function () {
    $("#submitbtn").click(function () {
        let id = document.getElementById("stdid").value;
        let name = document.getElementById("stdname").value;
        let visa = document.getElementById("visascore").value;
        let final = document.getElementById("finalscore").value;
        let total = visa * .4 + final * .6

        let row = "<tr>";

        if (total >= 60) {
            row +=  "<td>" + id + "</td>" +
                    "<td>" + name + "</td>" +
                    "<td>" + visa + "</td>" +
                    "<td>" + final + "</td>" +
                    '<td style="background-color: green;">' + total + "</td>" +
                    "</tr>"
        }
        else {
            row +=  "<td>" + id + "</td>" +
                    "<td>" + name + "</td>" +
                    "<td>" + visa + "</td>" +
                    "<td>" + final + "</td>" +
                    '<td style="background-color: red;">' + total + "</td>" +
                    "</tr>"

        }
        $("table > tbody:last").append(row);

    })
})