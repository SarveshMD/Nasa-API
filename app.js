document.querySelector("#main_image").src = vars.hdurl;
document.querySelector("#image_anchor").href = vars.hdurl;
document.getElementById("date").innerHTML = vars.date;
document.getElementById("img_title").innerHTML = vars.title;
document.getElementById("explanation").innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + vars.explanation;

cpright = vars.copyright;
document.getElementById("copyright").innerHTML = vars.year + " " + cpright;

