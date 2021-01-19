document.querySelector("#main_image").src = vars.url;
document.querySelector("#image_anchor").href = vars.url;
document.getElementById("date").innerHTML = vars.date;
document.getElementById("img_title").innerHTML = vars.title;
document.getElementById("explanation").innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + vars.explanation;
document.getElementById("switch").innerHTML = "Switch to HD Image";

var tracker = 0;
document.querySelector("#switch").addEventListener("click", function(){
	if (tracker % 2 == 0) {
		document.querySelector("#main_image").src = vars.hdurl;
		document.querySelector("#image_anchor").href = vars.hdurl;
		document.getElementById("switch").innerHTML = "Switch to Normal Image";
	}
	if (tracker %2 == 1) {
		document.querySelector("#main_image").src = vars.url;
		document.querySelector("#image_anchor").href = vars.url;
		document.getElementById("switch").innerHTML = "Switch to HD Image";
	}
	tracker++;
})
cpright = vars.copyright;
document.getElementById("copyright").innerHTML = vars.year + " " + cpright;

