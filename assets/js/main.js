document.getElementById('registr').addEventListener('submit', async function (event) {
    event.preventDefault(); 

    const formData = new FormData(this);
    formData.append('action', 'login');

    const status = document.getElementById('status'); 
    try {
      
        const response = await fetch('./temp/function.php', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.text();
            status.textContent = 'Данные успешно отправлены: ' + result;
            status.style.color = 'green';
        } else {
            throw new Error('Ошибка при отправке данных.');
        }
    } catch (error) {

        status.textContent = 'Ошибка: ' + error.message;
        status.style.color = 'red';
    }
});