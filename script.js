
function sortObject(o) {
    var sorted = {},
    key, a = [];

    for (key in o) {
	if (o.hasOwnProperty(key)) {
	    a.push(key);
	    }
    }

    a.sort();

    for (key = 0; key < a.length; key++) {
	sorted[a[key]] = o[a[key]];
    }
    return sorted;
}

function Div(cl, html) {
    var d = document.createElement("div");
    d.setAttribute("class", cl);
    if(html != undefined)
	d.innerHTML = html;
    return d;
}

function render() {
    var key, vid, list = document.getElementById("list");
    movies = sortObject(movies);
    list.innerHTML = "";
    for(key in movies) {
	vid = document.createElement("a");
	vid.setAttribute("class", "video");
	vid.setAttribute("href", (movies[key]["path"] + "/" + movies[key]["file"])); 

	if(movies[key]["art"])
	    vid.appendChild(new Div("art", '<img src="' + movies[key]["path"] + "/" + movies[key]["art"] + '">'))
	else
	    vid.appendChild(new Div("art", '<img src="./default.jpg">'))
	vid.appendChild(new Div("title", movies[key]["title"]))
	
	list.appendChild(vid);
    }
}


$(document).ready(function() {
    render();
});

