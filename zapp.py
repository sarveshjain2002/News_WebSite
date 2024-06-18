import streamlit as st

# Define HTML, CSS, and JavaScript code
custom_html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>TrendyTechnieNews-by Sarvesh Udapurkar</title>
    <style>
        body { background-color: #f8f9fa; }
        .navbar-nav .nav-link {
            color: #fff !important;
            font-size: 16px;
            font-family: "Arial", Verdana, Tahoma, sans-serif;
        }
        .navbar { background-color: #343a40 !important; }
        .navbar-brand { font-size: 30px; }
        .nav-link { border-radius: 10px; padding: 8px 20px; margin: 10px; transition: background-color 0.3s ease; }
        .nav-link:hover { background-color: #e1800a; border-radius: 5px 20px 5px 20px; color: #fff; }
        .navbar-toggler { border: none; color: #fff; }
        .form-control { border-radius: 8px; }
        .navbar-brand .hover-effect:hover { color: #f27e12; background-color: #f5cd67; border-radius: 5px 20px 5px 20px; padding: 5px 8px 5px 5px; }
        #newsType { margin-bottom: 20px; }
        #newsdetails .card { border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); transition: box-shadow 0.3s ease; }
        #newsdetails .card:hover { box-shadow: 0 0 20px rgba(0, 0, 0, 0.3); }
        #newsdetails .card-title { font-size: 18px; font-weight: bold; margin-bottom: 10px; }
        #newsdetails .text-primary { color: #007bff; font-size: 14px; margin-bottom: 5px; }
        #newsdetails .text-muted { font-size: 14px; margin-bottom: 10px; }
        #newsdetails .btn-dark { background-color: #343a40; color: #fff; border: none; border-radius: 20px; padding: 5px 15px; font-size: 14px; transition: background-color 0.3s ease; }
        #newsdetails .btn-dark:hover { background-color: #23272b; }
        .mt-5 { background-color: #343a40; padding: 20px 0; }
        .mt-5 .navbar { background-color: transparent !important; }
        .mt-5 .navbar h5 { font-size: 20px; color: #fff; }
        .mt-5 .container-fluid h6 { color: #fff; margin-top: 10px; }
    </style>
</head>
<body class="m-0 p-0">
    <div class="container-fluid m-0 p-0">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand text-warning" href="#">
                    <span class="hover-effect" style="margin-right: 50px;">TrendyTechnieNews</span>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="#" id="general">General News</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="#" id="business">Business News</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="#" id="sport">Sports News</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="#" id="technology">Technology News</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="#" id="entertainment">Entertainment News</a></li>
                    </ul>
                    <form class="d-flex">
                        <input class="form-control me-2" type="text" id="newsQuery" placeholder="Search news">
                        <button class="btn btn-outline-warning" type="button" id="searchBtn">Search</button>
                    </form>
                </div>
            </div>
        </nav>
        <div>
            <div class="row m-3" id="newsType"></div>
            <div class="row m-3" id="newsdetails"></div>
        </div>
        <div class="mt-5">
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark mt-4">
                <div class="container-fluid">
                    <h5 class="text-white me-auto ms-auto">Welcome<span class="text-warning"> to TrendyTechnieNews</span></h5>
                </div>
            </nav>
            <div class="container-fluid">
                <h6 class="text-center">Copyright &copy; 2023 trendytechnienews.com | All rights reserved</h6>
                <h3 class="text-center"><span class="text-warning">By-Sarvesh Udapurkar(Jain)</span></h3>
            </div>
        </div>
    </div>
    <script>
    const API_KEY = "1c310d66ef4448d1a7ccc045499f1ea3";
    const HEADLINES_NEWS = "https://newsapi.org/v2/top-headlines?country=in&apiKey=";
    const GENERAL_NEWS = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=";
    const BUSINESS_NEWS = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=";
    const SPORTS_NEWS = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=";
    const ENTERTAINMENT_NEWS = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=";
    const TECHNOLOGY_NEWS = "https://newsapi.org/v2/top-headlines?country=in&category=technology&pageSize=8&apiKey=";
    const SEARCH_NEWS = "https://newsapi.org/v2/everything?q=";

    document.addEventListener("DOMContentLoaded", function() {
        document.getElementById("general").addEventListener("click", fetchGeneralNews);
        document.getElementById("business").addEventListener("click", fetchBusinessNews);
        document.getElementById("sport").addEventListener("click", fetchSportsNews);
        document.getElementById("technology").addEventListener("click", fetchTechnologyNews);
        document.getElementById("entertainment").addEventListener("click", fetchEntertainmentNews);
        document.getElementById("searchBtn").addEventListener("click", fetchQueryNews);
        fetchHeadlines();
    });

    async function fetchHeadlines() {
        const response = await fetch(HEADLINES_NEWS + API_KEY);
        await handleResponse(response, "Headlines");
    }

    async function fetchGeneralNews() {
        const response = await fetch(GENERAL_NEWS + API_KEY);
        await handleResponse(response, "Latest General News");
    }

    async function fetchBusinessNews() {
        const response = await fetch(BUSINESS_NEWS + API_KEY);
        await handleResponse(response, "Latest Business News");
    }

    async function fetchSportsNews() {
        const response = await fetch(SPORTS_NEWS + API_KEY);
        await handleResponse(response, "Latest Sports News");
    }

    async function fetchTechnologyNews() {
        const response = await fetch(TECHNOLOGY_NEWS + API_KEY);
        await handleResponse(response, "Latest Technology News");
    }

    async function fetchEntertainmentNews() {
        const response = await fetch(ENTERTAINMENT_NEWS + API_KEY);
        await handleResponse(response, "Entertainment News");
    }

    async function fetchQueryNews() {
        const query = document.getElementById("newsQuery").value;
        if (!query) return;
        const response = await fetch(SEARCH_NEWS + encodeURIComponent(query) + "&apiKey=" + API_KEY);
        await handleResponse(response, `Search Results for: ${query}`);
    }

    async function handleResponse(response, newsType) {
        const data = await response.json();
        if (data.status === "ok") {
            const articles = data.articles;
            const newsdetails = document.getElementById("newsdetails");
            newsdetails.innerHTML = "";
            articles.forEach(article => {
                const col = document.createElement("div");
                col.className = "col-sm-12 col-md-4 col-lg-3 p-2 card";
                col.innerHTML = `
                    <div class="p-2">
                        <img src="${article.urlToImage}" alt="News Image" height="matchparent" width="100%">
                        <div>
                            <h5 class="card-title">${article.title}</h5>
                            <h6 class="text-primary">${article.publishedAt}</h6>
                            <h6 class="text-muted">${article.author}</h6>
                            <p class="text-muted">${article.description}</p>
                            <a class="btn btn-dark" target="_blank" href="${article.url}">Read More</a>
                        </div>
                    </div>
                `;
                newsdetails.appendChild(col);
            });
            document.getElementById("newsType").innerText = newsType;
        }
    }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Streamlit app
# st.set_page_config(page_title="TrendyTechnieNews by Sarvesh Udapurkar", layout="wide")
# st.components.v1.html(custom_html, height=2000, scrolling=True)
# Streamlit app
st.set_page_config(page_title="TrendyTechnieNews by Sarvesh Udapurkar", layout="wide")
# st.write("Custom HTML integration example:")
st.html(custom_html)


