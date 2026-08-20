document.addEventListener('DOMContentLoaded', () => {
    // State
    let currentMode = 'explain';
    let isStreaming = false;
    
    // DOM Elements
    const courseSelect = document.getElementById('course-select');
    const modeButtons = document.querySelectorAll('.mode-btn');
    const chatMessages = document.getElementById('chat-messages');
    const questionInput = document.getElementById('question-input');
    const sendBtn = document.getElementById('send-btn');
    
    // Configure marked.js for secure rendering if needed, 
    // basic config is fine for now.
    
    // Initialize
    loadCourses();
    
    // Event Listeners
    modeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            if (isStreaming) return;
            setMode(btn.dataset.value);
        });
    });
    
    sendBtn.addEventListener('click', sendMessage);
    
    questionInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    questionInput.addEventListener('input', () => {
        sendBtn.disabled = questionInput.value.trim() === '' || isStreaming;
    });
    
    // Functions
    async function loadCourses() {
        try {
            const response = await fetch('/api/courses');
            if (response.ok) {
                const data = await response.json();
                if (data.courses && data.courses.length > 0) {
                    courseSelect.innerHTML = ''; // Clear default
                    data.courses.forEach(course => {
                        const option = document.createElement('option');
                        option.value = course;
                        option.textContent = course;
                        courseSelect.appendChild(option);
                    });
                }
            }
        } catch (error) {
            console.error('Failed to load courses:', error);
        }
    }
    
    function setMode(mode) {
        currentMode = mode;
        modeButtons.forEach(btn => {
            if (btn.dataset.value === mode) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }
    
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function getTypingIndicatorHTML() {
        return `
            <div class="typing-indicator">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        `;
    }
    
    async function sendMessage() {
        const question = questionInput.value.trim();
        if (!question || isStreaming) return;
        
        const course = courseSelect.value;
        
        // Reset input
        questionInput.value = '';
        sendBtn.disabled = true;
        isStreaming = true;
        
        // Add User message
        addUserMessage(question);
        
        // Add Assistant container with typing indicator
        const assistantMsgEl = createAssistantMessageContainer();
        const contentEl = assistantMsgEl.querySelector('.message-content');
        
        scrollToBottom();
        
        try {
            const response = await fetch('/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question, course, mode: currentMode })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            let buffer = '';
            let fullContent = '';
            
            // Remove typing indicator before first token
            let isFirstToken = true;
            
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                
                buffer += decoder.decode(value, { stream: true });
                const lines = buffer.split('\n');
                
                // Keep the last incomplete line in buffer
                buffer = lines.pop(); 
                
                let currentEvent = 'message';
                
                for (const line of lines) {
                    if (line.trim() === '') continue;
                    
                    if (line.startsWith('event: ')) {
                        currentEvent = line.slice(7).trim();
                        continue;
                    }
                    
                    if (line.startsWith('data: ')) {
                        const dataStr = line.slice(6);
                        
                        try {
                            const data = JSON.parse(dataStr);
                            
                            if (currentEvent === 'token') {
                                if (isFirstToken) {
                                    contentEl.innerHTML = '';
                                    isFirstToken = false;
                                }
                                fullContent += data.token;
                                
                                // Render markdown with streaming dot
                                const parsedHTML = marked.parse(fullContent);
                                contentEl.innerHTML = parsedHTML + '<span class="streaming-dot"></span>';
                                
                                // Apply syntax highlighting
                                contentEl.querySelectorAll('pre code').forEach((block) => {
                                    hljs.highlightElement(block);
                                });
                                
                                scrollToBottom();
                            } 
                            else if (currentEvent === 'sources') {
                                renderSources(assistantMsgEl, data.sources);
                                scrollToBottom();
                            }
                            else if (currentEvent === 'error') {
                                if (isFirstToken) contentEl.innerHTML = '';
                                contentEl.innerHTML += `<p style="color: #ef4444;">Error: ${data.error}</p>`;
                                scrollToBottom();
                            }
                            else if (currentEvent === 'done') {
                                // Final render without streaming dot
                                contentEl.innerHTML = marked.parse(fullContent);
                                contentEl.querySelectorAll('pre code').forEach((block) => {
                                    hljs.highlightElement(block);
                                });
                            }
                        } catch (e) {
                            console.error('Error parsing SSE data:', e, dataStr);
                        }
                    }
                }
            }
            
            // Just in case it finishes without a done event
            const dot = contentEl.querySelector('.streaming-dot');
            if (dot) dot.remove();
            
        } catch (error) {
            console.error('Fetch error:', error);
            contentEl.innerHTML = `<p style="color: #ef4444;">Connection error. Please try again.</p>`;
        } finally {
            isStreaming = false;
            sendBtn.disabled = questionInput.value.trim() === '';
            questionInput.focus();
            scrollToBottom();
        }
    }
    
    function addUserMessage(text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message user';
        msgDiv.innerHTML = `
            <div class="message-bubble">
                <div class="message-content">
                    <p>${escapeHTML(text)}</p>
                </div>
            </div>
        `;
        chatMessages.appendChild(msgDiv);
    }
    
    function createAssistantMessageContainer() {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message assistant';
        msgDiv.innerHTML = `
            <div class="message-bubble">
                <div class="message-content">
                    ${getTypingIndicatorHTML()}
                </div>
            </div>
        `;
        chatMessages.appendChild(msgDiv);
        return msgDiv;
    }
    
    function renderSources(messageEl, sources) {
        if (!sources || sources.length === 0) return;
        
        const sourcesContainer = document.createElement('div');
        sourcesContainer.className = 'sources-container';
        
        sources.forEach(source => {
            const card = document.createElement('div');
            card.className = 'source-card';
            
            const simPercentage = Math.round((source.similarity || 0) * 100);
            
            card.innerHTML = `
                <span class="source-label">${escapeHTML(source.label || 'Document')}</span>
                <span class="source-sim">${simPercentage}%</span>
            `;
            
            sourcesContainer.appendChild(card);
        });
        
        messageEl.appendChild(sourcesContainer);
    }
    
    function escapeHTML(str) {
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }
});
