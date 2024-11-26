<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>IOT-PROJECT</h1>
<p align="left">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/3ina/iot-project?style=plastic&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/3ina/iot-project?style=plastic&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/3ina/iot-project?style=plastic&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/3ina/iot-project?style=plastic&color=0080ff" alt="repo-language-count">
</p>
<p align="left">Built with the tools and technologies:</p>
<p align="left">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=plastic&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
</p>
</div>
<br clear="right">

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

This project is a **real-time dashboard** designed to display sensor data, camera feeds, and system statuses using **FastAPI**, **WebSockets**, and **JWT authentication**. It runs on a **Raspberry Pi**, integrating multiple hardware components for real-time data collection and visualization.

---


### **Purpose**
- Display live data from sensors (e.g., DHT22, MQ-9, motion detector).
- Stream real-time video from a camera module.
- Provide real-time system status updates.
- Securely restrict access to authorized users using JWT authentication.

---

##  Features

1. **WebSocket-based Data Streaming**:
   - Real-time updates for:
     - Sensor data (e.g., temperature, humidity, gas levels, motion detection).
     - Camera streams (real-time video feed).
     - System health and status logs.
2. **JWT Authentication**:
   - Protects WebSocket endpoints and ensures only authenticated users can connect.
   - Token-based authentication with login functionality.
3. **Frontend**:
   - Displays live updates from WebSocket streams.
   - Includes a login page for user authentication.
   - Renders real-time sensor data, system statuses, and camera streams.
---


## **Technical Components**

### **1. Backend**
- **Framework**: FastAPI
  - Handles HTTP routes, WebSocket connections, and authentication.
- **WebSocket Endpoints**:
  - `/ws`: Streams sensor data.
  - `/ws/status`: Streams system status updates.
  - `/ws/camera`: Streams live camera feed.
- **Authentication**:
  - Implements JWT-based authentication for login and secure access to WebSocket endpoints.
- **Sensor and Camera Interaction**:
  - Reads real-time data from sensors using Raspberry Pi GPIO pins.
  - Streams live video from a connected camera module.

### **2. Frontend**
- **Technology**: HTML/CSS/JavaScript
  - Connects to WebSocket endpoints for live updates.
  - Includes:
    - Login page for user authentication and JWT token retrieval.
    - Real-time rendering of sensor data, statuses, and camera feeds.

### **3. Hardware Integration**
- **Raspberry Pi**:
  - Runs the FastAPI backend.
  - Interfaces with sensors and cameras through GPIO pins.
- **Sensors**:
  - DHT22: Temperature and humidity sensor.
  - MQ-9: Gas detection sensor.
- **Camera**:
  - Provides live video feed for the dashboard.


##  Project Structure

```sh
└── iot-project/
    ├── main.py
    ├── requirement.txt
    ├── sensor.py
    └── templates
        └── index.html
```


###  Project Index
<details open>
	<summary><b><code>IOT-PROJECT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/3ina/iot-project/blob/master/requirement.txt'>requirement.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/3ina/iot-project/blob/master/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/3ina/iot-project/blob/master/sensor.py'>sensor.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/3ina/iot-project/blob/master/templates/index.html'>index.html</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with iot-project, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python


###  Installation

Install iot-project using one of the following methods:

**Build from source:**

1. Clone the iot-project repository:
```sh
❯ git clone https://github.com/3ina/iot-project
```

2. Navigate to the project directory:
```sh
❯ cd iot-project
```
3. create virtual environment
```sh
❯ python -m venv venv
```
4. active virtualenv
 
5. install dependencies
```sh
❯ pip install -r requierments.txt
```




---


##  Contributing

- **💬 [Join the Discussions](https://github.com/3ina/iot-project/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/3ina/iot-project/issues)**: Submit bugs found or log feature requests for the `iot-project` project.
- **💡 [Submit Pull Requests](https://github.com/3ina/iot-project/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/3ina/iot-project
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/3ina/iot-project/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=3ina/iot-project">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

