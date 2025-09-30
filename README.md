<html>
<body>

<h1>Financial AI agent</h1>
<hr>
<h2>Description</h2>
<p>At this point the application allows google authentication and gpt requests. You login with you google account (temp: should add the users email to google api + app's postgres manually). Then you are free to make requests to the AI connected to the app. Currently it does not support emails, calendar or Hubspot (unfortunately. Time constraints took their toll). However it is an absolutely functional gpt chat</p>
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
<li><del>auth page (login/password)</del></li>
<li><del>login with Google account</del></li>
<li>login with Hubspot account</li>
<li><del>main page</del></li>
    <ul>
    <li><del>current chat display</del></li>
    <li><del>new chat button</del></li>
    <li><del>list of chats</del></li>
    <li><del>messages display: text, date, extra elements</del></li>
    <li><del>send messages</del></li>
    </ul>
<li><del>exit button</del></li>
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
<li>POST /message/send - sends a message in a specific chat (both message and chat_id are passed in JSON body). Either no redirect (if chat is already opened), or redirect to chat page if the message was first in the chat</li>
</ul>
<p>TODO:</p>
<ul>
<li><del>Basic FastAPI app</del></li>
<li><del>PostgreSQL setup + migrations</del>/li>
<li><del>/login endpoint</del></li>
<li><del>/auth endpoint</del></li>
<li><del>JWT token authorization/authentication</del></li>
<li><del>Google auth</del></li>
<li>Hubspot auth</li>
<li><del>/ endpoint</del></li>
<li><del>/chat/{id} endpoint</del></li>
<li><del>/message/send endpoint</del></li>
<li><del>Real AI responses</del></li>
<li>Use gmail as ai context (unfulfilled due to time constraints)</li>
<li>Use calendar as ai context (unfulfilled due to time constraints)</li>
<li>Use hubspot as ai context (unfulfilled due to time constraints)</li>
</ul>
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
<li>
<p><strong>OPENAI_TOKEN: string</strong></p>
<p>Default value: [empty]</p>
<p>API token for OpenAI. Possibly you can go without it</p>
</li>
<li>
<p><strong>OPENAI_MODEL: string</strong></p>
<p>Default value: gpt-5</p>
<p>OpenAI model to use. If not model is set, gpt-5 will be used by default</p>
</li>
<li>
<p><strong>GOOGLE_CLIENT_ID: string</strong></p>
<p>Your Google Cloud client id for their API access</p>
</li>
<li>
<p><strong>GOOGLE_CLIENT_SECRET: string</strong></p>
<p>Your Google Cloud client secret for their API access</p>
</li>
<li>
<p><strong>GOOGLE_REDIRECT_URL: string</strong></p>
<p>Your own endpoint, where Google auth api should make a callback to</p>
</li>
<li>
<p><strong>SSL_KEY: string</strong></p>
<p>path to ssl key .pem file (for https)</p>
</li>
<li>
<p><strong>SSL_CERT: string</strong></p>
<p>path to ssl certificate .pem file (for https)</p>
</li>
</ul>
</body>
</html>