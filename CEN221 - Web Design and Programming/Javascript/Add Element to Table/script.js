function addRecord(){
    let id = document.createElement("td");
    let name = document.createElement("td");
    let visa = document.createElement("td");
    let final = document.createElement("td");
    let totalScore = document.createElement("td");
    let del = document.createElement("td");
    let deleteBtn = document.createElement("button");
    
    let total = visascore.value*.4 + finalscore.value*.6; 

    deleteBtn.textContent="Delete";
    del.appendChild(deleteBtn);

    id.textContent = stdid.value;
    name.textContent = stdname.value;
    visa.textContent = visascore.value;
    final.textContent = finalscore.value;
    totalScore.textContent = total;
    
    let row = document.createElement("tr");
    
    row.appendChild(id);
    row.appendChild(name);
    row.appendChild(visa);
    row.appendChild(final);
    row.appendChild(totalScore);
    row.appendChild(del);

    StudentList.appendChild(row);

    stdid.value="";
    stdname.value="";

    stdname.focus();

    deleteBtn.onclick=function(){
        StudentList.removeChild(this.parentNode.parentNode);
    }
}