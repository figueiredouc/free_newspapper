document.getElementById('url-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário
  
    const url = document.getElementById('url-input').value;
  
    if (!url) {
      alert('Please enter a valid URL');
      return;
    }
  
    // Fazendo o pedido à API
    fetch('http://127.0.0.1:5000/fetch-html', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        document.getElementById('html-output').textContent = `Error: ${data.error}`;
      } else {
        const newWindow = window.open('', '_blank');
        newWindow.document.write(data.html); 
        newWindow.document.close(); 
      }
  
      // Mostra a área de resultado na página original
      document.getElementById('result').style.display = 'block';
    })
    .catch(error => {
      document.getElementById('html-output').textContent = `Error: ${error}`;
      document.getElementById('result').style.display = 'block';
    });
  });
  