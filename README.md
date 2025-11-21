# 🚀 DailyLearningMail — AI-Powered Daily Tech Learning Agent

DailyLearningMail is an autonomous AI system that generates **daily tech-learning emails** containing crisp explanations, DSA problems, real-world insights, and fun facts — all beautifully formatted in HTML and delivered directly to subscribers.

The goal is simple:  
### **Learn one useful tech concept every day — in just 3 minutes.**

---

## 📌 Features

- ✨ **AI-generated daily tech lessons**  
- 📬 **Beautiful, mobile-friendly HTML emails**  
- 🧠 **DSA question + solution in every edition**  
- 🔧 **Concept explanation with examples**  
- 🔗 **Real-world applications & fun facts**  
- 🌐 **Auto-send to subscribers via Gmail SMTP**  
- 🗂️ **Import subscribers from Excel/CSV**  
- 🤖 **Agent-based architecture (autonomous pipeline)**  
- 🛡️ **Error handling & delivery tracking**

---

## 🧠 Problem This Solves

People struggle with:
- Information overload  
- No consistent learning routine  
- Low retention when concepts aren’t repeated  

DailyLearningMail fixes this by delivering small, clear, high-quality tech lessons **once a day**, directly to your inbox.

---

## 🤖 Why Agents?

AI agents make this possible because they can:

- Autonomously generate structured content  
- Format it into clean HTML  
- Deliver personalized emails  
- Scale to thousands of learners  
- Continue running daily without manual work  

This system acts as your **AI tutor** — planning, generating, formatting, and sending lessons automatically.

---

## 🏗️ Architecture Overview

Subscribers (Excel/CSV)
|
v
AI Content Generator ---> Markdown/Raw Text
|
v
HTML Formatter ---> Beautiful Email Template
|
v
Mail Sender ---> Delivered to Inbox

### Components

#### **1. Content Generator Agent**
- Uses OpenAI API  
- Generates:
  - Subject line  
  - Tech concept explanation  
  - DSA question + optimal solution  
  - Real-world example  
  - Fun fact  
- Output: markdown or structured text  

#### **2. HTML Formatter**
- Converts markdown → HTML  
- Injects content into a responsive email template  
- Formats code blocks for email compatibility  

#### **3. Delivery Agent**
- Sends emails through Gmail SMTP / Google API  
- Handles bulk sending  
- Tracks successes & failures  
- Retries failed deliveries  

---

## 🔧 Tech Stack

- **Python**  
- **OpenAI API**  
- **SMTP (Gmail)**  
- **Pandas**  
- **Markdown / BeautifulSoup**  
- **HTML/CSS Templates**  
- **Cron / Task Scheduler**

---

## 🚀 Setup & Installation

### 1. Clone the Repo
```bash
git clone https://github.com/fateisintersting/learningmail.git
cd learningmail
```
GOOGLE_API_KEY=your_key
SENDER_EMAIL=your_email
APP_PASSWORD=your_gmail_app_password

## Run Code
python main.py


