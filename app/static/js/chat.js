document.addEventListener('DOMContentLoaded', function () {
    const socket = io();
    const userInput = document.getElementById('user-input');
    const submitButton = document.getElementById('submit-button');
    const resetButton = document.getElementById('reset-button');
    const modelSelect = document.getElementById('model-select');
    const promptSelect = document.getElementById('prompt-select');
    const markdownView = document.getElementById('markdown-view');
    const formattedView = document.getElementById('formatted-view');
    const viewToggle = document.getElementById('view-toggle');
    const copyButton = document.getElementById('copy-button');

    let currentResponse = '';
    let isFormattedView = false;
    let currentSystemPrompt = '';

    // --- Event Listeners ---
    promptSelect.addEventListener('change', (e) => {
        currentSystemPrompt = e.target.value;
        userInput.focus();
    });

    submitButton.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            markdownView.textContent = 'Thinking...';
            formattedView.innerHTML = '';
            currentResponse = '';
            socket.emit('send_message', {
                message: userMessage,
                system_prompt: currentSystemPrompt,
                model: modelSelect.value
            });
        }
    });

    resetButton.addEventListener('click', () => {
        userInput.value = '';
        markdownView.textContent = '';
        formattedView.innerHTML = '';
        currentResponse = '';
        userInput.style.height = 'auto'; // Reset height
        userInput.focus();
    });

    viewToggle.addEventListener('click', () => {
        isFormattedView = !isFormattedView;
        updateView();
    });

    copyButton.addEventListener('click', () => {
        if (currentResponse) {
            navigator.clipboard.writeText(currentResponse).then(() => {
                copyButton.textContent = 'Copied!';
                setTimeout(() => { copyButton.textContent = 'Copy Markdown'; }, 2000);
            });
        }
    });

    // Auto-resize textarea
    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    // Handle keydown for Cmd/Ctrl+Enter to submit
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) {
            e.preventDefault();
            submitButton.click();
        }
    });

    // --- SocketIO Handlers ---
    socket.on('connect', () => console.log('Connected to server.'));
    socket.on('ai_response', (data) => {
        currentResponse = data.response;
        updateView();
    });

    // --- Helper Functions ---
    function addCopyButtons() {
        formattedView.querySelectorAll('div.codehilite').forEach(function(div) {
            var btn = document.createElement('button');
            btn.className = 'copy-btn';
            btn.innerText = 'Copy';
            btn.onclick = function() {
                var code = div.querySelector('pre').innerText;
                navigator.clipboard.writeText(code)
                    .then(() => {
                        btn.innerText = "Copied!";
                        setTimeout(() => btn.innerText = "Copy", 2000);
                    });
            };
            div.appendChild(btn);
        });
    }

    function updateView() {
        if (isFormattedView) {
            markdownView.style.display = 'none';
            formattedView.style.display = 'block';
            formattedView.classList.add('formatted-content');
            viewToggle.textContent = 'Show Markdown';

            fetch('/render_markdown', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: currentResponse })
            })
            .then(response => response.json())
            .then(data => {
                formattedView.innerHTML = data.html;
                addCopyButtons(); // Add buttons after content is rendered
            });

        } else {
            markdownView.style.display = 'block';
            formattedView.style.display = 'none';
            markdownView.textContent = currentResponse;
            formattedView.classList.remove('formatted-content');
            viewToggle.textContent = 'Show Formatted';
        }
    }

    // --- Page Initialization ---
    if (promptSelect.options.length > 0) {
        currentSystemPrompt = promptSelect.options[0].value;
    }
});
