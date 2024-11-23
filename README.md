<h1><b>Trending Keyword-Based Natural Language Generation</b></h1>

<p>
  <a href="https://www.linkedin.com/feed/update/urn:li:activity:7265881345527037952">
    <b>Read the original LinkedIn post about this project</b>
  </a>
</p>

---

<h2><b>Overview</b></h2>

<p>
  This project demonstrates how to generate realistic, topic-focused text by:
</p>
<ul>
  <li>Identifying <b>trending technology keywords</b></li>
  <li>Analyzing related <b>academic abstracts</b> for popular subtopics</li>
  <li>Using <b>GPT-4</b> to create cohesive blog posts</li>
</ul>
<p>
  The approach incorporates <b>keyword analysis</b>, <b>academic research</b>, and <b>advanced language modeling</b> to produce well-rounded, informative content.
</p>

---

<h2><b>Features</b></h2>

<ul>
  <li><b>Topic Selection</b><br>
      Automatically selects a trending technology topic using predefined(for now) or (tbd)fetched data.</li>
  <li><b>Keyword Extraction</b><br>
      Analyzes abstracts from academic papers to extract the most relevant subtopics.</li>
  <li><b>Content Generation</b><br>
      Uses GPT-4 to generate blog posts based on selected keywords and retrieved context.</li>
  <li><b>Visualization</b><br>
      Creates a <b>word cloud</b> to visualize the most popular keywords extracted from the research.</li>
  <li><b>Contextual Data Integration</b><br>
      Incorporates <b>Retrieval-Augmented Generation (RAG)</b> principles to enrich the content with accurate, up-to-date information.</li>
</ul>

---

<h2><b>Dependencies</b></h2>

<p>Before running the code, ensure you have the following libraries installed:</p>
<ul>
  <li><code>openai</code>: For GPT-based text generation</li>
  <li><code>langchain</code>: For orchestrating the data processing pipeline</li>
  <li><code>pandas</code>: For keyword analysis</li>
  <li><code>spacy</code>: For natural language processing and keyword extraction</li>
  <li><code>matplotlib</code>: For keyword visualization</li>
  <li><code>wordcloud</code>: For generating keyword word clouds</li>
  <li><code>pinecone-client</code>: For setting up a vector database (if RAG is used)</li>
</ul>

<p>Install the required packages using:</p>

<pre><code>pip install openai langchain pandas spacy matplotlib wordcloud pinecone-client</code></pre>

---

<h2><b>Usage</b></h2>

<h3><b>1. Configure API Keys</b></h3>
<ul>
  <li>Set your <b>OpenAI API key</b> for GPT-4 generation.</li>
  <li>Configure your <b>Pinecone API key and environment</b> if using RAG for contextual retrieval.</li>
</ul>

<h3><b>2. Run the Script</b></h3>
<p>Execute the script to:</p>
<ul>
  <li>Fetch trending topics.</li>
  <li>Analyze academic abstracts for popular subtopics.</li>
  <li>Generate a blog post based on a chosen keyword.</li>
</ul>

<pre><code>python trending_keyword_nlg.py</code></pre>

<h3><b>3. View Results</b></h3>
<ul>
  <li>A <b>word cloud</b> will visualize the extracted keywords.</li>
  <li>The generated <b>blog post</b> will be printed to the console and saved as a text file.</li>
</ul>

---

<h2><b>Example Workflow</b></h2>

<ol>
  <li>The script selects "Artificial Intelligence" as the trending topic.</li>
  <li>Retrieves academic abstracts related to "Artificial Intelligence."</li>
  <li>Analyzes abstracts to identify keywords, such as <b>"Winograd Schemas."</b></li>
  <li>Uses GPT-4 to generate a blog post titled <b>"An Introduction to Winograd Schemas."</b></li>
  <li>Saves the output to <code>winograd_blog_post.txt</code>.</li>
</ol>

---

<h2><b>Future Enhancements</b></h2>

<ul>
  <li>Add real-time trending topic extraction using news or social media APIs.</li>
  <li>Automate deployment with cloud-based pipelines (e.g., Azure, AWS, Databricks).</li>
  <li>Enhance contextual retrieval with a graph-backed RAG pipeline for richer content.</li>
</ul>

---

<h2><b>References</b></h2>

<ul>
  <li>
    <b>Original LinkedIn Post:</b>
    <a href="https://www.linkedin.com/feed/update/urn:li:activity:7265881345527037952">
      Natural Language Generation Using Trending Keywords
    </a>
  </li>
</ul>
