<h1>🍽️ API de Restaurantes — FastAPI, OOP e Consumo de API Externa</h1>

<p>
Este projeto é uma API construída com <strong>FastAPI</strong>, aplicando conceitos de 
<strong>Python Orientado a Objetos</strong>, <strong>consumo de API externa</strong>, 
<strong>tratamento de dados JSON</strong> e <strong>persistência local</strong>.
</p>

<ul>
  <li>✔️ Listar todos os restaurantes disponíveis</li>
  <li>✔️ Visualizar o cardápio de um restaurante específico</li>
  <li>✔️ Enviar avaliações (nota + comentário)</li>
  <li>✔️ Listar avaliações salvas para cada restaurante</li>
  <li>✔️ Organizar regras de negócio usando Service Layer</li>
</ul>

<hr/>

<h2>🚀 Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.10+</li>
  <li>FastAPI</li>
  <li>Uvicorn</li>
  <li>Requests</li>
  <li>JSON como armazenamento local</li>
  <li>Programação Orientada a Objetos (OOP)</li>
</ul>

<hr/>

<h2>📁 Estrutura do Projeto</h2>

<pre>
restaurantes_api/
│
├── main.py
├── services/
│     └── restaurante_service.py
│
└── database/
      └── avaliacoes.json
</pre>

<hr/>

<h2>🔄 Endpoints da API</h2>

<h3>1️⃣ Listar todos os restaurantes</h3>
<p><strong>Método:</strong> GET</p>
<pre>/api/restaurantes/</pre>

<h3>2️⃣ Listar cardápio de um restaurante</h3>
<p><strong>Método:</strong> GET</p>
<pre>/api/restaurantes/{nome}</pre>
<p><strong>Retorno:</strong></p>
<ul>
  <li>item</li>
  <li>price</li>
  <li>description</li>
</ul>

<h3>3️⃣ Enviar avaliação do restaurante</h3>
<p><strong>Método:</strong> POST</p>
<pre>/api/restaurantes/{nome}/avaliar?nota=4.5&amp;comentario=Muito+bom</pre>
<p>As avaliações são salvas no arquivo:</p>
<pre>database/avaliacoes.json</pre>

<h3>4️⃣ Listar avaliações do restaurante</h3>
<p><strong>Método:</strong> GET</p>
<pre>/api/restaurantes/{nome}/avaliacoes</pre>

<hr/>

<h2>🧠 Conceitos Aplicados</h2>
<ul>
  <li>Leitura e escrita em arquivos JSON</li>
  <li>Consumo de API externa com <code>requests</code></li>
  <li>Encapsulamento da lógica de negócio (Service Layer)</li>
  <li>Path Parameters e Query Parameters no FastAPI</li>
  <li>Retorno estruturado em formato JSON</li>
  <li>Boas práticas de organização de projeto backend</li>
</ul>

<hr/>

<h2>▶️ Como Executar o Projeto</h2>

<h3>1. Criar o ambiente virtual</h3>
<pre><code>python3 -m venv venv</code></pre>

<h3>2. Ativar o ambiente</h3>
<p><strong>Linux / Mac:</strong></p>
<pre><code>source venv/bin/activate</code></pre>
<p><strong>Windows:</strong></p>
<pre><code>venv\Scripts\activate</code></pre>

<h3>3. Instalar dependências</h3>
<pre><code>pip install fastapi uvicorn requests</code></pre>

<h3>4. Executar o servidor</h3>
<pre><code>uvicorn main:app --reload</code></pre>

<h3>5. Acessar a documentação automática</h3>
<ul>
  <li>Swagger UI: <code>http://127.0.0.1:8000/docs</code></li>
</ul>

<hr/>

<h2>📌 Melhorias Futuras (To-Do)</h2>
<ul>
  <li>Autenticação de usuários</li>
  <li>Banco de dados SQLite / PostgreSQL</li>
  <li>Paginação de cardápios</li>
  <li>Filtro por preço/categoria</li>
  <li>Upload de imagens</li>
  <li>Testes automatizados (pytest)</li>
</ul>

<hr/>

<h2>👨‍💻 Autor</h2>
<p>
<strong>Lucas André</strong> — Desenvolvedor Backend em formação<br/>
Apaixonado por Python, APIs, dados e construção de produtos.
</p>
