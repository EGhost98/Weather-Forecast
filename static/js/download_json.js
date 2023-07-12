const Wea_Data = JSON.parse("{{ raw_json|escapejs }}");

// Function to download the JSON file
function downloadJSON(filename, text) {
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

// Attach click event listener to the download button
document.getElementById("downloadButton").addEventListener("click", function() {
    downloadJSON("weather_forecast.json", JSON.stringify(Wea_Data, null, 2));
});
