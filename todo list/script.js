var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");
var li = document.getElementsByTagName("li");
var deletable = document.getElementsByClassName("delete");

function inputLength(){
	return input.value.length;
}

function createListElement(){
	var li = document.createElement("li");
	li.appendChild(document.createTextNode(input.value));
	
	var deleteButton = document.createElement("button");
	deleteButton.setAttribute("class", "delete");
	deleteButton.appendChild(document.createTextNode("Delete!"));
	li.appendChild(deleteButton);
	ul.appendChild(li);
	input.value = "";

}


function addListAfterClick() {
	if (inputLength() !== 0){
		createListElement();
	}
}

function addListAfterKeypress(event) {
	if (inputLength() !== 0 && event.keyCode === 13){
		createListElement();
	}
}

function done(event) {
	event.target.classList.toggle("done");
}


function createDeleteButton(){
	for (let i = 0; i < li.length; i++){
		var deleteButton = document.createElement("button");
		deleteButton.setAttribute("class", "delete");
		deleteButton.appendChild(document.createTextNode("Delete!"));
		li[i].appendChild(deleteButton);
	}
}


function clicked(event){
	if (event.target.className === "delete"){
		event.target.parentElement.remove();
	}
	else {
		event.target.classList.toggle("done");
	}
}


createDeleteButton();
button.addEventListener("click", addListAfterClick);
input.addEventListener("keypress", addListAfterKeypress);
ul.addEventListener("click", clicked);





