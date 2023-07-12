document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('toggle-api-key');
    var apiKeyField = document.getElementById('api-key-field');

    toggleButton.addEventListener('click', function() {
        if (apiKeyField.style.display === 'none') {
            apiKeyField.style.display = 'block';
        } else {
            apiKeyField.style.display = 'none';
        }
    });
});