function getFormData(formId) {
    const form = document.getElementById(formId);
    const formData = new FormData(form);
    return Object.fromEntries(formData.entries());
}

function createClient(event) {
    event.preventDefault();
    const data = getFormData('create-client-form');
    const apiKey = data.apiKey; 

    fetch('/create_client', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey 
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json().then(data => ({ status: response.status, body: data })))
    .then(({ status, body }) => {
        const resultDiv = document.getElementById('create-client-result');
        if (status === 201) {
            resultDiv.textContent = 'Client created successfully: ' + JSON.stringify(body);
        } else {
            resultDiv.textContent = 'Error creating client: ' + JSON.stringify(body);
        }
    })
    .catch(error => {
        const resultDiv = document.getElementById('create-client-result');
        resultDiv.textContent = `Error creating client: ${error.message}`;
    });
}

document.getElementById('create-client-form').addEventListener('submit', createClient);

document.getElementById('update-client-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let clientName = document.getElementById('update-client-name').value;
    let updatedClientName = document.getElementById('updated-client-name').value;
    let providers = document.getElementById('update-providers').value.split(',');

    fetch(`/update_client/${clientName}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            client: updatedClientName,
            providers: providers
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => console.error('Error:', error));
});

document.addEventListener('DOMContentLoaded', function() {
    function getClient(event) {
        event.preventDefault();
        const clientName = document.getElementById('get-client-name').value;
        const apiKey = document.getElementById('api-key').value;
        fetch(`/signingClient/${encodeURIComponent(clientName)}`, {
            method: 'GET',
            headers: { 
                'Content-Type': 'application/json',
                'x-api-key': apiKey
            }
        })
        .then(response => response.json().then(data => ({ status: response.status, body: data })))
        .then(({ status, body }) => {
            const resultDiv = document.getElementById('get-client-result');
            if (status === 200) {
                resultDiv.textContent = 'Client information: ' + JSON.stringify(body);
            } else {
                resultDiv.textContent = 'Error getting client information: ' + JSON.stringify(body);
            }
        })
        .catch(error => {
            const resultDiv = document.getElementById('get-client-result');
            resultDiv.textContent = `Error getting client information: ${error.message}`;
        });
    }

    const getClientForm = document.getElementById('get-client-form');
    if (getClientForm) {
        getClientForm.addEventListener('submit', getClient);
    } else {
        console.error("Form with id 'get-client-form' not found");
    }
});