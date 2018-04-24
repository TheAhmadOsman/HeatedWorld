function readJSON(fileLocation) {
    var parsed;
    parsed = jQuery.get(fileLocation, function (data) {
        localStorage.setItem(fileLocation, data);
    });
}