// function readJSON(fileLocation){
//    var request = new XMLHttpRequest();
//    request.open("GET", fileLocation, false)
//    request.send(null)
//    var my_JSON_object = JSON.parse(request.responseText)
// }
// function readJSON(file, callback) {
//     var rawFile = new XMLHttpRequest();
//     rawFile.overrideMimeType("application/json");
//     rawFile.open("GET", file, true);
//     rawFile.onreadystatechange = function() {
//         if (rawFile.readyState === 4 && rawFile.status == "200") {
//             callback(rawFile.responseText);
//         }
//     }
//     rawFile.send(null);
// }

// //usage:
// readTextFile("../data.json", function(text){
//     var data = JSON.parse(text);
//     console.log(data);
// });
function readJSON(fileLocation){
	var parsed
	parsed = jQuery.get(fileLocation, function(data) {
		localStorage.setItem(fileLocation, data)
	    //return parsed
	});
}