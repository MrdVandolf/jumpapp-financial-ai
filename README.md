<html>
<body>

<h1>Financial AI agent</h1>
<hr>
<h2>Description: WIP</h2>
<hr>
<h2>Environment</h2>

<ul>
<li>
<p><strong>APP_HOST: string</strong></p>
<p>Default value: localhost</p>
<p>FastAPI application host (backend host)</p>
</li>
<li>
<p><strong>APP_PORT: integer</strong></p>
<p>Default value: 8080</p>
<p>FastAPI application port (backend port)</p>
</li>
<li>
<p><strong>POSTGRES_USER: string</strong></p>
<p>Default value: postgres</p>
<p>PostgreSQL user for backend</p>
</li>
<li>
<p><strong>POSTGRES_PASSWORD: string</strong></p>
<p>Default value: password</p>
<p>PostgreSQL password for backend</p>
</li>
<li>
<p><strong>POSTGRES_HOST: string</strong></p>
<p>Default value: localhost</p>
<p>PostgreSQL host for backend</p>
</li>
<li>
<p><strong>POSTGRES_PORT: integer</strong></p>
<p>Default value: 5432</p>
<p>PostgreSQL port for backend</p>
</li>
<li>
<p><strong>POSTGRES_DB: string</strong></p>
<p>Default value: database</p>
<p>PostgreSQL database name. If no database with this name is found, a new one will be created</p>
</li>
<li>
<p><strong>JWT_KEY: string</strong></p>
<p>Default value: secret</p>
<p>Secret key for JWT tokens</p>
</li>
</ul>


<hr>
<h2>Components</h2>
<hr>
<h3>Frontend</h3>
<p><strong>Stack: HTML, CSS, JS</strong></p>
<p>Features:</p>
<ul>
<li>JWT for sessions</li>
<li>Sessions</li>
<li>chat history must be stored</li>
<li>allow only Google/Hubspot accounts to register</li>
</ul>
<p>TODO:</p>
<ul>
<li>auth page (login/password)</li>
<li>login/register with Google account</li>
<li>login/register with Hubspot account</li>
<li>main page</li>
    <ul>
    <li>current chat display</li>
    <li>new chat button</li>
    <li>list of chats</li>
    <li>messages display: text, date, extra elements</li>
    <li>send messages</li>
    </ul>
<li>exit button</li>
</ul>
<hr>
<h3>Backend (web)</h3>
<p><strong>Stack: Python (3.11), FastAPI, PostgreSQL</strong></p>
<p>Features:</p>
<ul>
<li>JWT tokens for sessions (stored in cookies)</li>
<li>Auth check on ANY page/endpoint</li>
<li>PostgreSQL for storage: users, chats, chat_history, more (?)</li>
<li>Google auth</li>
<li>Hubspot auth</li>
<li>Auto-redirect to /login if unauthorized</li>
</ul>
<p>Endpoints:</p>
<ul>
<li>GET / - main page - returns a list of chats the user had</li>
<li>GET /login - login page - provides a form to login (username/Google/Hubspot)</li>
<li>POST /auth - login attempt - passes username/email + sha_256 (?) password. Redirects to main page on success</li>
<li>GET /chat/{id} - opens one specific chat user previously had</li>
<li>POST /chat/new - creates a new empty chat for user with an {id}. Redirects to /chat/{id} on success</li>
<li>POST /chat/send - sends a message in a specific chat (both message and chat_id are passed in JSON body). No redirect, but message and answer both appear on the current page</li>
</ul>
<p>TODO:</p>
<ul>
<li>Basic FastAPI app</li>
<li>PostgreSQL setup + migrations</li>
<li>/login endpoint</li>
<li>/auth endpoint</li>
<li>JWT token authorization/authentication</li>
<li>Google auth</li>
<li>Hubspot auth</li>
<li>/ endpoint</li>
<li>/chat/{id} endpoint</li>
<li>/chat/send endpoint</li>
<li>/chat/new endpoint</li>
<li>Mock AI responses</li>
</ul>
</body>
</html>