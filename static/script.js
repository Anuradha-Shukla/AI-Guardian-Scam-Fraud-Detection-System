document.getElementById("scanBtn").onclick = function(){

document.getElementById("status").innerText="Scanning message...";

setTimeout(function(){
document.getElementById("status").innerText="Analyzing keywords...";
},1000);

setTimeout(function(){
document.getElementById("status").innerText="Running AI model...";
},2000);

}