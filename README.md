Mini SIEM Dashboard

A lightweight Security Information and Event Management (SIEM) dashboard built to collect, analyze, and visualize security events in real time. This project demonstrates core SIEM concepts including log ingestion, parsing, monitoring, and alert visualization.

Overview

Mini SIEM Dashboard is designed as a simplified security monitoring solution that helps:

Aggregate logs from multiple sources

Parse and normalize event data

Visualize security-related activities

Identify suspicious patterns and anomalies

This project is ideal for learning and demonstrating:

Log analysis fundamentals

Security monitoring workflows

Dashboard design for cybersecurity use cases

Backend-to-frontend data pipelines

Features

Real-time log ingestion

Event parsing and normalization

Interactive dashboard interface

Basic alert detection logic

Search and filtering capabilities

Clean and responsive UI

Tech Stack

Frontend

React

Charting library (e.g., Chart.js / Recharts)

Backend

Node.js / Express

Python (for log processing / parsing if applicable)

Database

MongoDB / PostgreSQL (update if different)

Cloud / DevOps (Optional)

AWS

Docker

CI/CD pipelines

Architecture

Log sources generate security events

Backend API collects and processes logs

Events are stored in the database

Dashboard visualizes metrics and alerts

Users can filter and investigate suspicious activity

Installation
1. Clone the Repository
git clone https://github.com/johnjame12/mini-siem-dashboard.git
cd mini-siem-dashboard
2. Install Dependencies

Backend:

cd backend
npm install

Frontend:

cd frontend
npm install
3. Configure Environment Variables

Create a .env file in the backend folder and configure:

PORT=5000
DATABASE_URL=your_database_connection_string
4. Run the Application

Backend:

npm start

Frontend:

npm start

The dashboard will be available at:

http://localhost:3000
Use Cases

Security event monitoring

Failed login detection

IP activity tracking

Basic anomaly detection

Learning SIEM fundamentals

Future Improvements

Role-based access control (RBAC)

Advanced alert rules engine

Integration with external log sources

Elasticsearch integration

Real-time WebSocket updates

Threat intelligence feed integration

Screenshots

(Add screenshots of your dashboard here)

Learning Objectives

This project was built to strengthen knowledge in:

Full-stack development

Security monitoring concepts

Log parsing and analysis

System design fundamentals

Cloud deployment workflows

Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

License

This project is licensed under the MIT License.
