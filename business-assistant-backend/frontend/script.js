// Навигация между страницами
document.querySelectorAll('.nav-btn').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        this.classList.add('active');
        
        document.querySelectorAll('.page').forEach(page => {
            page.classList.remove('active');
        });
        
        const pageId = this.getAttribute('data-page');
        document.getElementById(pageId).classList.add('active');
    });
});

let messageHistory = [];

async function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    
    if (!message) return;

    // Блокируем интерфейс на время запроса
    input.disabled = true;
    document.querySelector('.input-area button').disabled = true;
    
    addMessage(message, 'user');
    input.value = '';
    
    messageHistory.push({
        text: message,
        sender: 'user',
        timestamp: new Date().toLocaleString()
    });
    
    // Показываем индикатор "печатает"
    const typingIndicator = document.createElement('div');
    typingIndicator.className = 'message bot typing-indicator';
    typingIndicator.innerHTML = '<em>🤖 Помощник печатает...</em>';
    document.getElementById('messages').appendChild(typingIndicator);
    document.getElementById('messages').scrollTop = document.getElementById('messages').scrollHeight;
    
    try {
        // ★ РЕАЛЬНЫЙ ВЫЗОВ ВАШЕГО API ★
        const response = await fetch('http://localhost:8000/api/v1/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: message,
                user_id: 1
            })
        });
        
        // Убираем индикатор
        typingIndicator.remove();
        
        if (response.ok) {
            const data = await response.json();
            const aiResponse = data.answer;
            addMessage(aiResponse, 'bot');
            
            messageHistory.push({
                text: aiResponse,
                sender: 'bot', 
                timestamp: new Date().toLocaleString()
            });
        } else {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
    } catch (error) {
        typingIndicator.remove();
        console.error('Error:', error);
        addMessage('❌ Ошибка подключения к серверу. Убедитесь, что бэкенд запущен на localhost:8000', 'bot');
        
        messageHistory.push({
            text: 'Ошибка соединения',
            sender: 'system', 
            timestamp: new Date().toLocaleString()
        });
    } finally {
        // Разблокируем интерфейс
        input.disabled = false;
        document.querySelector('.input-area button').disabled = false;
        input.focus();
    }
    
    updateHistoryPage();
}

function addMessage(text, sender) {
    const messagesContainer = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.innerHTML = `<strong>${sender === 'user' ? '👤 Вы' : '🤖 Бизнес-помощник'}:</strong> ${text}`;
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

document.querySelectorAll('.action-btn').forEach(button => {
    button.addEventListener('click', function() {
        const question = this.getAttribute('data-question');
        document.getElementById('messageInput').value = question;
        
        document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelector('[data-page="chat"]').classList.add('active');
        document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
        document.getElementById('chat').classList.add('active');
        
        setTimeout(() => sendMessage(), 500);
    });
});

function updateHistoryPage() {
    const historyList = document.getElementById('historyList');
    historyList.innerHTML = '';
    
    messageHistory.slice().reverse().forEach(msg => {
        const historyItem = document.createElement('div');
        historyItem.className = 'stat-card';
        historyItem.innerHTML = `
            <p><strong>${msg.sender === 'user' ? 'Вы' : 'Помощник'}:</strong> ${msg.text}</p>
            <small>${msg.timestamp}</small>
        `;
        historyList.appendChild(historyItem);
    });
}

document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

updateHistoryPage();