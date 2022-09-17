var image1 = document.getElementById("image1");

image1.addEventListener("mouseover", function(){
	this.style = "box-shadow:2px 2px 2px grey";
})
image1.addEventListener("mouseout", function(){
	this.style = "";
})


var image2 = document.getElementById("image2");

image2.addEventListener("mouseover", function(){
	this.style = "box-shadow:2px 2px 2px grey";
})
image2.addEventListener("mouseout", function(){
	this.style = "";
})


var image3 = document.getElementById("image3");

image3.addEventListener("mouseover", function(){
	this.style = "box-shadow:2px 2px 2px grey";
})
image3.addEventListener("mouseout", function(){
	this.style = "";
})


var button1 = document.getElementById("button1");
button1.addEventListener("click", function(){
	document.write(input1)
	phoneNumber = number.value;
	if (this.value != String){
		document.write("Working")
	}
})

