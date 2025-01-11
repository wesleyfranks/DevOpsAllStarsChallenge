The formatting issue in the README likely stems from how markdown syntax is interpreted. Let me fix the formatting for clarity and proper display in your README.

# 🌦️ OpenWeather API Demo - Day 1 of #DevOpsAllStarsChallenge 🌟

This project is part of the **30-Day DevOps All-Stars Challenge**, focusing on building a weather dashboard that interacts with the **OpenWeather API** and AWS S3 to fetch, process, and store real-time weather data. 🚀

📺 **YouTube Video Tutorial**: [Watch Here](https://www.youtube.com/watch?v=4smNS8XSHx0&t=1s)

## 🛠️ **Technologies Used**
- 🐍 **Python**: Core scripting language for handling API requests and cloud interactions.
- ☁️ **AWS S3**: Cloud storage for saving weather data in JSON format.
- 🌦️ **OpenWeather API**: Fetches real-time weather data for specified cities.
- 📦 **Boto3**: AWS SDK for Python to programmatically manage S3 buckets and objects.
- 🔐 **dotenv**: Securely manages environment variables for API keys and configurations.
- 🖥️ **Command-Line Interface**: Built with `argparse` for dynamic control.

## ✨ **Features**
1. **Fetch Weather Data**  
   Retrieves weather information such as temperature, humidity, and conditions for specified cities using the OpenWeather API.

2. **Save Data to AWS S3**  
   Stores the fetched weather data in AWS S3 in a structured JSON format, including timestamps for organization.

3. **Dynamic CLI Options**  
   Supports actions like running the program or deleting the S3 bucket via command-line arguments.

4. **Bucket Management**  
   Automatically creates the required S3 bucket if it doesn’t exist and can delete it when no longer needed.

## 📜 **How to Use**

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/wesleyfranks/OpenWeather-API-Demo.git
   cd OpenWeather-API-Demo

	2.	Install dependencies:

pip install -r requirements.txt


	3.	Create a .env file to store your environment variables:

touch .env

Example .env file:

OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your_bucket_name


	4.	Set up AWS credentials to interact with S3:
	•	Refer to AWS CLI Configuration.

Run the Program
	•	Fetch weather data and save it to AWS S3:

python weather_dashboard.py run


	•	Delete the S3 bucket and its contents:

python weather_dashboard.py delete



🌟 Highlights from the Challenge
	•	Dynamic Weather Retrieval: Fetches weather data for Houston, Austin, and Dallas in real-time.
	•	Error Handling: Improved resilience for API failures and bucket operations.
	•	Resource Cleanup: Ensures AWS resources are cleaned up properly using the delete action.

📺 Video Walkthrough

Follow along with the challenge’s Day 1 tutorial:

🤝 Contributing

Contributions, issues, and feedback are welcome! Feel free to open a pull request or issue to help improve the project.

📄 License

This project is licensed under the MIT License.

This version ensures correct formatting with proper spacing, indentation, and clear bullet points. Copy this into your `README.md` file, and it should display correctly now. Let me know if you encounter any other issues! 🚀
