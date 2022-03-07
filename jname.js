function addfield(){
    var a=document.getElementById("tabfield").value;
    var tab=document.getElementById("selfield");
    var row=document.createElement("tr");
    var rdata=document.createElement("td");
    var rtext=document.createTextNode(a);
    rdata.append(rtext);
    row.append(rdata);
    tab.append(row);
    }
    document.getElementById("btn").addEventListener("click",addfield);
